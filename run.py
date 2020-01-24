#!/usr/bin/python3
import time
import datetime
import twitter

SRC_FILE = 'unique_drugnames_943.txt'
DST_FILE = 'posted_drugnames.txt'
TWITTER_CSV = 'twitter-credentials.csv'


def get_twitter_api():
    with open('twitter-credentials.csv', 'r') as fp:
        data = fp.readlines()
        data = [line.rstrip('\n') for line in data]
    try:
        api = twitter.Api(consumer_key=data[0],
                          consumer_secret=data[1],
                          access_token_key=data[2],
                          access_token_secret=data[3])
        return api
    except Exception as e:
        print(e)
        return None


def get_unused_drugname():
    # get all previously posted drugnames
    with open(DST_FILE, 'r') as fp:
        posted_names = fp.readlines()
        posted_names = [name.rstrip('\n') for name in posted_names]

    # get all names
    with open(SRC_FILE, 'r') as fp:
        all_names = fp.readlines()
        all_names = [name.rstrip('\n') for name in all_names]

    # get an unused name and deposit it in posted names
    unused_names = list(set(all_names).difference(set(posted_names)))
    name_to_post = unused_names[0]

    new_posted_names = posted_names + [name_to_post]
    new_posted_names = [name + '\n' for name in new_posted_names]
    with open(DST_FILE, 'w') as fp:
        fp.writelines(new_posted_names)
    return name_to_post


def send_tweet(drugname):
    # clean up name
    clean_drugname = drugname.upper()
    clean_drugname = clean_drugname[0] + clean_drugname[1:].lower()
    tweet_text = f'Drug of the day: {clean_drugname}'

    # post tweet
    print(f'Posting text: {tweet_text}')
    api = get_twitter_api()
    status = api.PostUpdate(tweet_text)
    print(f'{status.user.name} just posted: {status.text}')
    return True


def handle_post_tweet():
    drugname = get_unused_drugname()
    result = send_tweet(drugname)
    if result:
        print('Successfully posted tweet.')


if __name__ == "__main__":
    # if for some reason this script is still running
    # after 2 years, we'll stop it.
    for i in range(0, 365 * 2):
        # sleep until 12PM Pacific = 7PM UTC
        now = datetime.datetime.today()
        future = datetime.datetime(now.year, now.month, now.day, 19, 0)
        if now.hour >= 19:
            future += datetime.timedelta(days=1)
        time.sleep((future - now).seconds)

        # finish sleeping, post a tweet!
        print('=' * 20)
        print(f'The time is now {datetime.datetime.today()}')
        print('Posting tweet...')
        handle_post_tweet()

        time.sleep(65 * 60)  # sleep 1 hour after posting!

