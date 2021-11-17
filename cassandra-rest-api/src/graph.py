import plotly.graph_objects as go
import plotly


def candlestick_chart(df, file_name):
  fig = go.Figure([go.Candlestick(x=df['datetime'],
                                       open=df['open'],
                                       high=df['high'],
                                       low=df['low'],
                                       close=df['close'])])
  
  
  fig.update_layout(xaxis_rangeslider_visible=False,
                    title='Bitcoin live share price evolution',
                    yaxis_title='Stock Price (USD per Shares)')
  
  plotly.offline.plot(fig, filename=f'templates/{file_name}.html', auto_open=False)

def line_chart(df, file_name):
  fig = go.Figure()

  fig.add_trace(go.Scatter(x=df['datetime'],
                           y=df['close']))
                           
  fig.update_layout(title='Bitcoin Line Chart Price',
                    yaxis_title='Stock Price (USD per Shares)')

  plotly.offline.plot(fig, filename=f'templates/{file_name}.html', auto_open=False)