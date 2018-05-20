---
categories: ["Datengarten"]
series: "Datengarten"
title: "Datengarten 81"
no: 81
subtitle: "Verteilte Schlüsselerzeugung und Schwellenwertkryptografie für OpenPGP"
speaker: Heiko Stamer
speaker_url: https://savannah.nongnu.org/projects/libtmcg
date: 2017-10-10T00:00:00+02:00
event_date: 2017-10-10T20:00:00+02:00
location: CCCB
language: Deutsch
streaming: false
---
{{< datengarten-infobox >}}

Folien: https://www.nongnu.org/libtmcg/dg81_slides.pdf 

Obwohl das Konzept der Schwellenwertkryptografie (Desmedt, 1987) und dessen
Umsetzung (Desmedt und Frankel, 1989) seit Jahrzehnten bekannt sind, kommen
diese Ansätze in der Praxis bisher nur selten zum Einsatz. Die grundlegende
Idee ist dabei, dass sich ein geheimer Schlüssel aus mehreren Einzelteilen
zusammensetzt, die jeweils auf verschiedenen Systemen gespeichert bzw.
verarbeitet werden und/oder sich unter der Kontrolle verschiedener Personen/
Institutionen befinden. Eine kryptografische Operation (z.B. Signatur oder
Entschlüsselung) kann innerhalb der getroffenen Sicherheitsannahmen nur
dann durchgeführt werden, wenn eine festgelegte Anzahl von Parteien (Schwelle)
im Rahmen eines (interaktiven) Protokolls zur gemeinsamen Lösung beiträgt.
Neben den vielfältigen Anwendungsszenarien für Gruppen oder Institutionen
lässt sich damit auch das Risiko von (Seitenkanal-)Angriffen reduzieren.

Sichere und relativ effiziente Verfahren für eine verteilte Schlüsselerzeugung
existieren ebenfalls seit Jahren, haben jedoch abseits von akademischen 
Beiträgen (Kate und Goldberg, 2009; Atwater und Hengartner, 2016) und einigen
Prototypen [1, 2] in der Öffentlichkeit kaum breitere Anwendung gefunden.
Allenfalls die sehr allgemeine Technik der Geheimnisteilung (Shamir, 1979) wird
im kommerziellen Sektor und FOSS-Bereich [3, 4] eingesetzt. Mit der zunehmenden
Bedeutung von elektronischen Währungen wie Bitcoin sind zukünftig weitere
wissenschaftliche Arbeiten (z.B. Gennaro, Goldfeder und Narayanan, 2016) und
hoffentlich auch praktische Resultate wie [5] zu erwarten. 

Der Vortrag stellt meine eigenen Bemühungen vor, dezentrale Konzepte wie
verteilte Schlüsselerzeugung und Schwellenwertkryptografie für OpenPGP nutzbar
zu machen. Das Ergebnis ist eine experimentelle Implementierung [6] innerhalb
der freien C++ Bibliothek LibTMCG [7] für Schlüsselerzeugung (Gennaro, Jarecki,
Krawczyk und Rabin, 2007), Entschlüsselung (Cramer, Gennaro und Schoenmakers,
1997) und Signaturerstellung (Canetti, Gennaro, Jarecki, Krawczyk und Rabin,
1999). Die damit erzeugten öffentlichen ElGamal- und DSA-Schlüssel sind
OpenPGP-kompatibel und können daher ohne Einschränkung für Verschlüsselung
und Signaturverfifikation verwendet werden. Die Entschlüsselung und Signatur
setzt allerdings Interaktion zwischen den beteiligten Parteien voraus. Im
Vortrag werden auch potentielle Anwendungsszenarien (z.B. spezielle Postfächer
für Whistleblower und Signierung von Quelltexten bzw. ISO-Images) diskutiert.

[1] https://crysp.uwaterloo.ca/software/DKG/

[2] https://crysp.uwaterloo.ca/software/shatter/

[3] http://www.digital-scurf.org/software/libgfshare

[4] http://point-at-infinity.org/ssss/

[5] https://github.com/citp/TwoFactorBtcWallet

[6] https://www.nongnu.org/libtmcg/libTMCG.html/Tools.html

[7] https://www.nongnu.org/libtmcg/

[Atwater und Hengartner, 2016]
Erinn Atwater and Urs Hengartner.
Shatter: Using Threshold Cryptography to Protect Single Users with Multiple Devices.
9th ACM Conference on Security & Privacy in Wireless and Mobile Networks, pp. 91--102, 2016.

[Canetti, Gennaro, Jarecki, Krawczyk und Rabin, 1999]
Ran Canetti, Rosario Gennaro, Stanislaw Jarecki, Hugo Krawczyk, and Tal Rabin.
Adaptive Security for Threshold Cryptosystems.
Advances in Cryptology -- CRYPTO'99, LNCS 1666, pp. 98--116, 1999.

[Cramer, Gennaro und Schoenmakers, 1997]
Ronald Cramer, Rosario Gennaro, and Berry Schoenmakers.
A Secure and Optimally Efficient Multi-Authority Election Scheme.
Advances in Cryptology -- EUROCRYPT'97, LNCS 1233, pp. 103--118, 1997.

[Gennaro, Goldfeder und Narayanan, 2016]
Rosario Gennaro, Steven Goldfeder, and Arvind Narayanan.
Threshold-Optimal DSA/ECDSA Signatures and an Application to Bitcoin Wallet Security.
Applied Cryptography and Network Security, LNCS 9696, pp. 156--174, 2016.

[Gennaro, Jarecki, Krawczyk und Rabin, 2007]
Rosario Gennaro, Stanislaw Jarecki, Hugo Krawczyk, and Tal Rabin.
Secure Distributed Key Generation for Discrete-Log Based Cryptosystems.
Journal of Cryptology, Vol. 20 Nr. 1, pp. 51--83, 2007.

[Desmedt, 1987]
Yvo Desmedt.
Society and group oriented cryptography: A New Concept.
Advances in Cryptology -- CRYPTO'87, LNCS 293, pp. 120--127, 1987.

[Desmedt und Frankel, 1989]
Yvo Desmedt and Yair Frankel.
Threshold Cryptosystems.
Advances in Cryptology -- CRYPTO'89, LNCS 435, pp. 307--315, 1989.

[Kate und Goldberg, 2009]
Aniket Kate and Ian Goldberg.
Distributed Key Generation for the Internet.
29th IEEE International Conference on Distributed Computing Systems, pp. 119--128, 2009.

[Shamir, 1979]
Adi Shamir.
How to Share a Secret.
Communications of the ACM, Vol. 22 Nr. 11, pp. 612-613, 1979."
