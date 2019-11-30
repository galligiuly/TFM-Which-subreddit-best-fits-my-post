# TFM - Which subreddit best fits my post?
Kschool - Master Data Science

The purpose of my project is train an NLP model that could be able to suggest the fittest subreddit for bloggers who want publish in Reddit.
Given a text from a post or a blog, my NLP model would suggest in which subreddit it could be published

_Multy-Class Classification problem_



## Project Presentation

https://slides.com/galligiuly/galligiuly/live?context=editing#/



## Data

The following [link](<https://console.cloud.google.com/bigquery?p=fh-bigquery%2F&project=reddit-254019&folder&organizationId>) refers to a collection of 1.7 billion comments profit uploaded on BigQuery and from where I started to analyze and query the data used for my work.

Specifically I've used the tables 

_public data_

 - fh-bigquery:reddit_comments.
 - fh-bigquery:reddit_posts.

_my tables for the project_

*  reddit-254019
* reddit-master

#### reddit_comments

The table of comments gives me a huge amount of text that helps me with my purpose. 

Analyzing `number of comments` and `number of unique authors` that write comments, give me a filter used to find the most popular subreddits that grow at a specific time during the life of Reddit and remain still active.

#### reddit_posts

Apart from the analysis of comments I decided to make an analysis for posts because the original post (title and corpus of it) should contain more key words that better identify the subreddit, precious information for my study.

The idea is the same as for the comments, filter the parameters most important that give me the most popular subreddits still actives nowadays.

#### Objective

What I need is to find the subreddits with a constant popularity during the years.

The most accurate way is to find a function that, once the data has been normalized, is capable to suggest me the subreddit most populars in order of number of comments, number of unique authors that write on it and the score assigned. This is an idea that I'll develop in the future, with more time.

For now, I'll just explore my data, analyzing number of wrintng authors, number of comments and score, comparing them and searching a criteria for my selection.



## GCP

The projects on my GCP I've created for this job are:

*  reddit-254019
* reddit-master



In **reddit-master** (where are stored all results that metters) I've created Bucket for:

| Bucket name            | Bucket data                                                  |
| ---------------------- | ------------------------------------------------------------ |
| reddit_comments_master | All differents results of queries from `fh-bigquery:reddit_comments.` |
| reddit_posts_master    | All differents results of queries from `fh-bigquery:reddit_posts.` |
| reddit_final_results   | DataFrames that I have been saving in all the steps to import into the next Colab. |
| reddit_models          | Last models of my job.                                       |




## Project organization

| Folder                                                       | Description                                                  | Key Results (if expected)                                  |
| :----------------------------------------------------------- | ------------------------------------------------------------ | ---------------------------------------------------------- |
| [00_images](https://github.com/galligiuly/TFM-Which-subreddit-best-fits-my-post/tree/master/00_images) | All images used in this project                              | #N/A                                                       |
| [01_data](https://github.com/galligiuly/TFM-Which-subreddit-best-fits-my-post/tree/master/01_data) | csv's results of statistic to better understand the data that, for dimentions, could save in GitHub | Statistic results                                          |
| [02_inspection](https://github.com/galligiuly/TFM-Which-subreddit-best-fits-my-post/tree/master/02_inspection) | Process applied to find the subreddit's target for my job.   | comments_2018-*  posts_2018 .                              |
| [03_cleaning](https://github.com/galligiuly/TFM-Which-subreddit-best-fits-my-post/tree/master/03_cleaning) | Data clieaning and pre-processing                            | comments_posts_2018_V2.csv comments_posts_tokenized_df.pkl |
| [04_vectiorization_modelling](https://github.com/galligiuly/TFM-Which-subreddit-best-fits-my-post/tree/master/04_vectiorization_modelling) | Colab where I've tried differents types of vectorizations and combinations with models (only on one subreddit) | #N/A                                                       |
| 05_final_modelling                                           | Appling all modes to all my data.                            |                                                            |
| modelling_LRC_TFIDF                                          | precision: 0.49                                       recall: 0.49                                      f1-score: 0.49 | model_lr.joblib                                            |
| modelling_SVM_TFIDF                                          | precision: 0.50                                     recall: 0.50                                      f1-score: 0.50 | model_svm.joblib                                           |
| modelling_RandomForestClassifier_TFIDF                       | precision: 0.49                                       recall: 0.49                                      f1-score: 0.49 |                                                            |
| modelling_NB_TFIDF.ipynb                                     | *precision: 0.49                                       recall: 0.49                                      f1-score: 0.49* |                                                            |
|                                                              |                                                              |                                                            |



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

`numpy`

`nltk`

`sklearn`

`gensim`

`xgboost`

`matplotlib`

`altair`

`spacy`



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



# Steps to exectute the job

<u>Please, execute the notebooks following the numeration assigned to them</u>

The fist part of the exploration data is in BigQuery. 

In my Colabs I've been saving the queries used and the correspondig csv result (in case of queries to get finals DataFrames)

Once the the csv with the selected data has been downloaded

- commments: reddit_comments_master/comments_2018-*
- posts: reddit_posts_master/posts_2018 .

I've cleaned it and merged in a final global DataFrame named `comments_posts_2018_V2.csv`

From here, I've staterd pre-pocessing the data normalizing and tokenizing it. The result of this process has been `comments_posts_tokenized_df.pkl`

As the dimention of the DataFrame, I've splited it into 14 (one for subreddit) and I've been "testing" vectorizations and models on it.



# Contingency Plan

A DataFrame of 10865638 lineas involves a huge job not only in terms of training, managing an setting times but also of computer capabilities.

That's why I preferred to not lose the opportunity to conclude my analysis but to redimension the DataFrame in order to be able to pass through all ML processes with my data.

Colabs and Jupters with 08 numeratin are realte to the contingency plan rapresented with all the prevous categories (subreddits) but with a reduced number of rows: 2164569.



| Jupyter name              | Description/score                                            | File output                                             |
| ------------------------- | ------------------------------------------------------------ | ------------------------------------------------------- |
| 06_08.01_contingency_plan | Downloead, cleaning, tokenization, vectorization and saving of the new DataFrame | red_comments_posts.csv red_comments_posts_tokenized.pkl |
| 08.02_modelling_LRC       | precision: 0.54                                       recall: 0.54                                          f1-score: 0.54 | red_model_lrc.pkl                                       |
| 08.03_modelling_SVM       |                                                              |                                                         |
| 08.04_modelling_RFC       |                                                              |                                                         |
| 08.05_modelling_LSTM      |                                                              |                                                         |
|                           |                                                              |                                                         |



#### Last change to improve my model

After trainig differents models, seatching the best paramas for each, I can see that the most complicated subreddits to train with a sufficient success are:



| Category    | subreddit     | subreddit_id | difficulty                                                   |
| ----------- | ------------- | :----------: | ------------------------------------------------------------ |
| Discussion  | IAmA          |      1       | Ask Me Anything - every discussion can be planted here so it's like a global subreddit where you can find discussions about every category I've choosen |
| Humor       | funny         |      5       | The mayor data here are pictures and videos with a few comments and almost without "keywords" for my model |
| Educational | todayilearned |      12      | Same as IAmA                                                 |
| News        | worldnews     |      13      | Can find be considered a summary of all the other subreddits I've chosen |

As my best model is LSTM I'll train it without these 4 categories and see if the final results:



| Jupyter name | Description/score | File output |
| ------------ | ----------------- | ----------- |
|              |                   |             |

