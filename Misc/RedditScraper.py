import praw

# Define user agent
user_agent = "TikTokSaaS"

# Create an instance of reddit class
reddit = praw.Reddit(username="Objective_Ad7158",
                     password="Ferbiscool2!",
                     client_id="oTWvTeP37ydTpslHTUDRZQ",
                     client_secret="0-8gGOzvYqiQylNjBKqPZf5Vio_7eg",
                     user_agent=user_agent
)

# Create sub-reddit instance
subreddit_name = "LongDistance"

# Gets title of hot posts in category
hot_posts = reddit.subreddit(subreddit_name).hot(limit=10)
for post in hot_posts:
    print(post.title)

# Reddit Submission Body Text
submission = reddit.submission(url="https://www.reddit.com/r/LongDistance/comments/zx5def/my_20f_boyfriend_20m_emotionally_cheated_on_me_i/")
print(submission.selftext)
