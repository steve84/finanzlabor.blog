---
title: Kostenlose Kennzahlen für Aktien beschaffen
p: data/gatherdata/gatherdata.md
date: 2019-10-05 00:00:01
updated: 2024-01-07 00:00:01
tags:
- Theorie
- Data Collection
categories: Data Mining
toc: true
thumbnail: /gallery/thumbnails/data/gatherdata/thumbnail_square.jpg
cover: /gallery/thumbnails/data/gatherdata/thumbnail.jpg
---

In unserer Zeit werden Daten immer wichtiger. Jede Person hinterlässt auf der Welt digitale Spuren. Werden diese Informationen miteinander kombiniert, kann ein Profil dieses Individuums erstellt werden. Nun kann dieser Person spezifische Werbung eingeblendet werden. Daten werden von vielen Experten als die Währung des 21. Jahrhunderts angesehen.

Machen wir nun einen Sprung in die Finanzwelt. Wie finde ich aus dem Dschungel von börsennotierten Unternehmen diejenigen, welche einen Piotroski F-Score von 8 oder mehr haben? Oder ein KGV von unter 12 mit einer EBIT-Marge von über 20%?
Um diese Papiere zu finden, braucht es aktuelle, vollständige sowie korrekte Fundamentalkennzahlen möglichst vieler Unternehmen. Dieser Beitrag beschäftigt sich mit verschiedenen Methoden (inklusive Beispielen) zur Beschaffung von genau diesen Informationen.

<!-- more -->

*Aktualisiert am 07.01.2024*

## Methoden

Es existieren diverse Methoden um Daten von externen Dienstleistern zu beschaffen. Einige werden im Anschluss vorgestellt und --- so einfach wie möglich --- erklärt. Es gibt mit Sicherheit noch weitere Ansätze um an die benötigten Informationen zu gelangen, doch der Autor beschränkt sich auf diejenigen, welche er bereits erfolgreich verwendet/angewendet hat.

### Crawling

Mit Hilfe eines Computerprogramms werden Daten von einer Website extrahiert und auf einem Datenträger abgelegt. Die meisten Anbieter von Finanzdaten (z.B. [Morningstar](https://morningstar.com)) haben sich dagegen abgesichert und limitieren die Anzahl Aufrufe ihrer Online-Portale, welche von der gleichen Quelle stammen. Ein sogenannter Crawler für die Daten von [onvista](https://onvista.de) könnte so aussehen:

1. Der [Aktien-Finder von onvista.de](https://www.onvista.de/aktien/finder/) verwendet eine (nicht dokumentierte) REST-API[^1] um alle Aktien, welche den eingegebenen Kriterien entsprechen, in einer Resultat-Liste anzuzeigen
2. In der Antwort dieses API-Aufrufs (im JSON-Format[^2]) finden wir alle Aktien unter der Eigenschaft *data/list*, die Anzahl Treffer unter *data/total*. Die wichtigste Information verbirgt sich jedoch unter *data/list[0]/urls/WEBSITE*
3. Diese Information verwenden wir nun, um die nächste Unterseite aufzurufen. Nehmen wir an, das erste Resultat unserer Suche lautet */aktien/AXA-Aktie-FR0000120628*. Nun erweitern wir dieses zu */aktien**/kennzahlen**/AXA-Aktie-FR0000120628* und wir landen auf der Seite mit den [Fundamentaldaten zur AXA](https://www.onvista.de/aktien/kennzahlen/AXA-Aktie-FR0000120628)
4. Nun extrahiert der Crawler alle benötigten Informationen und speichert diese in einem vordefinierten Format ab
5. Die Schritte 3-4 werden wiederholt, bis alle Resultate aus Schritt 2 abgearbeitet sind

Die heutigen Browser (Chrome und Firefox) bieten Entwicklertools (F12-Taste), um den Netzwerkverkehr zu analysieren (Tab Netzwerk bei Chrome, Netzwerkanalyse bei Firefox). Mit dem Filter XHR (XMLHttpRequest[^3]) werden nur Datenübertragungen angezeigt.

Die nicht dokumentierten REST-APIs sind meist durch ein Token (eine verschlüsselte Zeichenfolge) geschützt, welches durch den Empfänger validiert wird. Wird kein oder ein falsches Token mitgeschickt, werden keine Daten geliefert.

Dieses Verfahren ist jedoch nicht sehr performant, da auch unwichtige Informationen von den jeweiligen Webseiten geladen werden. Es kann mehrere Stunden dauern, um alle verfügbaren Wertpapier abzuarbeiten.

###  API

Die Abkürzung steht für **A**pplication **P**rogramming **I**nterface und ist eine Schnittstelle zur Programmierung von Anwendungen. Die Schnittstelle definiert, wie die Anwendung zu den gewünschten Informationen kommt und wie die Antwort im Detail aussieht. Eine Dokumentation beschreibt alle verfügbaren Einstiegspunkte und die dazugehörigen Argumente. Eine sehr bekannte Form einer API ist die REST-API. Anschliessend zwei einfache Beispiele einer solchen API (die Links rechts oben existieren nicht und die Zahlen der Unternehmen sind fiktiv):

{% codeblock Alle Firmen lang:json http://finanzlabor.blog/firmen http://finanzlabor.blog/firmen %}
[{"id": 1, "name": "Logitech"}, {"id": 2, "name": "Volkswagen"}]
{% endcodeblock %}

{% codeblock Eigenkapital und Bilanzsumme der Firma mit der ID 1 ab dem Jahr 2018 lang:json http://finanzlabor.blog/firmen/1/fundamentaldaten?include=eigenkapital,bilanzsumme&from=2018 http://finanzlabor.blog/firmen/1/fundamentaldaten?include=eigenkapital,bilanzsumme&from=2018 %}
[{"id": 12, "name": "Bilanzsumme", "value": 240'000, "currency": "CHF", "year": 2018}, {"id": 19, "name": "Eigenkapital", "value": "24'000", "currency": "CHF", "year": 2018}]
{% endcodeblock %}

Somit verfügen wir über die beiden Kennzahlen und können nun zum Beispiel die Eigenkapitalquote berechnen (in diesem Beispiel 10%). Die Antwort einer REST-API wird im JSON-Format gesendet.

Es existieren einige APIs zu Fundamentaldaten von Unternehmen, welche an der Börse notiert sind. In den Beispielen gehe ich auf einige meiner Favoriten ein.

### Bulk

Einige Dienstleister bieten die Möglichkeit, alle verfügbaren Daten in einem Rutsch zu beziehen. Meist geschieht dies in einer oder mehreren Dateien im CSV[^4]-Format. Diese könnten wie folgt aussehen (Zahlen sowie ISIN der Unternehmen sind fiktiv):

{% codeblock CSV-Beispiel %}
name,isin,jahr,bilanzsumme,eigenkapital
Logitech,CH123123123,2018,240'000,24'000
Volkswagen,DE456456456,2018,550'000,123'000
{% endcodeblock %}

Diese Informationen sind so lange auf dem aktuellsten Stand, bis ein einziges Unternehmen neue Daten veröffentlicht. Mit einer API würde die Möglichkeit bestehen (sofern der Anbieter diese Funktionalität zur Verfügung stellt), die neusten Kennzahlen für genau dieses jederzeit zu beziehen.

Der Anbieter definiert das Format der gelieferten Daten. Dieses entspricht nicht immer den Anforderungen des Anwenders und muss für die weitere Verarbeitung umgeformt werden.

Ein Vorteil dieser Methode ist, dass die Daten nur periodisch (z.B. einmal pro Monat) heruntergeladen werden müssen und daher die Zugriffe aufs Internet reduziert werden. Meistens werden die Daten für Batches (Ein Computerprogramm, welches regelmässig gewisse Operationen durchführt und protokolliert) verwendet, welche die Änderungen zu den bestehenden Daten einpflegen. Die Server auf denen die Batches ausgeführt werden, haben nicht die Möglichkeit auf Daten aus dem Internet zuzugreifen (aus Sicherheitsgründen). Die Datei wird am Anfang der Durchführung von der lokalen Festplatte oder eines internen Servers abgeholt.


## Beispiele

Wenden wir nun das Gelernte in der Praxis an. Anbei einige Beispiele zur Beschaffung von Finanzdaten.

### Google Finance

Innerhalb von Goolge Docs gibt es die Möglichkeit, auf Finanzdaten von Google zuzugreifen. Mit Hilfe der Funktion GOOGLEFINANCE können diverse Kennzahlen ausgelesen werden. Auf der Hilfsseite[^5] werden alle verfügbaren Attribute (z.B. pe für das KGV) beschrieben. Der folgende Aufruf zeigt das aktuelle KGV der Logitech AG:

{% codeblock KGV von Logitech lang:excel %}
=GOOGLEFINANCE("LOGN", "pe")
{% endcodeblock %}

Und der aktuelle Kurs (inkl. Währung) der gleichen Firma:

{% codeblock Aktueller Kurs von Logitech lang:excel %}
=CONCAT(CONCAT(GOOGLEFINANCE("LOGN", "price"), " "), GOOGLEFINANCE("LOGN", "currency"))
{% endcodeblock %}

Leider sind nur wenige Fundamentalkennzahlen verfügbar. Google Finance ist ideal für die Beschaffung von historischen Kursdaten.

### Yahoo Finance
Auch das Portal Yahoo Finance stellt Daten zu einzelnen Finanzprodukten zur Verfügung. Diese können entweder über den Browser oder über Software-Bibliotheken abgerufen werden. Ein Beispiel für Letzteres ist das Python-Paket yfinance. Der nachfolgende Programm-Code zeigt bezieht ebenfalls das KGV der Firma Logitech:

{% codeblock KGV von Logitech lang:python %}
import yfinance as yf

logi = yf.Ticket('LOGI')
print(logi.info['forwardPE'])
# 24.1671
{% endcodeblock %}

In einem {% post_link programming/chart_plotting/chart_plotting 'anderen Blog-Beitrag' %} wird aufgezeigt, wie mit Hilfe einer weiteren Bibliothek, Kursdiagramme visualisiert werden können.

### SimFin

Das Ziel von [SimFin](https://simfin.com/) ist, Fundamentaldaten für Privatinvestoren frei verfügbar zu machen. Mit Hilfe von automatisierter Datensammlung und Machine Learning Algorithmen werden die Informationen aufbereitet. Danach werden diese mit Hilfe der Community validiert/korrigiert. Im Moment (Stand Anfang Januar 2024) werden zirka 5'000 Firmen (mehrheitlich US-Aktien) abgedeckt und ca. 51'000 Geschäftsabschlüsse wurden verarbeitet. Die Daten können mit Hilfe zweier uns nun bekannten Methoden abgerufen werden:
* *API Zugriff*: Als registierter Benutzer (genannt SimFin Free) können 2 Anfragen pro Sekunde gemacht werden. Damit sind Daten der letzten 7 Jahre abrufbar (mit dem günstisten Abo sind es 10 Jahre). SimFin stellt eine eigene Python-Bibliothek zur Verfügung[^6]
* *Bulk Download*: Diese Möglichkeit steht allen registrierten Benutzern (SimFin Free) offen. Die Datensätze sind jedoch um 12 Monate verzögert (die aktuellsten Daten müssen via API bezogen werden) und werden als CSV-Datei angeboten. Diese sind über mehrere Kategorien verteilt (z.B. generelle Informationen zu der Firma, Erfolgsrechnung sowie Geldflussrechnung).  Die einzelnen Firmen sind einem Aktienmarkt eines bestimmten Landes zugeordnet. Aktuell gibt es drei Märkte, welche gewählt werden können (USA, China und Deutschland). Es kann ebenfalls das Intervall der Aufzeichnungen bestimmt werden (Jahres- oder Quartalszahlen)

### Nasdaq Data Link (Quandl)

**Hinweis vom 07.01.2024**: Wurde von Quandl nach Nasdaq Data Link umbenannt. Ebenfalls sind einige der unten aufgeführten Datensätze aktuell nicht verfügbar.

Ähnlich wie SimFin bietet [Nasdaq Data Link](https://data.nasdaq.com) (ehemals Quandl) Datensätze im Bereich Finanzen an. Es werden jedoch auch andere Asset-Klassen wie zum Beispiel Immobilien oder Rohstoffe abgedeckt. Die Website stellt die Daten nicht selber zur Verfügung sondern vermittelt zwischen Datenbezüger und Datenanbieter. Die meisten Angebote sind kostenpflichtig, es existieren jedoch auch einige kostenlose. Unter *Explore* kann man nach verschiedenen Datensätzen filtern. Hier einige meiner Favoriten:
* *Aktienpreise an den verschiedenen Börsen*: Frankfurt (Name des Datensatzes: FSE, kostenlos), Euronext (EURONEXT, kostenlos)
* *Fundamentaldaten*: Robur Global Select Stock Fundamentals (RB1, Premium), Core US Fundamentals (SF1, Premium)

Ich habe vor einiger Zeit den Robur Datensatz (RB1) für einen Monat (100 USD) gekauft. Danach habe ich das Angebot wieder gekündigt, da ich eine gewisse Zeit mit leicht veralteten Daten arbeiten konnte.

### Alpha Vantage
Alpha Vantage ist ein weiterer guter Datenlieferant, welcher eine eigene Schnittstelle anbietet. Diese stellt Kurs- und Fundamentaldaten sowie technische Indikatoren bereit. Für den kostenlosen Zugang ist eine Registierung nötig, danach können 25 Abfragen pro Tag gesendet werden. Nachfolgendes Beispiel zeigt die Ermittlung des KGVs von IBM auf (der Demo-Zugang ist auf die Firma IBM beschränkt):

{% codeblock KVG von IBM lang:python %}
import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=IBM&apikey=demo'
r = requests.get(url)
data = r.json()

print(data['PERatio'])
# 20.54
{% endcodeblock %}

Das gewünschte Symbol kann mit Hilfe der *Ticker Search*[^7] Funktion ermittelt werden. In der API-Dokumentation[^8] sind noch weitere Beispiele zu finden.

## Ausblick

Für die weiteren Verarbeitungsschritte sind wir auf eine solide Datenbasis angewiesen. In einem {% post_link data/simfin_transformation/simfin_transformation 'nächsten Beitrag'%} werde ich zeigen, wie die Daten von SimFin bezogen und in ein eigenes Format konvertiert werden.

[^1]: [Dev Insider: Was ist REST API?](https://www.dev-insider.de/was-ist-rest-api-a-667357)
[^2]: [Einführung in JSON](https://www.json.org/json-de.html)
[^3]: [Wiki-Seite von selfhtml zum Thema XMLHttpRequest](https://wiki.selfhtml.org/wiki/JavaScript/XMLHttpRequest)
[^4]: [Wikipedia-Seite zum CSV-Dateiformat](https://de.wikipedia.org/wiki/CSV_(Dateiformat))
[^5]: [Hilfsseite der Google Docs Funktion GOOGLEFINANCE](https://support.google.com/docs/answer/3093281?hl=de)
[^6]: [GitHub-Projekt der SimFin-Bibliothek (Python)](https://github.com/SimFin/simfin)
[^7]: [Alpha Vantage Symbolsuche](https://www.alphavantage.co/documentation/#symbolsearch)
[^8]: [Alpha Vantage API-Dokumentation](https://www.alphavantage.co/documentation/)