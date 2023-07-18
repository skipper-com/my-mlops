AWS_REGION="eu-central-1"

# Dynamically generated by TF
export MODEL_BUCKET_PROD="stg-mlflow-models-code-pilugin-dtc-mlops"
export PREDICTIONS_STREAM_NAME="stg-ride_predictions-dtc-mlops"
export LAMBDA_FUNCTION="stg-prediction_lambda_dtc-mlops"

# Model artifacts bucket from the previous weeks (MLflow experiments)
export MODEL_BUCKET_DEV="dtc-mlops"

# Get latest RUN_ID from latest S3 partition.
# NOT FOR PRODUCTION!
# In practice, this is generally picked up from your experiment tracking tool such as MLflow or DVC
export RUN_ID=$(aws s3api list-objects-v2 --bucket ${MODEL_BUCKET_DEV} \
--query 'sort_by(Contents, &LastModified)[-1].Key' --output=text | cut -f2 -d/)
export RUN_ID=963d555a1f614713ae1ae1e12a77c875


# NOT FOR PRODUCTION!
# Just mocking the artifacts from training process in the Prod env
aws s3 sync s3://${MODEL_BUCKET_DEV} s3://${MODEL_BUCKET_PROD}

# Set new var RUN_ID in existing set of vars.
variables="{PREDICTIONS_STREAM_NAME=${PREDICTIONS_STREAM_NAME}, MODEL_BUCKET=${MODEL_BUCKET_PROD}, RUN_ID=${RUN_ID}}"

# https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html
aws lambda update-function-configuration --function-name ${LAMBDA_FUNCTION} --environment "Variables=${variables}"