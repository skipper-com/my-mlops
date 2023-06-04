
## Q1. Human-readable name
You’d like to give the first task, read_data a nicely formatted name. How can you specify a task name? Hint: look in the docs at https://docs.prefect.io or check out the doc string in a code editor.
- @task(retries=3, retry_delay_seconds=2, name="Read taxi data")
- @task(retries=3, retry_delay_seconds=2, task_name="Read taxi data")
- @task(retries=3, retry_delay_seconds=2, task-name="Read taxi data")
- @task(retries=3, retry_delay_seconds=2, task_name_function=lambda x: f"Read taxi data")
*** Answer: @task(retries=3, retry_delay_seconds=2, name="Read taxi data") *** 


## Q2. Cron
Cron is a common scheduling specification for workflows. Using the flow in orchestrate.py, create a deployment. Schedule your deployment to run on the third day of every month at 9am UTC. What’s the cron schedule for that?
- 0 9 3 * *
- 0 0 9 3 *
- 9 * 3 0 *
- * * 9 3 0
*** Answer: 0 9 3 * * *** 


## Q3. RMSE
Download the January 2023 Green Taxi data and use it for your training data. Download the February 2023 Green Taxi data and use it for your validation data. Make sure you upload the data to GitHub so it is available for your deployment. Create a custom flow run of your deployment from the UI. Choose Custom Run for the flow and enter the file path as a string on the JSON tab under Parameters. Make sure you have a worker running and polling the correct work pool. View the results in the UI. What’s the final RMSE to five decimal places?
- 6.67433
- 5.19931
- 8.89443
- 9.12250
***Answer: 10***


Launch the tracking server locally for MLflow
Now we want to manage the entire lifecycle of our ML model. In this step, you'll need to launch a tracking server. This way we will also have access to the model registry. 
In case of MLflow, you need to:
* launch the tracking server on your local machine,
* select a SQLite db for the backend store and a folder called `artifacts` for the artifacts store.
You should keep the tracking server running to work on the next three exercises that use the server.

## Q4. Tune model hyperparameters
Now let's try to reduce the validation error by tuning the hyperparameters of the `RandomForestRegressor` using `optuna`. We have prepared the script `hpo.py` for this exercise. Your task is to modify the script `hpo.py` and make sure that the validation RMSE is logged to the tracking server for each run of the hyperparameter optimization (you will need to add a few lines of code to the `objective` function) and run the script without passing any parameters. After that, open UI and explore the runs from the experiment called `random-forest-hyperopt` to answer the question below. Note: Don't use autologging for this exercise. The idea is to just log the information that you need to answer the question below, including:
* the list of hyperparameters that are passed to the `objective` function during the optimization,
* the RMSE obtained on the validation set (February 2022 data).
What's the best validation RMSE that you got?
* 1.85
* 2.15
* 2.45
* 2.85
***Answer: 2.45***


## Q5. Promote the best model to the model registry
The results from the hyperparameter optimization are quite good. So, we can assume that we are ready to test some of these models in production. In this exercise, you'll promote the best model to the model registry. We have prepared a script called `register_model.py`, which will check the results from the previous step and select the top 5 runs. After that, it will calculate the RMSE of those models on the test set (March 2022 data) and save the results to a new experiment called `random-forest-best-models`.Your task is to update the script `register_model.py` so that it selects the model with the lowest RMSE on the test set and registers it to the model registry.
Tips for MLflow:
* you can use the method `search_runs` from the `MlflowClient` to get the model with the lowest RMSE,
* to register the model you can use the method `mlflow.register_model` and you will need to pass the right `model_uri` in the form of a string that looks like this: `"runs:/<RUN_ID>/model"`, and the name of the model (make sure to choose a good one!). What is the test RMSE of the best model?
* 1.885
* 2.185
* 2.555
* 2.955
***Answer: 2.185***


## Q6. Model metadata
Now explore your best model in the model registry using UI. What information does the model registry contain about each model?
* Version number
* Source experiment
* Model signature
* All the above answers are correct
***Answer: Version number***


## Your code (link to GitHub or other public code-hosting website). Remember: no code - no scores!
ddd


## Learning in public links
Links to social media posts where you share your progress with others (LinkedIn, Twitter, etc). Use #mlopszoomcamp tag. The scores for this part will be capped at 7 point. Please make sure the posts are valid URLs starting with "https://"
