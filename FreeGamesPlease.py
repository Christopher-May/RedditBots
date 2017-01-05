# -*- coding: utf-8 -*-
"""
@author: Christopher May
"""
import time
import praw

#Checks if reddit submission is about free games and isnt already searched
#submission is the reddit article and already_done is a list of submission.id
# returns true if the submission is related to free games and hasnt already been looked at
def check_condition(submission,already_done):
    gameWords = ['free', '%100','100%']
    title = submission.title.lower()
    
    freeGame = any(string in title for string in gameWords)
    if submission.id not in already_done and freeGame:
        return True

#Sends me a message on reddit if free game is found
#submission is the reddit article
#
def send_message(submission):
    message = '[Have a free GAME!!](%s)' % submission.short_link
    r.send_message('jajakaha','Here',message)


if __name__ is '__main__': 
    r = praw.Reddit(user_agent='Free games monitor by ChrisM')
    r.login('username','password') #replace username and password with actual uname and password
    already_done = []
    
    while True:
        #gets subreddits and puts them into a list
        subreddits = [r.get_subreddit('gamedeals'),r.get_subreddit('games')]
        
        for subreddit in subreddits:
            for submission in subreddit.get_hot(limit=15):
                if check_condition(submission,already_done):
                    already_done.append(submission.id)
                    send_message(submission)
                    
        #goes to sleep then starts up again
        time.sleep(1800)
        

