---
title: Fear and Greed Index Daten beziehen und visualisieren
p: programming/fear_greed_api/fear_greed_api.md
date: 2022-07-18 20:00:00
tags:
- Programmierung
- Python
- Experiment
categories: Programmierung
toc: false
thumbnail: /gallery/thumbnails/programming/fear_greed_api/thumbnail.jpg
---

Der heutige, eher etwas kürzere Beitrag beschäftigt sich mit der Beschaffung und Darstellung des *Fear and Greed* Index mit Hilfe der Python-Bibliothek mplfinance (Visualisierung von Börsendaten). Die Daten werden über eine nicht offizielle (diese wird von der CNN-Webseite verwendet) API bezogen und in die benötigten Software-Objekte verwandelt. Zum Schluss wird der Verlauf mit einem MSCI-Weltindex verglichen. Dabei kommt eine verblüffende Beobachtung ans Tageslicht...

<!-- more -->

## Voraussetzungen

Damit die nachfolgenden Befehle auch korrekt ausgeführt werden können, muss eine funktionierende Python-Umgebung vorhanden sein. {% post_link data/environment/environment 'Eine Möglichkeit (Anaconda) wurde in einem der ersten Beiträge auf diesem Blog vorgestellt' %}. Zusätzlich müssen noch folgende Python-Pakete installiert werden:

* [yfinance](https://github.com/ranaroussi/yfinance)
* [mplfinance](https://github.com/matplotlib/mplfinance)

## Befehle
Zuerst müssen alle benötigten Bibliotheken importiert werden:


```python
import pandas as pd
import requests
import mplfinance as mpf
import yfinance as yf
```

Anschliessend wird die URL des Datenlieferanten definiert (Quelle: CNN). Dieser liefert die Daten des Fear & Greed Index im JSON-Format. Damit die Anfrage auch erfolgreich durchgeführt werden kann, muss sich die aufrufende Applikation als Browser ausgeben (Header-Eigenschaft *user-agent*).


```python
url = 'https://production.dataviz.cnn.io/index/fearandgreed/graphdata'

headers = dict()
headers['user-agent'] = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
```

Nun werden die Daten mit Hilfe der Bibliothek *requests* angefordert. Sofern die Anfrage korrekt verarbeitet wurde, wird die Antwort in einem DataFrame-Objekt abgelegt. Dabei wird nur ein Teil der Daten verwendet, welche vom Service zurückgeliefert werden. Damit das Objekt später mit *mplfinance* visualisiert werden kann, muss der Index der Datenstruktur korrekt gesetzt sein und die OHLC-Eigenschaften (jedoch haben alle den gleichen Wert) vorhanden sein.


```python
req = requests.get(url, headers=headers)

if req.status_code == 200:
    # Antwort von Zeichenkette in Objekt umwandeln
    resp = req.json()
    # Sind die gewünschten Daten vorhanden?
    if 'fear_and_greed_historical' in resp.keys() and 'data' in resp['fear_and_greed_historical'].keys():
        # Daten in pandas DataFrame umwandeln
        df = pd.DataFrame(resp['fear_and_greed_historical']['data'])
        # Index korrekt aufbereiten
        df = df.set_index(pd.to_datetime(df['x'].apply(lambda x: x), unit='ms'))
        # OHLC Wert setzen
        df['Close'] = df['y']
        df['Open'] = df['Close']
        df['High'] = df['Close']
        df['Low'] = df['Close']
```

Das Resultat validieren:


```python
df
```

|| x                             | y            | rating    | Close        | Open      | High      | Low       |
|-------------------------------|--------------|-----------|--------------|-----------|-----------|-----------|
| x                             |
| 2021-07-19 00:00:00.000000000 | 1.626653e+12 | 13.807443 | extreme fear | 13.807443 | 13.807443 | 13.807443 | 13.807443 |
| 2021-07-20 00:00:00.000000000 | 1.626739e+12 | 20.633333 | extreme fear | 20.633333 | 20.633333 | 20.633333 | 20.633333 |
| 2021-07-21 00:00:00.000000000 | 1.626826e+12 | 24.466667 | extreme fear | 24.466667 | 24.466667 | 24.466667 | 24.466667 |
| 2021-07-22 00:00:00.000000000 | 1.626912e+12 | 25.200000 | fear         | 25.200000 | 25.200000 | 25.200000 | 25.200000 |
| 2021-07-23 00:00:00.000000000 | 1.626998e+12 | 29.133333 | fear         | 29.133333 | 29.133333 | 29.133333 | 29.133333 |
| ...                           | ...          | ...       | ...          | ...       | ...       | ...       | ...       |
| 2022-07-14 00:00:00.000000000 | 1.657757e+12 | 23.171773 | extreme fear | 23.171773 | 23.171773 | 23.171773 | 23.171773 |
| 2022-07-15 00:00:00.000000000 | 1.657843e+12 | 26.834423 | fear         | 26.834423 | 26.834423 | 26.834423 | 26.834423 |
| 2022-07-16 00:00:00.000000000 | 1.657930e+12 | 26.834423 | fear         | 26.834423 | 26.834423 | 26.834423 | 26.834423 |
| 2022-07-18 00:00:00.000000000 | 1.658102e+12 | 29.351119 | fear         | 29.351119 | 29.351119 | 29.351119 | 29.351119 |
| 2022-07-18 17:56:10.767000064 | 1.658167e+12 | 29.351119 | fear         | 29.351119 | 29.351119 | 29.351119 | 29.351119 |
<p>265 rows × 7 columns</p>



Danach wird ein Referenz-Index gesucht, welcher den kompletten Weltmarkt abbildet. In diesem Beispiel wird der iShares MSCI ACWI UCITS ETF USD (Acc) verwendet, welcher an der XETRA in Euro gehandelt wird:


```python
quote = yf.Ticker('IUSQ.DE')
hist = quote.history(period='max')
# Nicht relevante Spalten entfernen
hist = hist.drop(columns=['Dividends', 'Volume', 'Stock Splits'])
```

Im Anschluss wird das Erscheinungsbild unserer Grafik definiert.


```python
mc = mpf.make_marketcolors(up='#00ff00', down='#ff0000', inherit=True)
s = mpf.make_mpf_style(base_mpf_style='nightclouds', marketcolors=mc)
```

Die beiden Resultate werden zusammengeführt (Inner-Join). Mit der Anweisung wird sichergestellt, das nur die Einträge verwendet werden, welche in beiden Objekten vorkommen (bezogen auf die Zeitstempel). Die Datenfelder mit gleichem Namen werden dabei mit einem Suffix (*_fng:* Fear & Greed, *_acwi:* MSCI ACWI) versehen.


```python
df_all = pd.merge(df, hist, how='inner', left_index=True, right_index=True, suffixes=['_fng', '_acwi'])
# Nicht relevante Spalten entfernen
df_all = df_all.drop(columns=['rating', 'x', 'y'])
df_all
```

|| Close_fng  | Open_fng  | High_fng  | Low_fng   | Open_acwi | High_acwi | Low_acwi  | Close_acwi |
|------------|-----------|-----------|-----------|-----------|-----------|-----------|------------|
| 2021-07-19 | 13.807443 | 13.807443 | 13.807443 | 13.807443 | 60.240002 | 60.279999 | 59.169998  | 59.570000 |
| 2021-07-20 | 20.633333 | 20.633333 | 20.633333 | 20.633333 | 59.910000 | 60.369999 | 59.650002  | 60.259998 |
| 2021-07-21 | 24.466667 | 24.466667 | 24.466667 | 24.466667 | 60.470001 | 60.700001 | 60.389999  | 60.680000 |
| 2021-07-22 | 25.200000 | 25.200000 | 25.200000 | 25.200000 | 61.009998 | 61.080002 | 60.730000  | 60.990002 |
| 2021-07-23 | 29.133333 | 29.133333 | 29.133333 | 29.133333 | 61.259998 | 61.480000 | 61.169998  | 61.480000 |
| ...        | ...       | ...       | ...       | ...       | ...       | ...       | ...        | ...       |
| 2022-07-12 | 25.969248 | 25.969248 | 25.969248 | 25.969248 | 60.240002 | 60.610001 | 60.110001  | 60.459999 |
| 2022-07-13 | 23.427080 | 23.427080 | 23.427080 | 23.427080 | 60.230000 | 60.299999 | 59.259998  | 59.619999 |
| 2022-07-14 | 23.171773 | 23.171773 | 23.171773 | 23.171773 | 59.750000 | 59.990002 | 58.910000  | 59.040001 |
| 2022-07-15 | 26.834423 | 26.834423 | 26.834423 | 26.834423 | 59.470001 | 60.410000 | 59.369999  | 60.080002 |
| 2022-07-18 | 29.351119 | 29.351119 | 29.351119 | 29.351119 | 60.389999 | 60.709999 | 60.150002  | 60.430000 |
<p>253 rows × 8 columns</p>



Grenzen für den Fear & Greed Index werden festgelegt (25: Extreme Angst, 75: Extreme Gier)


```python
hls = dict()
hls['hlines'] = (25, 75)
hls['colors'] = ['r', 'g']
hls['linewidths'] = (1,1,)
hls['linestyle'] = ['dashed']
```

Nun ist alles vorbereitet, um die finale Grafik zu erstellen. Dabei werden die Werte des Fear & Greed Index im oberen (und einem gleitenden Durchschnitt mit Fenstergrösse 8), diejenigen des ACWI-Index im unteren Panel angezeigt.


```python
ap = [
    mpf.make_addplot(
        df_all['Close_acwi'],
        ylabel='Price (%s)' % quote.info['currency'],
        color='purple',
        panel=1)
]

mpf.plot(
    df_all.rename(columns={'Open_fng': 'Open', 'High_fng': 'High', 'Low_fng': 'Low', 'Close_fng': 'Close'}),
    type='line',
    title='Fear and Greed',
    ylabel='Rating',
    mav=8,
    hlines=hls,
    linecolor='yellow',
    volume=False,
    addplot=ap,
    style=s,
    figscale=1.5,
    panel_ratios=(1,1)
)
```



![Gegenüberstellung von Fear & Greed und MSCI ACWI Index](output_18_0.png)



Dabei kann beobachtet werden, dass der Verlauf der beiden Linien sehr ähnlich ist. Diese Tatsache wird mit Hilfe der Korrelationsmatrix überprüft und bestätigt.


```python
df_all[['Close_fng','Close_acwi']].corr()
```


|| Close_fng  | Close_acwi |
|------------|------------|
| Close_fng  | 1.000000   | 0.751183 |
| Close_acwi | 0.751183   | 1.000000 |
