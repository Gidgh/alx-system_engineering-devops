#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    # Set a custom User-Agent to avoid any issues with Reddit's API
    headers = {'User-Agent': 'My Reddit API Client'}

    # Construct the URL to query the subreddit's information
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        try:
            # Parse the JSON response
            data = response.json()
            # Extract the number of subscribers from the response
            subscribers = data['data']['subscribers']
            return subscribers
        except KeyError:
            # If the necessary key is not found in the response JSON
            return 0
    else:
        # If the subreddit is invalid or there's an issue with the request
        return 0

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        subscribers = number_of_subscribers(subreddit)
        print("{:d}".format(subscribers))

