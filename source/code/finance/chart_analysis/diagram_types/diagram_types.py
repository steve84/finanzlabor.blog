import yfinance as yf
import mplfinance as mpf


def createFigure(data, filename='chart.png', type='candle', volume=False,
                 title='Price USD', figratio=(16, 9), figscale=1.25):
    mpf.plot(data, type=type, title=title, ylabel='Price USD',
             volume=volume, savefig=filename, figratio=figratio,
             figscale=figscale)


# Symbol von Yahoo Finance
symbol = 'ACWI'
# Start-Datum für den Chart
start_date = '01-01-2020'

# Preise via yfinance herunterladen
prices = yf.Ticker(symbol)
data = prices.history(period='3y', interval='1d')

# Kerzen-Chart erstellen
createFigure(data=data.loc[start_date:],
             title='Typ: Kerzen (Candlestick), Periode: 1 Tag',
             filename='candle_chart_1d_%s.png' % symbol)

# OHLC-Chart erstellen
createFigure(data=data.loc[start_date:], title='Typ: OHLC, Periode: 1 Tag',
             filename='ohlc_chart_1d_%s.png' % symbol, type='ohlc')

# Linien-Chart erstellen
createFigure(data=data.loc[start_date:],
             title='Typ: Linie (Line), Periode: 1 Tag',
             filename='line_chart_1d_%s.png' % symbol, type='line')

# Linien-Chart inklusive Handelsvolumen erstellen
createFigure(data=data.loc[start_date:],
             title='Typ: Linie (Line) inkl. Volumen, Periode: 1 Tag',
             filename='line_chart_1d_%s.png' % symbol, type='line',
             volume=True)

# Preise erneut laden (Zeiteinheit: 5 Tage)
data = prices.history(period='3y', interval='5d')
data['Date_Col'] = data.index

# Neues Startdatum
start_date = '06-01-2018'
# Zweites Kerzen-Chart erstellen
createFigure(data=data.loc[start_date:],
             title='Typ: Kerzen (Candlestick), Periode: 1 Woche',
             filename='candle_chart_1w_%s.png' % symbol)
