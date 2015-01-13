import numpy as np



def missing_vals(row) :
	"""Returns mask representing location of np.nan values"""
	return list(np.isnan(row))

def translate(row) :
	"""Returns the translation of one row of data in its music format"""
	boolean = missing_vals(row)
	transrow = ''.join(str(int(x)) for x in boolean)
	return transrow




def tests() :
	no_nans = np.array([1,2,4])
	all_nans = np.array([np.nan, np.nan, np.nan])
	some_nans = np.array([1, np.nan , 0.0, 1.0])

	assert missing_vals(no_nans) == [False]*3
	assert missing_vals(all_nans) == [True]*3
	assert missing_vals(some_nans) == [False, True, False, False]

	assert translate(no_nans) == "000"
	assert translate(all_nans) == "111"
	assert translate(some_nans) == "0100"

	print "tests pass"

tests()