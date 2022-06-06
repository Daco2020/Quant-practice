# %%
import finterstellar as fs


df = fs.get_price('AAPL', start_date='2020-01-01', end_date='2020-12-31')
print(df)

# %%
fs.draw_chart(df, right='AAPL')

fs.rsi(df, w=14) # w=14 > 일봉 기준 14일간의 주가의 상대적 세기
fs.draw_chart(df, left='rsi', right='AAPL')

# %%
fs.indicator_to_signal(df, factor='rsi', buy=40, sell=60)
# %%
fs.position(df)
fs.draw_chart(df, left='rsi', right='position_chart')
# %%
df # df에 어떤 컬럼이 들어있는지 확인 가능
# %%
fs.evaluate(df, cost=.001)
fs.draw_chart(df, left='acc_rtn_dp', right='AAPL')
df
# %%
fs.performance(df, rf_rate=0.01)
# %%
# buy=60, sell=40 전략으로 매매했다면?
fs.indicator_to_signal(df, factor='rsi', buy=60, sell=40)
fs.position(df)
fs.evaluate(df, cost=.001)
fs.performance(df, rf_rate=0.01)
fs.draw_chart(df, left='rsi', right='position_chart')
fs.draw_chart(df, left='acc_rtn_dp', right='AAPL')
# %%
