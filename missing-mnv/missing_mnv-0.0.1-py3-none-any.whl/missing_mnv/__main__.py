import pandas as pd
import sys
import numpy as np
from sklearn.impute import SimpleImputer


imp=SimpleImputer(missing_values=np.nan,strategy="mean")


data=pd.read_csv(str(sys.argv[1]))
data=data.replace(["na","n/a","NA","N/A","-",".",""," ","Na"],np.nan)


data=imp.fit_transform(data)
data=pd.DataFrame(data)
print(data)
