#!/usr/bin/env python
# coding: utf-8

import pickle
import sys
import os

import pandas as pd

# year = int(sys.argv[1])
# month = int(sys.argv[2])
year = 2022
month = 1
S3_ENDPOINT_URL = 'http://localhost:4566'
# input_file = f"https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year:04d}-{month:02d}.parquet"
# output_file = f"taxi_type=yellow_year={year:04d}_month={month:02d}.parquet"
input_file = f's3://nyc-duration/yellow_tripdata_{year:04d}-{month:02d}.parquet'
output_file = f"s3://nyc-duration/taxi_type=yellow_year={year:04d}_month={month:02d}.parquet"


def get_input_path(year, month):
    default_input_pattern = 'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year:04d}-{month:02d}.parquet'
    input_pattern = os.getenv('INPUT_FILE_PATTERN', default_input_pattern)
    return input_pattern.format(year=year, month=month)


def get_output_path(year, month):
    default_output_pattern = 's3://nyc-duration-prediction-alexey/taxi_type=fhv/year={year:04d}/month={month:02d}/predictions.parquet'
    output_pattern = os.getenv('OUTPUT_FILE_PATTERN', default_output_pattern)
    return output_pattern.format(year=year, month=month)


def read_data(filename) -> pd.DataFrame():
    """
    Docstring is empty
    """
    options = {
        'client_kwargs': {
            'endpoint_url': S3_ENDPOINT_URL
        }
    }
    
    df = pd.read_parquet(filename, storage_options=options)
    
    #df = pd.read_parquet(filename)

    return df

def save_data(df, file) -> None:
    """
    Docstring is empty
    """
    options = {
        'client_kwargs': {
            'endpoint_url': S3_ENDPOINT_URL
        }
    }

    df.to_parquet(
        file,
        engine='pyarrow',
        compression=None,
        index=False,
        storage_options=options
    )
    
    return True


def prepare_data(df, categorical) -> pd.DataFrame():
    """
    Prepare data function
    """
    df["duration"] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df["duration"] = df.duration.dt.total_seconds() / 60
    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()
    df[categorical] = df[categorical].fillna(-1).astype("int").astype("str")

    return df


def main(year, month):
    """
    Main function
    """
    #input_file = get_input_path(year, month)
    #output_file = get_output_path(year, month)

    with open("model.bin", "rb") as f_in:
        dv, lr = pickle.load(f_in)

    categorical = ["PULocationID", "DOLocationID"]

    df = read_data(input_file)
    df = prepare_data(df, categorical)
    df["ride_id"] = f"{year:04d}/{month:02d}_" + df.index.astype("str")

    dicts = df[categorical].to_dict(orient="records")
    X_val = dv.transform(dicts)
    y_pred = lr.predict(X_val)

    print("predicted mean duration:", y_pred.mean())

    df_result = pd.DataFrame()
    df_result["ride_id"] = df["ride_id"]
    df_result["predicted_duration"] = y_pred

    save_data(df_result, output_file)
    print(df_result["predicted_duration"].sum())


if __name__ == "__main__":
    main(year, month)
