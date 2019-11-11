# Database schema



The data set used is a pubblic collection of 1.7 billion reddit comments and posts loaded on BigQuery in this [link](https://console.cloud.google.com/bigquery?p=fh-bigquery%2F&project=reddit-254019&folder&organizationId)



#### 1 - Comments table - fh-bigquery:reddit_comments.

Here below the description of the columns:



| Column name            | Column Description                                           | Type    |
| ---------------------- | ------------------------------------------------------------ | ------- |
| body                   | Corpus of the comment                                        | STRING  |
| score_hidden           | Setting where comments in the subreddit will have their score hidden for the specified number of minutes, after which the score will appear as normal | BOOLEAN |
| archived               | All posts are automatically archived after 6 month and can no longer be commented on | BOOLEAN |
| name                   | Full name of the submission                                  | STRING  |
| author                 | Username of the author of the comment                        | STRING  |
| author_flair_text      | Only for some subreddit there is the possibility to add text, or in some cases icons from a list, to the  name | STRING  |
| downs                  | Number of downvotes                                          | INTEGER |
| created_utc            | Date when the submission was created                         | INTEGER |
| subreddit_id           | Id that univocally identify the subreddit                    | STRING  |
| link_id                | Id that univocally identify the link                         | STRING  |
| parent_id              | Id that univocally identify the name of the thing being replied to | STRING  |
| score                  | Or Karma, it show the puntuation when people upvote your posts and comments, you lose it when you get downvoted | INTEGER |
| retrieved_on           | Date when the post has been retrieved                        | INTEGER |
| controversiality       | If an item falls within a boundary of upvote ratios, it's controversial | INTEGER |
| gilded                 | Giving an Award, or "gilding", is a way to show appreciation for an exceptional contribution to Reddit. This distinguishes it with an Award for all to see, and some even grant the honoree special bonus benefits | INTEGER |
| id                     | Id that univocally identify the subreddit                    | STRING  |
| subreddit              | Name of the subreddit                                        | STRING  |
| ups                    | Number of upvotes                                            | INTEGER |
| distinguished          | When a moderator removes a submission for violating the rules of their subreddit, they often post a distinguished comment on the link explaining why it was removed | STRING  |
| author_flair_css_class | CSS (Cascading Style Sheets) class for author´s flair        | STRING  |





#### 2 - 	Posts table - fh-bigquery:reddit_posts.

Here below the description of the columns:



| Column name            | Column description                                           | Type    |
| ---------------------- | ------------------------------------------------------------ | ------- |
| created_utc            | Date when the submission was created                         | INTEGER |
| subreddit              | Name of the subreddit                                        | STRING  |
| author                 | Username of the author of the post                           | STRING  |
| domain                 | Domain's name for each subreddit                             | STRING  |
| url                    | The URL the submission links to, or the permalink if a self-post | STRING  |
| num_comments           | count of comments                                            | INTEGER |
| score                  | Or Karma, it show the puntuation when people upvote your posts and comments, you lose it when you get downvoted | INTEGER |
| ups                    | Number of upvotes                                            | INTEGER |
| downs                  | Number of downvotes                                          | INTEGER |
| title                  | The title of the submission                                  | STRING  |
| selftext               | Corpus of the post                                           | STRING  |
| saved                  | BOOLEAN that indicate if the post is saved                   | BOOLEAN |
| id                     | Id that univocally identify the subreddit                    | STRING  |
| from_kind              | Code of tracking the post                                    | STRING  |
| gilded                 | Giving an Award, or "gilding", is a way to show appreciation for an exceptional contribution to Reddit. This distinguishes it with an Award for all to see, and some even grant the honoree special bonus benefits | INTEGER |
| from                   | Code of tracking the post                                    | STRING  |
| stickied               | Way to highlight a post. Mods can do that by making sticky the post and it will be always the top post on the subreddit's frontpage, independent of votes and time since posting | BOOLEAN |
| retrieved_on           | Date when the post has been retrieved                        | INTEGER |
| over_18                | BOOLEAN that idicate if the subreddit is for over_18 year hold. Whether or not the submission has been marked as NSFW | BOOLEAN |
| thumbnail              | In the post has been submitted a imgur.com link              | STRING  |
| subreddit_id           | Id that univocally identify the subreddit                    | STRING  |
| hide_score             | Subreddit settings where the score is not showed             | BOOLEAN |
| link_flair_css_class   | CSS (Cascading Style Sheets) class for author´s flair        | STRING  |
| author_flair_css_class | CSS (Cascading Style Sheets) class for author´s flair        | STRING  |
| archived               | All posts are automatically archived after 6 month and can no longer be commented on | BOOLEAN |
| is_self                | The post doesn't link outside of reddit                      | BOOLEAN |
| from_id                | Id of tracking the post                                      | STRING  |
| permalink              | "Copy Link Location" of the post                             | STRING  |
| name                   | Full name of the submission                                  | STRING  |
| author_flair_text      | Only for some subreddit there is the possibility to add text, or in some cases icons from a list, to the  name | STRING  |
| quarantine             | A community will be Quarantined on Reddit when it deem its content to be extremely offensive or upsetting to the average redditor. The purpose of quarantining a community is to prevent its content from being accidentally viewed by those who do not wish to do so. | BOOLEAN |
| link_flair_text        | The link flair’s text content (sort of like a submission category within a subreddit), or None if not flaired. | STRING  |
| distinguished          | When a moderator removes a submission for violating the rules of their subreddit, they often post a distinguished comment on the link explaining why it was removed | STRING  |





