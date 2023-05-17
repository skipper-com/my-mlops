Q1. Downloading the data
We'll use the same NYC taxi dataset, but instead of "Green Taxi Trip Records", we'll use "Yellow Taxi Trip Records". Download the data for January and February 2022. Read the data for January. How many columns are there?
16
17
18
19
Answer: 19


Q2. Computing duration
Now let's compute the duration variable. It should contain the duration of a ride in minutes. What's the standard deviation of the trips duration in January?
41.45
46.45
51.45
56.45
Answer: 46.45


Q3. Dropping outliers
Next, we need to check the distribution of the duration variable. There are some outliers. Let's remove them and keep only the records where the duration was between 1 and 60 minutes (inclusive). What fraction of the records left after you dropped the outliers?
90%
92%
95%
98%
Answer: 98%


Q4. One-hot encoding
Let's apply one-hot encoding to the pickup and dropoff location IDs. We'll use only these two features for our model. Turn the dataframe into a list of dictionaries
Fit a dictionary vectorizer. Get a feature matrix from it What's the dimensionality of this matrix (number of columns)?
2
155
345
515
715
Answer: 515


Q5. Training a model
Now let's use the feature matrix from the previous step to train a model. Train a plain linear regression model with default parameters. Calculate the RMSE of the model on the training data. What's the RMSE on train?
6.99
11.99
16.99
21.99
Answer: 6.99


Q6. Evaluating the model
Now let's apply this model to the validation dataset (February 2022). What's the RMSE on validation?
7.79
12.79
17.79
22.79
Answer: 7.79

Your code (link to GitHub or other public code-hosting website). Remember: no code - no scores!
ddd


Learning in public links
Links to social media posts where you share your progress with others (LinkedIn, Twitter, etc). Use #mlopszoomcamp tag. The scores for this part will be capped at 7 point. Please make sure the posts are valid URLs starting with "https://"