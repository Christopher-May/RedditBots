# -*- coding: utf-8 -*-
"""
@author: Christopher May
"""
import praw
from yahoo_finance import Share


def bot_action(name,c, verbose=True, respond=True):
    share = Share(name.upper())
    if share.get_price != 'none':
        if verbose:
            print("| Name | Price | Volume | Book Data | 200 day moving avg |\n| {n} | {p} | {v} | {b} | {t} |".format(n=share.get_name(),p=share.get_price(),v=share.get_volume(),b=share.get_book_value(),t=share.get_200day_moving_avg()))
        if respond:
            message = "| Name | Price | Volume | Book Data | 200 day moving avg | \n:--:|:--:|:--:|:--:|:--:|\n {n}| {p}| {v}| {b}| {t}".format(n=share.get_name(),p=share.get_price(),v=share.get_volume(),b=share.get_book_value(),t=share.get_200day_moving_avg())
            c.reply(message)
            
def check_condition(c):
    text = c.body
    words = text.split()
    for word in words:
        if '$?' in word[:2]:
                bot_action(word[2:],c)

if __name__ is '__main__':
    
    r = praw.Reddit(user_agent = 'Stocks Moniter by ChrisM')
    
    r.login('jajakaha','shhhh')
    
    for c in praw.helpers.comment_stream(r,'chrisisgod'):
        check_condition(c)
