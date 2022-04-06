---
title: Chart-Plotting
p: programming/chart_plotting/chart_plotting.md
date: 2022-04-06 20:00:00
tags:
- Programmierung
- Python
categories: Programmierung
toc: false
thumbnail: /gallery/thumbnails/programming/efficiency_tipps/thumbnail.jpg
---

Der heutige Beitrag behandelt die Beschaffung, Manipulation und Darstellung von Kursdaten mit Hilfe der Python-Bibliotheken yfinance (Ermöglicht den Bezug von Daten von Yahoo Finance) und mplfinance (Visualisierung von Börsendaten). Die nachfolgenden Codestücke sind ideal für

<!-- more -->

## Voraussetzungen

Damit die nachfolgenden Befehle auch korrekt ausgeführt werden können, muss eine funktionierende Python-Umgebung vorhanden sein. Eine Möglichkeit wurde in einem der ersten Beiträge auf diesem vorgestellt. Zusätzlich müssen noch folgende Python-Pakete installiert werden:

* [yfinance](https://github.com/ranaroussi/yfinance)
* [mplfinance](https://github.com/matplotlib/mplfinance)
* [ta](https://technical-analysis-library-in-python.readthedocs.io/en/latest/)

## Befehle

Zuerst müssen alle benötigten Bibliotheken importiert werden:


```python
import yfinance as yf
import pandas as pd
import numpy as np
import mplfinance as mpf
from ta.trend import MACD
```

Danach kann eine beliebige Aktie beziehungsweise ein ETF gesucht werden. Um das Ticker-Symbol zu finden, kann auf der Seite [Yahoo Finance](https://finance.yahoo.com/) im Suchfeld die gewünschte Aktie gesucht werden, wobei das Symbol in der ersten Spalte der Suchresultate steht (bei Tesla zum Beispiel TSLA). In diesem Beispiel verwenden wird den iShares MSCI ACWI UCITS ETF USD (Acc), welcher an der XETRA in Euro gehandelt wird:


```python
quote = yf.Ticker("IUSQ.DE")
```

Nun können verschiedenen Aktionen auf dem Ticker-Objekt durchgeführt werden. Eine davon ist der Bezug von historischen Kursen. Mit Hilfe der Periode kann die Anzahl der Resultate gesteuert werden (mit *max*" werden alle verfügbaren Datensätze geladen):


```python
hist = quote.history(period='max')
```

Nun kann das Ergebnis der Abfrage angeschaut werden. Dies ist wichtig, um allfällige Fehler in den Daten zu finden. Es kann manchmal vorkommen, dass Unregelmässigkeiten in den Daten von Yahoo Finance auftauchen.


```python
hist
```

|| Open       | High      | Low       | Close     | Volume    | Dividends | Stock Splits |
|------------|------------|-----------|-----------|-----------|-----------|-----------|--------------|
| Date       |
| 2011-10-21 | 21.370001 | 21.370001 | 21.370001 | 21.370001 | 0         | 0            | 0   |
| 2011-10-24 | 21.370001 | 21.370001 | 21.370001 | 21.370001 | 0         | 0            | 0   |
| 2011-10-25 | 21.370001 | 21.370001 | 21.370001 | 21.370001 | 0         | 0            | 0   |
| 2011-10-26 | 21.370001 | 21.370001 | 21.370001 | 21.370001 | 0         | 0            | 0   |
| 2011-10-27 | 21.370001 | 21.370001 | 21.370001 | 21.370001 | 0         | 0            | 0   |
| ...        | ...       | ...       | ...       | ...       | ...       | ...          | ... |
| 2022-03-31 | 65.050003 | 65.320000 | 64.959999 | 64.959999 | 158336    | 0            | 0   |
| 2022-04-01 | 64.900002 | 65.489998 | 64.820000 | 64.820000 | 198900    | 0            | 0   |
| 2022-04-04 | 65.220001 | 65.769997 | 65.000000 | 65.720001 | 83534     | 0            | 0   |
| 2022-04-05 | 65.970001 | 66.080002 | 65.660004 | 65.839996 | 114113    | 0            | 0   |
| 2022-04-06 | 65.620003 | 65.699997 | 64.489998 | 64.639999 | 77849     | 0            | 0   |
<p>2651 rows × 7 columns</p>


In der Ausgabe ist zu sehen, dass nicht nur die Schlusskurse mitgeliefert werden. Dividenden sowie das Handelsvolumen werden ebenfalls von der Datenquelle geliefert.

Nun soll der Kursverlauf in einem Diagramm visualisiert werden. Dazu sind einige Vorbereitungsarbeiten notwendig. Die nächsten beiden Zeilen definieren die Gestaltung des resultierenden Diagrammes. Der dritte Befehl legt die Anzahl an Datenpunkten fest, welche in der Grafik gezeichnet werden sollen.


```python
mc = mpf.make_marketcolors(up='#00ff00', down='#ff0000', inherit=True)
```


```python
s = mpf.make_mpf_style(base_mpf_style='nightclouds', marketcolors=mc)
```


```python
number_of_datapoints = 50
```

Die nachfolgende Anweisung generiert mit Hilfe von mplfinance ein Liniendiagramm inklusive Handelsvolumen. Die Werte für den Titel sowie die Y-Achse des oberen Diagrammes werden aus dem Attribut *info* des *quote*-Objektes entnommen. Mit Hilfe der Option *figscale* kann die Grösse der Grafik beeinflusst werden. Die Methode *tail* liefert die letzten x-Einträge des DataFrame's (pandas Datenobjekt) zurück.


```python
mpf.plot(hist.tail(number_of_datapoints), type='line', title=quote.info['longName'], ylabel='Price (%s)' % quote.info['currency'], volume=True, style=s, figscale=1.5)
```



![png](output_15_0.png)



Nun haben wir jedoch das Problem, dass wir nur einen sehr kleinen Datenbereich anzeigen können. Um alle Datenpunkte (ca. 2'600) anzeigen zu können, müssen die Datenpunkte zusammengelegt werden. Dazu werden pandas-Hilfsmethoden verwendet, um 5 Handelstag zu einem Datensatz zusammen zu legen.


```python
hist_1w = hist.asfreq('1D').resample('5D').agg({'Open': lambda x: x.bfill().iloc[0], 'High': max, 'Low': min, 'Close': lambda x: x.pad().iloc[-1], 'Volume': sum})
```

Danach wird das Resultat überprüft und die Anzahl der Datenpunkte erhöht:


```python
hist_1w
```

|| Open       | High      | Low       | Close     | Volume    |
|------------|------------|-----------|-----------|-----------|-----------|
| Date       |
| 2011-10-21 | 21.370001 | 21.370001 | 21.370001 | 21.370001 | 0.0      |
| 2011-10-26 | 21.370001 | 21.370001 | 21.370001 | 21.370001 | 0.0      |
| 2011-10-31 | 21.370001 | 21.370001 | 21.370001 | 21.370001 | 0.0      |
| 2011-11-05 | 21.370001 | 21.370001 | 21.370001 | 21.370001 | 0.0      |
| 2011-11-10 | 21.370001 | 21.370001 | 21.370001 | 21.370001 | 0.0      |
| ...        | ...       | ...       | ...       | ...       | ...      |
| 2022-03-17 | 62.720001 | 64.180000 | 62.200001 | 63.779999 | 242524.0 |
| 2022-03-22 | 64.309998 | 64.930000 | 64.209999 | 64.690002 | 309921.0 |
| 2022-03-27 | 64.989998 | 65.629997 | 64.839996 | 64.959999 | 567759.0 |
| 2022-04-01 | 64.900002 | 66.080002 | 64.820000 | 65.839996 | 396547.0 |
| 2022-04-06 | 65.620003 | 65.699997 | 64.489998 | 64.639999 | 77849.0  |
<p>765 rows × 5 columns</p>

```python
number_of_datapoints = 200
```

Die Python-Bibliothek mplfinance bietet auch die Möglichkeit, den bestehenden Grafen mit Weiteren zu überlagern. Nun soll in einem nächsten Schritt ein Element der technischen Analyse integriert werden. In diesem Fall handelt es sich um den [MACD Oszillator](https://school.stockcharts.com/doku.php?id=technical_indicators:moving_average_convergence_divergence_macd). Dieser wird auf dem Schlusskurs berechnet:


```python
macd_obj = MACD(hist_1w['Close'].tail(number_of_datapoints))
```

Nun werden die zusätzlichen Datenpunkte in einem Array abgelegt. Mit dem Attribut *panel* wird der Ort angegeben, wo die Punkte gezeichnet werden sollen (wobei das erste Diagramm den Wert 0 hat):


```python
adps = [
    mpf.make_addplot(macd_obj.macd_diff(), type='bar', ylabel='MACD', panel=1),
    mpf.make_addplot(macd_obj.macd(), type='line', color='w', panel=1),
    mpf.make_addplot(macd_obj.macd_signal(), type='line', color='r', panel=1)
]
```

Nun wird das neue Diagramm angezeigt. Dieses Mal wird ein Kerzen-Diagramm mit einem gleitenden Durchschnitt (mit Fenstergrösse 14) erstellt. Darunter ist der MACD Oszillator zu finden:


```python
mpf.plot(hist_1w.tail(number_of_datapoints), addplot=adps, type='candle', mav=(14,), style=s, figscale=1.5)
```



![png](output_26_0.png)



Als letzter Schritt sollen die Kauf- beziehungsweise Verkaufssignale berechnet und im Diagramm angezeigt werden. Dazu werden wieder Methoden der pandas-Bibliothek verwendet. Ändert das MACD-Histogramm von Zeitpunkt *t-1* zu *t* das Vorzeichen (Plus zu Minus), handelt es sich um ein Verkaufssignal. Wechselt das Vorzeichen von Minus zu Plus, bedeutet dies ein Kaufssignal.


```python
sell_signal = macd_obj.macd_diff().rolling(2).apply(lambda x: 1 if x[0] > 0 and x[1] < 0 else 0).fillna(0).rename('Sell_Signal')
```


```python
buy_signal = macd_obj.macd_diff().rolling(2).apply(lambda x: 1 if x[0] < 0 and x[1] > 0 else 0).fillna(0).rename('Buy_Signal')
```

Im Anschluss werden die Signale zu dem bestehenden Datenobjekt hinzugefügt und als Subplot in das bereits bestehende Array aufgenommen


```python
hist_1w['Sell_Signal'] = hist_1w.join(sell_signal).apply(lambda x: x['High'] + 2 if x['Sell_Signal'] == 1 else np.nan, axis=1)
```


```python
adps.append(mpf.make_addplot(hist_1w['Sell_Signal'].tail(number_of_datapoints), type='scatter', markersize=50, marker='v', panel=0))
```


```python
hist_1w['Buy_Signal'] = hist_1w.join(buy_signal).apply(lambda x: x['Low'] - 2 if x['Buy_Signal'] == 1 else np.nan, axis=1)
```


```python
adps.append(mpf.make_addplot(hist_1w['Buy_Signal'].tail(number_of_datapoints), type='scatter', markersize=50, marker='^', panel=0))
```

Danach wird das finale Diagramm erstellt:


```python
mpf.plot(hist_1w.tail(number_of_datapoints), addplot=adps, type='candle', mav=(14,), style=s, figscale=1.5)
```



![png](output_36_0.png)
