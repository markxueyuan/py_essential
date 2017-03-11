import pandas as pd
import numpy as np

# Generating data for subsequent use


index =pd.date_range('1/1/2000', periods=8)

s = pd.Series(np.random.randn(5),
              index=['a', 'b', 'c', 'd', 'e'])

df = pd.DataFrame(np.random.randn(8, 3),
                  index=index,
                  columns=['A', 'B', 'C'])


wp = pd.Panel(np.random.randn(2, 5, 4),
              items=['Item1', 'Item2'],
              major_axis = pd.date_range('1/1/2000',
                                         periods=5),
              minor_axis = ['A', 'B', 'C', 'D'])


# head and tail

long_series = pd.Series(np.random.randn(1000))

long_series.head()
long_series.tail(3)
long_series.head(1) # These operations will not change the original data

# Attributes

df[:2] # first two rows

df.columns = [x.lower() for x in df.columns] # get and change the columns

s.values

df.values

wp.values


df = pd.DataFrame(
    {
        'one' : pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
        'two' : pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd']),
        'three' : pd.Series(np.random.randn(3), index = ['b', 'c', 'd'])
    }
)

row = df.ix[1]

column = df["three"]

df.sub(row, axis='columns')




