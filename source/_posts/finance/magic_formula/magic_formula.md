---
title: Magic Formula - Theorie und Praxis
p: finance/magic_formula/magic_formula.md
date: 2019-11-14 18:00:00
tags:
- Theorie
- Experiment
- Aktien
- Data Visualization
- Data Science
- Python
categories: Finanzen
toc: true
thumbnail: /gallery/thumbnails/finance/magic_formula/thumbnail.jpg
---
Die Magic Formula von Joel Greenblatt ist eine der bekanntesten Anlagetechniken des 21. Jahrhunderts. In diesem Beitrag wird die Formel vorgestellt und in einem praktischen Teil angewendet. Zum Schluss werden die besten 20 Aktien, welche durch die Formel ermittelt wurden, in visualisierter Form vorgestellt. Nachmachen ausdrücklich empfohlen!

<!-- more -->

## Einführung

Im Jahre 2005 veröffentlichte der Hedge-Fund-Manager und Investor Joel Greenblatt das Buch "The Little Book That Beats The Market" (Erschienen im [Wiley Verlag](https://www.wiley.com/en-us/The+Little+Book+That+Beats+the+Market-p-9780470893661)). Dieses verkaufte sich 300'000 Mal und bewog den Autoren dazu, eine Neuauflage mit dem Namen "The Little Book That Still Beats The Market" auf den Markt zu bringen. In den beiden Büchern beschreibt Greenblatt, wie Investoren mit einer Formel, bestehend aus zwei Kennzahlen, den Aktienmarkt schlagen können. Er gab ihr den Namen "Magic Formula".

### Kennzahlen

Für die Berechnung werden die Gewinn- sowie Kapitalrendite (Earnings Yield, Return on Capital) verwendet. Nachfolgend die Definition der beiden Kennzahlen. Für die Berechnung der beiden Werte wird das EBIT (Earnings before interest and taxes, Gewinne vor Zinsen und Steuern) verwendet:
$$
EBIT = {Revenue - COGS - Operating\ Expenses}
$$

Bei COGS (Costs of goods sold) handet es sich um die Kosten für die verkaufte Ware. Um das das EBIT zu erhalten, werden die Waren- sowie Betriebskosten (Operating expenses) vom Umsatz abgezogen.
Der Firmenwert des jeweiligen Unternehmens wird wie folgt berechnet:
$$
Enterprise\ Value = {Market\ capitalization + Total\ debts - Cash}
$$

Mit Hilfe der beiden Hilfskennzahlen kann nun die Gewinnrendite errechnet werden:
$$
Earnings\ Yield = {EBIT \over Enterprise\ Value}
$$

Zur Berechnung der Kapitalrendite werden das Netto-Umlaufvermögen (Net Working Capital)[^1] sowie das Netto-Anlagevermögen (Net Fixed Assets)[^2] benötigt:
$$
Net\ Working\ Capital ={ Current\ Assets - Cash - Current\ Liabilities}
$$

$$
Net\ Fixed\ Assets = {Total\ Assets - Current\ Assets - Intangibles - Goodwill}
$$

Zum Schluss die Berechnung der Rendite mit Hilfe des oben bereits verwendeten EBITs:
$$
Return\ On\ Capital = {EBIT \over Net\ Working\ Capital + Net\ Fixed\ Assets}
$$

Nun ist der schwierigste Teil des Beitrags überstanden. Die Berechnung der einzelnen Werte wird im praktischen Teil anhand eines Beispieles aufgezeigt.

### Vorgehensweise

Die Magic Formula wird mit einer strikten Vorgehensweise angewendet. Damit sollen Emotionen aus dem Spiel gelassen werden und das sogenannt "Stock picking" nach eindeutigen Regeln betrieben werden. Die Umsetzung wurde von Greenblatt wie folgt beschrieben:

* Festlegung eines Minimums für die Marktkapitalisierung der einzelnen Firmen (normalerweise 50 Mio. USD)
* Ausschluss von Unternehmungen aus den Bereichen Finanzen und Energie
* Ausschluss von Fremdfirmen (Es werden nur Aktien aus einem bestimmten Land untersucht)
* Berechnung des Gewinnrendite
* Berechnung der Kapitalrendite
* Anhand der Gewinnrendite Rang zuweisen (der Firma mit der höchsten Rendite wird die 1 zugewiesen)
* Anhand der Kapitalrendite Rang zuweisen (der Firma mit der höchsten Rendite wird die 1 zugewiesen)
* Die Summe der beiden Ranglistenplätze ergibt den Gesamtrang
* Kauf der 20-30 besten Wertpapier (Einmalkauf oder verteilt über mehrere Monate)
* Nach einem Jahr Neubeurteilung und Rebalancing des Portfolios (Verkauf von defizitären Werten vor der 1 Jahres-Marke, Verkauf von Gewinnern eine Woche nach Jahresfrist)
* Strategie mindestens 5-10 Jahre verfolgen

### Performance
Im Buch vergleicht Greenblatt die Performance der grössten 1'000 Aktien (anhand der Marktkapitalisierung) für die Jahre 1988 bis 2004:

* Magic Formula (30 Aktien): 22.9%
* Markt (gleich gewichtet zu 0.1%): 11.7%
* S&P 500 (nach Marktkapitalisierung gewichtet):  12.4%

In einem anderen Vergleich werden 2'500 US-Aktien anhand der Formel bewertet und nach Rang aufsteigend sortiert. Danach wird die Rangliste in 10 Gruppen mit je 250 Wertpapieren aufgeteilt (Gruppe 1 beinhaltet Rang 1 bis 250, Gruppe 2 251 bis 500, usw.). Dann wird das CAGR der einzelnen Gruppen berechnet (von 1988 bis 2004) und miteinander verglichen. Greenblatt stellte fest, dass jede dieser Gruppen seinen Nachfolger outperformen konnte (z.B. Gruppe 1 mit 17.9% schlägt Gruppe 2 mit 15.6%, Gruppe 2 schlägt Gruppe 3 mit 14.89, usw.).

Aktuellere Zahlen (2005 bis 2018) sind auf Seekinging Alpha[^3] einsehbar:

* Performance: 104.62%
* CAGR: 5.49%
* Maximaler Drawdown: 62.92%

Es existieren auch einige Wikifolio-Zertifikate, zum Beispiel DE000LS9LMM2[^4]. Die Performance nach drei Jahren beträgt 3 Prozent und das investierte Kapital beläuft sich auf 12'000 CHF.


### Vor- und Nachteile

Diese Strategie hat ihre Stärken und natürlich auch Schwächen. Hier eine kurze Zusammenfassung der einzelnen Punkte:

* Vorteile
  * Einfache Berechnung
  * Keine Emotionen
  * Höhere Performance als der Referenzmarkt
  * Kann automatisiert berechnet werden (praktischer Teil dieses Beitrags)
* Nachteile
  * Hohe Transaktionskosten
  * Hoher Zeitaufwand für Kauf und Verkauf
  * Small und Mid Caps werden ignoriert
  * Disziplin

#### Kosten

Einer der grössten Schwächen dieser Strategie sind die Transaktionskosten ("Hin und her macht Taschen leer"). Das nachfolgende Beispiel vergleicht die Strategie von Herrn Greenblatt und ein einfaches ETF-Investment auf den S&P 500 über 17 Jahre hinweg. Zuerst werden einige Annahmen zu den beiden Strategien getroffen, um die Berechnung ein wenig zu vereinfachen:

* Beim untersuchten ETF handelt es sich um den iShares Core S&P 500 UCITS ETF (Acc) mit einer Total Expense Ratio (TER) von 7 Basispunkten. Die Fondwährung ist US-Dollar. Er ist einer der grössten ETFs auf diesen Index und wird daher für dieses Beispiel verwendet. Anhand der Zahlen von trackingdifferences.com[^5] werden die Gesamtkosten auf -20 Basispunkte festgestellt. Der ETF hat eine bessere Performance als der Referenzindex und es resultieren Gesamtkosten von -13 Basispunkten. In anderen Worten, der ETF kostet nichts und liefert ein besseres Resultat als die hier angenommenen 12.4%. Da jedoch eine solche Abweichung zum Referenzindex nicht definitiv angenommen werden kann, werden trotzdem die 7 Basispunkte als laufenden Kosten für den ETF berechnet.
* Für die Berechnungen wird ein Depot bei einem grossen Schweizer Finanzinstitut gewählt. Das Depot der beiden Strategien hat folgende Kostenstruktur für Transaktionen:
  * 0 - 1'000 USD: 25 USD
  * 1'001 - 5'000 USD: 35 USD

  Somit steigen die Transaktionskosten ab Jahr 13 von 25 auf 35 USD pro Transaktion an (Magic Formula). Das Depot hat eine Jahresgebühr von 90 CHF, welche direkt für Transaktionen verwendet werden können (Trading Credits). Daher fallen für die ersten Käufe/Verkäufe pro Jahr keine Courtagen an
* Für das erste Jahr werden für beide Strategien keine Kursbewegungen angenommen (Vereinfachung der Berechnung)
* Für den Wechselkurs von CHF/USD gilt die Parität
* Für die Magic Formula werden nur Aktien aus den USA berücksichtigt. Alle Zahlen in der Tabelle sind in US Dollar
* Im Buch wird kein Wort über die Dividenden der einzelnen Komponenten der Strategie verloren. Daher wird davon ausgegangen, dass die durchschnittliche Performance des S&P 500 anhand des Performance-Index (Total Return) berechnet wurde. Die Dividenden werden also reinvestiert
* Es wird ebenfalls angenommen, dass die Spreads für beide identisch sind und das alle getätigten Transaktionen als Ganzes (kein Teilausführungen) am gleichen Tag ausgeführt werden
* Die Steuern (z.B. die Stempelsteuer) werden für die Berechnung ebenfalls gestrichen
* Für die Performance werden 22,9% für die Magic Formula sowie 12.4% für den ETF angenommen

Die untenstehende Tabelle zeigt die Wertentwicklung der ersten und der letzten drei Jahre. Im ersten Jahr werden 30 Aktien (zu 333 USD, verteilt über 10 Monate) gekauft und es entstehen Kosten von 660 USD (30 x 25 USD abzüglich 90 USD Trading Credits). Für den ETF werden über den gleichen Zeitraum Anteile zu 1000 USD erworben (Kosten: 160 USD, 10 x 25 USD abzüglich Trading Credits).

<p align=center><b>Magic Formula Strategie (30 US-Aktien)</b></p>

|           |Jahr 1 |Jahr 2  |Jahr 3  |Jahr 15 |Jahr 16 |Jahr 17 |      |
|-----------|-------|--------|--------|--------|--------|--------|------|
|Startbetrag|0.00   |9'340.00 |10'068.86|51'269.53|61'000.25|72'959.30|      |
|Kosten     |660.00 |1'410.00 |1'410.00 |2'010.00 |2'010.00 |2'010.00 |      |
|Rendite    |0.00   |2138.86 |2305.77 |11740.72|13969.06|16707.68|      |
|Endbetrag  |9'340.00|10'068.86|10'964.63|61'000.25|72'959.30|87'656.99|15.02%|

<p align=center><b>ETF S&P 500 Strategie</b></p>

|           |Jahr 1 |Jahr 2  |Jahr 3  |Jahr 15 |Jahr 16 |Jahr 17 |      |
|-----------|-------|--------|--------|--------|--------|--------|------|
|Startbetrag|0.00   |9'840.00 |11'053.27|44'610.80|50'111.31|56'290.03|      |
|Kosten     |160.00 |6.89    |7.74    |31.23   |35.08   |39.40   |      |
|Rendite    |0.00   |1'220.16 |1'370.61 |5'531.74 |6'213.80 |6'979.96 |      |
|Endbetrag  |9'840.00|11'053.27|12'416.14|50'111.31|56'290.03|63'230.59|12.33%|

Fazit: Nach 17 Jahren hat die Magic Formula Strategie von ihrem grossen Vorsprung schon sehr viel verloren. Nur noch gerade 2.7% Mehrrendite sind übrig geblieben. Was in dieser Tabelle jedoch nicht eingerechnet ist, ist der Zeitaufwand. Die einzelnen Ver- und Zukäufe müssen jährlich manuell eingestellt (Falls Limit als Ordertyp verwendet wird) und überprüft werden.

## Umsetzung

Für die Umsetzung der Magic Formula Strategie werden wieder die Kennzahlen der SimFin-Datenbank ({% post_link data/gatherdata/gatherdata 'siehe Beitrag' %}) verwendet. Diese beinhaltet fast alle Zahlen, welche für die Berechnung benötigt werden.

### Zahlenbeispiel

Anhand der Zahlen der Firma IBM (Disclaimer: Der Autor ist nicht in direktem Besitz von Wertpapieren dieses Unternehmens) sollen nun die beiden benötigten Renditen berechnet werden, damit die lesende Person ein Gefühl für die Zahlen bekommt. Das Resultat kann gegebenenfalls für die spätere Validierung des erstellten Python-Skriptes dienen.

Leider können gewisse Kennzahlen nicht direkt von der SimFin-Website abgelesen werden. Die Zahlen werden aus einem Export, welcher in einem {% post_link data/simfin_transformation/simfin_transformation 'älteren Beitrag' %} erstellt wurde, bezogen. Das EBIT des Geschäftsjahres 2018 betrug 12'191 Mio. USD, der Firmenwert (Enterprise Value) 133'032 Mio. USD. Daraus resultiert eine Gewinnrendite von 9,164%. Folgende Zahlen werden aus der Bilanz entnommen (alles in Mio. USD):
* Total Assets (Bilanzsumme): 123'381
* Aktive
  * Cash (Liquide Mittel): 11'379
  * Current Assets (Kurzfristiges Umlaufvermögen): 49'145
* Passive
  * Current Liabilities (Kurzfristige Verbindlichkeiten): 38'227
  * Intangibles (Immaterielle Vermögensgegenstände): 3'087
  * Goodwill (Firmenwert): 36'265

Daraus resultieren folgende Zahlen

$$
Net\ Working\ Capital = 49'145 - 11'379 - 38'227 = -461
$$

$$
Net\ Fixed\ Assets = 123'381 - 49'145 - 3'087 - 36'265 = 34'884
$$

$$
Return\ on\ Capital = {12'191 \over -461 + 34'884} = 35.415\%
$$


### Python-Skript

Das nachfolgende Python-Skript untersucht Firmen innerhalb des SimFin-Datensatzes und erstellt Grafiken, welche die 20 besten Aktien anhand der Magic Formula enthalten. Kommentare innerhalb des Programmcodes sollen helfen, die einzelnen Schritte besser nachvollziehen und verstehen zu können. Leider sind, in der aktuellen Version des Datensatzes, die beiden Werte "Immaterielle Vermögensgegenstände" und "Firmenwert" nicht mehr in der kostenlosen Variante enthalten. Daher kann die Kapitalrendite nicht mehr korrekt berechnet werden.

{% include_code Lösungsdatei lang:python finance/magic_formula/magic_formula.py %}

### Resultate

Dieser Abschnitt stellt die Resultate des oben eingebundenen Skriptes vor. Nachdem die Firmen anhand von Marktkapitalisierung und Branchen gefiltert wurden, blieben 1'373 Unternehmungen übrig. Die letzten 4 Punkte zeigen die durchschnittlichen Werte (Median und arithmetisches Mittel) der Gewinnrendite (EY) und Kapitalrendite (ROC):

* Total Geschäftsabschlüsse: 13'861
* Total aktuelle Geschäftsabschlüsse: 1'761
* Total Geschäftsabschlüsse nach Filterung von Marktkapitalisierung und Branche: 1'271
* Total vollständige Geschäftsabschlüsse (alle Kennzahlen für die Magic Formula vorhanden): 1'269
* Median EY: 3.4467%
* Arithmetisches Mittel EY: -2.1525%
* Median ROC: 11.9094%
* Arithmetisches Mittel ROC: 28.8957%

Die Verteilung der einzelnen Werte befinden sich auf nachfolgender Grafik (Ausreisser wurden vorher entfernt):
![Verteilung der Gewinn- sowie Kaitalrendite aller untersuchten Unternehmen](density_plot.png)

Die exakten Werte der Top-20-Unternehmen:
![Gewinn- sowie Kaitalrendite der Top 20 (Der Eintrag für die Firma Zynex Inc. wurde zugunsten der Übersichtlichkeit weggelassen)](ey_roc.png)

Die einzelnen Ranglistenplätze der Firmen werden in der untenstehenden Illustration veranschaulicht:
![Rangierungen anhand der Magic Formula](ey_roc_rank.png)

Die Branchen-Verteilung der Top-20 der Magic Formula Strategie:
![Histogram zur Branchen-Verteilung der Top-20-Werte](industry_histogram.png)


[^1]: [Artikel zum Thema Net Working Capital von welt-der-bwl.de](https://welt-der-bwl.de/Net-Working-Capital)
[^2]: [Artikel (engl.) zum Thema Net Fixed Assets von stockopedia.com](https://www.stockopedia.com/ratios/net-fixed-assets-533/))
[^3]: [Artikel zur Magic Formula inklusive Rendite-Diagramm auf seekingalpha.com](https://seekingalpha.com/article/4176166-magic-formula-lost-sparkle)
[^4]: [Eines von vielen Wikifolio-Zertifikaten zur Magic Formula](https://www.wikifolio.com/de/ch/w/wf000mafog)
[^5]: [Tracking-Differenz des iShares S&P 500](https://www.trackingdifferences.com/ETF/ISIN/IE00B5BMR087)
