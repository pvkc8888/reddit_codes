# -*- coding: utf-8 -*-
import praw
import smtplib
import time

from email.mime.text import MIMEText


from reddit_credentials import client_id, client_secret, password, user_agent, username

reddit = praw.Reddit(client_secret=client_secret,
                     client_id=client_id,
                     password=password,
                     username=username,
                     user_agent=user_agent)

# change the name_of_the_subreddit to the subreddit that you want.
# Bonus Tip: if you want notifications from mutliple subreddits, it can be done by adding '+' between the names of subreddits, e.g: 'askreddit+ama' will give notifications from both r/AskReddit and r/AMA

subreddit = reddit.subreddit('name_of_the_subreddit')
while True:
    for submission in subreddit.stream.submissions():
        try:
            # you can change the text of the email to your liking.
            msg = MIMEText('''
                New submission on r/{} :
                Title: {}
                Author: {}
                URL: {}'''.format(submission.subreddit, submission.title, submission.author, submission.url))
            # print(msg)
            msg['Subject'] = submission.title  # replace submission.title with the subject that you want in your email.

            msg['From'] = "alphabeta@gmail.com"  # sender's email
            msg['Reply-to'] = "alphabeta@gmail.com"  # reply to email
            msg['To'] = "betalpha@gmail.com"  # receiver's email
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login('gmail_username_here', 'gmail_password_here')
            server.sendmail('senders_email', 'receivers_email', str(msg))
            server.close()
            #time.sleep(1 * 60)
        except Exception as e:
            print(str(e))
