# TFM - Which subreddit best fits my post?
Kschool - Master Data Science


The purpose of my project is train an NLP model that could be able to suggest the fittest subreddit for bloggers who want publish in Reddit.
Given a text from a post or a blog, my NLP model would suggest in which subreddit it could be published


## Project Presentation

https://slides.com/galligiuly/galligiuly/live?context=editing#/


## Data

The following (link)[https://bigquery.cloud.google.com/table] refers to a collection of 1.7 billion comments profit uploaded on BigQuery and from where I started to analyze and query the data used for my work.

Specifically I've used the tables 
 - fh-bigquery:reddit_comments.
 - fh-bigquery:reddit_posts.


## Project organization

- statistics to better understand the data 
- data ispection
- data cleaning







#### Queries draft

```sql	
SELECT
  subreddit,
  COUNT(body) AS number_comments,
  EXTRACT(YEAR
  FROM
    TIMESTAMP_SECONDS(created_utc)) year,
  EXTRACT(month
  FROM
    TIMESTAMP_SECONDS(created_utc)) month
FROM
  `fh-bigquery.reddit_comments.2018_*`
GROUP BY
  1,
  3,
  4
ORDER BY
  2 DESC
```





```sql	
SELECT
  score,
  subreddit,
  title,
  selftext
FROM
  [fh-bigquery:reddit_posts.2019_03],
  [fh-bigquery:reddit_posts.2019_04],
  [fh-bigquery:reddit_posts.2019_05]
WHERE
  score > 80
  AND LENGTH(title) > 5
  AND selftext != '[deleted]'
  AND selftext != '[removed]'
  AND selftext != '[ Removed by reddit in response to a copyright notice. ]'
  AND selftext != 'NaN'
  AND selftext != ''
  AND subreddit != 'de'
LIMIT
  10000000
```





```sql
SELECT score, subreddit, body
FROM 
[fh-bigquery:reddit_comments.2019_03],
[fh-bigquery:reddit_comments.2019_04],
[fh-bigquery:reddit_comments.2019_05],

where score > 80
AND length(body) > 10
AND body != '[deleted]'
AND body != '[removed]'
AND body != '[ Removed by reddit in response to a copyright notice. ]'
AND body != 'NaN'
AND body != ''
AND subreddit != 'de'
LIMIT 10000000
```








  







