---
title: "Technische Analyse – Teil II: Grundlagen"
p: finance/chart_analysis/diagram_types/gaming_stocks.md
date: 2020-06-14 18:00:00
tags:
- Technische Analyse
- Data Visualization
- Aktien
categories: Finanzen
toc: true
thumbnail: /gallery/thumbnails/finance/chart_analysis/diagram_types/thumbnail.jpg
---

Diagramme sind Grafiken, welche zur Darstellung von Daten, Sachverhalten oder Informationen verwendet werden. In der technischen Analyse beinhalten diese in der Regel ein zweidimensionales kartesisches Koordinatensystem, welche aus einer Abszissen- (horizontal) und einer Ordinatenachse (vertikal), welche orthogonal (im rechten Winkel) aufeinander stehen, bestehen. Der Schnittpunkt der beiden Achsen wird Ursprung genannt. Auf der x-Achse (Abszisse) wird im Normalfall die Zeit, auf der y-Achse der Preis abgetragen. Da weder Zeit noch Preis negative Werte annehmen können, werden die Datenpunkte im ersten Quadrant des Koordinatensystems abgebildet. Um gewisse Sachverhalte besser darstellen zu können, kann es vorkommen, dass nur bestimmte Abschnitte der beiden Achsen sichtbar sind. Bewegt sich eine Preis im beobachteten Zeitfenster zwischen 30 und 50 USD, werden die Bereiche von 0 bis 25 sowie 55+ nicht dargestellt. Moderne Chart-Software führt diese Optimierung automatisch aus, sobald eine vordefinierte oder fixe Zeitspanne ausgewählt wurde. Die Mehrheit der Diagramme verwenden lineare Koordinaten – Die Differenz zwischen zwei Koordinatenpunkten, auf der dazugehörigen Achse, haben immer den gleichen Wert. Bei einer logarithmischen Skala wird der Wertunterschied zwischen zwei Koordinaten immer grösser, je weiter weg man sich vom Ursprung bewegt.

<!-- more -->

Es besteht die Möglichkeit, die Preisentwicklung in verschiedenen Zeitspannen wiederzugeben. Nach Abschluss eines solchen Intervalls werden die fünf Messgrössen (Eröffnungs-, Höchst-, Tiefst- und Schlusskurs sowie Volumen) festgehalten. Eine Dauer von unter vier Stunden wird für kurzfristigere Analysen (Daytrading), längere Zeiträume für langfristiges handeln verwendet.

Inhaltsverzeichnis der Serie "Technische Analyse":

* {% post_link finance/chart_analysis/introduction/introduction 'Einführung (Begriffsdefinition, Dow Theorie)' %}
* *Grundlagen (verschiedene Diagrammtypen, Zeitintervalle, Widerstands- und Unterstützunglinien)*
* Trendlinien/-kanäle
* Volumen und Lücken (Gaps)
* Preismuster (Double Top, Flaggen, Rechtecke, uvm.)
* Kerzenmuster (Hanging Man, Marubozu, Spinning Top, uvm.)
* Fibonacci (Geschichte, Definition, Retracement Levels)
* Technische Indikatoren (Gleitende Durchschnitte, Bollingerbänder)
* Oszillatoren (RSI, MACD, Momentum, uvm.)
* Technische Umsetzung mit Python (Installation, Diagramme zeichnen, Mustererkennung)

## Chart-Typen

Es existieren unzählige verschiedene Diagrammtypen. In diesem Kapitel werden fünf davon näher vorgestellt und mit Beispielen ergänzt.  Als Datenquelle dient die Kursentwicklung des iShares ACWI ETFs von der Firma MSCI Inc. ETFs iShares ACWI, welcher den Referenzindex MSCI All Coutry World Index (ACWI) abbildet. Der Fond wird an der NASDAQ in US Dollar gehandelt.

### Linie (Line)

Das Linien-Diagramm ist eines der bekanntesten Diagramm-Typen überhaupt. Dabei werden die abgetragenen Datenpunkte durch gerade Linien miteinander verbunden. Damit werden normalerweise die Schlusskurse einer Aktie visualisiert. Auf dem Beispiel-Diagramm sind die täglichen Schlusskurse seit Jahresbeginn (YTD) eingezeichnet. Die beiden Trend-Phasen (Beginn der Corona-Krise sowie die anschliessende Erholung)

![MSIC ACWI ETF, Typ: Linie (Line), Periode: 1 Tag](line_chart_1d_ACWI.png)

### Kerzen (Candlestick)

Der Kerzenkörper (engl. body) zeigt den Eröffnungskurs sowie den Schlusskurs an. Ist dieser grün (bzw. weiss), war dieser am Ende der Beobachtung höher als zu Beginn. Ein roter (bzw. schwarze) Körper zeigt das Gegenteil an. Das Ende des Kerzendochts (engl. shadows oder wicks) zeigt den höchsten beziehungsweise tiefsten Wert innerhalb einer Beobachtung. Im unten abgebildeten Kerzen-Chart zum ACWI ETF sind nicht nur die Schlusskurse, sondern auch die Geschichte der Entstehung derjenigen, ersichtlich. Die Entstehung einer Lücke (Gap), welche in einem späteren Beitrag dieser Serie vorgestellt wird, ist in einem Linien-Diagramm nicht sichtbar. Diese, am 11. Juni 2020 entstandene Gegebenheit, ist für manche Chart-Techniker ein wichtiger Hinweis für den weiteren Kursverlauf.

![MSIC ACWI ETF, Typ: Kerzen (Candlestick), Periode: 1 Tag](candle_chart_1d_ACWI.png)

Es existieren Ableitungen wie zum Beispiel die Heikin-Ashi-Kerzen, welche mit Hilfe der OHLC-Werte ($P_O$, $P_H$, $P_L$ und $P_C$) - des vorhergehenden $t-1$ sowie aktuellen Tages $t$ - berechnet werden:

$$
P_{C_{t}} = {\frac{1}{4} (P_{O_{t}} + P_{C_{t}} + P_{H_{t}} + P_{L_{t}})}
$$

$$
P_{O_{t}} = {\frac{1}{2} (P_{O_{t-1}} + P_{C_{t-1}})}
$$

$$
P_{H_{t}} = {Max[P_{H_{t}}, P_{O_{t}}, P_{C_{t}}]}
$$

$$
P_{L_{t}} = {Min[P_{L_{t}}, P_{O_{t}}, P_{C_{t}}]}
$$

Dabei handelt es sich um eine sehr einfache Form der Berechnung, es existieren noch weit komplexere Formeln für die Konstruktion des Kerzentyps. Durch die Glättung dieser Werte wirkt die Kerzenabfolge harmonischer. Damit werden zum Beispiel rote „Störkerzen" in einem positiven Trend, mit mehrere grünen Kerzen, eliminiert.

![MSIC ACWI ETF, Typ: Heikin-Ashi-Kerzen, Periode: 1 Tag](heikin_ashi_candle_chart_1d_ACWI.png)

### Balken (Bar)
Dieser Diagrammtyp hat im Gegensatz zu den Kerzen keinen ausgefüllten Körper sonder markiert Eröffnung (links) und Schluss (rechts) mit einem simplen Querstrich. Diese schlankere Abwandlung der Kerzencharts ist für die Kombination mit anderen Diagramm-Typen (zum Beispiel eine Überlagerung des gleitenden Durchschnittes in Form einer Linie) ideal.

![MSIC ACWI ETF, Typ: Balken (Bar), Periode: 1 Tag](bar_chart_1d_ACWI.png)

### Renko
Dieser Chart-Typ zeigt nur eine Veränderung an, wenn der Kurs eine vordefinierte Veränderung erfährt. Die Zeitachse hat daher keinen linearen Verlauf wie die bis hierhin vorgestellten Typen. Die einzelnen Elemente haben alle die gleiche Länge und Höhe, sie unterscheiden sich nur durch ihre Farbe (grün: positive Bewegung, rot: negative Bewegung) und Position (jedes Element schliesst direkt an der oberen oder unteren Ecke seines Vorgängers an). Lange Seitwärtsbewegungen ohne grosse Schwankungen sind daher nicht auf dem Diagramm ersichtlich. Um von einer Aufwärtsbewegung in eine Abwärtsbewegung (oder umgekehrt) zu wechseln, muss der Preis sich um mindestens das Zweifache der vordefinierten Veränderung bewegen. In der, mit Hilfe von tradingview erstellten Grafik, sind die beiden aktuellsten Trendphasen sehr gut ersichtlich. Es wurde ein Betrag von 3 USD als Blockhöhe festgelegt und es braucht daher eine Gegenbewegung von 6 USD um einen Farbwechsel zu bewirken Allgemein ist das Renko-Diagramm perfekt dazu geeignet, um primäre Trendphasen zu visualisieren. Die Striche unter- oder oberhalb der Renko-Bauklötze zeigen an, ob in der Zeitdauer zwischen aktuellem und nachfolgendem Block ein Preis, welcher eine Trendwende herbei gefügt hätte, existiert hat. Da es sich dabei nicht um den Schlusskurs gehandelt hat, wurde kein neuer Block in entgegengesetzter Farbe an die bestehende Kette angehängt. Diese Hilfslinien treten meistens kurz vor und kurz nach einer Trendumkehrung auf.

![MSIC ACWI ETF, Typ: Renko, Periode: 1 Tag](renko_chart_1d_ACWI.png)

### Point and Figure
Die „Point and Figure"-Diagramme (kurz P&F) haben grosse Ähnlichkeit mit den Renko-Diagrammen. Bewegungen, welche die geforderte Preisdifferenz übersteigen, werden mit X‘s (positive Bewegung) und O‘s (negative Bewegung) in die Grafik eingezeichnet. Zusätzlich wird noch die Mindestanzahl definiert, welche benötigt wird, um eine Umkehrung herbeizuführen. Im Gegensatz zu den Renko-Charts (mindestens 2) ist dieser Wert frei wählbar. Oft verwendete Grössen für diesen Parameter sind 1, 2 oder 3. Der Titel eines solchen Charts beinhaltet meistens diese beiden Informationen. Die Zeichenfolge „1 x 3" bedeutet, dass sich der Preis um mindestens 1 Einheit verändern muss, um auf der Grafik sichtbar zu werden. Beträgt die Differenz 3 Einheiten, wird eine neue Spalte mit dem anderen Zeichen begonnen. Daher besteht eine Spalte aus mindestens 3 Symbolen (beziehungsweise 1 für eine 1-Punkt-Umkehrung, 2 für eine 2-Punkte-Umkehrung). Für das Beispiel einer 3-Punkte-Umkehrung wurde eine geforderte Preisdifferenz von 1.5 USD festgelegt. Auch hier sind die beiden Corona-Trendphasen in den letzten beiden Spalten ersichtlich. Aktuell ist der Kurs noch 1.19 USD davon entfernt, eine Umkehrung bei 72 USD herbeizuführen (letztes X bei 76.50 USD, aktueller Preis 73.19 USD, Betrag für die Umkehrung 3 x 1.5 USD = 4.5 USD). Bei einer 2-Punkte-Umkehrung würde die letzte Spalte aus 2 O‘s bestehen.

![MSIC ACWI ETF, Typ: Point and Figure, Periode: 1 Tag](pf_chart_1d_ACWI.png)

## Unterstützungs-/Widerstandslinien

Die Unterstützungs- beziehungsweise Widerstandslinie ist eine horizontale Gerade, an welcher die Preisbewegungen mehrfach abprallen und sich nach der Berührung in die gegen gesetzte Richtung weiter bewegen. Je häufiger eine solche Linie getestet (touchiert) wird, umso signifikanter wird diese. Wird diese imaginäre Marke nach mehrmaligem testen durchbrochen, findet ein Rollenwechsel statt. Dabei wird ein Widerstand zu einer Unterstützung und umgekehrt. Dieser Rollentausch ist im Kerzen-Diagramm der Unilever-Aktie gegen Ende von Q1 2019 gut ersichtlich.

![Unilever NV, Typ: Kerzen (Candlestick), Periode: 1 Tag](candle_chart_1d_support_resistance_UNA.AS.png)

Das Zeichnen einer solchen Geraden ist keine exakte Wissenschaft und es gibt mehrere Vorgehensweisen um diese zu erstellen. Mehrheitlich werden die beiden Enden der Preisentwicklung innerhalb einer Zeitperiode verwendet. Dazu wird die Linie mit Hilfe eines Kerzen-Charts bestmöglich an die Enden der einzelnen Kerzendochte konstruiert. Eine gewisse Ungenauigkeit muss jedoch in Kauf genommen werden, da nicht jeder Docht exakt auf der gezeichneten Linie enden wird. Dieses Problem ist auf dem Kerzendiagramm der Nestlé-Aktie gut ersichtlich. Die eingezeichnete Widerstandslinie wird fünfmal getestet und wird im ersten Quartal 2019 durchbrochen. Bei den Schnittpunkten 2 bis 4 endet die Verlängerung der Kerze fast exakt auf der gezogenen Geraden. Der obere Docht der sechsten Kerze endet mit einem deutlich grösseren Abstand als seine Nachfolger.

![Nestlé SA, Typ: Kerzen (Candlestick), Periode: 1 Tag](candle_chart_5d_support_resistance_NESN.SW.png)

In der Nähe solcher Linien ist häufig ein erhöhtes Handelsvolumen zu beobachten. Die Wahrscheinlichkeit, dass sich der Preis in der nahen Zukunft weiter von der berührten Linie wegbewegt (abprallt), steigt. Oft entstehen die Marken bei runden Zahlen, da sich die menschliche Psyche damit wohler fühlt. Manche Broker runden exotische Beträge automatisch auf die nächste Zwischenstufe auf (z.B. in Stufen von 5 Rappen beziehungsweise Cents) oder ab.

## Ausblick

Widerstands- und Unterstützungslinien sind eine Spezialform von Trendlinien, welche im nächsten Artikel der Serie, zusammen mit den Trendkanälen, erklärt werden.


[^1]: ["Heikin-Ashi: A Better Candlestick", Investopedia](https://www.investopedia.com/trading/heikin-ashi-better-candlestick)
