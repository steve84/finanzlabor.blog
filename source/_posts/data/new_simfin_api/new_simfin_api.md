---
title: Neue SimFin-API - Ein Schritt in die falsche Richtung?
p: data/new_simfin_api/new_simfin_api.md
date: 2020-02-01 08:00:00
tags:
- Data Collection
- Python
- Theorie
categories: Data Mining
thumbnail: /gallery/thumbnails/data/new_simfin_api/thumbnail.jpg
---

Zu Beginn des Jahres 2020 hat [SimFin](https://simfin.com/) einige Änderungen bezüglich der Bereitstellung Ihrer Bulk Daten vorgenommen. Dieser Beitrag fasst in einem ersten Teil die Neuheiten kurz zusammen und gibt im Anschluss einige weiterführende Informationen. Dieser Wechsel hat zur Folge, dass einige Artikel auf diesem Blog nicht mehr valide sind, diese werden solange mit einem Hinweis versehen. Die davon betroffenen Abschnitte werden in den nächsten Tagen an die neuen Gegebenheiten angepasst.

<!-- more -->

Nun zu den wichtigsten Änderungen des SimFin-Angebots:

* Es ist nun nicht mehr möglich, einen kompletten Export der Finanzdaten zu beziehen
* Die einzelnen Kennzahlen wurden in Teilgebiete aufgeteilt:
  * Balance Sheet (Bilanz)
  * Income Statement (Erfolgsrechnung)
  * Cash Flow (Geldflussrechnung)
  * Share Price (Aktienkurs)
* Es gibt verschiedene Märkte (USA, Deutschland, Kanada, Italien und Singapur), die Firmen werden anhand ihres Heimatmarktes zugeteilt. Etwa 99% der Daten stammen aus dem US-Aktienmarkt
* Die Liste der Sektoren/Branchen ist einfacher zugänglich
* In der kostenlosen Variante werden nicht mehr alle Kennzahlen mitgeliefert
* Die aktuellsten Daten werden nur bezahlenden Kunden zur Verfügung gestellt. Der kostenlose Export beinhaltet keine Geschäftsabschlüsse, welche innerhalb des letzten Jahres veröffentlicht wurden (12 Monate verzögert)
* Es wird nun eine offizielle (Beta-Version) [Python-Bibliothek](https://simfin.readthedocs.io/en/latest/) angeboten
* Diverse spannende Tutorials werden zur Verfügung gestellt:
  * [Basics](https://github.com/SimFin/simfin-tutorials/blob/master/01_Basics.ipynb)
  * [Resampling](https://github.com/SimFin/simfin-tutorials/blob/master/02_Resampling.ipynb)
  * [Growth Returns](https://github.com/SimFin/simfin-tutorials/blob/master/03_Growth_Returns.ipynb)
  * [Signals](https://github.com/SimFin/simfin-tutorials/blob/master/04_Signals.ipynb)
  * [Data Hubs](https://github.com/SimFin/simfin-tutorials/blob/master/05_Data_Hubs.ipynb)
  * [Performance Tips](https://github.com/SimFin/simfin-tutorials/blob/master/06_Performance_Tips.ipynb)
  * [Stock Screener](https://github.com/SimFin/simfin-tutorials/blob/master/07_Stock_Screener.ipynb)
  * [Statistical Analysis](https://github.com/SimFin/simfin-tutorials/blob/master/08_Statistical_Analysis.ipynb)
  * [Machine Learning](https://github.com/SimFin/simfin-tutorials/blob/master/09_Machine_Learning.ipynb)
  * [Neural Networks](https://github.com/SimFin/simfin-tutorials/blob/master/10_Neural_Networks.ipynb)

# Bemerkungen

Dieser Abschnitt enthält einige kurze Ausführungen zu den oben aufgeführten Punkten.

## Marktzugehörigkeit der Firmen

Jedes einzelne Unternehmen, welches in der Datenbank von SimFin erfasst ist, wird in einen Markt eingeteilt. Es gibt jedoch zwei Restriktionen:
* Existieren nicht alle benötigten Daten (z.B. Aktienkurse) im Heimatmarkt, wird die Firma vom Export ausgeschlossen (z.B. Alibaba, da der chinesische Markt im Moment nicht abgebildet wird)
* Existiert die gleiche Firma in zwei Regionen wird diese nur im Export ihres Heimatmarktes verwendet (z.B. Adidas, welche bei SimFin im amerikanischen sowie deutschen Markt vorhanden ist)

##  Data Hubs

Neu werden abgeleitete Kennzahlen, welche nicht aus der Bilanz, Erfolgs -oder Geldflussrechnung abgelesen werden können, über sogenannte Data Hubs bezogen. Diese werden in dem oben aufgelisteten Tutorial beschrieben.

## Zwischenspeicherung der Daten

Die neue Bibliothek erstellt zu Beginn ein Verzeichnis auf der lokalen Entwicklungsumgebung. Dieses wird dazu verwendet, heruntergeladene Finanzdaten abzulegen. Mit Hilfe eines Parameters kann die Gültigkeitsdauer festgelegt werden. Danach werden die Daten erneut mit denen auf der SimFin-Datenbank abgeglichen. Damit werden unnötige Server-Abfragen verhindert und die Performance wird dadurch erhöht.

# Fazit

Vom Ziel, Fundamentaldaten für alle frei zur Verfügung zu stellen, hat sich SimFin ein grosses Stück entfernt. Die Verantwortlichen begründen die Einschränkungen dadurch, dass von Ihrer Seite immer noch sehr viel manueller Aufwand hinter dem Projekt steckt. Die Kosten seien nicht gedeckt, an dem gesteckten Ziel soll sich jedoch nichts ändern. Positiv zu sehen sind die neuen Tutorials, welche einige Tipps und Tricks für die Verwendung der SimFin-Bibliothek beinhalten. Die neue Python-Bibliothek macht, obschon es sich um eine Beta-Version handelt, einen guten ersten Eindruck.
