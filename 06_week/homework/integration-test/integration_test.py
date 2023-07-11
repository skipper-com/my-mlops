import pandas as pd
import os
from datetime import datetime

S3_ENDPOINT_URL = 'http://localhost:4566'
year = 2022
month = 1

def dt(hour, minute, second=0):
    """
    Helper function
    """
    return datetime(2022, 1, 1, hour, minute, second)


def main():
    expected_df = pd.DataFrame({
                                'PULocationID': ['-1', '1', '1'],
                                'DOLocationID': ['-1', '-1', '2'],
                                'tpep_pickup_datetime': [dt(1, 2), dt(1, 2), dt(2, 2)],
                                'tpep_dropoff_datetime': [dt(1, 10), dt(1, 10), dt(2, 3)],
                                'duration': [8.0, 8.0, 1.0]                        
                                })

    options = {
        'client_kwargs': {
            'endpoint_url': S3_ENDPOINT_URL
        }
    }

    expected_df.to_parquet(
        f's3://nyc-duration/yellow_tripdata_{year:04d}-{month:02d}.parquet',
        engine='pyarrow',
        compression=None,
        index=False,
        storage_options=options
    )

if __name__ == "__main__":
    main()