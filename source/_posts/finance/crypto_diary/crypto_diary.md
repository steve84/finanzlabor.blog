---
title: Mein Krypto-Tagebuch
p: finance/crypto_diary/crypto_diary.md
date: 2021-01-30 09:00:00
tags:
- Theorie
- Kryptowährungen
- Blockchain
categories: Finanzen
toc: true
thumbnail: /gallery/thumbnails/finance/crypto_diary/thumbnail.jpg
---

Fast vier Jahre hat es gedauert, bis ich mir die Zeit genommen hatte, in die unbekannte Welt der Blockchain-Technologie (beziehungsweise Kryptowährungen) einzutauchen. In den Weihnachtsferien 2020 habe ich mich umfassend mit den Themen beschäftigt und möchte nun die Leser diese Blogs auf meine Reise ins Unbekannte minehmen. Dieser Beitrag ist in Form eines Tagebuches gestaltet, dieser liest sich von unten nach oben und wird laufend ergänzt. Er soll aufzeigen, wie meine Herangehensweise an ein neues Thema war und welche Erkenntnisse ich auf meinem Weg gewonnen habe. Auf Erklärungen zu den Funktionsweisen der einzelnen Technologien versuche ich im Rahmen dieses Beitrages so gut wie möglich zu verzichten.

<!-- more -->

**Hinweis in eigner Sache (Werbung)**: Ich verwende für den Kauf/Verkauf von Kryptowährungen die Börse Binance (die Gründe dafür werden in den nächsten Zeilen aufgeführt). Diese betreibt das [Binance Referral Program](https://www.binance.com/en/activity/referral), welches einen Bruchteil der Transaktionskosten an die Kunden zurückzahlt (Kickback). Wenn Ihr euch über [meinen Link](https://accounts.binance.com/de/register?ref=BNYR5DG3) anmeldet, erhaltet ihr 10 Prozent meiner anfallenden Gebühren (Ich erhalte ebenfalls 10 Prozent). Weitere Informationen zum Programm können der Binance-Webseite entnommen werden. Haben euch die nachfolgenden Zeilen beim Einstieg in die Krypto-Szene geholfen, wäre ich euch dankbar, wenn ihr euch über [diesen Link](https://accounts.binance.com/de/register?ref=BNYR5DG3) anmelden würdet. Bei Fragen könnte ihr euch auch direkt bei mir melden (kontakt@finanzlabor.blog). Ich bedanke mich bereits schon jetzt für eure Unterstützung. Nun wünsche ich viel Spass beim Lesen.


## 16. Oktober 2021
Seitdem Binance im Sommer 2021 den Geldtransfer via SEPA-Überweisung nicht mehr anbietet, habe ich kein Geld mehr auf die Börse übertragen können/wollen. In den letzten Tagen bin ich endlich dazu gekommen, mir einen neuen Weg dafür zu suchen. Dazu musste ich einen neuen Account bei einer Exchange eröffnen, welche diese Art von Überweisungen noch akzeptiert. Dabei bin ich auf [CoinMetro](https://coinmetro.com) gestossen. Nach einigen fehlgeschlagenen Versuchen konnte ich den KYC-Prozess doch noch erfolgreich abschliessen. Nun ging es darum, das eingezahlte Kapital von dieser Börse nach Binance zu transferieren. Leider musste ich den ersten Versuch abbrechen, da nach einem Transfer von USD Coins (Stable Coin) im Wert von 50 Euro nur noch etwa 7 Euro bei der Zieldestination angekommen wären. Grund dafür sind die hohen Gas-Fees auf der Ethereum Blockchain. Nun ging es darum, eine kostengünstigere Alternative zu finden, welche auch von CoinMetro angeboten wird. Nach Konsulation eines [Blog-Artikels](https://blog.nano.org/cryptocurrency-fee-comparison-which-crypto-has-the-lowest-fees-4e9118590e1f) zu diesem Thema, habe ich mich für Ripple (XRP) entschieden (extrem schneller Transfer). Anbei nun meine Vorgehensweise:

* SEPA-Überweisung nach CoinMetro im Wert von 50 Euro
* Umwandlung der 49 Euro (nach Abzug der Gebühr von pauschal einem Euro) nach Ripple (Kurs von 0.885928 XRP/EUR , 55.3 XRP)
* Wallet-Informationen von Binance für Ripple ermitteln
* Auf CoinMetro Abhebung („Withdraw“) initialisieren
* Eingabe der Ziel-Wallet und Durchführen des Transfers zu Binance
* Bestätigung der Übertragung nach Binance abwarten
* Ripple in einen Stable Coin umwandeln (zum Beispiel nach USD Tether)

Bei tiefen Beträgen entsteht bereits eine sehr hohe Gebühr für die SEPA-Überweisung (im diesem Beispiel 2 Prozent), dazu kommen noch die Spreads (tiefes Handelsvolumen) sowie die Transferkosten (etwa 0.15 Prozent) für die Nutzung der Ripple-Infrastruktur. Dies ist jedoch immer noch um einiges günstiger als die Binance-Kreditkartengebühren von 3.5% beziehungsweise 10$ (der höhere Betrag der beiden). Ein Dauerauftrag von wöchentlich 50 Euro sollte daher besser zu einem monatlichen Auftrag im Wert von 200 Euro umgewandelt werden.

## 7. März 2021

Nun wollte ich noch ein wenig tiefer in die Krypto-Materie eintauchen. Dazu habe ich mir, mit Hilfe der API von [messari.io](https://messari.io/), einige weitere Informationen zu den einzelnen Projekten beschafft:

* Art der Einführung
* Initiale Verteilung (Investoren, Oranisationen/Gründer und "Pre-mined" Rewards/Airdrops)
* Konsensus-Mechanismen
* Emissionstypen
* Maximale Anzahl an Coins/Token
* Aktivität der Projekt(weiter)entwicklung
* Präsenz in den sozialen Medien

Nun folgen die einzelnen Tabellen, welche ich aus diesen Daten erstellt habe. Zusätzlich habe ich einige weiterführendn Informationen zusammen getragen, welche bei der Interpretation der Inhalte helfen sollen. Der Herausgeber der Schnittstelle verfügt über eine eigene Erklärungsseite[^10], welche jedoch nur in englischer Sprache verfügbar ist.

Es gibt verschiedene Vorgehensweisen, um eine neue Währung in den Markt einzuführen. Ich habe versucht, die einzelnen Varianten in meinen eigenen Worten zu beschreiben:
* **Fair Launch**: Bei der Einführung ist die komplette Menge der verfügbaren Coins/Token erwerbbar
* **Crowdsale**: Ähnlich wie "Fair Launch". Es existieren jedoch bereits vorgeschürfte (pre-mined) Coins/Token, welche vorerst nicht für die Öffentlichkeit zugänglich sind
* **Centralized Distribution**: Die Coins/Token werden von einer zentralen Stelle aus verwaltet und gesteuert
* **Ledger Fork**: Der Coin/Token ist durch einen Fork (Gabelung) eines bestehenden Coins/Token entstanden
* **Private Sale**: Die komplette, initial herausgegebenen Menge an Coins/Token ist nur für eine vordefinierte Gruppe verfügbar. So können zum Beispiel Aktionäre, in Form von Coins/Token der herausgebenden Aktiengesellschaft, sich in einer anderen Form an der Firma beteiligen
* **Airdrop**: Die Coins/Token werden unter den Interessenten kostenlos verteilt
* **Initial Exchange Offering**: Ähnlich wie ein IPO in der Aktien-Welt

Die meisten Projekte verteilten bei der Einführung ihre Coins in mehrere Töpfe auf um diese auf verschiedene Empfängergruppen zu verteilen.

![Initiale Versorgung Top 25 Marktkapitalisierung (Stand 20.03.2021)](crypto_marketcap_supply.png)
Weiteres Bild: [Initiale Versorgung Top Sektoren (Stand 20.03.2021)](crypto_sector_supply.png)

Um die nachfolgende Tabelle zu verstehen, müssen zuerst die beiden Begriffe Mint und Burn erklärt werden. Mint (Prägung) bedeutet die Erweiterung des bestehenden Angebots eines Vermögenswertes (durch Erschaffung eines Coins/Tokens), Burn (Verbrennung) die Reduzierung des Angebots (durch Zerstörung des Coins/Tokens).

* **Burn and Mint**: Das ausstehende Angebot des Vermögenswerts (Assets) kann sowohl schrumpfen als auch zunehmen, abhängig von der Netzwerknutzung und deren Auswirkungen auf deflationäre (Burn) und inflationäre (Mint) Mechanismen
* **Deflationary**: Das ausstehende Angebot des Vermögenswerts schrumpft im Laufe der Zeit aufgrund von programmatischen oder nicht-programmatischen Burn-Mechanismen. Beachten Sie, dass in einigen Fällen ein Mindestvorrat festgelegt ist und die Verbrennungsmechanismen bei Erreichen dieses Wertes stoppen.
* **Fixed Supply**: Das ausstehende Angebot des Vermögenswerts ist fest. Es gibt keine inflationären oder deflationären Mechanismen.
* **Inflationary**: Das ausstehende Angebot des Vermögenswerts erhöht sich im Laufe der Zeit aufgrund von Prägemechanismen. Beachten Sie, dass in einigen Fällen eine Angebotsobergrenze festgelegt ist und die Prägemechanismen bei Erreichen dieser Obergrenze aufhören.

![Konsensus-Mechanismen Top 25 Marktkapitalisierung (Stand 20.03.2021)](crypto_marketcap_consensus.png)
Weiteres Bild: [Konsensus-Mechanismen Top Sektoren (Stand 20.03.2021)](crypto_sector_consensus.png)

Um die Korrektheit eines generierten Blockes zu validieren, existieren verschiedene Konsens-Mechanismen. Eine gute Zusammenstellung der einzelnen Methoden ist auf der Seite coin-ratgeber.de[^11] zu finden.

Die meisten Krypto-Projekte stellen den Programmcode der Öffentlichkeit zur Verfügung. Dies erlaubt die Mitarbeit interessierter Software-Entwickler auf der ganzen Welt. Die Dateien werden auf der Plattform GitHub verwaltet, welche die Kollaboration unter den Entwicklern vereinfacht. Diese ermöglicht es, den Projekten zu folgen (GitHub Beobachter) oder als Lesezeichen gespeichert (GitHub Sterne) zu werden. Möchten Programmänderungen der Versionsverwaltung mitgeteilt werden, müssen diese zuerst in sogenannte "Commits" verpackt werden. Diese beinhalten eine oder mehrere geänderte Datei(en) und eine Meldung, welche den Grund oder Zweck der Anpassungen beschreibt. Nach einiger Zeit wird mit Hilfe der Änderungen eine neue Version gebaut, welche danach die aktuell betriebene Software ersetzt.

![Software-Entwicklung Top 25 Marktkapitalisierung (Stand 20.03.2021)](crypto_marketcap_dev.png)
Weiteres Bild: [Software-Entwicklung Top Sektoren (Stand 20.03.2021)](crypto_sector_dev.png)

Eine weitere spannende Informationsquelle ist der Social-News-Aggregator Reddit. Die Anzahl aktiver Benutzer beziehungsweise Abonnenten auf dieser Plattform könnten vielleicht etwas über die aktuelle Akzeptanz eines Projektes aussagen.

![Social Media Top 25 Marktkapitalisierung (Stand 20.03.2021)](crypto_marketcap_social_media.png)
Weiteres Bild: [Social Media Top Sektoren (Stand 20.03.2021)](crypto_sector_social_media.png)

## 22. Februar 2021

Die Zahlen sind alle rot und zweistellig im Minus. Ich verspürte den inneren Drang, meine monatliche Investitionssumme sofort in eine der Kryptowährungen zu investieren. Fomo ("Fear of missing out", die Angst etwas zu verpassen) heisst der, in letzter Zeit oft verwendete Begriff dazu. Ich schritt zur Tat: Bitcoin war mit etwa 13 Prozent im Minus, als ich meinen ersten Kaufauftrag eingestellt hatte (etwas unter dem Kurs, welcher zuletzt festgestellt wurde). Es passierte das Gegenteil meiner Annahme, der Kurs erholte sich in grossen Schritten und meine Order wurde nicht ausgeführt. Es folgte eine grüne Kerze nach der anderen.  Ich wollte unbedingt meine ersten BTCs in meiner Wallet haben und zog den Preis nach. Nach zwei weiteren erfolglosen Versuchen wurde die Transaktion durchgeführt (bei 43'038 Euro pro Bitcoin). Die Ernüchterung folgte während den nachfolgenden Tagen. Nach einer kurzfristigen Erholung stürzte der Kurs um weitere 18 Prozent (14 Prozent im Vergleich zu meinem Trade) ab. Die Moral der Geschichte: Nicht einer verpassten Möglichkeit hinterher rennen. Die nächste Chance lässt meist nicht lange auf sich warten (Anfang Januar war der letzte grössere Rücksetzer um fast 30 Prozent).

Die restlichen 20 Prozent meines verfügbaren monatlichen Guthabens wurden in LINK (Chainlink) investiert (bei 22,5 Euro pro Link). Ich habe mich aus folgenden Gründen für die beiden Investments entschieden:

* Bitcoin (BTC)
    * Immer mehr Institutionelle sind investiert
    * Macht über 60 Prozent des gesamten Krypto-Marktkapitals aus
    * Die Anzahl ist beschränkt
* Chainlink (LINK)
    * Es existieren bereits Projekte, welche die Dienstleistung in Anspruch nehmen (Aave, Polkadot)
    * Ist der Sektor-Leader im Bereich "Oracle Networks"
    * Die Anzahl ist beschränkt

## 6. Januar 2021

Nun ging es darum, einen monatlichen Dauerauftrag von meiner Bank zu Binance zu erstellen. Um den Betrag der Überweisung zu bestimmen, habe ich zu Beginn des Jahres meine Budgetplanung aktualisiert. Dabei komme ich auf eine Sparrate von ca. 46%, davon möchte ich zirka 2.5% in Kryptowährungen anlegen. Um die gewünschte Allokation im Gesamtportfolio bis Ende des Jahres 2021 herzustellen, müssen zusätzliche Beträge überwiesen werden.

## 27. Dezember 2020

Nun war mein Fiat-Konto wieder auf ein paar Cent geschrumpft und ich hatte Zeit, mir einen Überblick über die Crypto-Welt zu verschaffen. Ich wusste bereits, was für einen Zweck Bitcoin und Ethereum haben, aber wofür werden die Anderen verwendet? Mit dieser Frage im Hinterkopf machte ich mich im Internet auf die Suche nach Antworten. Leider habe ich nirgends direkt etwas brauchbares dazu gefunden, sondern bin über Umwege auf die Plattform [messari.io](https://messari.io/) gestossen. Dabei handelt es sich um eine Webseite, welche "Crypto Research, Data and Tools" anbietet. Diese lässt sich via API ansprechen und war für mich der ideale Datenlieferant für meine Recherchen. Die Schnittstelle liefert für jedes Crypto-Projekt verschiedene Metadaten (Sektor, Anzahl aktive Projekte, Hashrate, uvm.) und historische Preise.

Als Erstes wollte ich nun herausfinden, wie stark die einzelnen Coins miteinander korrelieren. Ziel dieser Betrachtung war die Bestimmung eines Kryptoportfolios mit möglichst hoher Diversifikation. Ebenfalls wollte ich die gängige Aussage ("Bitcoin ist die Flut, die alle Boot zum Schwimmen bringt") einiger Kryptoinvestoren untersuchen. Daher erstellte ich zwei Korrelationsmatrizen, eine anhand der 25 grössten Projekte (gemessen an der Marktkapitalisierung) sowie der einzelnen Sektor-Platzhirsche (erneut anhand der Marktkapitalisierung). Dabei entstanden folgende Bilder:

![Korrelation Top 25 Marktkapitalisierung (Stand 20.03.2021)](marketCapCorrel.png)

Weitere Bilder:
[Korrelation Top 25 Marktkapitalisierung 100 Tage (Stand 20.03.2021)](marketCapCorrel100.png), [Korrelation Top 25 Marktkapitalisierung 1 Jahr (Stand 20.03.2021)](marketCapCorrel365.png)
[Korrelation Top Sektoren 100 Tage (Stand 20.03.2021)](sectorCorrel100.png), [Korrelation Top Sektoren 1 Jahr (Stand 20.03.2021)](sectorCorrel365.png), [Korrelation Top Sektoren (Stand 20.03.2021)](sectorCorrel.png)

Die nächste Frage welche mich beschäftige, war die Performance der einzelnen Währungen (absolut und in Relation zu Bitcoin). Daraus resultierten die nachfolgenden Grafiken, welche die monatlichen Bewegungen der einzelnen Werte in Prozent anzeigen (wobei die Y-Achse beim aktuellen Monat beginnt). Dabei ist auch zu sehen, dass einige der Branchen-Krösusse erst seit einigen Monaten existieren.

![Performance Top 25 Marktkapitalisierung (Stand 20.03.2021)](marketCapPerf.png)

Weitere Bilder:
[Performance in Relation zu Bitcoin Top 25 Marktkapitalisierung (Stand 20.03.2021)](marketCapPerfToBTC.png)
[Performance Top Sektoren (Stand 20.03.2021)](sectorPerf.png), [Performance in Relation zu Bitcoin Top Sektoren (Stand 20.03.2021)](sectorPerfToBTC.png)

## 26. Dezember 2020

Nun treffe ich erneut auf das {% post_link finance/stock_selection/stock_selection 'Auswahl-Paradoxon (wie bei den Einzelaktien)' %} und bin vor lauter verfügbaren Kryptowährungen komplett überfordert. Welche Funktion haben sie? Wer steckt dahinter? Wie lange gibt es diese bereits? Welche soll ich nun kaufen? Mir war jetzt bewusst, dass ich mir mehr Zeit nehmen muss, um tiefer in Materie einzutauchen. Nur so wird es möglich sein, eine Investitionsstrategie für mich auszuarbeiten.

Plötzlich stiess ich jedoch auf eine Nachricht, welche mein geplantes Vorgehen komplett über den Haufen geworfen hatte. Kurz vor Weihnachten wurde Ripple (XRP), eine der aktuell grössten Kryptowährungen auf dem Markt, von der amerikanischen Börsenaufsicht SEC verklagt[^9]. Der Kurs fiel um 75-Prozent, ich nutze die entstandene Einstiegschance (es handelt sich hierbei um keine Anlageempfehlung, es handelt sich dabei um eine riskante Wette). Eine Niederlage vor Gericht wäre ein Schlag ins Gesicht für die ganze Kryptoszene, die Zukunft von Bitcoin und Co. wäre meiner Meinung nach in Gefahr.

## 5. Dezember 2020

Nachdem die Registrierung abgeschlossen, die 2-Faktoren-Authentisierung aktiviert und meine Identität durch das Hochladen der Vorder- und Rückseite meiner Identitätskarte, Aufnahme eines Selbstportraits sowie Hinterlegung eines Dokumentes bestätigt war, konnte ich mit der Transferierung von FIAT-Geld beginnen. Der Begriff *fiat* stammt auf dem Lateinischen und bedeutet: "Ein Objekt ohne inneren Wert, welches als Tauschmittel verwendet wird". Dies ist im Moment nur mit Euro kostenlos möglich (es kann jedoch sein, dass deine Bank für die Ausführung einer SEPA-Überweisung einen gewissen Betrag in Rechnung stellt). Ich versuchte die Transaktion via TransferWise abzuwickeln, was jedoch nicht möglich war. In den Nutzungsbedienungen wird diese Einschränkung klar formuliert (bei Revolut ebenfalls). Der Transfer wurde danach via PostFinance durchgeführt, nach einigen Tagen war der Betrag zum Investieren bereit.

## 4. Dezember 2020

Nun sind meine Wissenslücken gedeckt und ich fühle mich bereit für den Kauf von Kryptowährungen. Nun stellt sich mir die Frage, wo und wie kann ich das tun? Diese werden direkt an Börsen gehandelt, es gibt also keinen Broker dazwischen. Im Web gibt es einige Vergleichsseiten[^7][^8] der einzelnen Handelsplätze. Die Seiten bieten meist mehrere Filterfunktionen (SEPA Überweisung möglich, Einsteigerfreundlichkeit) an und stellen die Möglichkeit zur Verfügung, nach dem aktuellen Kaufpreis (inklusive Gebühren) zu sortieren. Binance ist zur Zeit die günstigste und grösste (anhand des Handelsvolumen) Börse. Ich habe mich danach noch mit einem Kumpel ausgetauscht, welcher bisher nur gute Erfahrungen mit dem Anbieter gemacht hatte. Einer Anmeldung stand also nichts mehr im Wege.

## 3. Dezember 2020

Ich nehme mir also die Zeit und beginne mich in das Thema einzulesen. Dazu habe ich mir die beiden Whitepaper[^3][^4] der grössten (Anhand der Marktkapitalisierung) Blockchain-Projekte heruntergeladen und ausgedruckt. Ich sage bewusst nicht Krytowährungen, da Ethereum keine Währung ist. Es handelt sich dabei um eine Plattform für Smart Contracts, welche mit Ether am Laufen gehalten wird. Das letzte Mal, dass ich die Kurzfassung eines IT-Projektes in dieser Form komplett durchgelesen hatte, war während meines Master-Studiums vor 6 Jahren. Ich musste beide Dokumente mehrfach durchgehen, es tauchten mehre Fragen auf. Da es sich bei dieser Art von Texten um eine Zusammenfassung des Projektes handelt, musste ich mich für weitere Ausführungen anderen Quellen bedienen. Dabei bin ich auf den Kryptographie Crashkurs von Dr. Julian Hosp gestossen. Die beiden Teile 14 "Wie funktionieren Bitcoin Transaktionen im Detail?"[^5] und 15 "Bitcoin Mining im Detail erklärt"[^6] konnte den Grossteil meiner offenen Punkte abdecken.

## 30. November 2020

Das Corona-Virus hat uns voll im Griff und die Zeit steht praktisch still. Die Regierungen haben über das ganze Jahr unglaubliche Mengen an neuem Geld erschaffen. Die Entwertung des Geldes schreitet weiter voran, die Zinsen auf den Spar- sowie 3a-Konten streben gegen Null (oder sind sogar negativ). Ich hinterfrage die ersten beiden Säulen des 3-Säulen-Systems der Schweiz, schreibe die AHV-Rente sowie einen grossen Teil der Pensionskassengelder ab. Nun strahlt ein heller Stern am Himmel, welcher ein wenig Licht in die dunkle Stimmung bringt. Nein, der Himmelskörper hat nichts mit der Bibelgeschichte zu tun. Er ist das "digitale" Gold, die ganze Welt spricht darüber. Der Kurs des Bitcoins hat sein Allzeithoch bei etwa 20‘000 US-Dollar erreicht und ich möchte nun entlich kompetent mitreden können.

## Februar 2019

Im Schweizer Fernsehen lief eine Reportage über Blockchain und deren Anwendungsgebiete[^2]. Die vorgestellten Projekte waren alle noch am Anfang ihrer Entwicklung. Sie wirkten auf mich wie eine Spielerei, zeigten jedoch das vorhandene Potenzial auf. Auch zu dieser Zeit beschäftigte ich mich mit dem Thema nur in Form von Videos, ohne die Details zu den einzelnen Implementierungen anzuschauen.

## Sommer 2017

Während meiner Arbeit in der IT-Branche hörte ich zum ersten Mal etwas von einer Kryptowährung. Ein Arbeitskollege besass bereits Bitcoins, ein Anderer war gerade dabei Anteile zu erwerben. Letzterer berichtete mir, dass er diese an einem Ticket-Automaten der Schweizerischen Bundesbahnen[^1] (SBB) erwerben werde. Einige Tage später zeigte er mir seinen Kontostand auf seinem Smartphone. Leider war ich zu dieser Zeit noch in meiner Aktien-Welt gefangen und war gegenüber dieser neuen Währung eher negativ eingestellt. Mir fehlte einfach die Substanz dahinter, der faire Wert war und ist immer noch nicht wirklich zu ermitteln. Ich nahm mir jedoch nie die Zeit (oder andere Themen hatten eine höhere Priorität), mich mit dem technischen Hintergrund zu beschäftigen. Einige Monate später trennten sich die Wege, mein Arbeitskollege wechselte die Stelle, Bitcoin und Co. verschwanden in den Hintergrund.

[^1]: [Mit Bitcoin bequem und einfach einkaufen, sbb.ch](https://www.sbb.ch/de/bahnhof-services/am-bahnhof/services-am-billettautomat/bitcoin.html)
[^2]: [Blockchain verstehen: die digitale Zukunft wird dezentral, srf.ch](https://srf.ch/play/tv/redirect/detail/130c3b53-ef1b-41f1-9d4a-10719f3d5777)
[^3]: [Vitalik Buterin, Ethereum White Paper, A Next Generation Smart Contract & Decentralized Application Platform](https://blockchainlab.com/pdf/Ethereum_white_paper-a_next_generation_smart_contract_and_decentralized_application_platform-vitalik-buterin.pdf)
[^4]: [Satoshi Nakamoto, Bitcoin: A Peer-to-Peer Electronic Cash System](https://bitcoin.org/bitcoin.pdf)
[^5]: [Dr. Julian Hosp, Krypographie Crashkurs, Teil 14 "Wie funktionieren Bitcoin Transaktionen im Detail"?, youtube.com](https://youtu.be/38eMoZzk76U)
[^6]: [Dr. Julian Hosp, Krypographie Crashkurs, Teil 15 "Bitcoin Mining im Detail erklärt", youtube.com](https://youtu.be/4jd9qk3wq3Q)
[^7]: [Kostenvergleich der Krypto-Börsen, cryptoradar.co](https://cryptoradar.co/de/bitcoin-kaufen)
[^8]: [Ranking der Krypto-Börsen anhand der Marktkapitalisierung, coinmarketcap.com](https://coinmarketcap.com/de/rankings/exchanges/)
[^9]: [US-Börsenaufsicht SEC erhebt Anklage gegen Blockchain-Unternehmen Ripple, handelsblatt.com](https://www.handelsblatt.com/finanzen/maerkte/devisen-rohstoffe/kryptowaehrung-us-boersenaufsicht-sec-erhebt-anklage-gegen-blockchain-unternehmen-ripple/26745598.html)
[^10]: [Messari Classifications, messari.io](https://messari.io/article/messari-classifications)
[^11]: [Konsensus-Mechanismen bie Kryptowährungen, coin-ratgeber.de](https://coin-ratgeber.de/einfuehrung-konsensus-mechanismen-bei-kryptowaehrungen/)
