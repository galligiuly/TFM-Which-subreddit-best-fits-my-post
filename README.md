# TFM - Which subreddit best fits my post?
Kschool - Master Data Science

The purpose of my project is to train an NLP model that could be able to suggest the fittest subreddit for bloggers who want publish in Reddit.
Given a text from a post or a blog, my NLP model would suggest in which subreddit it could be published

_Multy-Class Classification problem_



## Project Presentation

https://slides.com/galligiuly/galligiuly/live?context=editing#/



## Data

The following [link](<https://console.cloud.google.com/bigquery?p=fh-bigquery%2F&project=reddit-254019&folder&organizationId>) refers to a collection of 1.7 billion comments uploaded to BigQuery and from where I started to analyze and query the data used for my work.

Specifically I've been using the tables: 

_public data_

 - fh-bigquery:reddit_comments.
 - fh-bigquery:reddit_posts.

_my tables for the project_

*  reddit-254019
* reddit-master

#### reddit_comments

The table of comments gives me a huge amount of text that helps me with my purpose. 

Analyzing `number of comments` and `number of unique authors` that write comments, has been a filter used to find the most popular subreddits that grow at a specific time during the life of Reddit and still remain active.

#### reddit_posts

Apart from the analysis of comments I decided to make an analysis for posts because the original post (title and corpus of it) should contain more key words that better identify the subreddit, precious information for my study.

The idea is the same as for the comments, filter the parameters most important that give me the most popular subreddits still actives nowadays.

#### Objective

What I need is to find the subreddits with a constant popularity during the years.

The most accurate way is to find a function that, once the data has been normalized, is capable to suggest me the subreddit most populars in order of number of comments, number of unique authors that write on it and the score assigned. This is an idea that I'll develop in the future, with more time.

For now, I'll just explore my data, analyzing number of wrintng authors and number of comments (score has been excluded during the exploration), comparing them and searching a criteria for my selection.



## GCP

The projects on my GCP that I've created for this job are:

*  reddit-254019
* reddit-master



In **reddit-master** (where are stored all results that metters) I've created Bucket for:

| Bucket name            | Bucket data                                                  |
| ---------------------- | ------------------------------------------------------------ |
| reddit_comments_master | All differents results of queries from `fh-bigquery:reddit_comments.` |
| reddit_posts_master    | All differents results of queries from `fh-bigquery:reddit_posts.` |
| reddit_final_results   | DataFrames that I have been saving in all the steps to import into the next Colab. |
| reddit_models          | All models of my job.                                        |



# Project organization

| Folder                                                       | Description                                                  | Key Results (if expected)                                    |
| :----------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [00_images](https://github.com/galligiuly/TFM-Which-subreddit-best-fits-my-post/tree/master/00_images) | All images used in this project                              | *#N/A*                                                       |
| [01_data](https://github.com/galligiuly/TFM-Which-subreddit-best-fits-my-post/tree/master/01_data) | csv's results of statistic to better understand the data that, for dimentions, couldn't save in GitHub | Statistic results                                            |
| [02_inspection](https://github.com/galligiuly/TFM-Which-subreddit-best-fits-my-post/tree/master/02_inspection) | Process applied to find the subreddit's target for my job.   | comments_top100.csv                                         authors_top100.csv                               titles_top100.csv                authors_in_posts_top100.csv               comments_2018-*                                             posts_2018 . |
| [03_cleaning](https://github.com/galligiuly/TFM-Which-subreddit-best-fits-my-post/tree/master/03_cleaning) | Data clieaning and pre-processing                            | comments_posts_2018_V2.csv comments_posts_tokenized_df.pkl             "comments_posts_" + {subreddit} + ".pkl" |
| [04_vectiorization_modelling](https://github.com/galligiuly/TFM-Which-subreddit-best-fits-my-post/tree/master/04_vectiorization_modelling) | Colab where I've tried differents types of vectorizations and combinations with models (only on one subreddit) | *#N/A*                                                       |
| [05_final_modelling](https://github.com/galligiuly/TFM-Which-subreddit-best-fits-my-post/tree/master/05_final_modelling) | Complete DataFrame with 10865638 lineas of comments and posts | model_lr.joblib                                       model_svm.joblib                                     model_rfc_joblib |
| [06_contingency_plan](https://github.com/galligiuly/TFM-Which-subreddit-best-fits-my-post/tree/master/06_contingency_plan) | Reduced amount of data in the DataFrame (<u>mode detail below</u>) | reduced_comments_2018-000000000000 reduced_posts_2018               red_comments_posts.csv red_comments_posts_tokenized.pkl    red_model_lrc.pkl                                 red_model_svm.pkl                               red_model_rfc.pkl                   red_model_lstm_30_batchsize_512_v2.h5 red_model_lstm_30_batchsize_150_10_subreddits.h5 |



## Model results - 1st part

| Jupyter                                | Score                                                        | File output      |
| -------------------------------------- | ------------------------------------------------------------ | ---------------- |
| modelling_LRC_TFIDF                    | precision: 0.49                                                   recall: 0.49                                                              f1-score: 0.49 | model_lr.joblib  |
| modelling_SVM_TFIDF                    | precision: 0.50                                     recall: 0.50                                                  f1-score: 0.50 | model_svm.joblib |
| modelling_RandomForestClassifier_TFIDF | precision: 0.44                                       recall: 0.39                                             f1-score: 0.38 | model_rfc_joblib |





# Subreddits selection

| Category    | subreddit     | subreddit_id |
| ----------- | ------------- | :----------: |
| Health      | Fitness       |      0       |
| Discussion  | IAmA          |      1       |
| Religion    | atheism       |      2       |
| Cute        | aww           |      3       |
| Geography   | europe        |      4       |
| Humor       | funny         |      5       |
| Video Games | gaming        |      6       |
| Movies      | movies        |      7       |
| Sport       | nba           |      8       |
| Politic     | politics      |      9       |
| cience      | science       |      10      |
| Technology  | technology    |      11      |
| Educational | todayilearned |      12      |
| News        | worldnews     |      13      |





# Tools used

- BigQuery
- DataStudio
- Colab
- Jupyter notebook





# Programming lenguages used

- Python

`

- BigQuery SQL





# Libraries

`pandas`

`numpy`

`nltk`

`sklearn`

`gensim`

`xgboost`

`matplotlib`

`altair`

`spacy`

`keras`

`tensorflow`

`seaborn`



# Steps to exectute the job

<u>Please, execute the notebooks following the numeration assigned to them</u>

The fist part of the exploration data is in BigQuery. 

In my Colabs I've been saving the queries used and the correspondig csv result (in case of queries to get finals DataFrames)



Once the the csv with the selected data has been downloaded you can follow the way with the full original data:

- commments: reddit_comments_master/comments_2018-*
- posts: reddit_posts_master/posts_2018

Or the one I've processd in the contingency plan (reducing the dimention of the DataFrame):

- commments: reddit_comments_master/reduced_comments_2018-000000000000
- posts: reddit_posts_master/reduced_posts_2018



I've cleaned it and merged in a final global DataFrame named `comments_posts_2018_V2.csv` (`red_comments_posts.csv ` in the contingency plan)

From here, I've staterd pre-pocessing the data normalizing and tokenizing it. The result of this process has been `comments_posts_tokenized_df.pkl` (`red_comments_posts_tokenized.pkl` in the contingency plan)

As the dimention of the DataFrame, I've splited it into 14 (one for subreddit) and I've been "testing" vectorizations and models on it.

The models used are from the most traditonals one (Logistic Regression and SVM) to algorithm based on decision tree (RandomForest) to finally try recurrent neural networks (LSMT)

The final metric I've used is Accuracy





# Contingency Plan

A DataFrame of 10865638 lines involves a huge job not only in terms of training, managing an setting times but also of computer capabilities.

That's why I preferred to not lose the opportunity to conclude my analysis but to redimension the DataFrame in order to be able to pass through all ML processes with my data.

Colabs and Jupters with 08 numeration are related to the contingency plan where I use the previous categories (subreddits) but with a <u>reduced number of total rows: 2164569</u>.



#### Project organization

| Folder                      | Description                                                  | Key Results (if expected)                               |
| --------------------------- | ------------------------------------------------------------ | ------------------------------------------------------- |
| 06_*08.01_contingency_plan* | Downloead, cleaning, tokenization, vectorization and saving of the new DataFrame | red_comments_posts.csv red_comments_posts_tokenized.pkl |



#### Models results - 2nd part

| Jupyter name                        | Score           | File output                           |
| ----------------------------------- | --------------- | ------------------------------------- |
| 06_08.02_modelling_LRC              | Accuracy: 0.540 | red_model_lrc.pkl                     |
| 06_08.03_modelling_SVM              | Accuracy: 0.542 | red_model_svm.pkl                     |
| 08.04_modelling_RFC                 | Accuracy: 0.445 | red_model_rfc.pkl                     |
| 06_08.05_modelling_LSTM             | Accuracy: 0.544 | red_model_lstm_30_batchsize_512_v2.h5 |
| 06_08.06_modelling_simpletransforer | Colab collapsed | *#N/A*                                |



#### Last change to improve my model

After trainig differents models, seatching the best paramas on each, I can see that the most complicated subreddits to train with a sufficient success are:

| Category    | subreddit     | subreddit_id | difficulty                                                   |
| ----------- | ------------- | :----------: | ------------------------------------------------------------ |
| Discussion  | IAmA          |      1       | Ask Me Anything - every discussion can be planted here so it's like a global subreddit where you can find discussions about every category I've choosen |
| Humor       | funny         |      5       | The mayor data here are pictures and videos with a few comments and almost without "keywords" for my model |
| Educational | todayilearned |      12      | Same as IAmA                                                 |
| News        | worldnews     |      13      | Can find be considered a summary of all the other subreddits I've chosen |



As my best model is LSTM I'll train it <u>without these 4 complicated categories</u> and see if the final results:



#### Models results - 3rd part

| Jupyter name             | Description/score | File output                                      |
| ------------------------ | ----------------- | ------------------------------------------------ |
| 06_*09_LSTM-keras_final* | Accuracy: 0.697   | red_model_lstm_30_batchsize_150_10_subreddits.h5 |



#### Finals subreddits used

| Category    | subreddit  | subreddit_id |
| ----------- | ---------- | :----------: |
| Health      | Fitness    |      0       |
| Religion    | atheism    |      1       |
| Cute        | aww        |      2       |
| Geography   | europe     |      3       |
| Video Games | gaming     |      4       |
| Movies      | movies     |      5       |
| Sport       | nba        |      6       |
| Politics    | politics   |      7       |
| science     | science    |      8       |
| Technology  | technology |      9       |





# Test My project

The only think you have to do is clone this report and execute the Jupyter `Proyect_testing.ipynb` 

You will need keras version 2.3.1 to execute the final model.





# Conclusions

LSTM model has completely win against all the other models.

All my models had a better result compared with the Accuracy on Baseline: 0.07136973635425176

