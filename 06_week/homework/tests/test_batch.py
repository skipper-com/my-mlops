from datetime import datetime
import pandas as pd
import batch
from pandas.testing import assert_frame_equal


def dt(hour, minute, second=0):
    """
    Helper function
    """
    return datetime(2022, 1, 1, hour, minute, second)


def test_prepare_data():
    """
    Test function
    """
    data = [
        (None,  None,   dt(1, 2),   dt(1, 10)),
        (1,     None,   dt(1, 2),   dt(1, 10)),
        (1,     2,      dt(2, 2),   dt(2, 3)),
        (None,  1,      dt(1, 2, 0),dt(1, 2, 50)),
        (2,     3,      dt(1, 2, 0),dt(1, 2, 59)),
        (3,     4,      dt(1, 2, 0),dt(2, 2, 1)),
    ]

    columns = [
        "PULocationID",
        "DOLocationID",
        "tpep_pickup_datetime",
        "tpep_dropoff_datetime",
    ]

    df = pd.DataFrame(data, columns=columns)
    actual_df = batch.prepare_data(df, columns[0:2])

    expected_df = pd.DataFrame({
                                'PULocationID': ['-1', '1', '1'],
                                'DOLocationID': ['-1', '-1', '2'],
                                'tpep_pickup_datetime': [dt(1, 2), dt(1, 2), dt(2, 2)],
                                'tpep_dropoff_datetime': [dt(1, 10), dt(1, 10), dt(2, 3)],
                                'duration': [8.0, 8.0, 1.0]                        
                               })
    
    assert_frame_equal(actual_df, expected_df)
