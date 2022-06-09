# %%
import finterstellar as fs

symbol = "DAL"
# get_ohlc 은 시고저종을 모두 구한다. 시고저종 df는 종목코드가 없다.
df = fs.get_ohlc(symbol, start_date="2020-01-01", end_date="2020-12-31")
df.tail()
# %%
fs.stochastic(df, symbol, n=14, m=3, t=3)
# %%
fs.draw_chart(df, left="slow_k", right=symbol)
# %%
# 평균회귀 전략
fs.indicator_to_signal(df, factor="slow_k", buy=20, sell=80)
fs.position(df)
fs.evaluate(df, cost=.001)
fs.performance(df, rf_rate=0.01)
fs.draw_trade_results(df)
# %%
# 모멘텀 전략
df = fs.get_ohlc(symbol, start_date="2020-01-01", end_date="2020-12-31")
fs.stochastic(df, symbol, n=14, m=3, t=3)
df.tail()
# %%
# 매매 신호를 위한 계산식이 indicator 로 저장한다.
df["indicator"] = df["slow_k"] - df["slow_d"]
df.tail()
"""
	DAL	slow_k	slow_d	indicator
Date				
2020-12-24	39.73	17.11	18.44	-1.33
2020-12-28	40.15	25.84	20.44	5.40
2020-12-29	40.03	24.35	22.43	1.92
2020-12-30	40.56	32.62	27.60	5.02
2020-12-31	40.21	35.93	30.97	4.96
"""
# %%
fs.indicator_to_signal(df, factor="indicator", buy=0, sell=0)
fs.position(df)
fs.evaluate(df, cost=.001)
fs.performance(df, rf_rate=0.01)
fs.draw_trade_results(df)
# %%
