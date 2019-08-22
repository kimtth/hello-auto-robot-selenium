import pandas as pd

if __name__ == '__main__':
    # generate new df
    df = pd.DataFrame({'num_legs': [2, 4, 8, 0],
                       'num_wings': [2, 0, 0, 0],
                       'num_specimen_seen': [10, 2, 1, 8]},
                      index=['falcon', 'dog', 'spider', 'fish'])
    print(df)

    # add new row with value
    df2 = pd.DataFrame({'num_legs': [10],
                        'num_wings': [12],
                        'num_specimen_seen': [13]}, index=['cat'])
    df = df.append(df2)
    print(df)

    # modify value to existing column
    df.loc['cat'] = [11, 12, 13]
    print(df)

    # add new column
    address = ['delhi', 'dangalore', 'chennai', 'patna', 'patna']
    df['address'] = address  # new column
    print(df)
