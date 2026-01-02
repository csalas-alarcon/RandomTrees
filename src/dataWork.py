import polars as pl 
import time
import typing

def leer() -> pl.DataFrame:
    q= pl.scan_csv("../data/diabetes.csv")
    df= q.collect()
    return df

def guardar_modelo(df: pl.DataFrame) -> None:
    id= time.time()
    df.write_json(f"../results/modelo{id}")
