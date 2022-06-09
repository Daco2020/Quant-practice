# %%
import finterstellar as fs

symbol = "TSM"
df = fs.get_price(symbol, start_date="2020-01-01", end_date="2020-12-31")
fs.draw_chart(df, right=symbol)
# %%
# 볼린저 기본 전략
fs.bollinger(df, w=20, k=2)
df.tail()
# %%
fs.draw_band_chart(df)
# %%
# 모멘텀 전략
fs.band_to_signal(df, buy="A", sell="B")
fs.position(df)
fs.evaluate(df, cost=.001)
fs.performance(df, rf_rate=0.01)
fs.draw_trade_results(df)
# %%
# 평균회귀 전략
fs.band_to_signal(df, buy="D", sell="B")
fs.position(df)
fs.evaluate(df, cost=.001)
fs.performance(df, rf_rate=0.01)
fs.draw_trade_results(df)




# %%
# 볼린저 수정 전략
df = fs.get_price(symbol, start_date="2020-01-01", end_date="2020-12-31")
fs.bollinger(df, w=20, k=1)
# %%
# 모멘텀 전략
fs.band_to_signal(df, buy="A", sell="B")
fs.position(df)
fs.evaluate(df, cost=.001)
fs.performance(df, rf_rate=0.01)
fs.draw_trade_results(df)
# %%
# 평균회귀 전략
fs.band_to_signal(df, buy="D", sell="B")
fs.position(df)
fs.evaluate(df, cost=.001)
fs.performance(df, rf_rate=0.01)
fs.draw_trade_results(df)



# %%
# 합성전략
df["s1"] = fs.band_to_signal(df, buy="A", sell="B")
df["s2"] = fs.band_to_signal(df, buy="D", sell="B")
fs.combine_signal_or(df, "s1", "s2") # combine_signal_and() : and 조건
# %%
fs.position(df)
fs.evaluate(df, cost=.001)
fs.performance(df, rf_rate=0.01)
fs.draw_trade_results(df)
# %%
"""
# 합성전략 결과 값
CAGR: 52.14%
Accumulated return: 48.14%
Average return: 1.69%
Benchmark return : 90.66%
Number of trades: 28
Number of win: 12
Hit ratio: 42.86%
Investment period: 0.9yrs
Sharpe ratio: 1.03
MDD: -20.23%
Benchmark MDD: -26.40%
"""