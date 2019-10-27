# Data statistic



The data set used is a pubblic collection of 1.7 billion reddit comments and posts loaded on BigQuery in this [link](https://console.cloud.google.com/bigquery?p=fh-bigquery%2F&project=reddit-254019&folder&organizationId)

###  Comments statistic

The data we consider relevant to select the subreddit to be analyzed is related to the number of comments  and the average of the score in each subreddit.

#### Count of comments

We will filter the top 100 subreddits with more comments per month using the following query:

```SQL	
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



