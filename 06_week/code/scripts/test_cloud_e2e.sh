export KINESIS_STREAM_INPUT="stg-ride_events-dtc-mlops"
export KINESIS_STREAM_OUTPUT="stg-ride_predictions-dtc-mlops"

SHARD_ID=$(aws kinesis put-record \
        --stream-name ${KINESIS_STREAM_INPUT} \
        --partition-key 1 \
        --data '{"ride": {
            "PULocationID": 130,
            "DOLocationID": 205,
            "trip_distance": 3.66
        },
        "ride_id": 156}'  \
        --query 'ShardId'
    )
#--cli-binary-format raw-in-base64-out  \
#SHARD_ITERATOR=$(aws kinesis get-shard-iterator --shard-id ${SHARD_ID} --shard-iterator-type TRIM_HORIZON --stream-name ${KINESIS_STREAM_OUTPUT} --query 'ShardIterator')

#aws kinesis get-records --shard-iterator $SHARD_ITERATOR
