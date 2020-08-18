
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def lineplot(frames_y, figL , figW , df , predictions,frames_x=1,no_of_datapoints=0):
     
     '''
     Draws Line plots stacks them on one another

     '''
     plt.style.use('fivethirtyeight')
     fig, ax = plt.subplots(frames_y,frames_x,figsize=(figL,figW))
     counter=0
     while counter<frame_y:
        ax[counter].plot(df.index.values[-no_of_datapoints:],df.Close.values[-no_of_datapoints:],linewidth=1 , marker='*')
        counter+=1
        ax[counter].plot(df.index.values[-no_of_datapoints:],predictions.values[-no_of_datapoints:],linewidth=1, marker='.')
        counter+=1

     plt.show()
