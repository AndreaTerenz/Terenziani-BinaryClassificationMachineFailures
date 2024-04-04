import math
import collections
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

random_state = 42

def multiscatter(X, ys, features, target, ncols = 3, nrows = None, figsize = (5, 3.5), main_title="", title_size = 30, plot_title_size = 10):
    if nrows is None:
        nrows = math.ceil((len(features)-1)/ncols)

    figwidth = ncols*figsize[0]
    figheigth = nrows*figsize[1]

    plt.figure(figsize=[figwidth, figheigth])

    if main_title:
        plt.suptitle(main_title, size=title_size)

    for i, feature in enumerate(features):
        plt.subplot(nrows, ncols, i+1)
        plt.title(f"'{feature}' vs '{target}'", fontsize=plot_title_size)

        if isinstance(ys, collections.abc.Sequence):
            for y in ys:
                plt.scatter(X[feature], y, s=4);
        else:
            plt.scatter(X[feature], ys, s=4);

def grid_search_cv(X, y, estimator, param_grid : dict, scoring : str = "neg_mean_squared_error", cv=None):
    """
    Run grid search Cross-validation to find optimal estimator using the given data, parameters and scoring metric

    Returns the best estimator found by GridSearchCV
    """

    cv_grid = GridSearchCV(
        estimator=estimator,
        param_grid=param_grid,
        scoring=scoring,
        cv=cv
    )

    cv_grid.fit(X, y)

    return cv_grid.best_estimator_

def split_dataset(df: pd.DataFrame, target_col : str) -> tuple:
    """
    Split a dataset `df` into a dataframe of features `X` and a target column `y`, selecting it
    with `target_col`.

    Returns a tuple `(features dataframe, target column)`
    """

    X = df.drop(labels=target_col, axis=1)
    y = df[target_col]

    return X, y

def useful_stats(y_true, y_pred, X_data):
    """
    Compute useful statistics given the data `X_data`, the correct labels `y_true` and the predicted labels `y_pred`.
    
    Returns a tuple containing:
    - F-score
    - p-value
    - rMSE
    - R2 factor
    """

    y_true_mean = np.mean(y_true)

    SSM = np.sum((y_pred - y_true_mean) ** 2.)
    SSE = np.sum((y_true - y_pred) ** 2.)
    SST = np.sum((y_true - y_true_mean) ** 2.)
    
    # Each datapoint is an observation --> Each row is an observation
    n_obs, n_features = X_data.shape
    p = n_features+1
    n = n_obs

    DFM = p - 1
    DFE = n - p
    DFT = n - 1

    MSM = SSM / DFM
    MSE = SSE / DFE
    MST = SST / DFT

    F_score = MSM / MSE
    p_value = 1-scipy.stats.f.cdf(F_score, DFM, DFE) #find p-value of F test statistic 
    rmse = math.sqrt(MSE)
    r_squared = 1 - (SSE/SST)

    return F_score, p_value, rmse, r_squared


def run_poly_regression(X_tr, y_tr, X_te, y_te, degree = 2, model = LinearRegression(), fit_model = True):
    """
    Run polynomial regression, training with (`X_tr`, `y_tr`) and predicting with (`X_te`, `y_te`).
    Use `model` to provide a specific LinearRegression estimator and `fit_model` to indicate whether the model
    should be fitted on the training data (usually yes) or is already trained

    Returns:
    - the fitted model
    - the prediction done on `X_te`
    - tutple of stats on the prediction (F-score, p-value, rmse, R squared)
    """

    X_te_poly = X_te

    if degree > 1:
        polFea = PolynomialFeatures(degree=degree,include_bias=False)
        X_tr = polFea.fit_transform(X_tr.values)
        X_te_poly = polFea.transform(X_te)

    if fit_model:
        model.fit(X_tr, y_tr)
    
    y_pred = model.predict(X_te_poly)
    stats = useful_stats(y_te, y_pred, X_te_poly)

    return model, y_pred, stats