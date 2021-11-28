import praw
from textblob import TextBlob

reddit = praw.Reddit('bot')


for submission in list(reddit.subreddit('cats').top(time_filter='all')):
    blob = TextBlob(str(submission.title))
    polarity = blob.sentiment.polarity
    submission.comments.replace_more(limit=None)


##looking for term 
    if 'kitten' in submission.title.lower():
        if polarity > 0:
            submission.upvote()
            print('upvoted submission')
        else:
            submission.downvote()
            print('downvoted submission')
    if 'cat' in submission.title.lower():
        if polarity < 0:
            submission.upvote()
            print('upvoted submission')
        else:
            submission.downvote()
            print('downvoted submission')
    all_comments = submission.comments.list()


##looking for polarity pos/neg
    for comment in submission.comments.list():
        blob = TextBlob(str(comment.body))
        if 'kitten' in comment.body.lower():
            if polarity > 0:
                comment.upvote()
                print('upvoted comment')
            else:
                comment.downvote()
                print('downvoted comment')
        if 'cat' in comment.body.lower():
            if polarity < 0:
                comment.upvote()
                print('upvoted comment')
            else:
                comment.downvote()
                print('downvoted comment')