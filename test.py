# %%
import finterstellar as fs


df = fs.get_price('AAPL', start_date='2020-01-01', end_date='2020-12-31')
print(df)

# %%
fs.draw_chart(df, right='AAPL')

fs.rsi(df, w=14) # w=14 > 일봉 기준 14일간의 주가의 상대적 세기
fs.draw_chart(df, left='rsi', right='AAPL')

# %%
