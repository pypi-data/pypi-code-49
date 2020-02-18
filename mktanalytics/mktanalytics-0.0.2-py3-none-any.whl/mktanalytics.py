import numpy as np


def rv_cc_estimator(sample,n=22):
	"""
	Realized volatility close to close calculation. Returns a time series of the realized volatility.

	Sample: series or dataframe of closing prices indexed by date
	n: sample size period for the volatility
	"""
	returns = np.divide(sample, sample.shift(1))
	log_returns = np.log(returns)
	ann_log_returns = 252*np.power(log_returns,2)/n
	return 100 * np.sqrt(ann_log_returns.rolling(window=n,min_periods=n).sum())