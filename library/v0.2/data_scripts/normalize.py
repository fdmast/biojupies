#################################################################
#################################################################
############### Normalize Dataset
#################################################################
#################################################################

#############################################
########## 1. Load libraries
#############################################
##### 1. General support #####
import scipy.stats as ss
import numpy as np
import warnings
import os
from rpy2.robjects import r, pandas2ri
pandas2ri.activate()

##### 2. R #####
r.source(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'R', 'normalize.R'))

#######################################################
#######################################################
########## S1. Dataset Normalization
#######################################################
#######################################################

#############################################
########## 1. Z-score
#############################################

def zscore(data):

	# Get raw data
	rawdata = data['rawdata']

	# Z-score without warnings
	with warnings.catch_warnings():
		warnings.simplefilter("ignore")
		rawdata = rawdata/rawdata.sum()
		rawdata = np.log10(rawdata+1)
		zscore = rawdata.apply(ss.zscore, axis=1).dropna()

	# Return
	return zscore

#############################################
########## 2. VST
#############################################

def vst(data):

	return pandas2ri.ri2py(r.vst(pandas2ri.py2ri(data['rawdata'])))

#############################################
########## 3. Quantile Normalization
#############################################

def quantile(data):

	return pandas2ri.ri2py(r.quantile(pandas2ri.py2ri(data['rawdata'])))
