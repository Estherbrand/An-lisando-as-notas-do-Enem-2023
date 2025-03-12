import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats  

data = pd.read_json('enem_2023.json')

data.describe()

