---
title: SimFin Bulk Export transformieren
p: data/simfin_transformation/simfin_transformation.md
date: 2019-09-16 16:46:21
tags:
- Experiment
- Python
- Anaconda
categories: Data Mining
toc: true
thumbnail: /gallery/thumbnails/data/simfin_transformation/thumbnail.jpg
---
Dieser Blog-Beitrag beschäftigt sich mit der Transformation von Daten. Es kann vorkommen, dass die Struktur von bestehenden Datenquellen nicht für die Weiterverarbeitung passt. Die von SimFin bereitgestellten Exporte haben einen eher exotischen Aufbau. In unserem Experiment wird ein solcher Export eingelesen und, nach dem Motto „Was nicht passt wird passend gemacht“, erneut in einen anderen Export (als CSV) geschrieben. Dazu wird eine Entwicklungsumgebung vorausgesetzt, welche in einem älteren Beitrag beschrieben wurde.

<!-- more -->

Theorie

Bevor mit dem praktischen Teil begonnen werden kann, müssen noch einige theoretische Inhalte vermittelt werden.

Datenformat

SimFin bietet zwei verschiedene Datenformate an. Welche dies sind und wie sie sich voneinander unterscheiden, soll kurz erläutert werden.

Narrow

Hier gibt es für jedes Unternehmen pro Kennzahl pro Zeitperiode einen Eintrag. Für die Firma Apple sind 11 Geschäftsjahre (ohne Quartalszahlen) mit je 51 Kennzahlen vorhanden. Das sind bereits über 500 Zeilen für ein Unternehmen. Dies resultiert in fast 3 Millionen Einträge in dem heruntergeladenen CSV. Die Datei ist also vertikal aufgebaut.

Wide

Bei diesem Format haben wir pro Firma und Geschäftsjahr eine Spalte. Die Zeilen stellen Beobachtungszeitpunkte dar, wo mindestens ein Unternehmen eine Kennzahl veröffentlicht hat. Der Nachteil dieses Formates besteht darin, dass ein Unternehmen höchstens 4 Mal im Jahr ihre Zahlen veröffentlicht und es entstehen dadurch viele leer Einträge in der CSV-Datei.

SimFin Python Bibliothek

SimFin bietet eine eigene Python-Bibliothek an, um die Daten aus einem Bulk Download zu laden. Diese kann jedoch nur mit Dateien im Wide-Format umgehen. SimFin stellt auch einfache Beispiele in demselben GitHub-Repository zur Verfügung.

Hier die wichtigsten Funktionen und Klassen der bereitgestellten Python-Dateien

Die Klasse SimFinDataset in der Datei extractor.py hat einen Konstruktor mit folgenden Argumenten:
dataFilePath: Der Pfad zu dem heruntergeladenen Bulk Export
csvDelimiter: Der Delimiter, welche beim Herunterladen gewählt wurde. Standardeinstellung ist semicolon. Für Komma getrennte Exporte kann comma mitgegeben werden
startDate: Startdatum der Einträge (Ältere werden nicht geladen) im Format 1984-10-26
endDate: Enddatum der Einträge (Neuere werden nicht geladen) im gleichen Format wie startDate
excludeMissing: Sollen unvollständige Einträge (z.B. eine Kennzahl fehlt) ausgelassen werden. Standardmässig werden alle geladen

Danach sind die Daten in den unten stehenden Feldern abgelegt:
numIndicators: Anzahl der Indikatoren
numCompanies: Anzahl der Firmen
companies: Firmen der Klasse Company als Array
timePeriodsDates: Alle Beobachtungszeitpunkte (Zeilen im CSV)

Die Klasse Company in der Datei extractor.py repräsentiert ein einzelnes Unternehmen und hat folgende Eigenschaften:
id: Eine eindeutige Identifikationsnummer, um die einzelnen Unternehmen voneinander zu unterscheiden
name: Der Name der Firma
ticker: Das Kürzel
industryCode: Die Branchen-Zuordnung der Firma.
finYearMonthEnd: Der Monat, in welchem das Geschäftsjahr endet
data: Hier werden die Kennzahlen abgelegt (in einem Array mit Objekten der Klasse Indicator, welche wir unten behandeln)
Eine weitere wichtige Klasse ist, wie oben erwähnt, die Indicator-Klasse in der Datei extractor.py:
name: Der Name der Kennzahl
values: Die dazugehörigen Werte der Kennzahl in einem Array

Praktischer Teil

Nun zum praktischen Teil. Für den Export soll pro Firma und Zeitpunkt nur eine Zeile existieren. Dies ist einfacher zu lesen und die meisten Datenverarbeitungswerkzeuge erwarten dieses Format.

Bulk Export herunterladen
Nach der Anmeldung auf der SimFin-Website kann unter Data Access die Option Bulk Download gewählt werden. Nun stehen verschiedene Varianten des Exports zur Verfügung. Die nachfolgenden  Abschnitte erklären die einzelnen Optionen. Für unser Experiment werden folgende Einstellungen verwendet:
Dataset: Stock prices + Fundamentals (Detailed)
Options
Update fundamentals & ratios on: Period end-date
Time periods fundamentals: TTM
General data format: Wide
Delimiter string of CSV: Semicolon

Vorgehensweise

Nun können die Daten gelesen und in ein gewünschtes Format konvertiert werden. Die folgenden Schritte zeigen einen möglichen Ablauf eines Python-Programmes:

1. Laden des Exports mit Hilfe der Klasse SimFinDataset
2. Jedes geladene Unternehmen durchgehen
3. Alle Beobachtungszeitpunkte durchgehen
4. Nur Zeitpunkte anschauen, welche auf ein Monatsende fallen
5. Die Werte in einer Datenstruktur ablegen
6. Eine neue Zeile in die resultierende CSV-Datei schreiben, falls diese Werte enthält, welche nicht zu folgender Liste gehören:
Share Price
Common Shares Outstanding
Avg. Basic Shares Outstanding
Avg. Diluted Shares Outstanding
Market Capitalisation
7. Schritte 2-6 wiederholen, bis alle Unternehmen abgearbeitet wurden

Für den oben erstellten Ablauf gibt es ein paar Ausnahmen:
Für den Indikator ‚Share price‘ muss ein Wochentag verwendet werden. Fällt der Geschäftsabschluss auf einen Samstag oder Sonntag, soll der Wert von dem davor liegenden Freitag benutzt werden.
Es kann vorkommen, dass Aussagen zu den ausstehenden Aktien nicht am Tag des Abschlusses protokolliert werden. Daher wird die letzte bereitgestellte (falls diese nach dem letzten Geschäftsabschluss vermerkt wurde) Zahl verwendet
Es sollen nur Zeilen geschrieben werden, welche mindestens eine Fundamentalkennzahl enthalten (dies sind Quartals- und Jahreszahlen)


Lösungsbeschreibung

Die Lösung kann unter sdsdf heruntergeladen werden. Es ist nur eine mögliche Lösung für dieses Problem. Nachfolgend werden die Kernpunkte des Skriptes erläutert.

CSV lesen und schreiben
Der Export wird mit der Funktion SimFinDataset geladen, welche aus der SimFin Bibliothek stammt. Für das Schreiben der neuen Datei wird ein csv.DictWriter (https://docs.python.org/3/library/csv.html#csv.DictWriter) verwendet. Dieser ermöglicht es, Schlüssel/Wert-Paare direkt in die Ausgabedatei zu schreiben (ohne sich um die Reihenfolge kümmern zu müssen). Mit dem Attribut fieldnames werden die Schlüsselfelder (sowie ihre Reihenfolge) definiert. Um der Datei eine Kopfzeile hinzuzufügen, wird die Funktion writeheader einmalig (noch bevor die erste Datenzeile mit writerow geschrieben wird) aufgerufen.

Monatsende überprüfen
Es sollen nur Beobachtungszeitpunkte näher angeschaut werden, welche den letzten Tag eines Monats repräsentieren. Mit Hilfe der Funktion calendar.monthrange (https://docs.python.org/3.7/library/calendar.html) wird anhand von Monat und Jahr der erste sowie letzte Tag ermittelt. Dies ist für den Februar sehr hilfreich, weil die Funktion Schaltjahre berücksichtigt.

Wochentag ermitteln
Die Funktion weekday auf dem datetime Objekt ermittelt den dazugehörigen Wochentag (https://docs.python.org/3.7/library/datetime.html#datetime.datetime). 0 steht für Montag, 6 für Sonntag.

Dauer und Ressourcen
Die Durchlaufzeit des Skripts hängt stark von der Rechenpower der Maschine ab. Die Funktion zum Laden aller Einträge benötigt einige Gigabytes an Speicher und es kann zu einem MemoryError (vorallem bei 32bit Systemen) kommen. Sollte dies vorkommen, sollte man falls möglich ein anderes System verwenden. Die Einschränkungen mit Hilfe von startDate/endDate sollten die Menge an verwendetem Speicher reduzieren (danach können die einzelnen, kleineren Exporte zusammengefügt werden).
