import polars as pl 

q= (
    pl.scan_csv("../data/diabetes.csv")
)

df= q.collect()

for i in df:
    print(i)

