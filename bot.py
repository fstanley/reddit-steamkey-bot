from urllib.parse import quote_plus

import praw
import re
from pushbullet import Pushbullet

# Input your pushbullet API key here
pb = Pushbullet('')

productKey = re.compile(r'(?<![a-zA-Z0-9\-\/])(?=.*\d)([A-Z0-9!?#*@&]{5}-[A-Z0-9!?#*@&]{5}-[A-Z0-9!?#*@&]{5})')

def main():
    # Input your reddit API and user credintials here
    reddit = praw.Reddit(
        client_id='',
        client_secret='',
        user_agent='',
        username='',
        password='')

    subreddit = reddit.subreddit('All')
    for comment in subreddit.stream.comments():
        process_comment(comment)

def process_comment(comment):
    body = comment.body
    match = productKey.search(body)
    if match:
        link = 'http://reddit.com' + comment.permalink
        print(body)
        print(link)
        push = pb.push_link("Steam Key", link)
        print('------------------------------\n')
        print('\a')


if __name__ == '__main__':
    main()