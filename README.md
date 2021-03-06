# HW_04: ``` NotaCS40Bot``` 

## A. Purrpose
From our very first assignment in this class, I've stuck to a cat theme in my CS40 work. Since Prof. Izbicki said it was only a suggestion to make our bot politically focused, I decided to make my bot cat themed instead! You'll see just how purrfect the bot work is. 😽

#### Files Included
```bot.py``` Main file for NotaCS40bot, that will start leaving comments and replies as specified. \
```new_submission.py``` This file will make new submissions to a subreddit, manually alternating between making posts with text from generate_comment function and sharing posts from other threads.\
```vote_bot.py``` Vote bot will support postive comments about 'kittens' and downvote negative comments about cats. 

## B. Favorite Comment
My favorite threads for my bot to comment on were those about cats. NotaCS40bot responded to many cat related posts that were shared in various subreddits. A screenshot of a funny reply is attached below. 
<img width='70%' src=Screenshot_bot.png />


My bot's comments on this [this thread](https://www.reddit.com/r/redditdev/comments/7l9xju/how_to_post_new_threads_with_praw/) seemed pretty hilarious, so I'm sharing it as my favorite. \
[Replying to a political post about Obama with a silly sentence about kittens](https://old.reddit.com/r/BotTownFriends/comments/r3kpmk/i_love_the_way_her_little_ears_move_in_rhythm/hmc9ob0/) is the comment that makes me smile most.
 


## C. Bot Counter

```
len(comments)= 742
len(top_level_comments)= 286
len(replies)= 456
len(valid_top_level_comments)= 286
len(not_self_replies)= 452
len(valid_replies)= 452
========================================
valid_comments= 738
========================================
```

## D. Score

My HW_04 : NotaCS40bot should be awarded points as follows:


| Points | Task |
| :-: | --- |
| +3 |(task 0): get a list of all of the comments in the submission |
| +3 | (task 1): filter all_comments to remove comments that were generated by your bot |
|+3 |(task 2): if you have not made any comment in the thread, then post a top level comment
|+3 |(task 3): filter the not_my_comments list to also remove comments that you've already replied to
|+3 |(task 4): randomly select a comment from the comments_without_replies list
|+3 |(task 5): select a new submission for the next iteration
|+2 |Created a repository|

| Points | Optional Tasks |
| :-: | --- |
|+2 |1. Getting at least 100 valid comments posted.|
|+2 |2. Getting at least 500 valid comments posted.|
|   |3. Getting at least 1000 valid comments posted.|
|+2 |4. Make your bot create new submission posts instead of just new comments. With at least 200 submissions, some of which should be self posts and some link posts.|
|   |5. Create an "army" of 5 bots that are all posting similar comments.|
|   |6. Instead of having your bot reply randomly to posts, make your bot reply to the most highly upvoted comment in a thread that it hasn't already replied to.|
|+2 |7. Have your bot upvote any comment or submission that mentions your favorite candidate (or downvote submission mentioning a  you do not like).|
|+2 |7.5 You may earn an additional two points if you use the TextBlob sentiment analysis library to determine the sentiment of all the posts that mention your favorite candidate. If the comment/submission has positive sentiment, then upvote it; if the comment/submission has a negative sentiment, then downvote it.|

| **Total Points** | **Assignment** |
| :-: | --- |
| **30** |**Homework_04** |

