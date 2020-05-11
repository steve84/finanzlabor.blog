---
title: Technische Analyse mit Python – Teil 1 - Diagramm-Typen und Handelsvolumen
p: finance/chart_analysis/diagram_types/gaming_stocks.md
date: 2023-04-27 20:00:00
tags:
- Technische Analyse
- Data Visualization
- Python
categories: Finanzen
toc: true
thumbnail: /gallery/thumbnails/finance/chart_analysis/diagram_types/thumbnail.jpg
---

Alle bisherigen Beiträge auf diesem Blog befassten sich ausschliesslich mit der Analyse von Fundamentaldaten. In der, in den nächsten Wochen folgenden Serie von Beiträgen, wird das Thema Chartanalyse (bezw. technische Analyse) behandelt.

In diesem Artikel geht es um die Darstellung von Aktienkursen mit Hilfe von diversen Python-Bibliotheken. Deren Installation wird im ersten Abschnitt erläutert, danach werden die verschiedenen Diagramm-Typen vorgestellt. Grafiken mit unterschiedlichen Zeitintervallen inklusive Handelsvolumen werden im praktischen Teil des Beitrags erstellt.

<!-- more -->

## Installation von Python-Bibliotheken

Um die nachfolgenden Zeichnungen zu erzeugen, wird eine Entwicklungsumgebung vorausgesetzt. Wie diese aufgesetzt wird, wurde bereits in einem {% post_link data/environment/environment 'älteren Beitrag' %} erklärt.

Folgende Bibliotheken werden verwendet:
* yfinance[^1] (Aktienkurse von Yahoo Finance)
* mplfinance[^2] (Darstellung von Aktienkursen)
* ta-lib (Hilfsmittel für technische Analysen)
* pandas (Datenanalyse)

Die einzelnen Pakete können via Anaconda Prompt installiert werden:

{% codeblock lang:bash %}
pip install yfinance mplfinance pandas
{% endcodeblock %}

### TA-Lib

TA-Lib wird im ersten Teil der Serie noch nicht verwendet, die Installation dient als Vorbereitung für die weiteren Teile. Um die Bibliothek auf der Entwicklungsumgebung zu installieren, sollte ein vorkompiliertes Paket verwendet werden. Um die korrekte Datei herunterzuladen, müssen zuerst Informationen über Betriebssystem und installierte Python-Version beschafft werden:
* Python-Version ermitteln: *python \-\-version*
* Windows-Systemtyp: Mit der [Hilfestellung von Microsoft](https://support.microsoft.com/de-ch/help/13443/windows-which-version-am-i-running) ermitteln, ob ein 32 oder 64-Bit System verwendet wird

Auf der Seite von Christoph Gohlke wird unter TA-Lib die Version, anhand der oben ermittelten Informationen, heruntergeladen. Die beiden Ziffern nach den Kleinbuchstaben cp stehen für die Python-Major-Version (cp37 für die Version 3.7.x), win32 für 32-Bit-Systeme und win-amd64 für 64-Bit-Systeme. Nachdem das Herunterladen der Datei abgeschlossen ist, wird diese mit Hilfe des folgenden Befehls installiert:

{% codeblock lang:bash %}
pip install TA_Lib-0.4.17-cp37-cp37m-win_amd64.whl
{% endcodeblock %}

Somit steht der Erstellung eines neuen Charts nichts mehr im Wege.

## Praktischer Teil

Mplfinance unterstützt zurzeit (oder in einer der nächsten Versionen) folgende Diagramm-Typen:

* Kerzen (engl. Candlestick): Der Kerzenkörper zeigt den Eröffnungskurs sowie den Schlusskurs an. Ist dieser grün (bzw. weiss), war der am Ende der Beobachtung höher als zu Beginn. Eine rote (bzw. schwarze) Kerze zeigt das Gegenteil an. Das Ende des Kerzendochts zeigt den höchsten beziehungsweise tiefsten Wert innerhalb der Beobachtung.
* OHLC (Open, High, Low, Close): Hat im Gegensatz zu den Kerzen keinen ausgefüllten Körper sonder markiert Eröffnung (links) und Schluss (rechts) mit einem simplen Querstrich
* Linie (engl. Line): Zeigt nur die Schlusskurse an und verbindet die einzelnen Beobachtungen miteinander
* Renko: Dieser Chart-Typ zeigt nur eine Veränderung an, wenn der Kurs eine vordefinierte Veränderung erfährt. Alle Elemente haben die gleiche Länge und unterscheiden sich nur durch ihre Farbe (grün: positive Bewegung, rot: negative Bewegung) und Position (jedes Element schliesst direkt an seinen Vorgänger an). Lange Seitwärtsbewegungen ohne grosse Schwankungen sind daher nicht auf dem Diagramm ersichtlich.

Um eines der oben erwähnten Diagramme als Grafik zu erstellen, werden aktuelle Börsendaten benötigt. Mit der installierten Anwendung *yfinance* können die Daten von Yahoo Finance bezogen werden. Dazu wird lediglich, dass zum Wertpapier zugehörige Symbol benötigt. Die Symbol-Bezeichnungen können auf der Website von [Yahoo Finance](https://finance.yahoo.com/) gefunden werden. Dazu wird einfacher der Name des gesuchten Wertpapiers in die Suche eingegeben, danach kann das Kennzeichen aus den Vorschlägen entnommen werden (links vor den Namen).

Mit der *history*-Methode können historische Kursdaten geladen werden. Als Parameter können *period* (Zeitraum der Beobachtungen) und *interval* (Häufigkeit der Beobachtungen) mitgegeben werden. Alle möglichen Werte können aus dem Blogartikel des Entwicklers entnommen werden.

Die einzelnen Charts können mit mplfinance kreiert und als Datei abgespeichert werden. Die Dokumentation beinhaltet einige Beispiele und kann bei Fragen und Problemen konsultiert werden. Leider ist diese auf eine neuere Version der Software aufgebaut. So können zum Beispiel noch keine Renko-Diagramme gezeichnet werden. Mit der Methode *plot* werden die Kurse zum Leben erweckt.

Die Bibliothek bietet auch die Möglichkeit, das Handelsvolumen in die diversen Kursverläufe zu integrieren. Diese werden in den unteren Bereich der Grafik integriert und zeigen die Anzahl der gehandelten Wertpapiere pro Zeitintervall auf.

### Diagramme mit Python erstellen

Das nachfolgende Code-Stück erstellt 4 verschiedene Bilder. Als Grundlage dienen die Kurse des ETFs iShares ACWI, welcher den Referenzindex MSCI All Coutry World Index (ACWI) abbildet. Der ETF wird an der NASDAQ in US Dollar gehandelt. Alle Graphen, mit Ausnahme des Letzten, verfügen über einen Intervall von einem Tag. Der Letzte signalisiert nur jede Handelswoche eine Beobachtung. Alle drei möglichen Diagramm-Typen sind vertreten und eines der Kerzen-Diagramme enthält zusätzlich das dazugehörige Handelsvolumen.

{% include_code Diagramm-Typen mit Python erstellen lang:python finance/chart_analysis/diagram_types/diagram_types.py %}

Während der Ausführung der Python-Datei in der Kommandozeile wurden folgende Bilder erstellt:

![Typ: Kerzen (Candlestick), Periode: 1 Tag](candle_chart_1d_ACWI.png)
![Typ: OHLC, Periode: 1 Tag](ohlc_chart_1d_ACWI.png)
![Typ: Linie (Line) inkl. Volumen, Periode: 1 Tag](line_chart_1d_ACWI.png)
![Typ: Kerzen (Candlestick), Periode: 5 Tage](candle_chart_1w_ACWI.png)

Der nächste Teil der Serie befasst sich mit Unterstützungs -und Trendlinien, gleitende Durchschnitte  und Bändern.

[^1]: [Blog-Beitrag über die Verwendung von yfinance](https://aroussi.com/post/python-yahoo-finance)
[^2]: [Wiki-Seit von mplfinance (inkl. diverser Beispiele)](https://github.com/matplotlib/mplfinance)
[^3]: [Seite mit vorkompilierten TA-Lib Paketen](https://www.lfd.uci.edu/~gohlke/pythonlibs)
