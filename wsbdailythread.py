# -*- coding: utf-8 -*-
import praw

from reddit_credentials import client_id, client_secret, password, user_agent, username

reddit = praw.Reddit(client_secret='QQWp0t3_g9cPKG2EUlBpt0fgRpQ',
                     client_id='P4hYgtV_Yw1LzQ',
                     # password=password,
                     # username=username,
                     user_agent='NoHopeInWorld')

# submission = reddit.subreddit('wallstreetbets').hot(limit=1)
# print(submission.title)
while True:
    for submission in reddit.subreddit('wallstreetbets').hot(limit=1):
        submission.comment_sort = 'new'
        submission.comments.replace_more(limit=0)
        for new_comment in submission.comments.list():
            print(new_comment.body)
            print('............................')
