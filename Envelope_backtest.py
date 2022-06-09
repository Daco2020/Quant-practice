# %%
import finterstellar as fs

symbol = "BA"
df = fs.get_price(symbol, start_date="2020-01-01", end_date="2020-12-31")
fs.draw_chart(df, right=symbol)
# %%
fs.envelope(df, w=20, spread=.1)
df.tail() # 데이터 중 꼬리만 보여준다.
# %%
fs.draw_band_chart(df) # envelope 밴드 형태를 출력함
# %%
# 모멘텀 전략
fs.band_to_signal(df, buy="A", sell="B")
# %%
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
