# databeat
## An experiment in the possibility of hearing the patterns in your data

Given a numpy array with missing values represented as `np.NaN`s, the array is read like sheet music where each row is a "beat" of the time measure and each column is a pitch. Missing values represent sound, and where values are present there is silence at their respective pitch. 

## Todos

To allow the user to apply their own filters on the data (i.e. not just missing values representing sound) change so that it accepts any matrix of binary values
