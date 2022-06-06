# %%
import finterstellar as fs

# %%
symbol = 'MSFT'
df = fs.get_price(symbol, start_date='2020-01-01', end_date='2020-12-31')
fs.draw_chart(df, right=symbol)
# %%
# macd 호출 시 단기, 장기, 시그널 기간을 함께 지정할 수 있음
# 지정하지 않으면 기본값 적용(short=12, long=26, signal=9)
fs.macd(df)
"""
<결과 값>
Symbols	MSFT	macd	macd_signal	macd_oscillator
Date				
2019-12-31	157.70	0.00	0.00	0.00
2020-01-02	160.62	0.07	0.04	0.03
"""
# %%
fs.draw_chart(df, right=['macd','macd_signal','macd_oscillator'])
# %%
fs.indicator_to_signal(df, factor='macd_oscillator', buy=0, sell=0)
# %%
# 생략된 구간을 보고 싶을 경우 아래처럼 범위를 지정하고 함수내에 넣으면 된다.
df.loc['2020-10-01':'2020-10-10']
# %%
# position : 거래 결과로 보유 중인 재산 상태를 의미
fs.position(df)
fs.draw_chart(df, right='position_chart', left='macd_oscillator')

# %%
fs.evaluate(df, cost=.001)
fs.performance(df, rf_rate=0.01)
fs.draw_trade_results(df)

# %%
"""
<결과 값>
CAGR: 21.76%
Accumulated return: 21.83%
Average return: 1.84%
Benchmark return : 41.04%
Number of trades: 12
Number of win: 6
Hit ratio: 50.00%
Investment period: 1.0yrs
Sharpe ratio: 0.71
MDD: -11.28%
Benchmark MDD: -28.24%
-----
- 벤치마크 기준 수익율이 못미치지만 이는 우상향 종목이었기 때문
- 벤치마크 기준 MDD를 낮추어 안정성을 강화했다고 볼 수 있음
"""