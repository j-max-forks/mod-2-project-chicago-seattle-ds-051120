import pandas as pd
import numpy as np
import matplotplib.pyplot as plt
from statsmodels.api import OLS


def fit_linear(df, columns)
    '''
    Parameters:
    DF: Dataframe with y assumed to be sale_price
    
    X: List of columns to be used as predictors for sale_price

    ----------------------------
    Returns:
    Prints summary and returns fit OLS model
    
    '''

    y = df.saleprice
    X = df[columns]
    X = sm.add_constant(X)
    lr = OLS(y, X)
    model = lr.fit()
    
    print(model.summary())
    
    return model