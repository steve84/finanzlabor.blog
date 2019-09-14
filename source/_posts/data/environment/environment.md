---
title: Entwicklungsumgebung für Datenanalyse einrichten
p: data/environment/environment.md
date: 2019-09-14 09:26:37
tags:
- Experiment
- Python
- Anaconda
categories: Data Mining
toc: true
thumbnail: /gallery/thumbnails/data/environment/thumbnail.jpg
---

Um Experimente mit Daten durchzuführen braucht es eine Entwicklungsumgebung. Darin wird Python verwendet, um kleine Programme zu schreiben. Diese Programmiersprache eignet sich ideal für Datenanalysen und ist relativ einfach zu lernen/lesen. Der Blog verwendet ausschliesslich Python in der Version 3. Das Ziel dieses Beitrages ist die Bereitstellung und erste Verwendung einer solchen Infrastruktur. Dazu braucht es nicht wirklich viel, die folgenden Unterkapitel beschreiben die einzelnen Schritte.

<!-- more -->

## Installation Betriebssystem und Anaconda

Die meisten Leser dieses Blogs verwenden Windows als Betriebssystem. Der Autor möchte jedoch auch eine Alternative aufzeigen und daher werden zwei Varianten erleutert.

### Windows

Dieser Abschnitt beschreibt die Installation auf einer Windows-Umgebung. Anleitungen und Hilfestellungen werden als externe Links angegeben.

#### Installation Anaconda

Anaconda ist eine Python Data Science Plattform, also genau das richtige für unsere Experimente. Alle wichtigen Pakete für Datenanalyse, künstliche Intelligenz und Datenvisualisierung sind darin enthalten oder können einfach nachinstalliert werden. Anaconda ist ebenfalls für Linux und macOS verfügbar. Das [Handbuch](https://docs.anaconda.com/anaconda/install/) beschreibt die Installation.

### Ubuntu (Linux)

Linux kann ebenfalls unter Windows betrieben werden oder direkt als Basissystem auf einem PC. Mit Hilfe einer virtuellen Maschine können beide parallel betrieben werden, ohne das bestehende Windows von der Festplatte entfernen zu müssen. Die nachfolgenden Unterkapitel beschreiben die Lösung mit der virtuellen Maschine.

#### Installation Oracle VirtualBox

Der erste Schritt besteht nun darin, die [VirtualBox Software zu installieren](https://www.thomas-krenn.com/de/wiki/VirtualBox_installieren).

#### Installation Ubuntu mit VirtualBox

Nun wird eine neue virtuelle Maschine mit Ubuntu ausgestattet. Ubuntu eignet sich optimal für Windows-Umsteiger. Die [Installationsanleitung](https://medium.com/@tushar0618/install-ubuntu-16-04-lts-on-virtual-box-desktop-version-30dc6f1958d0) kann mit Hilfe von Google Chrome auf Deutsch übersetzt werden.


#### Installation Anaconda

Nun ist die virtuelle Maschine bereit und kann mit diversen Programmen erweitert werden. Für die Installation von Anaconda folgen wir der Anleitung des Hersteller (siehe ). Es besteht auch die Mögichkeit ohne Anaconda zu arbeiten, dazu müssen die hier verwendeten Pakete manuell via [Python Pip](https://wiki.ubuntuusers.de/pip/) installiert werden.


## Installation Git

Um gewisse bestehende Projekte zu verwenden, muss Git installiert werden. [Was Git ist](https://git-scm.com/book/de/v1/Los-geht%E2%80%99s-Wozu-Versionskontrolle%3F) und [wie es installiert wird](https://git-scm.com/book/de/v1/Los-geht%E2%80%99s-Git-installieren), kann den beiden Links entnommen werden.


## Testen der Entwicklungsumgebung

Um zu überprüfen, ob alle installierten Komponenten funktionieren, kann folgender Test durchgeführt werden:

* Klonen des Git-Repositories von SimFin: *git clone https://github.com/SimFin/bd-extractor.git*
* Öffnen des Anaconda Powershell Prompts (oder eines Terminals unter Linux)
* Wechsel in das geklonte Git-Repository (mit Hilfe von *cd*)
* Eingabe des Befehls *python sample-extraction.py*

Nun sollten mehrere Zeilen ausgegeben werden, welche wiefolgt beginnen:

{% codeblock %}
Number of indicators in dataset: 33
Number of companies in dataset (companies with some missing values removed): 962
{% endcodeblock %}

Somit ist alles bereit, um in die Tiefen der Datenanalyse einzutauchen.

## Ausblick
Im nächsten Beitrag wird ein aktueller SimFin Bulk Export heruntergeladen und in ein anderes Format umgeformt, welches sich besser für die weitere Verarbeitung eignet.
