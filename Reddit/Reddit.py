import praw
import pandas as pd

user_agent = "TikTokSaaS"

# Create an instance of reddit class
reddit = praw.Reddit(username="Objective_Ad7158",
                     password="Ferbiscool2!",
                     client_id="oTWvTeP37ydTpslHTUDRZQ",
                     client_secret="0-8gGOzvYqiQylNjBKqPZf5Vio_7eg",
                     user_agent=user_agent
                     )

def main():
    sub = input('Enter Subreddit: ')
    posts = []
    subreddit = reddit.subreddit(sub)
    for post in subreddit.top(time_filter="week", limit=26):
        posts.append(
            [post.title, post.score, post.url, post.selftext])
    posts = pd.DataFrame(posts, columns=['title', 'score', 'url', 'body'])
    print(posts['score'])



if __name__ == "__main__":
    main()