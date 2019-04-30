import csv
#import pandas as pd
import string
n318=n319=n409=n421=n422=n423=n424=n426=0
p318=p319=p409=p421=p422=p423=p424=p426=0
dd = csv.writer(open("delta_sent.csv", 'w'))
aa = csv.writer(open("amer_sent.csv", 'w'))
un = csv.writer(open("unit_sent.csv", 'w'))
sw = csv.writer(open("sw_sent.csv", 'w'))
dd.writerow(["date", "neg","pos"])
aa.writerow(["date", "neg","pos"])
un.writerow(["date", "neg","pos"])
sw.writerow(["date", "neg","pos"])

with open('processed_twitter_data/delta.csv', 'r') as f:
    field_names = f.readline().strip().split(',')   # extract the field names
    for line in f:
        fields = line.strip().split(',')  # extract value of each field
        if 'Mon Mar 18' in fields[0]:
            words = line.strip().split(' ')
            for word in words:
                word = word.translate(str.maketrans('', '', string.punctuation)).lower()
                with open('words/opinion-lexicon-English_negative-words.txt') as neg:
                    for line in enumerate(neg):
                        #.rstrip() strips word of new line character
                        if word == line[1].rstrip():
                            n318 += 1
                with open('words/opinion-lexicon-English_positive-words.txt') as pos:
                    for line in enumerate(pos):
                        if word == line[1].rstrip():
                            p318 += 1
        if 'Tue Mar 19' in fields[0]:
            words = line.strip().split(' ')
            for word in words:
                word = word.translate(str.maketrans('', '', string.punctuation)).lower()
                with open('words/opinion-lexicon-English_negative-words.txt') as neg:
                    for line in enumerate(neg):
                        if word == line[1].rstrip():
                            n319 += 1
                with open('words/opinion-lexicon-English_positive-words.txt') as pos:
                    for line in enumerate(pos):
                        if word == line[1].rstrip():
                            p319 += 1
        if 'Tue Apr 09' in fields[0]:
            words = line.strip().split(' ')
            for word in words:
                word = word.translate(str.maketrans('', '', string.punctuation)).lower()
                with open('words/opinion-lexicon-English_negative-words.txt') as neg:
                    for line in enumerate(neg):
                        if word == line[1].rstrip():
                            n409 += 1
                with open('words/opinion-lexicon-English_positive-words.txt') as pos:
                    for line in enumerate(pos):
                        if word == line[1].rstrip():
                            p409 += 1
        if 'Sun Apr 21' in fields[0]:
            words = line.strip().split(' ')
            for word in words:
                word = word.translate(str.maketrans('', '', string.punctuation)).lower()
                with open('words/opinion-lexicon-English_negative-words.txt') as neg:
                    for line in enumerate(neg):
                        if word == line[1].rstrip():
                            n421 += 1
                with open('words/opinion-lexicon-English_positive-words.txt') as pos:
                    for line in enumerate(pos):
                        if word == line[1].rstrip():
                            p421 += 1
        if 'Mon Apr 22' in fields[0]:
            words = line.strip().split(' ')
            for word in words:
                word = word.translate(str.maketrans('', '', string.punctuation)).lower()
                with open('words/opinion-lexicon-English_negative-words.txt') as neg:
                    for line in enumerate(neg):
                        if word == line[1].rstrip():
                            n422 += 1
                with open('words/opinion-lexicon-English_positive-words.txt') as pos:
                    for line in enumerate(pos):
                        if word == line[1].rstrip():
                            p422 += 1
        if 'Tue Apr 23' in fields[0]:
            words = line.strip().split(' ')
            for word in words:
                word = word.translate(str.maketrans('', '', string.punctuation)).lower()
                with open('words/opinion-lexicon-English_negative-words.txt') as neg:
                    for line in enumerate(neg):
                        if word == line[1].rstrip():
                            n423 += 1
                with open('words/opinion-lexicon-English_positive-words.txt') as pos:
                    for line in enumerate(pos):
                        if word == line[1].rstrip():
                            p423 += 1
        if 'Wed Apr 24' in fields[0]:
            words = line.strip().split(' ')
            for word in words:
                word = word.translate(str.maketrans('', '', string.punctuation)).lower()
                with open('words/opinion-lexicon-English_negative-words.txt') as neg:
                    for line in enumerate(neg):
                        if word == line[1].rstrip():
                            n424 += 1
                with open('words/opinion-lexicon-English_positive-words.txt') as pos:
                    for line in enumerate(pos):
                        if word == line[1].rstrip():
                            p424 += 1
        if 'Fri Apr 26' in fields[0]:
            words = line.strip().split(' ')
            for word in words:
                word = word.translate(str.maketrans('', '', string.punctuation)).lower()
                with open('words/opinion-lexicon-English_negative-words.txt') as neg:
                    for line in enumerate(neg):
                        if word == line[1].rstrip():
                            n426 += 1
                with open('words/opinion-lexicon-English_positive-words.txt') as pos:
                    for line in enumerate(pos):
                        if word == line[1].rstrip():
                            p426 += 1

    dd.writerow(['3/18/19', n318, p318])
    dd.writerow(['3/19/19', n319, p319])
    dd.writerow(['4/9/19', n409, p409])
    dd.writerow(['4/21/19', n421, p421])
    dd.writerow(['4/22/19', n422, p422])
    dd.writerow(['4/23/19', n423, p423])
    dd.writerow(['4/24/19', n424, p424])
    dd.writerow(['4/26/19', n426, p426])

with open('processed_twitter_data/american.csv', 'r') as f:
    field_names = f.readline().strip().split(',')   # extract the field names
    for line in f:
        fields = line.strip().split(',')  # extract value of each field
        if 'Mon Mar 18' in fields[0]:
            words = line.strip().split(' ')
            for word in words:
                word = word.translate(str.maketrans('', '', string.punctuation)).lower()
                with open('opinion-lexicon-English_negative-words.txt') as neg:
                    for line in enumerate(neg):
                        if word == line[1].rstrip():
                            n318 += 1
                with open('opinion-lexicon-English_positive-words.txt') as pos:
                    for line in enumerate(pos):
                        if word == line[1].rstrip():
                            p318 += 1
        if 'Tue Mar 19' in fields[0]:
            words = line.strip().split(' ')
            for word in words:
                word = word.translate(str.maketrans('', '', string.punctuation)).lower()
                with open('opinion-lexicon-English_negative-words.txt') as neg:
                    for line in enumerate(neg):
                        if word == line[1].rstrip():
                            n319 += 1
                with open('opinion-lexicon-English_positive-words.txt') as pos:
                    for line in enumerate(pos):
                        if word == line[1].rstrip():
                            p319 += 1
        if 'Tue Apr 09' in fields[0]:
            words = line.strip().split(' ')
            for word in words:
                word = word.translate(str.maketrans('', '', string.punctuation)).lower()
                with open('opinion-lexicon-English_negative-words.txt') as neg:
                    for line in enumerate(neg):
                        if word == line[1].rstrip():
                            n409 += 1
                with open('opinion-lexicon-English_positive-words.txt') as pos:
                    for line in enumerate(pos):
                        if word == line[1].rstrip():
                            p409 += 1
        if 'Sun Apr 21' in fields[0]:
            words = line.strip().split(' ')
            for word in words:
                word = word.translate(str.maketrans('', '', string.punctuation)).lower()
                with open('opinion-lexicon-English_negative-words.txt') as neg:
                    for line in enumerate(neg):
                        if word == line[1].rstrip():
                            n421 += 1
                with open('opinion-lexicon-English_positive-words.txt') as pos:
                    for line in enumerate(pos):
                        if word == line[1].rstrip():
                            p421 += 1
        if 'Mon Apr 22' in fields[0]:
            words = line.strip().split(' ')
            for word in words:
                word = word.translate(str.maketrans('', '', string.punctuation)).lower()
                with open('opinion-lexicon-English_negative-words.txt') as neg:
                    for line in enumerate(neg):
                        if word == line[1].rstrip():
                            n422 += 1
                with open('opinion-lexicon-English_positive-words.txt') as pos:
                    for line in enumerate(pos):
                        if word == line[1].rstrip():
                            p422 += 1
        if 'Tue Apr 23' in fields[0]:
            words = line.strip().split(' ')
            for word in words:
                word = word.translate(str.maketrans('', '', string.punctuation)).lower()
                with open('opinion-lexicon-English_negative-words.txt') as neg:
                    for line in enumerate(neg):
                        if word == line[1].rstrip():
                            n423 += 1
                with open('opinion-lexicon-English_positive-words.txt') as pos:
                    for line in enumerate(pos):
                        if word == line[1].rstrip():
                            p423 += 1
        if 'Wed Apr 24' in fields[0]:
            words = line.strip().split(' ')
            for word in words:
                word = word.translate(str.maketrans('', '', string.punctuation)).lower()
                with open('opinion-lexicon-English_negative-words.txt') as neg:
                    for line in enumerate(neg):
                        if word == line[1].rstrip():
                            n424 += 1
                with open('opinion-lexicon-English_positive-words.txt') as pos:
                    for line in enumerate(pos):
                        if word == line[1].rstrip():
                            p424 += 1
        if 'Fri Apr 26' in fields[0]:
            words = line.strip().split(' ')
            for word in words:
                word = word.translate(str.maketrans('', '', string.punctuation)).lower()
                with open('opinion-lexicon-English_negative-words.txt') as neg:
                    for line in enumerate(neg):
                        if word == line[1].rstrip():
                            n426 += 1
                with open('opinion-lexicon-English_positive-words.txt') as pos:
                    for line in enumerate(pos):
                        if word == line[1].rstrip():
                            p426 += 1

    aa.writerow(['3/18/19', n318, p318])
    aa.writerow(['3/19/19', n319, p319])
    aa.writerow(['4/9/19', n409, p409])
    aa.writerow(['4/21/19', n421, p421])
    aa.writerow(['4/22/19', n422, p422])
    aa.writerow(['4/23/19', n423, p423])
    aa.writerow(['4/24/19', n424, p424])
    aa.writerow(['4/26/19', n426, p426])

with open('processed_twitter_data/united.csv', 'r') as f:
    field_names = f.readline().strip().split(',')   # extract the field names
    for line in f:
        fields = line.strip().split(',')  # extract value of each field
        if 'Mon Mar 18' in fields[0]:
            words = line.strip().split(' ')
            for word in words:
                word = word.translate(str.maketrans('', '', string.punctuation)).lower()
                with open('opinion-lexicon-English_negative-words.txt') as neg:
                    for line in enumerate(neg):
                        if word == line[1].rstrip():
                            n318 += 1
                with open('opinion-lexicon-English_positive-words.txt') as pos:
                    for line in enumerate(pos):
                        if word == line[1].rstrip():
                            p318 += 1
        if 'Tue Mar 19' in fields[0]:
            words = line.strip().split(' ')
            for word in words:
                word = word.translate(str.maketrans('', '', string.punctuation)).lower()
                with open('opinion-lexicon-English_negative-words.txt') as neg:
                    for line in enumerate(neg):
                        if word == line[1].rstrip():
                            n319 += 1
                with open('opinion-lexicon-English_positive-words.txt') as pos:
                    for line in enumerate(pos):
                        if word == line[1].rstrip():
                            p319 += 1
        if 'Tue Apr 09' in fields[0]:
            words = line.strip().split(' ')
            for word in words:
                word = word.translate(str.maketrans('', '', string.punctuation)).lower()
                with open('opinion-lexicon-English_negative-words.txt') as neg:
                    for line in enumerate(neg):
                        if word == line[1].rstrip():
                            n409 += 1
                with open('opinion-lexicon-English_positive-words.txt') as pos:
                    for line in enumerate(pos):
                        if word == line[1].rstrip():
                            p409 += 1
        if 'Sun Apr 21' in fields[0]:
            words = line.strip().split(' ')
            for word in words:
                word = word.translate(str.maketrans('', '', string.punctuation)).lower()
                with open('opinion-lexicon-English_negative-words.txt') as neg:
                    for line in enumerate(neg):
                        if word == line[1].rstrip():
                            n421 += 1
                with open('opinion-lexicon-English_positive-words.txt') as pos:
                    for line in enumerate(pos):
                        if word == line[1].rstrip():
                            p421 += 1
        if 'Mon Apr 22' in fields[0]:
            words = line.strip().split(' ')
            for word in words:
                word = word.translate(str.maketrans('', '', string.punctuation)).lower()
                with open('opinion-lexicon-English_negative-words.txt') as neg:
                    for line in enumerate(neg):
                        if word == line[1].rstrip():
                            n422 += 1
                with open('opinion-lexicon-English_positive-words.txt') as pos:
                    for line in enumerate(pos):
                        if word == line[1].rstrip():
                            p422 += 1
        if 'Tue Apr 23' in fields[0]:
            words = line.strip().split(' ')
            for word in words:
                word = word.translate(str.maketrans('', '', string.punctuation)).lower()
                with open('opinion-lexicon-English_negative-words.txt') as neg:
                    for line in enumerate(neg):
                        if word == line[1].rstrip():
                            n423 += 1
                with open('opinion-lexicon-English_positive-words.txt') as pos:
                    for line in enumerate(pos):
                        if word == line[1].rstrip():
                            p423 += 1
        if 'Wed Apr 24' in fields[0]:
            words = line.strip().split(' ')
            for word in words:
                word = word.translate(str.maketrans('', '', string.punctuation)).lower()
                with open('opinion-lexicon-English_negative-words.txt') as neg:
                    for line in enumerate(neg):
                        if word == line[1].rstrip():
                            n424 += 1
                with open('opinion-lexicon-English_positive-words.txt') as pos:
                    for line in enumerate(pos):
                        if word == line[1].rstrip():
                            p424 += 1
        if 'Fri Apr 26' in fields[0]:
            words = line.strip().split(' ')
            for word in words:
                word = word.translate(str.maketrans('', '', string.punctuation)).lower()
                with open('opinion-lexicon-English_negative-words.txt') as neg:
                    for line in enumerate(neg):
                        if word == line[1].rstrip():
                            n426 += 1
                with open('opinion-lexicon-English_positive-words.txt') as pos:
                    for line in enumerate(pos):
                        if word == line[1].rstrip():
                            p426 += 1

    un.writerow(['3/18/19', n318, p318])
    un.writerow(['3/19/19', n319, p319])
    un.writerow(['4/9/19', n409, p409])
    un.writerow(['4/21/19', n421, p421])
    un.writerow(['4/22/19', n422, p422])
    un.writerow(['4/23/19', n423, p423])
    un.writerow(['4/24/19', n424, p424])
    un.writerow(['4/26/19', n426, p426])

with open('processed_twitter_data/southwest.csv', 'r') as f:
    field_names = f.readline().strip().split(',')   # extract the field names
    for line in f:
        fields = line.strip().split(',')  # extract value of each field
        if 'Mon Mar 18' in fields[0]:
            words = line.strip().split(' ')
            for word in words:
                word = word.translate(str.maketrans('', '', string.punctuation)).lower()
                with open('opinion-lexicon-English_negative-words.txt') as neg:
                    for line in enumerate(neg):
                        if word == line[1].rstrip():
                            n318 += 1
                with open('opinion-lexicon-English_positive-words.txt') as pos:
                    for line in enumerate(pos):
                        if word == line[1].rstrip():
                            p318 += 1
        if 'Tue Mar 19' in fields[0]:
            words = line.strip().split(' ')
            for word in words:
                word = word.translate(str.maketrans('', '', string.punctuation)).lower()
                with open('opinion-lexicon-English_negative-words.txt') as neg:
                    for line in enumerate(neg):
                        if word == line[1].rstrip():
                            n319 += 1
                with open('opinion-lexicon-English_positive-words.txt') as pos:
                    for line in enumerate(pos):
                        if word == line[1].rstrip():
                            p319 += 1
        if 'Tue Apr 09' in fields[0]:
            words = line.strip().split(' ')
            for word in words:
                word = word.translate(str.maketrans('', '', string.punctuation)).lower()
                with open('opinion-lexicon-English_negative-words.txt') as neg:
                    for line in enumerate(neg):
                        if word == line[1].rstrip():
                            n409 += 1
                with open('opinion-lexicon-English_positive-words.txt') as pos:
                    for line in enumerate(pos):
                        if word == line[1].rstrip():
                            p409 += 1
        if 'Sun Apr 21' in fields[0]:
            words = line.strip().split(' ')
            for word in words:
                word = word.translate(str.maketrans('', '', string.punctuation)).lower()
                with open('opinion-lexicon-English_negative-words.txt') as neg:
                    for line in enumerate(neg):
                        if word == line[1].rstrip():
                            n421 += 1
                with open('opinion-lexicon-English_positive-words.txt') as pos:
                    for line in enumerate(pos):
                        if word == line[1].rstrip():
                            p421 += 1
        if 'Mon Apr 22' in fields[0]:
            words = line.strip().split(' ')
            for word in words:
                word = word.translate(str.maketrans('', '', string.punctuation)).lower()
                with open('opinion-lexicon-English_negative-words.txt') as neg:
                    for line in enumerate(neg):
                        if word == line[1].rstrip():
                            n422 += 1
                with open('opinion-lexicon-English_positive-words.txt') as pos:
                    for line in enumerate(pos):
                        if word == line[1].rstrip():
                            p422 += 1
        if 'Tue Apr 23' in fields[0]:
            words = line.strip().split(' ')
            for word in words:
                word = word.translate(str.maketrans('', '', string.punctuation)).lower()
                with open('opinion-lexicon-English_negative-words.txt') as neg:
                    for line in enumerate(neg):
                        if word == line[1].rstrip():
                            n423 += 1
                with open('opinion-lexicon-English_positive-words.txt') as pos:
                    for line in enumerate(pos):
                        if word == line[1].rstrip():
                            p423 += 1
        if 'Wed Apr 24' in fields[0]:
            words = line.strip().split(' ')
            for word in words:
                word = word.translate(str.maketrans('', '', string.punctuation)).lower()
                with open('opinion-lexicon-English_negative-words.txt') as neg:
                    for line in enumerate(neg):
                        if word == line[1].rstrip():
                            n424 += 1
                with open('opinion-lexicon-English_positive-words.txt') as pos:
                    for line in enumerate(pos):
                        if word == line[1].rstrip():
                            p424 += 1
        if 'Fri Apr 26' in fields[0]:
            words = line.strip().split(' ')
            for word in words:
                word = word.translate(str.maketrans('', '', string.punctuation)).lower()
                with open('opinion-lexicon-English_negative-words.txt') as neg:
                    for line in enumerate(neg):
                        if word == line[1].rstrip():
                            n426 += 1
                with open('opinion-lexicon-English_positive-words.txt') as pos:
                    for line in enumerate(pos):
                        if word == line[1].rstrip():
                            p426 += 1

    sw.writerow(['3/18/19', n318, p318])
    sw.writerow(['3/19/19', n319, p319])
    sw.writerow(['4/9/19', n409, p409])
    sw.writerow(['4/21/19', n421, p421])
    sw.writerow(['4/22/19', n422, p422])
    sw.writerow(['4/23/19', n423, p423])
    sw.writerow(['4/24/19', n424, p424])
    sw.writerow(['4/26/19', n426, p426])

