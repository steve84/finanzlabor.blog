---
title: Fundamentalkennzahlen für Aktien beschaffen
p: data/gatherdata/gatherdata.md
date: 2019-09-01 10:33:25
tags:
- Theorie
- Data Collection
categories: Data Mining
toc: true
thumbnail: /gallery/thumbnails/data/gatherdata/thumbnail.jpg
---

In unserer Zeit werden Daten immer wichtiger. Jede Person hinterlässt auf der Welt digitale Spuren. Werden diese Informationen miteinander kombiniert, kann ein Profil dieses Individuums erstellt werden. Nun kann dieser Person spezifischere Werbung eingeblendet werden. Daten werden von vielen Experten als die Währung des 21. Jahrhunderts angesehen.

Machen wir nun einen Sprung in die Finanzwelt. Wie finde ich aus dem Dschungel von börsennotierten Unternehmen diejenigen, welche einen Piotroski F-Score von 8 oder mehr haben? Oder ein KGV von unter 12 mit einer EBIT-Marge von 20%?
Um diese Papiere zu finden, braucht es aktuelle, vollständige sowie korrekte Fundamentalkennzahlen möglichst vieler Unternehmen. Dieser Beitrag beschäftigt sich mit verschiedenen Methoden (inklusive Beispielen) zur Beschaffung von genau diesen Informationen.

<!-- more -->

*Disclaimer:* Der Autor hält Logitech Namenaktien in seinem Privatbesitz. Dieser Beitrag verwendet diese in mehreren, fiktiven Beispielen.

## Methoden

Es existieren diverse Methoden um Daten von externen Dienstleistern zu beschaffen. Einige werden im Anschluss vorgestellt und - so einfach wie möglich – erklärt. Es gibt mit Sicherheit noch weitere Ansätze um an die benötigten Informationen zu gelangen, doch der Autor beschränkt sich auf diejenigen, welche er bereits erfolgreich verwendet hat.

### Crawling

Mit Hilfe eines Computerprogramms werden Daten von einer Website extrahiert und auf einem Datenträger abgelegt. Die meisten Anbieter von Finanzdaten (z.B. [Morningstar](https://morningstar.com)) haben sich dagegen abgesichert und limitieren die Anzahl Aufrufe ihrer Online-Portale, welche von der gleichen Quelle stammen. Ein sogenannter Crawler für die Daten von [onvista](https://onvista.de) könnte so aussehen:

1. Der [Aktien-Finder von onvista.de](https://www.onvista.de/aktien/finder/) verwendet eine (nicht dokumentierte) REST-API (siehe [API](#API)) um alle Aktien, welche den eingegebenen Kriterien entsprechen, in einer Resultat-Liste anzuzeigen
2. In der Antwort dieses API-Aufrufs (im [JSON](https://www.json.org/json-de.html)-Format) finden wir alle Aktien unter der Eigenschaft *stocks*, die Anzahl Treffer unter *totalHits*. Die wichtigste Information verbirgt sich jedoch unter *url*
3. Diese Information verwenden wir nun, um die nächste Unterseite aufzurufen. Nehmen wir an, das erste Resultat unserer Suche lautet */aktien/AXA-Aktie-FR0000120628*. Nun erweitern wir dieses zu */aktien/fundamental/AXA-Aktie-FR0000120628* und wir landen auf der Seite mit den [Fundamentaldaten zur AXA](https://www.onvista.de/aktien/fundamental/AXA-Aktie-FR0000120628)
4. Nun extrahiert der Crawler alle benötigten Informationen und speichert diese in einem vordefinierten Format ab
5. Wiederholung der Schritte 3-4 bis alle Resultate aus Schritt 2 abgearbeitet wurden

Die heutigen Browser (Chrome und Firefox) bieten Entwicklertools (F12-Taste), um den Netzwerkverkehr zu analysieren (Tab Netzwerk bei Chrome, Netzwerkanalyse bei Firefox). Mit dem Filter XHR (XMLHttpRequest) werden nur Datenübertragungen angezeigt.

Die nicht dokumentierten REST-APIs sind meist durch ein Token (eine verschlüsselte Zeichenfolge) geschützt, welche durch den Empfänger validiert wird. Wird kein oder ein falsches Token mitgeschickt, werden keine Daten geliefert.

Dieses Verfahren ist jedoch nicht sehr performant, da auch unwichtige Informationen von den jeweiligen Websiten geladen wird. Es kann mehrere Stunden dauern, um alle verfügbaren Wertpapier abzuarbeiten.

###  API

Die Abkürzung steht für **A**pplication **P**rogramming **I**nterface und ist eine Schnittstelle zur Programmierung von Anwendungen. Die Schnittstelle definiert, wie die Anwendung zu den gewünschten Informationen kommt und wie die Antwort im Detail aussieht. Eine Dokumentation beschreibt alle verfügbaren Einstiegspunkte und die dazugehörigen Argumente. Eine sehr bekannte Form einer API ist die [REST-API](https://www.dev-insider.de/was-ist-rest-api-a-667357/) (die genauen Details dazu möchte ich für diesen Beitrag auslassen). Anschliessend zwei einfache Beispiele einer solchen API (die Links rechts oben existieren nicht und die Zahlen der Unternehmen sind fiktiv):

{% codeblock Alle Firmen lang:json http://finanzlabor.blog/firmen http://finanzlabor.blog/firmen %}
[{"id": 1, "name": "Logitech"}, {"id": 2, "name": "Volkswagen"]
{% endcodeblock %}

{% codeblock Eigenkapital und Bilanzsumme der Firma mit der ID 1 ab dem Jahr 2018 lang:json http://finanzlabor.blog/firmen/1/fundamentaldaten?include=eigenkapital,bilanzsumme&from=2018 http://finanzlabor.blog/firmen/1/fundamentaldaten?include=eigenkapital,bilanzsumme&from=2018 %}
[{"id": 12, "name": "Bilanzsumme", "value": 240'000, "currency": "CHF", "year": 2018}, {"id": 19, "name": "Eigenkapital", "value": "24'000", "currency": "CHF", "year": 2018}]
{% endcodeblock %}

Somit verfügen wir über die beiden Kennzahlen und können nun die Eigenkapitalquote berechnen. Die Antwort einer REST-API wird im JSON-Format gesendet.

Es existieren einige APIs zu Fundamentaldaten von Unternehmen, welche an der Börse notiert sind. In den Beispielen gehe ich auf einige meiner Favoriten ein.

### Bulk

Einige Dienstleister bieten die Möglichkeit, alle verfügbaren Daten in einem Rutsch zu beziehen. Meist geschieht dies in einer oder mehreren Dateien im [CSV](https://de.wikipedia.org/wiki/CSV_(Dateiformat)-Format. Diese könnten wie folgt aussehen (Zahlen sowie ISIN der Unternehmen sind fiktiv):

{% codeblock CSV-Beispiel %}
name,isin,jahr,bilanzsumme,eigenkapital
Logitech,CH123123123,2018,240'000,24'000
Volkswagen,DE456456456,2018,550'000,123'000
{% endcodeblock %}

Diese Informationen sind so lange auf dem aktuellsten Stand, bis ein Unternehmen neue Daten veröffentlicht. Mit einer API würde die Möglichkeit bestehen (sofern der Anbieter diese Funktionalität zur Verfügung stellt), die neusten Kennzahlen jederzeit zu beziehen.

Der Anbieter definiert das Format der gelieferten Daten. Dieses entspricht nicht immer den Anforderungen des Anwenders und muss für die weitere Verarbeitung umgeformt werden.

Ein Vorteil dieser Methode ist, dass die Daten nur periodisch (einmal pro Monat) heruntergeladen werden müssen und daher die Zugriffe aufs Internet reduziert werden. Meistens werden die Daten für Batches (Ein Computerprogramm, welches regelmässig gewisse Operationen durchführt und protokolliert) verwendet, welche die Änderungen zu den bestehenden Daten einpflegen. Die Server auf denen die Batches ausgeführt werden, haben nicht die Möglichkeit auf Daten aus dem Internet zuzugreifen (aus Sicherheitsgründen). Die Datei wird am Anfang der Durchführung von der lokalen Festplatte oder eines internen Servers abgeholt.


## Beispiele

Wenden wir nun das Gelernte in der Praxis an. Anbei einige Beispiele zur Beschaffung von Finanzdaten.

### Google Finance

Innerhalb von Goolge Docs gibt es die Möglichkeit, auf Finanzdaten von Google zuzugreifen. Mit Hilfe der Funktion GOOGLEFINANCE können diverse Kennzahlen ausgelesen werden. Auf der Hilfsseite werden alle verfügbaren Attribute (z.B. pe für das KGV) beschrieben. Der folgende Aufruf zeigt das aktuelle KGV der Logitech AG:

{% codeblock KGV von Logitech lang:excel %}
=GOOGLEFINANCE("LOGN", "pe")
{% endcodeblock %}

Und der aktuelle Kurs (inkl. Währung) der gleichen Firma:

{% codeblock Aktueller Kurs von Logitech lang:excel %}
=CONCAT(CONCAT(GOOGLEFINANCE("LOGN", "price"), " "), GOOGLEFINANCE("LOGN", "currency"))
{% endcodeblock %}

Leider sind nur wenige Fundamentalkennzahlen verfügbar. Google Finance ist ideal für die Beschaffung von historischen Kursdaten.

### Simfin

Das Ziel von [Simfin](https://simfin.com/) ist, Fundamentaldaten für Privatinvestoren frei verfügbar zu machen. Mit Hilfe von automatisierter Datensammlung und Machine Learning Algorithmen werden die Informationen aufbereitet. Danach werden diese mit Hilfe der Community validiert/korrigiert. Im Moment (Stand Ende August 2019) werden 2'540 Firmen (mehrheitlich US-Aktien) abgedeckt und ca. 277'000 Geschäftsabschlüsse wurden verarbeitet. Die Daten können mit Hilfe zweier uns nun bekannten Methoden abgerufen werden:
* *API Zugriff*: Als normaler Benutzer können 2'000 Anfragen pro Tag gemacht werden. Für das zehnfache an Aufrufen ist eine Premium-Abo notwendig (SimFin+ regular, 9.99 Euro pro Monat). Für unlimitierten Zugriff werden 29.99 Euro pro Monat fällig
* *Bulk Download*: Diese Möglichkeit steht allen registrierten Benutzern offen. Die Daten werden als CSV-Datei angeboten und es kann zwischen 4 verschiedenen Datensätzen (Kurs -und Fundamentaldaten, detaillierte Kurs- und Fundamentaldaten, nur Fundamentaldaten, nur detaillierte Fundamentaldaten) gewählt werden. Es kann ebenfalls der Intervall der Aufzeichnungen bestimmt werden (Jahres -oder Quartalszahlen)

### Quandl

Ähnlich wie Simfin bietet [Quandl](https://www.quandl.com) Datensätze im Bereich Finanzen an. Es werden jedoch andere Asset-Klassen wie zum Beispiel Immobilien oder Rohstoffe abgedeckt. Die Website stellt die Daten nicht selber zur Verfügung sondern vermittelt zwischen Datenbezüger und Datenanbieter. Die meisten Angebote sind kostenpflichtig, es existieren jedoch auch einige kostenlose. Unter *Explore* kann man nach verschiedenen Datensätzen filtern. Hier einige meiner Favoriten:
* *Aktienpreise an den verschiedenen Börsen*: Frankfurt (Name des Datensatzes: FSE, kostenlos), Euronext (EURONEXT, kostenlos)
* *Fundamentaldaten*: Robur Global Select Stock Fundamentals (RB1, Premium), Core US Fundamentals (SF1, Premium)

Ich habe vor einiger Zeit den Robur Datensatz für einen Monat (100 USD) gekauft. Danach habe ich das Angebot wieder gekündigt, da ich eine gewisse Zeit mit leicht veralteten Daten arbeiten kann.

### Wallmine
Ein weiterer guter Datenlieferant. Leider gibt es hier keine Möglichkeit alle Daten zu beziehen. Unter *Tools* - *Stock screener* existieren diverse Filteroptionen, danach können bis zu 1'000 Einträge als CSV heruntergeladen werden. Beim Export gibt es einen kleinen Trick, damit die Datei alle verfügbaren Spalten enthält:

1. Standardmässig werden nur die Kennzahlen des aktiven Tabs (z.B. Financial, Technical, Momentum, usw.) exportiert. Mit dem Wechsel auf das Tab *Custom* besteht die Möglichkeit die Felder des Exports zu bestimmen
2. Nach dem Öffnen der Entwicklertools (F12-Taste) und dem Selektieren (Ctrl + Shift + C) des Dropdrown-Feldes mit dem Namen *Choose a column* wird das HTML-Element *select* sichtbar (innerhalb des Entwicklertools)
3. Nach einem Rechtsklick auf dieses Element erscheint ein Kontextmenü und mit Hilfe von *Kopieren* - *Äussers HTML* (Firefox) oder *Copy* - *Copy outerHTML* (Chrome)
4.  Der Inhalt wird nun in einen Texteditor kopiert (z.B. Notepad++) und die erste und letzte Zeile (*select*-Tags) entfernt. Nun sind nur noch *option*-Elemente vorhanden (diese Repräsentieren die Auswahlmöglichkeiten der Dropdown-Liste)
5. Die erste Zeile wird ebenfalls gelöscht (mit dem Inhalt *Choose a column*), da sie als Platzhalter dient
6. Durch das Ersetzen von '<option value="' durch '' wird der vordere Teil entfernt (siehe erstes Bild in der unteren Bildstrecke)
7. Nun wird mit Hilfe eines regulären Ausdruckes der hintere Teil entfernt (">(.\*)</option> ersetzen durch ''). Wichtig: Beim Suchen/Ersetzen-Dialog in Notepad++ muss die Option *Reguläre Ausdrücke* unter Suchoptionen aktiviert sein
8. Zum Schluss ersetzten wir '\r\n' durch ein Komma (auch hier muss *Reguläre Ausdrücke* aktiv sein)
9. Nun werden die Entwicklertools geschlossen und es wird die erste Option in der Dropdown-Liste ausgewählt (im Moment *Exchange*, Stand September 2019)
10. Nun wird der Link *Export to CSV* kopiert (Rechte Maustaste - *Adresse des Links kopieren* und ebenfalls in einen Texteditor kopiert
11. Das erste Element *Exchange* hat den Wert *e* (siehe erste Zeichen vor dem ersten Komma nach Schritt 8) und dieses wird im Link aus Schritt 10 wieder verwendet (der Link sieht je nach verwendeten Filteroptionen anders aus):
https://wallmine.com/screener/csv?d=d&f=e&o=m&page=282&r=cu
12. Nach dem Ersetzten des Parameters f durch das Resultat von Schritt 8 ist der Link nun komplett und kann in der Adresszeile des Browsers kopiert werden
13. Die heruntergeladene CSV-Datei sollte nun alle verfügbaren Spalten enthalten

<div class="justified-gallery">
<!-- Need an empty line here for the following markdown to be rendered -->
![Schritt 6](notepadpp_schritt_6.png)
![Schritt 7](notepadpp_schritt_7.png)
![Schritt 8](notepadpp_schritt_8.png)
</div>

## Ausblick

Für die weiteren Verarbeitungsschritte sind wir auf eine solide Datenbasis angewiesen. In einem der nächsten Beiträge werden ich zeigen, wie die Daten von Simfin bezogen und in ein eigenes Format
