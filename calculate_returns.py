import numpy as np
import pandas as pd 

def calc_return(df, daysout):
    df['NextClose']=df['Close'].shift(-daysout)
    df.dropna(inplace=True)
    df['Return'] = df.apply(lambda x : np.log(x['NextClose']/x['Close']) if \
                            x['Signal_Flag']==1 else 0 , axis=1)
    total_return = df['Return'].sum()

    print('The Return for the Strategy by holding for {} days  is : {}' .format(daysout, total_return))
    df['BuyandHold'] = np.log(df['NextClose']/df['Close'])
    buy_hold_r = df['BuyandHold'].sum()
    print('The Return for the BUY n HOLD Strategy by holding for {} days  is : {}' .format(daysout, buy_hold_r))
    
