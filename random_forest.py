
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import RandomizedSearchCV

def best_param_rf(X_train , y_train , iterations=100):
      


      # Number of trees is not a parameter that should be tuned, but just set large enough usually. There is no risk of overfitting in random forest with growing number of # trees, as they are trained independently from each other. 
      n_estimators = list(range(200, 2000, 200))

      # Number of features to consider at every split
      max_features = ['auto', 'sqrt', None, 'log2']

      # Maximum number of levels in tree
      # Max depth is a parameter that most of the times should be set as high as possible, but possibly better performance can be achieved by setting it lower.
      max_depth = list(range(10, 110, 10))
      max_depth.append(None)

      # Minimum number of samples required to split a node
      # Higher values prevent a model from learning relations which might be highly specific to the particular sample selected for a tree. Too high values can also lead to # under-fitting hence depending on the level of underfitting or overfitting, you can tune the values for min_samples_split.
      min_samples_split = [2, 5, 10, 20, 30, 40]

      # Minimum number of samples required at each leaf node
      min_samples_leaf = [1, 2, 7, 12, 14, 16 ,20]

      # Method of selecting samples for training each tree
      bootstrap = [True, False]

      # Create the random grid
      random_grid = {'n_estimators': n_estimators,
                     'max_features': max_features,
                     'max_depth': max_depth,
                     'min_samples_split': min_samples_split,
                     'min_samples_leaf': min_samples_leaf,
                     'bootstrap': bootstrap}

      print(random_grid)

      # New Random Forest Classifier to house optimal parameters
      rf = RandomForestClassifier()

      # Specfiy the details of our Randomized Search
      rf_random = RandomizedSearchCV(estimator = rf, param_distributions = random_grid, n_iter = iterations, cv = 3, verbose=2, random_state=42, n_jobs = -1)

      # Fit the random search model
      rf_random.fit(X_train, y_train)
      dictionary = dict()
      dictionary['Best Score'] = rf_random.best_score_
      dictionary['Best parameters'] = rf_random.best_estimator_.get_params()
      #print(f"Best score: {rf_random.best_score_}")
      #print("Best parameters set:")
      #best_parameters = rf_random.best_estimator_.get_params()
      #for param_name in sorted(random_grid.keys()):
      #  print(f"\t{param_name}: {best_parameters[param_name]}")
      return dictionary
def make_preds(new_data, trained_model , df):
      '''
      new_data : df except the prediction column
      trained_model : trained model for actual prediction
      df : dataframe with the date column
      returns a df
      '''
      pred1 = pd.DataFrame(trained_model.predict(new_data))
      ppp =df.reset_index()
      pred1 = pd.concat([pred1 , ppp.Date],axis=1)
      pred1= pred1.set_index('Date')
      pred1.columns = ['preds']
      return pred1
