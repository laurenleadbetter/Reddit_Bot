import praw
import random
import datetime
import time

# FIXME:
# copy your generate_comment function from the madlibs assignment here


madlibs = [
    "[CATS] are [WONDERFUL] [PETS].  They have all kinds of [TALENTS], like [SKILL].", \
    "[EVERYONE] should have a cat! [OTHER] are [BAD] pets, not as [WONDERFUL] as cats, they dont even [ACT_CAT].", \
    "[AREA] currently has an excess of [CATS]. You can [TAKE] a [CAT] from [SHELTER] today.", \
    "If I were a [CAT], I would be a [FAT] [COLOR] tabby. I would [EAT], and [SLEEP], and be lazy. That's all.",\
    "[LOOK] some of the greats like [GREAT1], [GREAT2], and [GREAT3] just to name a few. What do they all have in common? They're cats!",\
    "[INSTITUTION] ought to replace the president's dog with a cat! Imagine how [WONDERFUL] that would be. Maybe we can stage a [COUP], and our leader will be [GREAT1]...on second thought, maybe [GREAT2]. Purrfect. "
    ]

replacements = {
    'CATS' : ['Cats', 'Kitty Kats', 'Kittens'],
    'WONDERFUL' : ['wonderful', 'splendid','perfect'],
    'PETS' : ['pets', 'companions','furry friends'],
    'TALENTS' : ['special talents', 'super skills ', 'amazing activities'],
    'SKILL'  : ['hunting', 'leaping','being adorable'],
    'OTHER' : ['Dogs', 'Fish', 'Lizards','Snakes'],
    'BAD' : ['bad', 'insufficient', 'not great'],
    'ACT_CAT' : ['meow', 'derp around','purrrr'],
    'EVERYONE' : ['Everyone', 'You', 'All people'],
    'AREA' : ['Southern California', 'The Inland Empire', 'Greater Los Angeles area'],
    'SHELTER' : ['Petco', 'Ontario Rescue', 'Foothills SPCA'],
    'TAKE' : ['adopt','foster','take home'],
    'CAT' : ['cat', 'kitten', 'wonderful little cat'],
    'FAT' : ['fat', 'large', 'pillow-shaped'],
    'COLOR' : ['orange', 'gray', 'white'],
    'EAT' : ['eat', 'snack', 'munch'],
    'SLEEP' : ['sleep', 'nap', 'doze off'],
    'SECRET' : ['secret', 'key', 'most critical element'],
    'LOOK' : ['Let''s'' consider','Look at', 'Let''s'' admire'],
    'GREAT1' : ['The Sphinx', 'Tom from Tom & Jerry', 'The Cheshire Cat'],
    'GREAT2' : ['Garfield', 'Sailor Moon', 'Nayan Cat'],
    'GREAT3' : ['Mayor Stubs', 'Keyboard Cat', 'the cast of the musical CATS'],
    'INSTITUTION' : ['CMC', 'Claremont McKenna','CMC'],
    'COUP' : ['coup', 'revolt','upheaval']

    }




def generate_comment():
    '''
    This function generates random comments according to the patterns specified in the `madlibs` variable.

    To implement this function, you should:
    1. Randomly select a string from the madlibs list.
    2. For each word contained in square brackets `[]`:
        Replace that word with a randomly selected word from the corresponding entry in the `replacements` dictionary.
    3. Return the resulting string.

    For example, if we randomly seleected the madlib "I [LOVE] [PYTHON]",
    then the function might return "I like Python" or "I adore Programming".
    Notice that the word "Programming" is incorrectly capitalized in the second sentence.
    You do not have to worry about making the output grammatically correct inside this function.
    '''
    s= random.choice(madlibs)
    for k in replacements.keys():
        s= s.replace ('['+k+']', random.choice(replacements[k]))
    return(s)

# connect to reddit 
reddit = praw.Reddit('bot')

# select a "home" submission in the /r/BotTown subreddit to post to,
# and put the url below

# submission_url = 'https://www.reddit.com/r/NotaBottown/comments/r1e9ku/this_is_the_first_post/'
submission_url = 'https://old.reddit.com/r/BotTown2/comments/r0yi9l/main_discussion_thread/'

submission = reddit.submission(url=submission_url)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once
while True:

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions
    #submission.comments.replace_more(limit=None)
    submission.comments.replace_more(limit=None)
    all_comments = submission.comments.list()

    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    print('len(all_comments)=',len(all_comments))

    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    not_my_comments = []
    for comment in all_comments:
        if str(comment.author) != 'NotaCS40bot':
            not_my_comments.append(comment)

    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
    print('len(not_my_comments)=',len(not_my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (your bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)
    print('has_not_commented=',has_not_commented)

    if has_not_commented == True:
        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # a top level comment is created when you reply to a post instead of a message
        text =  generate_comment()
        submission.reply(text)
        pass

    else:
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
        comments_without_my_replies = []
        for comment in not_my_comments:
            replies = comment.replies
            this_works = True 
            for reply in replies:
                if reply.author != 'NotaCS40bot':
                    pass 
                else:
                    this_works = False
                    break 
            if this_works == True:
                comments_without_my_replies.append(comment)
            

        print('len(comments_without_my_replies)=',len(comments_without_my_replies))
    

            # if str(comment.replies.author) != 'NotaCS40bot':
            #     comments_without_replies.append(comment)


        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly
        print('len(comments_without_replies)=',len(comments_without_my_replies))

        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # these will not be top-level comments;
        # so they will not be replies to a post but replies to a message
        if comments_without_my_replies:
            comment = random.choice(comments_without_my_replies)
            try: 
                comment.reply(generate_comment())
            except praw.exceptions.RedditAPIException:
                print('not replying to a comment that has been deleted')



    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should be randomly selected from the 5 hottest submissions
 
    submission = random.choice(list(reddit.subreddit("bottown2").hot(limit=15))) 
    print('random top 5 thread=', submission.title)
    
    
    
    #add top 5 threads in bottown reddit - on documentation# )

    # We sleep just for 1 second at the end of the while loop.
    # This doesn't avoid rate limiting
    # (since we're not sleeping for a long period of time),
    # but it does make the program's output more readable.
    time.sleep(15)
