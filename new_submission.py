import praw
import random
import datetime
import time

from bot import generate_comment

reddit = praw.Reddit('bot')
subreddit = reddit.subreddit('notaBotTown')

###un/comment out mannual or posts from other subreddit

#MANNUAL
subreddit.submit(str(generate_comment), text=(str(generate_comment))) 

#POST FROM OTHER 
Subreddit = reddit.subreddit("Cats").top(limit=15)
for post in Subreddit:
    print('title=', post.title)
    reddit.subreddit("notabottown").submit(title=post.title, url=post.url)

