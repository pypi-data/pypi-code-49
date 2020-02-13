import os
from .interface import show_user, show_message, show_tweet
from tweepy import TweepError

def dm(api, target, content):
    target = target.replace('@', '')
    user = api.get_user(target)
    api.send_direct_message(user.id, content)


def search(api, query, count):
    results = api.search(query, count=count)
    for result in results:
        show_tweet(result)


def user(api, query, count):
    results = api.search_users(query, count=count)
    for user in results:
        show_user(user)


def post(api, content):
    api.update_status(content)


def chat(api, user):
    try:
        user = user.replace('@', '')
        user = api.get_user(user)
        me = api.me()
        messages = api.list_direct_messages(count=100)
        for message in sorted(messages, key=lambda message: int(message.created_timestamp)):
            if int(message.message_create["sender_id"]) == user.id:
                show_message(message, user)
            if int(message.message_create["sender_id"]) == me.id and int(message.message_create["target"]["recipient_id"]) == user.id:
                show_message(message, me, reverse=True)
    except TweepError:
        print('Sorry, user not found')


def read(api, count):
    public_tweets = api.home_timeline(count=count)
    for tweet in public_tweets:
        show_tweet(tweet)
