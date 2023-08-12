---
title: Fear & Greed Index
p: finance/fear_and_greed_index/fear_and_greed_index.md
date: 2020-11-30 18:00:00
tags:
- Theorie
- Aktien
- Data Visualization
categories: Finanzen
toc: true
thumbnail: /gallery/thumbnails/finance/fear_greed_index/thumbnail_square.jpg
cover: /gallery/thumbnails/finance/fear_greed_index/thumbnail.jpg
---

Von einem der bekanntesten und erfolgreichsten Investoren der Neuzeit stammt folgendes Zitat:

{% blockquote Warren Buffet %}
"Sei ängstlich, wenn andere gierig sind. Sei gierig, wenn andere ängstlich sind"
{% endblockquote %}

Doch wie erkennt ein Investor eine solche Marktlage (oder erste Anzeichen für eine Trendwende)? Eine mögliche Anlaufstelle ist der *Fear & Greed* (Angst & Gier) Index von CNN[^1]. Die Index-Konstruktion, Interpretation des Indexstandes sowie eine mögliche Trading-Strategie werden in den nachfolgenden Zeilen behandelt.

<!-- more -->

## Indikatoren

Der Index misst mit Hilfe von sieben Parametern den aktuellen Gemütszustand der Anleger. Diese sind:

* **Aktienkurs Momentum:** Der Kurs des S&P 500 wird mit dem gleitenden Durchschnitt (125 Tage) desselben Index verglichen.
* **Aktienkurs Stärke:** Die Anzahl der Aktien, welche über ihrem 52-Wochen-Höchststand liegen, wird mit der Anzahl derjenigen Wertpapiere verglichen, welche unter ihrem 52-Wochen-Tiefststand gehandelt werden.
* **Aktienkurs Handelsvolumen:** Bei diesem Indikator wird der *McClellan Volume Summation Index*[^2][^3] für die Ermittlung der Marktstimmung verwendet. Dieser kommt häufig in der technischen Analyse zur Anwendung und basiert auf dem Handelsvolumen von Aktien. Vereinfacht gesagt, stellt der Index das kumulierte Volumen von steigenden Aktien ins Verhältnis des Volumens von fallenden Aktien. Ein steigendes Volumen auf fallenden Papieren zeigt eine negative Stimmung unter den Anlegern an (Abverkauf).
* **Put/Call-Verhältnis:** Bei diesem Kriterium wird das Handelsvolumen von Put- beziehungsweise Call-Optionen, auf Wertpapiere aus dem S&P 500, in Relation gestellt. Wurde in den letzten 5 Handelstagen mehrheitlich auf fallende Kurse spekuliert (Put), wird dies als Zeichen eines Bärenmarktes interpretiert.
* **Nachfrage von Hochrisiko-Anleihen:** Die Rendite von sicheren Anleihen wird mit derjenigen von Hochrisiko-Anleihen verglichen. Liegen diese nahe zusammen (das höhere Risiko wird nur mit sehr geringer Mehrrendite belohnt), liegt eine geringe Nachfrage vor und in den Portfolios der Investoren wird mehrheitlich auf Aktien gesetzt. Schwächelt der Aktienmarkt, schichten die Anleger das Geld in Anleihen mit höherem Risiko um (Renditemaximierung).
* **Markt-Volatilität:** Die Schwankungsbreite des S&P 500 wird mit Hilfe des *Cboe Volatility Index*[^4] gemessen. Liegt dieser unterhalb des gleitenden Durchschnittes der letzten 50 Tage, zeigt dies eine eher positive Stimmung an.
* **Renditeunterschied zwischen Aktien und Staatsanleihen:** Die Amerikaner bezeichnen diesen Indikator auch als *Safe Haven Demand*, welcher die Nachfrage nach sicheren Investitionsvehikeln (in diesem Fall langjährige Staatsanleihen) beobachtet. Lässt die Nachfrage nach Aktien nach (da viele Investoren den sicheren Hafen ansteuern und das Depot in Anleihen umschichten), verschiebt sich die Nachfragekurve. Die Preise sinken und die Renditen der beiden Anlageklassen nähern sich an (Gesetz von Angebot und Nachfrage). Je kleiner diese Differenz ist, desto tiefer fällt die Punktzahl dieses Bewertungskriteriums aus.

Die Werte der einzelnen Kriterien werden mit den Daten aus der Vergangenheit (meistens innerhalb einer Zeitspanne von 2 Jahren) verglichen und entsprechend bewertet. Je weiter sich ein Wert vom Mittelwert entfernt, desto stärker schlägt dieser in eines der Extreme aus.

Der Wertebereich der einzelnen Kriterien sowie des gesamten Index liegt zwischen 0 und 100. Dieser wird in 5 gleich grosse Abschnitte unterteilt (20er-Schritte): *Extreme Angst*, *Angst*, *Neutral*, *Gier* oder *Extreme Gier*. Der Wert des Index, wird mit Hilfe des arithmetischen Mittels der einzelnen Indikatoren, bestimmt.

## Interpretation

![Aktuelle Marktlage vom 27. November 2020 sowie der Vergangenheit (Quelle: cnn.com)](fear_greed_tacho.png)

Die Website von CNN visualisiert die einzelnen Faktoren sowie den Index in Liniendiagrammen, welche eine Zeitdauer von zwei Jahren abdecken. Dabei fällt auf, dass die Bewertung zu Beginn des Jahres 2020 bei fast 100 Punkten war und sich danach auf eine rasante Talfahrt begab (auf fast 0 Punkte innerhalb weniger Wochen). Auch der kleine Einbruch an den Finanzmärkten anfangs Oktober ist im Indexverlauf gut ablesbar.

![Index-Verlauf der letzten zwei Jahre (Quelle: cnn.com)](fear_greed_chart.png)

## Anlagestrategie

Ob sich dieser Index für regelbasierte Zu- und Verkäufe eignet, müsste zuerst noch durch Backtesting (Simulation von Transaktionen anhand vorgegebener Kriterien über einen bestimmten Zeitraum in der Vergangenheit) untersucht werden. Eine mögliche antizyklische Strategie könnte wie folgt aussehen (keine Anlageempfehlung):
* Wechselt der Index von *Gier* auf *Extreme Gier* (die Linie durchstösst die 80er-Marke von unten) wird das Wertpapier abgestossen
* Wechselt der Index von *Extreme Angst* auf *Angst* (die Linie durchstösst die 20er-Marke von oben) wird das Wertpapier gekauft

Dies würde jedoch nur für Anlageinstrumente Sinn machen, welche stark USA-lastig sind, wie zum Beispiel der MSCI World (besteht zu 65% aus amerikanischen Aktien) oder einen Index auf den S&P 500 beziehungsweise NASDAQ. Grund dafür sind die einzelnen Indikatoren, auf welchen der *Fear and Greed* Index basiert. Wer sich die Mühe machen will, kann natürlich auch einen eigenen, europäischen Index kreieren.

## Fazit

Grundsätzlich kann gesagt werden, dass sich der Index als Indikator für die aktuelle Marktstimmung eignet. Auch für langfristige Entscheidungen kann er hinzu gezogen werden, die Entscheidung einer Investition sollte jedoch nicht nur aufgrund des Indexstandes gefällt werden.

[^1]: [Fear & Greed Index Seite von CNN Business](https://money.cnn.com/data/fear-and-greed/)
[^2]: [Breadth Indicator Beitrag von Investopedia](https://www.investopedia.com/terms/b/breadthindicator.asp)
[^3]: [Erklärung zu dem McClellan Summation Index auf Investopedia](https://www.investopedia.com/terms/m/mcclellansummation.asp)
[^4]: [Offizielle Website des Cboe VIX Index](https://markets.cboe.com/tradable_products/vix)
