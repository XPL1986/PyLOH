'''
Created on 2013-07-20

@author: Yi Li
'''
import numpy as np

BAF_N_MIN = 0.4
BAF_N_MAX = 0.6
BAF_T_MIN = 0.35
BAF_T_MAX = 0.65
BAF_COUNTS_MIN = 10
BAF_COUNTS_MAX = 95
BAF_BINS = np.array(range(0, 100 + 1))/100.0
LOH_FREC_MAX = 0.25
LOH_FREC_MIN = 0.16
SITES_NUM_MIN = 100
PHI_INIT = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
PHI_RANGE = [i/100.0 for i in range(2, 99)]
ETA = 1.01
#ETA = 1
BURN_IN = 10
EPS = np.finfo(float).eps

TAU = 1800
ALPHA = 0.5
SIGMA = 0.001
ERR = 0.01
EMPIRI_BAF = 0.485
EMPIRI_AAF = 1 - EMPIRI_BAF
GENOTYPES_NORMAL = ['AB']
COPY_NUMBER_NORMAL = [2]
COPY_NUMBER_BASE = [2, 4]
MU_N = [EMPIRI_BAF/(EMPIRI_BAF + EMPIRI_AAF)]

UPDATE_WEIGHTS = {}
UPDATE_WEIGHTS['x1'] = 0.9
UPDATE_WEIGHTS['y1'] = 0.1

CHROM_START = 0

CHROM_LIST = ['chr1', 'chr2', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7', 'chr8',
              'chr9', 'chr10', 'chr11', 'chr12', 'chr13', 'chr14', 'chr15',
              'chr16', 'chr17', 'chr18', 'chr19', 'chr20', 'chr21', 'chr22']


#CHROM_LENS = [247249719, 242951149, 199501827, 191273063, 180857866, 170899992,
#              158821424, 146274826, 140273252, 135374737, 134452384, 132349534,
#              114142980, 106368585, 100338915, 88827254, 78774742, 76117153,
#              63811651, 62435964, 46944323, 49691432]
