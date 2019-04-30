import csv
import time
import string
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, LSTM



#DELETE THE DATE, TEXT FROM TOP OF CSV FILES!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#also change the processed_twitter_data?
def create_tweet_dictionary(airline,dic_by_airline):
    dic = {}
    #file = "processed_twitter_data/" + airline + ".csv"
    file = airline + ".csv"
    with open(file, 'r') as f:
        f.readline().strip().split(',')   # extract the field names
        csv_reader = csv.reader(f, delimiter=',')
        for row in csv_reader:
            date = time.strftime('%m-%d-%Y', time.strptime(row[0], '%a %b %d %H:%M:%S +0000 %Y'))
            if date in dic:
                dic[date].append(row[1])
            else:
                dic[date] = [row[1]]

    dic_by_airline[airline] = dic
    return dic_by_airline

def featured_data(dic_by_airline):
#dic = dic_featured_data
    dic = {}
    for key, value in dic_by_airline.items():   #key=airline name, value= dictionary with (k,v) being (date,list)
        airline_dic = {}
        tweet_len = []
        for k,v in value.items():
            tweet_len.append(len(v))
        max_num_tweets = max(tweet_len)
        for k,v in value.items():   #k = date, v=list of tweets for that day
            neg = pos = word_cnt = 0   #set postive and negative words equal to zero before doing sentiment analysis
            for tweet in v:
                words = tweet.strip().split(' ')
                for word in words:
                    word = word.translate(str.maketrans('', '', string.punctuation)).lower() #get rid of punctionation and make lowercase
                    word_cnt += 1
                    with open('words/opinion-lexicon-English_negative-words.txt') as n:
                        for line in enumerate(n):
                            if word == line[1].rstrip(): # .rstrip() strips word of new line character
                                neg += 1
                    with open('words/opinion-lexicon-English_positive-words.txt') as p:
                        for line in enumerate(p):
                            if word == line[1].rstrip():
                                pos += 1

            count = len(v) #number of tweets

            airline_dic[k] = [pos/word_cnt, neg/word_cnt, count/max_num_tweets]
        dic[key] = airline_dic
        #print(airline_dic)
    return dic

def stock_preprocessing(csv_name, airline, stock_dic):
    data = pd.read_csv(csv_name)
    data['Date'] = pd.to_datetime(data.Date)
    data['Date'] = data['Date'].dt.strftime('%m-%d-%Y')

    data = data.drop(['Open','High','Low','Adj Close','Volume'],axis=1) #drops unused columns
    data['per_change'] = data['Close'] / data['Close'].shift(1) - 1 #add a new column that is percent change
    data = data.drop(['Close'],axis=1) #drops close column
    #print(data.head())
    data = data.dropna()     #drops values that have NaN value
    data = data.set_index('Date').T     #changes index to be the Date column and transposes dataframe
    data_dic = data.head().to_dict('list')      #changes dataframe into a dictionary, {'date': [per_change]}
    stock_dic[airline] = data_dic

    return stock_dic

def build_model(dic_featured_data, stock_dic):
    for key, value in dic_featured_data.items():       #key = airline name, value =
        #something specific for each airline here i think
        airline_stock = stock_dic[key]
        #print(airline_stock)
        X = pd.DataFrame([])
        y = pd.DataFrame([])
        for k, v in value.items():  # k = date, v=featured data
            if k in airline_stock:
                X = X.append(pd.DataFrame({'pos': v[0], 'neg': v[1], 'number': v[2]}, index=[k]))
                y = y.append(pd.DataFrame({'per_change': airline_stock[k]}, index=[k]))
        #so yea so then do the actual regression stuff
        #maybe just put that in another function and call that with (X,y)
        #run_regression(X,y)
        #put results into another dictionary lol? {airline as index, and then r^2 and other values as the top of dataframe)
        #to easily put the results into a table yea
        print(key)
        run_regression(X,y)
        #run_model(X, y)

        #df = open("dataframes.txt", "a+")
        #df.write("Airline: " + key + '\n')
        #df.write("Feature data dataframe: \n" + X.values)
        np.save('dataframes.txt', X.values)
        #df.write("Stock dataframe: /n" + y.values)
        np.save('dataframes.txt', y.values)
    #print(X)
    #print(y)

'''def run_model(X, y):

    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
    # x_train, x_test, y_train, y_test = np.array(X_train), np.array(X_test), np.array(y_train), np.array(y_test)
    # x_train = np.reshape(X_train, (len(X_train), len(X_train[0]), 1))
    # x_test = np.reshape(X_test, (len(X_test), len(X_test[0]), 1))
    print('y:')
    # print(list(y.values))
    y = [[x[0]] for x in y.values]
    x_train, y_train = np.array(X), np.array(y)
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

    print('y', y_train)
    print()

    batch_size = 1
    epochs = 1000

    model = Sequential()

    model.add(LSTM(38, input_shape=(x_train.shape[1], x_train.shape[2])))
    model.add(LSTM(38, input_shape=(x_train.shape[1], x_train.shape[2])))
    # model.add(LSTM(38))
    # model.add(LSTM(38))
    # model.add(LSTM(38))
    # model.add(LSTM(38))
    model.add(Dense(y_train.shape[1], activation='softmax'))

    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, verbose=2)

    y_pred_test = model.predict(x_train)

    print("Root mean squared error = %.4f" % np.sqrt(mean_squared_error(y_train, y_pred_test)))
    print("R-square = %.4f" % r2_score(y_train, y_pred_test))'''

def run_regression(X,y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

    # Create linear regression object
    regr = linear_model.LinearRegression()

    # Fit regression model to the training set
    regr.fit(X_train, y_train)

    # Apply model to the test set
    y_pred_test = regr.predict(X_test)

    print('\n')
    print("Root mean squared error = %.4f" % np.sqrt(mean_squared_error(y_test, y_pred_test)))
    print("R-square = %.4f" % r2_score(y_test, y_pred_test))
    print('Slope Coefficients:', regr.coef_)
    print('Intercept:', regr.intercept_)

def main():
    # dic_by_airlines = { 'airline' : {'date' : [tweet,tweet2,tweet3]}, 'airline': {'date' : [tweet,tweet2,tweet3]} }
    # dic = dic_featured_data = {'airline': {'date' : [pos,neg,number of tweets]}}
    dic_by_airline = {}     #{ 'airline' : {'date' : [tweet,tweet2,tweet3]}, 'airline': {'date' : [tweet,tweet2,tweet3]} }
    dic_featured_data = {}      #{'airline': {'date' : [pos words,neg words,number of tweets]}}
    stock_dic = {}          #{'airline': {'date' : [percent change ]}}

    dic_by_airline = create_tweet_dictionary("southwest", dic_by_airline)
    create_tweet_dictionary("united", dic_by_airline)
    #print(dic_by_airline)
    create_tweet_dictionary("delta", dic_by_airline)
    create_tweet_dictionary("american", dic_by_airline)
    dic_featured_data = featured_data(dic_by_airline)
    #print(dic_featured_data)

    stock_preprocessing('stock_data/DAL.csv', 'delta', stock_dic)
    stock_preprocessing('stock_data/LUV.csv', 'southwest', stock_dic)
    stock_preprocessing('stock_data/AAL.csv', 'american', stock_dic)
    stock_preprocessing('stock_data/UAL.csv', 'united', stock_dic)
    #print(stock_dic)
    build_model(dic_featured_data,stock_dic)

if __name__ == "__main__":
    main()

