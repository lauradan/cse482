import pandas as pd

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

stock_dic = {}
stock_preprocessing('stock_data/DAL.csv', 'delta',stock_dic)
print(stock_dic)