import pandas as pd
import numpy as np
import io
import matplotlib
import matplotlib.pyplot as plt
import pylab
#pylab.rcParams['figure.figsize'] = (10.0, 8.0)

def print_spacer():
    print('\n' + '-'*10 + '\n')

def print_methods(obj):
    print(', '.join(f for f in dir(obj) if not f.startswith('_')))


# Need to call plt.show()  for any matplatlib (and pandas) gui stuff to be shown.

##plot normalized histogram with 50 bins
# mu, sigma = 2, 0.5
# v = np.random.normal(mu, sigma, 10000)
# plt.hist(v, bins=20, normed=10)
plt.show()

# pandas Series:
# can create joint indexes
index_vals = [('Aistemos', 'tech'),
              ('Aistemos', 'sales'),
              ('Bose', 'tech'),
              ('TR', 'sales'),
              ('TR', 'marketing'),
              ('TR', 'tech')]
index = pd.MultiIndex.from_tuples(index_vals, names=['company', 'division'])
pd.Series([1,2,3,4,5,6], index=index)

# pandas Series:
# Vectorised operations
s = pd.Series([1, 2, 3, 4])
s += 1 # add one to each item
t = (s > 4) & (s != 5)
u = (s > 4) | (s == 2)
s[u]  # to use u as a selection into s
# But... we can just do the above in one line
s[(s > 4) | (s == 2)]


# Pandas dataframes:
# Basically combines a nunch of Series into a tabular structure
# Each column is a series

# DataFrame
a = pd.DataFrame([['alice', 23],
                  ['bob', 10],
                  ['caroline', 44]])

# DataFrame with column names
a = pd.DataFrame([['alice', 23],
                  ['bob', 10],
                  ['caroline', 44]],
                 columns=['name', 'age'])

# DataFrame from dicts, column names inferred from keys
a = pd.DataFrame([{'name': 'alice', 'age': 23},
                  {'name': 'bob', 'age': 10},
                  {'name': 'caroline', 'age': 44}])

# DataFrame from CSV (pandas CSV parsing is REALLY good - faster than python's `csv` module, better handling of messy data)
csv = io.StringIO(u"""
name,age
"alice",23
"bob",10
caroline,  44
""")
a = pd.read_csv(csv)

# DataFrame from json (word on JSON strings or file handles)
json_data = """
[{"name": "alice", "age": 23},
 {"name": "bob", "age": 10},
 {"name": "caroline", "age": 44}]
"""
a = pd.read_json(json_data)

# Also many more ways to read in dataframes (including html, sql, excel etc...)

# indexing

df = pd.read_csv(io.StringIO(u"""
name,age,editor
alice,23,vi
bob,10,emacs
caroline,44,vi
"""))

# getting a single column returns a series
df['age']

# getting multiple columns return a DataFrame
df[['age', 'editor']]

df[[0]]   # just column 0
df[[0,1]] # just columns 0 and 1
df[0:2]   # rows 0 and 1
df[-1:]   # just the last row

# getting with .loc (interger location based - not values refer to the index, not the row number)
df.loc[[0, 2]]
df.loc[[0, 2], ['editor', 'age']]
df.loc[[0, 2], ['editor', 'age']]

# getting with .iloc (integer position based)
df.iloc[0, 0]
df.iloc[-2:, 1:2]   # last 2 rows, just column 1

df['age'] > 10  # returns a Boolean Series
df[df['age'] > 10]

# Avoid iterating over dataframes - as this is MUCH slower than column-based operations
# for idx, series in df.iterrows():
#     print('index:', idx)
#     print(series)
#     print('---')

# iterate over each row as a tuple, significantly faster, no Series creation overhead
# for row in df.itertuples():
#     print(row)

#You can operate on DataFrame columns like series:
#df['age'] *= 2

#Useful Series functions:
df['age'].sum()
df['age'].mean()
df['age'].max()
df['age'].min()

#Missing values
csv = io.StringIO(u"""
name,birthday,height
alice,2000-10-10,4
bob,,8
caroline,1922-05-04,
,,
""")
df = pd.read_csv(csv)
df['birthday'] = pd.to_datetime(df['birthday']) # convert string date to datetime, more on this later
df


# fill missing values - returns Series of DataFrame depending on columns selected
#df['height'] = df['height'].fillna(100)

# many methods have an `inplace` argument, above could be written more compactly:
#df['height'].fillna(100, inplace=True)

# remove rows containing missing data with `dropna`
#df.dropna()


# Plotting - mostly convenience wrappers around matplotlib

# A line chart
#pd.Series(np.random.random(50)).plot()

# Histogram
# pd.Series(np.random.random(50)).hist()

# multiple series charts available from DataFrames
#pd.DataFrame(np.random.random((20, 3)), columns=['height', 'weight', 'age']).plot()


# Dataframe grouping

# Fake dataset for log messages (timestamp skipped for simplicity)
csv = io.StringIO(u"""
host,service,error
celia,cache-service,OOM
celia,cache-service,OOM
celia,domain-service,segfault
mike,cache-service,OOM
mike,domain-service,segfault
mike,domain-service,OOM
mike,domain-service,segfault
mike,domain-service,segfault
sulley,cache-service,OOM
""")
df = pd.read_csv(csv)

# Groupby does nothing meaningful until you ask for some result (many methods available)
df.groupby('host')

# number of rows per host, as Series
df.groupby('host').size()

# number of rows per host, per service
df.groupby(['host', 'service']).size()

# group by host, then get number of occurrences of each error type (as Series with multiple index)
df.groupby('host')['error'].value_counts()



# Dates / Times
csv = io.StringIO(u"""
where,when
here,2013-01-03T10:37:01
there,1999-06-09T15:01:10
someplace,2005-01-03
""")
df = pd.read_csv(csv)
df
