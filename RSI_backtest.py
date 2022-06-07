# %%
import finterstellar as fs


symbol = "VZ"
df = fs.get_price(symbol, start_date="2020-01-01", end_date="2020-12-31")
fs.draw_chart(df, right=symbol)
# %%
fs.rsi(df, w=14) # 14일 기준(기본값)
fs.draw_chart(df, left="rsi", right=symbol)
# %%
# 평균회귀 전략을 사용한 경우
fs.indicator_to_signal(df, factor="rsi", buy=30, sell=70)
fs.position(df)
fs.evaluate(df, cost=.001)
fs.performance(df, rf_rate=0.01)
fs.draw_trade_results(df)
# 만약 보유 중이라면 당일 주가로 수익률을 계산한다.
# %%
# 모멘텀 전략을 사용한 경우
fs.indicator_to_signal(df, factor="rsi", buy=70, sell=50)
fs.position(df)
fs.evaluate(df, cost=.001)
fs.performance(df, rf_rate=0.01)
fs.draw_trade_results(df)
"""
같은 전략이라도 종목별로 성과가 다르다.
종목 특성에 맞는 맞춤형 전략이 필요하다.
평균회귀는 박스권, 모멘텀은 우상향 종목에 적합함.
"""
# %%
