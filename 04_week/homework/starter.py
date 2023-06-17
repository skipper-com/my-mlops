import pickle
import pandas as pd
import numpy as np
import sys
import boto3


with open("model.bin", "rb") as f_in:
    dv, model = pickle.load(f_in)

categorical = ["PULocationID", "DOLocationID"]

year = int(sys.argv[1])  # 2022
month = int(sys.argv[2])  # 3


def read_data(filename):
    df = pd.read_parquet(filename)
    df["duration"] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df["duration"] = df.duration.dt.total_seconds() / 60
    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()
    df[categorical] = df[categorical].fillna(-1).astype("int").astype("str")

    return df


# year = 2022
# month = 2

df = read_data(
    f"https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year:04d}-{month:02d}.parquet"
)
dicts = df[categorical].to_dict(orient="records")
X_val = dv.transform(dicts)
y_pred = model.predict(X_val)

# df["ride_id"] = f"{year:04d}/{month:02d}_" + df.index.astype("str")

s3 = boto3.resource('s3',
         aws_access_key_id=ACCESS_ID,
         aws_secret_access_key= ACCESS_KEY)

output_file = f"s3://dtc-mlops/4hw/taxi_yellow_{year:04d}-{month:02d}.parquet"
df_result = pd.DataFrame()
df_result["ride_id"] = f"{year:04d}/{month:02d}_" + df.index.astype("str")
df_result["y_pred"] = y_pred
df_result.to_parquet(output_file, engine="pyarrow", compression=None, index=False)

print(np.mean(y_pred))
