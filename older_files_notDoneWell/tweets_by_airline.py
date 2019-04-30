import json
import csv

#creating and opening each csv file for each airline, creates header
dd = csv.writer(open("delta.csv", 'w'))
dd.writerow(["date", "text"])
aa = csv.writer(open("american.csv", 'w'))
aa.writerow(["date", "text"])
un = csv.writer(open("united.csv", 'w'))
un.writerow(["date", "text"])
sw = csv.writer(open("southwest.csv", 'w'))
sw.writerow(["date", "text"])

with open('twitter_data/airlines.json') as f:
    for line in f:
        tweet = json.loads(line)
        if ('delta airlines' in tweet['text'] or '@delta' in tweet['text']):
            # if('Mon Mar 18' in tweet['created_at']):
            # print("time: ", tweet['created_at'],"tweet: ", tweet['text'])
            dd.writerow([tweet['created_at'], tweet['text']])
        if ('american airlines' in tweet['text']):
            aa.writerow([tweet['created_at'], tweet['text']])
        if ('united airlines' in tweet['text']):
            un.writerow([tweet['created_at'], tweet['text']])
        if ('southwest airlines' in tweet['text']):
            sw.writerow([tweet['created_at'], tweet['text']])

with open('twitter_data/airlines2.json') as f:
    for line in f:
        tweet = json.loads(line)
        if ('delta airlines' in tweet['text'] or '@delta' in tweet['text']):
            dd.writerow([tweet['created_at'], tweet['text']])
        if ('american airlines' in tweet['text']):
            aa.writerow([tweet['created_at'], tweet['text']])
        if ('united airlines' in tweet['text']):
            un.writerow([tweet['created_at'], tweet['text']])
        if ('southwest airlines' in tweet['text']):
            sw.writerow([tweet['created_at'], tweet['text']])

with open('twitter_data/airlines3.json') as f:
    for line in f:
        tweet = json.loads(line)
        if ('delta airlines' in tweet['text'] or '@delta' in tweet['text']):
            dd.writerow([tweet['created_at'], tweet['text']])
        if ('american airlines' in tweet['text']):
            aa.writerow([tweet['created_at'], tweet['text']])
        if ('united airlines' in tweet['text']):
            un.writerow([tweet['created_at'], tweet['text']])
        if ('southwest airlines' in tweet['text']):
            sw.writerow([tweet['created_at'], tweet['text']])

with open('twitter_data/airlines4.json') as f:
    for line in f:
        tweet = json.loads(line)
        if ('delta airlines' in tweet['text'] or '@delta' in tweet['text']):
            dd.writerow([tweet['created_at'], tweet['text']])
        if ('american airlines' in tweet['text']):
            aa.writerow([tweet['created_at'], tweet['text']])
        if ('united airlines' in tweet['text']):
            un.writerow([tweet['created_at'], tweet['text']])
        if ('southwest airlines' in tweet['text']):
            sw.writerow([tweet['created_at'], tweet['text']])

with open('twitter_data/airlines5.json') as f:
    for line in f:
        tweet = json.loads(line)
        if ('delta airlines' in tweet['text'] or '@delta' in tweet['text']):
            dd.writerow([tweet['created_at'], tweet['text']])
        if ('american airlines' in tweet['text']):
            aa.writerow([tweet['created_at'], tweet['text']])
        if ('united airlines' in tweet['text']):
            un.writerow([tweet['created_at'], tweet['text']])
        if ('southwest airlines' in tweet['text']):
            sw.writerow([tweet['created_at'], tweet['text']])
