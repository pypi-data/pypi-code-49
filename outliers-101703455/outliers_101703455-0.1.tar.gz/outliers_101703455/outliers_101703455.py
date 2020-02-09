import numpy as np
import csv
from io import StringIO

def outlier(data):
    rows = []
    outliers = []
    buffer = StringIO()
    data.to_csv(buffer)
    buffer.seek(0)
    data1 = csv.reader(buffer)
    fields = next(data1)
    for row in data1:
        rows.append(int(row[-1]))
    sorted(rows)
    q1, q3 = np.percentile(rows,[25,75])
    iqr_value = q3-q1
    lower_bound_val = q1 -(1.5 * iqr_value) 
    upper_bound_val = q3 +(1.5 * iqr_value)
    for value in rows:
        if value not in range(int(lower_bound_val),int(upper_bound_val)):
            outliers.append(value)
    print("Outliers: ",outliers)
    print("No. of outliers or no. of rows to be removed: ",len(outliers))