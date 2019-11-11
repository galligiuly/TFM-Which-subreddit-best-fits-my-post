# TFM - Which subreddit best fits my post?
Kschool - Master Data Science


The purpose of my project is train an NLP model that could be able to suggest the fittest subreddit for bloggers who want publish in Reddit.
Given a text from a post or a blog, my NLP model would suggest in which subreddit it could be published


## Project Presentation

https://slides.com/galligiuly/galligiuly/live?context=editing#/


## Data

The following [link](<https://console.cloud.google.com/bigquery?p=fh-bigquery%2F&project=reddit-254019&folder&organizationId>) refers to a collection of 1.7 billion comments profit uploaded on BigQuery and from where I started to analyze and query the data used for my work.

Specifically I've used the tables 
 - fh-bigquery:reddit_comments.
 - fh-bigquery:reddit_posts.

#### reddit_comments

The table of comments gives me a huge amount of text that helps me with my purpose. 

Analyzing `number of comments` and `number of unique authors` that write comments give me a filter used to find the most popular subreddits that grow at a specific time during the life of Reddit and remain still active.

#### reddit_posts

Apart from the analysis of comments I decided to make an analysis for posts because the original post (title and corpus of it) should contain more key words that better identify the subreddit, precious information for my study.

The idea is the same as for the comments, filter the parameters most important that give me the most popular subreddits still actives nowadays.


## Project organization

- statistics to better understand the data 
- data ispection
- data cleaning



# Tools used

- BigQuery
- DataStudio
- Colab
- Jupyter notebook



# Programming lenguages used

- Python
- SQL



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
%%bigquery --project reddit-254019 comments_df
WITH
  q1 AS (
  SELECT
    DISTINCT(subreddit) uniq_subreddit,
    COUNT(DISTINCT(author)) AS num_uniq_authors,
    COUNT(body) AS number_comments,
    ROUND(AVG(score), 2) AS mean_score,
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
    5,
    6
  ORDER BY
    number_comments DESC,
    mean_score DESC)
SELECT
  uniq_subreddit,
  num_uniq_authors,
  number_comments,
  (number_comments - AVG(number_comments) OVER()) / stddev(number_comments) OVER() AS zscore_number_comments,
  mean_score,
  (mean_score - AVG(mean_score) OVER()) / stddev(mean_score) OVER() AS zscore_mean_score,
  year,
  month
FROM
  q1
ORDER BY
  zscore_number_comments DESC,
  zscore_mean_score DESC
```





```sql	
WITH
  q1 AS (
  SELECT
    DISTINCT(subreddit) uniq_subreddit,
    COUNT(DISTINCT(author)) AS num_uniq_authors,
    COUNT(body) AS number_comments,
    AVG(score) AS avg_score,
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
    5,
    6
  ORDER BY
    number_comments DESC,
    avg_score DESC),
  q2 AS (
  SELECT
    uniq_subreddit,
    COUNT(uniq_subreddit) AS present_month
  FROM
    q1
  GROUP BY
    uniq_subreddit )
SELECT
  q1.uniq_subreddit,
  ROUND (avg_score, 2) as avg_score,
  number_comments,
  year,
  present_month
FROM
  q1 
INNER JOIN
  q2
ON
  q1.uniq_subreddit = q2.uniq_subreddit
WHERE 
  present_month = 12
ORDER BY 
  number_comments DESC
 
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



## Final list of subreddit for my model



| Category                | Subreddit     |
| ----------------------- | ------------- |
| Sport                   | nba           |
| Video Games             | Games         |
| Music                   | Music         |
| Technology              | technology    |
| News                    | worldnews     |
| Politic                 | politics      |
| Money                   | Frugal        |
| Discussion              | AskReddit     |
| Humor                   | funny         |
| Educational             | todayilearned |
| Movies                  | movies        |
| Religion                | atheism       |
| Cute                    | aww           |
| Health                  | Fitness       |
| Geography               | europe        |
| Entertainment / Hobbies | DIY           |
| Science                 | science       |
| Books                   | books         |
| Food                    | food          |
| TV                      | television    |




  







