
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, plot_confusion_matrix
import numpy as np

def confus_matrix(signalflag , prediction , model=False ,X_test=False,y_test=False ,plot=False):
    ''' #cm.confus_matrix(actual_results,predictions,model,<test data(or new_data for prediction except target VAR)>,<actaul Target VAR> ,<plot=True>)
        Signal_Flag : Pandas Series of Actual Data Points
        predictions : Pandas Series of Predicted Data points
        model : trained model
        returns : the confusion matrix and accuracy , precision , recall 
        and specificity.
    '''    
    rf_matrix = confusion_matrix(signalflag,prediction)

    true_negatives = rf_matrix[0][0]
    false_negatives = rf_matrix[1][0]
    true_positives = rf_matrix[1][1]
    false_positives = rf_matrix[0][1]

    accuracy = (true_negatives + true_positives) / (true_negatives + true_positives + false_negatives + false_positives)
    percision = true_positives / (true_positives + false_positives)
    recall = true_positives / (true_positives + false_negatives)
    specificity = true_negatives / (true_negatives + false_positives)

    print('Accuracy: {}'.format(float(accuracy)*100))
    print('Percision: {}'.format(float(percision)*100))
    print('Recall: {}'.format(float(recall)*100))
    print('Specificity: {}'.format(float(specificity)*100))
    if plot==True:
        disp = plot_confusion_matrix(model, X_test, y_test, display_labels = ['Down Day', 'Up Day'], normalize = 'true', cmap=plt.cm.Blues)
        disp.ax_.set_title('Confusion Matrix - Normalized for the Actual Trading Data')
        plt.show()
