#!/usr/bin/python3
"""
This is a module that uses the get HTTP header method to get resources
from the Reddit API
"""
from requests import get


def number_of_subscribers(subreddit):
    """
    This is a function that gets the number of total subscribers for a given
    subreddit using the REDDIT API
    """
    if subreddit is None or type(subreddit) is not str:
        return 0

    user_agent = {'User-Agent': 'Google Chrome Version 115.0.0.0'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    resp = get(url, headers=user_agent, allow_redirects=False)
    result = resp.json()
    if resp.status_code == 404:
        return 0
    return result.get('data').get('subscribers')
