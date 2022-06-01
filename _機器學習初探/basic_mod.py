import requests
import numpy as np
import pandas as pd
import matplotlib as mpl
import sklearn
import tensorflow as tf
library_names = ['requests','NumPy','Pandas','Matplotlib','Scikit-Learn','TensorFlow']
library_versions = [requests.__version__,np.__version__,pd.__version__,mpl.__version__,sklearn.__version__,tf.__version__]
for lib_n,lib_v in zip(library_names,library_versions):
    print("{}版本為{}".format(lib_n,lib_v))