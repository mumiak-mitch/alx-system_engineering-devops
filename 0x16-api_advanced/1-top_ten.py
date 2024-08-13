#!/usr/bin/python3
"""
This module contains the function recurse to fetch all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list of titles of all hot articles
    for a given subreddit.

    :param subreddit: The subreddit to query
    :param hot_list: A list to accumulate the titles of hot articles
    :param after: The 'after' parameter for pagination, default is None
    :return: List of titles of hot articles, or None if subreddit is invalid
    """
    user = {'User-Agent': 'python:hot.articles:v1.0 (by /u/Even-Lingonberry-795)'}
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    params = {'limit': 100, 'after': after}
    
    response = requests.get(url, headers=user, params=params, allow_redirects=False)
    
    if response.status_code != 200:
        return None
    
    data = response.json().get('data', {})
    children = data.get('children', [])
    
    if not children:
        return hot_list if hot_list else None
    
    for post in children:
        hot_list.append(post['data']['title'])
    
    after = data.get('after', None)
    
    if after is None:
        return hot_list
    
    return recurse(subreddit, hot_list, after)


if __name__ == "__main__":
    from sys import argv
    result = recurse(argv[1])
    if result is not None:
        print(len(result))
    else:
        print("None")

