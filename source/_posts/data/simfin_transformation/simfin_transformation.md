---
title: SimFin Bulk Export transformieren
p: data/simfin_transformation/simfin_transformation.md
date: 2019-10-15 20:00:00
updated: 2024-01-28 00:00:01
tags:
- Experiment
- Python
- Anaconda
categories: Data Mining
toc: true
thumbnail: /gallery/thumbnails/data/simfin_transformation/thumbnail_square.jpg
cover: /gallery/thumbnails/data/simfin_transformation/thumbnail.jpg
---
Dieser Blog-Beitrag beschäftigt sich mit der Transformation von Daten. Es kann vorkommen, dass die Struktur von Datenexporten nicht für die Weiterverarbeitung passt. Die von [SimFin](https://simfin.com/) bereitgestellten Bulk-Daten sind in mehrere einzelne Exporte aufgeteilt. In unserem Experiment werden diese eingelesen und, nach dem Motto "Was nicht passt wird passend gemacht", in einen einzelnen Export (als CSV) geschrieben. Dazu wird eine Entwicklungsumgebung vorausgesetzt, welche in einem {% post_link data/environment/environment 'älteren Beitrag' %} beschrieben wurde.

<!-- more -->

## Theorie
Bevor mit dem praktischen Teil begonnen werden kann, folgen anbei noch einige theoretische Inhalte. Sie sollen dabei helfen, die bereitgestellte Lösungsvariante besser zu verstehen.

### Datensätze

Auf der SimFin-Website (unter "Bulk Data") ist eine Übersicht der einzelnen Datensätze inklusive deren Attribute zu finden. Mit Hilfe von Filterfunktionen kann die Form des Exports bestimmt werden:

* **Datensatz (engl. Dataset)**: Dieser Filter bestimmt, die im Export enthaltenen Attribute. Diese Selektion hat Einfluss auf die weiteren Filteroptionen (diese können zum Beispiel ausgeblendet werden, falls diese für den Export nicht relevant sind). Mehr dazu in einem der nächsten Abschnitte
* **Markt (engl. Market)**: In der SimFin-Datenbank wird jede enthaltene Firma einem Aktienmarkt zugeteilt. Jeder Markt hat eine Währung, in welcher alle Kennzahlen der darin enthaltenen Unternehmen notiert sind. Im Moment existieren zwei Märkte, welche Fundamentaldaten enthalten (USA und Deutschland, bzw. USD und EUR)
* **Zeitperiode (engl. Variant)**: Der Zeitintervall der Veröffentlichung der Daten. Die Option "Annual" liefert die Zahlen der Jahresabschlüsse der Firmen, "Quarterly" beinhaltet auch die Quartalszahlen und "Trailing Twelve Months (TTM)" die letzten 12 Monate
* **Details**: Mit der Option "Full" (nur für zahlende Kunden) werden alle verfügbaren Kennzahlen für den gewählten Datensatz exportiert. "Normal" liefert eine reduzierte Menge an Attributen

Die Option "Datensatz" enthält folgende (meist selbsterklärende) Auswahlmöglichkeiten:
* Bilanz (engl. Balance)
* Bilanz für Firmen aus dem Bankensektor
* Bilanz für Firmen aus dem Versicherungssektor
* Erfolgsrechnung (engl. Income Statement)
* Erfolgsrechnung für Firmen aus dem Bankensektor
* Erfolgsrechnung für Firmen aus dem Versicherungssektor
* Geldflussrechnung (engl. Cash Flow)
* Geldflussrechnung für Firmen aus dem Bankensektor
* Geldflussrechnung für Firmen aus dem Versicherungssektor
* Abgeleitete Kennzahlen und Verhältnisse (engl. Derived Figures & Ratios)
* Abgeleitete Kennzahlen und Verhältnisse für Firmen aus dem Bankensektor
* Abgeleitete Kennzahlen und Verhältnisse für Firmen aus dem Versicherungssektor
* Firmen (engl. Companies)
* Märkte (engl. Markets)
* Sketoren/Industrien (engl. Sector/Industry)
* Aktienkurse (engl. Share Prices)
* Aktienkurs-Verhältnisse (engl. Share Price Ratios)

### SimFin Python Bibliothek

SimFin bietet eine eigene Python-Bibliothek[^1] an, um die einzelnen Datensätze zu laden. Eine gute Einführung, in die Verwendung der Bibliothek, wird in den ersten 5 Kapiteln der zur Verfügung gestellten Tutorials vermittelt:
* [Basics](https://github.com/SimFin/simfin-tutorials/blob/master/01_Basics.ipynb) (Einführung in die Basisfunktionen sowie in die Datenanalyse mit pandas)
* [Resampling](https://github.com/SimFin/simfin-tutorials/blob/master/02_Resampling.ipynb) (Anzahl der Beobachtungspunkte erhöhen/verringern)
* [Growth Returns](https://github.com/SimFin/simfin-tutorials/blob/master/03_Growth_Returns.ipynb) (Berechnung von Wachstumskennzahlen)
* [Signals](https://github.com/SimFin/simfin-tutorials/blob/master/04_Signals.ipynb) (Berechnung von Kaufs-/Verkaufssignalen)
* [Data Hubs](https://github.com/SimFin/simfin-tutorials/blob/master/05_Data_Hubs.ipynb) (Von SimFin berechnete Daten, zum Beispiel die Gesamtkapitalrendite, via Hubs beziehen)

Die Tutorials wurden mit [Jupyter Notebook](https://jupyter.org/) erstellt. Diese Dokumente enthalten Live Code, Formeln, Visualisierungen sowie normaler Text.

## Praktischer Teil

Nun zum praktischen Teil. Für den Export sollen die verschiedenen Datensätze für alle verfügbaren Unternehmen in eine Export-Datei geschrieben werden. Damit muss für die zukünftige Datenverarbeitung nur eine Datei geladen werden.

### Vorgehensweise

Die folgenden Schritte zeigen einen möglichen Ablauf eines Python-Programms (in Pseudocode):

* Alle verfügbaren Märkte laden
  * Jeden Datensatz (Bilanz, Erfolgsrechnung sowie Geldflussrechnung) durchgehen (auch Banken und Versicherungen)
    * Jeden Markt durchgehen
      * Für den Markt die einzelnen Kennzahlen aus dem Datensatz laden
    * Alle Resultate der einzelnen Märkte untereinander anfügen
  * Alle Resultate der einzelnen Datensätze anhängen
* Alle Unternehmensinformationen laden und wieder anhängen
* Alle Industrien/Branchen laden und anhängen
* Alle Märkte erneut durchgehen
  * Die Aktienpreise laden und anhängen
* Alle Wertsignale (zum Beispiel KGV) laden und anhängen
* Alle Finanzsignale (zum Beispiel Gesamtkapitalrendite) laden und anhängen

Für den Aktienkurs muss ein Wochentag verwendet werden. Fällt das Datum des Jahres-/Quartalsabschlusses auf einen Samstag oder Sonntag, soll der Wert von dem davor liegenden Freitag genutzt werden.

## Lösungsbeschreibung

Die Lösung befindet sich unterhalb dieses Abschnittes (kann zugeklappt werden). Es ist nur eine mögliche Lösung für dieses Problem. Nachfolgend werden die Kernpunkte des Skriptes erläutert.

{% include_code Lösungsdatei lang:python data/simfin_transformation/bulkConverter.py %}

### Attribut-Namen als Konstanten
Die Bibliothek beinhaltet die einzelnen Feldnamen als Konstanten. Somit ist das Feld "Report Date" in der Variable "REPORT_DATE" hinterlegt. Die Konstanten werden auf der SimFin-Seite ebenfalls aufgeführt.

### CSV schreiben
Für das Schreiben der neuen Datei wird die Funktion to_csv[^2] verwendet. Diese schreibt die Daten im pandas-DataFrame (mit den Feld-Namen als Kopfzeile) in eine CSV-Datei.

### Datensätze konkatenieren
Um die einzelnen Zwischenresultate zu einem kompletten Datensatz zusammen zu fügen, wird die concat[^3]-Funktion von pandas verwendet. Diese verknüpft die einzelnen Teilstücke mit Hilfe der Indizes. Der Parameter axis entscheidet darüber, ob die Daten rechts (axis=0) oder unterhalb (axis=1) angehängt werden. Eine andere Möglichkeit bietet die merge[^4]-Funktion, falls es keine Schnittmenge der Indizes gibt.

### Wochentag ermitteln
Die Funktion weekday auf dem datetime[^5] Objekt ermittelt den dazugehörigen Wochentag. 0 steht für Montag, 6 für Sonntag.

### Laufzeit und Ressourcen
Die Durchlaufzeit des Skripts hängt stark von der Rechenpower der Maschine ab. Bei Erstausführung werden alle benötigten Daten auf der lokalen Festplatte abgelegt. Dies braucht Zeit und einiges an Speicherkapazität (ca. 800 MB). Der finale Export beträgt danach nur noch um die 20 MB.

[^1]: [SimFin Python API](https://simfin.readthedocs.io/en/latest/)
[^2]: [Offizielle pandas-Dokumentation zu to_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html)
[^3]: [Offizielle pandas-Dokumentation zu concat](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html)
[^4]: [Offizielle pandas-Dokumentation zu merge](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html)
[^5]: [Offizielle Python-Dokumentation zu datetime](https://docs.python.org/3.7/library/datetime.html#datetime.datetime)
