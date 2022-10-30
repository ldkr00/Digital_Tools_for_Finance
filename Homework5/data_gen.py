import pandas as pd
import numpy as np
import time

PATH = "./"

#logger for execution times
def log(path, method, time):
    with open(path + "times.txt", "a+") as out:
        out.write("execution time of {}: {} seconds\n".format(method, time))

#init vars for data
rowSize = 1e6
colSize = 5
column_to_duplicate = 3

#input check
if column_to_duplicate >= colSize:
    raise ValueError("Index of {} is out of range. Please choose an index less than {}.".format(column_to_duplicate, colSize))

#generate random data
colHeader = ["COL {}".format(i+1) for i in range(colSize - 1)]
df = pd.DataFrame(np.random.randint(0, rowSize, size=(int(rowSize), colSize - 1)), columns=colHeader)
df['COL {} - COPY'.format(column_to_duplicate)] = df.loc[:, 'COL {}'.format(column_to_duplicate)]


##export to HDF
start_time1 = time.time()
df.to_hdf(PATH + "DATA.h5", key='df', mode='w')
end_time1 = time.time()
log(PATH, "HDF", end_time1 - start_time1)

##export to Parquet
start_time2 = time.time()
df.to_parquet(PATH + "DATA.parquet")
end_time2 = time.time()
log(PATH, "Parquet", end_time2 - start_time2)

##export to Feather
start_time3 = time.time()
df.to_feather(PATH + "DATA.ftr")
end_time3 = time.time()
log(PATH, "Feather", end_time3 - start_time3)