import finterstellar as fs


df = fs.get_price('AAPL', start_date='2020-01-01', end_date='2020-12-31')
print(df)