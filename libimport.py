import numpy as np
import pandas as pd 
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import math
import pickle
import itertools
import scipy
from yellowbrick.regressor import ResidualsPlot
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import train_test_split, cross_val_score 
from statistics import mean 
from sklearn.preprocessing import StandardScaler, power_transform, PolynomialFeatures
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.feature_selection import RFE
import statsmodels.api as sm
