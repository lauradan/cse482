import tweepy
from tweepy import OAuthHandler
from tweepy import API

C_KEY = ''
C_SECRET = ''
A_TOKEN_KEY = ''
A_TOKEN_SECRET = ''

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN_KEY, A_TOKEN_SECRET)
api = tweepy.API(auth)

keyword = '@delta'
keyword2 = 'delta airlines'
keyword3 = 'american airlines'
keyword4 = 'united airlines'
keyword5 = 'southwest airlines'
posts = api.search(q=keyword,count=3200)
posts2 = api.search(q=keyword2,count=3200)
posts3 = api.search(q=keyword3,count=3200)
posts4 = api.search(q=keyword4,count=3200)
posts5 = api.search(q=keyword5,count=3200)

with open('delta.csv', 'w') as f:
    for tweet in posts:
        f.write(str(tweet.created_at))
        f.write(str(tweet.text.encode("utf-8")))
        f.write('\n')
    for tweet in posts2:
        f.write(str(tweet.created_at))
        f.write(str(tweet.text.encode("utf-8")))
        f.write('\n')
with open('american.csv', 'w') as f:
    for tweet in posts3:
        f.write(str(tweet.created_at))
        f.write(str(tweet.text.encode("utf-8")))
        f.write('\n')
with open('united.csv', 'w') as f:
    for tweet in posts4:
        f.write(str(tweet.created_at))
        f.write(str(tweet.text.encode("utf-8")))
        f.write('\n')
with open('southwest.csv', 'w') as f:
    for tweet in posts5:
        f.write(str(tweet.created_at))
        f.write(str(tweet.text.encode("utf-8")))
        f.write('\n')