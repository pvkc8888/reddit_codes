# -*- coding: utf-8 -*-
import praw
from reddit_credentials import client_id, client_secret, password, user_agent, username

reddit = praw.Reddit(client_secret=client_secret,
                     client_id=client_id,
                     password=password,
                     username=username,
                     user_agent=user_agent)
# change from books to the subreddit of the submission you are looking to download comments from

subreddit = reddit.subreddit('books')
BigDict = {
    0: {},
    1: {},
    2: {},
    3: {},
    4: {},
    5: {},
    6: {},
    7: {},
    8: {},
    9: {},
    10: {},
    11: {},
    12: {},
    13: {},
    14: {},
    15: {},
    16: {}
}
submission = reddit.submission(url='url_of_the_submission_here')
submission.comment_sort = 'top'  # this sorts the comments by top, you can change it to new or best if you like.
temp = 0
submission.comments.replace_more(limit=None)  # this replaces load more error in the comments.

# # The following loop goes through all the comments and adds them to a nested dictionary, in the following format:
# BigDict = {
#     0: {'1st layer comment id ': [1st layer comment text, upvotes]}
#     1: {'child comment to 1st layer comment id: ': ['child comment to 1st layer comment body', upvotes, parent.id]}
#       and so on for upto 16 layers....
# }


for comment in submission.comments.list():
    count += 1
    parent = str(comment.parent())
    if parent == submission.id:
        BigDict[0][comment.id] = [comment.body, comment.ups]
    else:
        if parent not in BigDict[temp]:
            temp += 1
            BigDict[temp + 1][comment.id] = [comment.body, comment.ups, parent]
        else:
            BigDict[temp + 1][comment.id] = [comment.body, comment.ups, parent]

# The following lines will write the comments on a text file, you can choose if you want to write all the comments, or only those that have atleast 50 upvotes(like I did below) or refer to PRAW documentation for more options.

filename = 'sauce.txt'
with open(filename, 'w') as file:
    for k, v in BigDict.items():
        if len(BigDict[k]) > 0:
            if k == 0:
                for items in v:
                    if BigDict[k][items][1] > 50:
                        try:
                            file.write(BigDict[k][items][0])
                            file.write('  Upvotes: {}\n'.format(BigDict[k][items][1]))
                            file.write('\n')
                        except Exception as e:
                            print(str(e))
            else:
                for items in v:
                    if BigDict[k][items][1] > 50:
                        try:
                            file.write(BigDict[k][items][0])
                            file.write('  Upvotes: {}\n'.format(BigDict[k][items][1]))
                            file.write('\n')
                            print()
                            file.write('The above comment is in reply to: {}\n '.format(BigDict[k - 1][BigDict[k][items][2]][0]))
                        except Exception as e:
                            print(str(e))
            file.write('------' * 20 + '\n')
            file.write('this is the end of level {} of comments \n'.format(k))
            file.write('------' * 20 + '\n')
