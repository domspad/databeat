import numpy as np

def missing_vals(row) :
	"""Returns mask representing location of np.nan values"""
	return list(np.isnan(row))

def tests() :
	no_nans = np.array([1,2,4])
	all_nans = np.array([np.nan, np.nan, np.nan])
	some_nans = np.array([1, np.nan , 0.0, 1.0])

	assert missing_vals(no_nans) == [False]*3
	assert missing_vals(all_nans) == [True]*3
	assert missing_vals(some_nans) == [False, True, False, False]

	print "tests pass"

tests()