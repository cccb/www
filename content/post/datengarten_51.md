---
title: "Datengarten 51"
subtitle: "Puppet … Konfigurationsmanagement"
date: 2015-05-12T00:00:00+02:00
---

-   Referent: Robert (https://twitter.com/zero\_0ne)
-   Termin: Dienstag, 12.5.2015, 20 Uhr
-   Ort: CCCB, Marienstraße 11, 10117 Berlin
-   Voraussetzungen: keine, der Eintritt ist kostenlos

"Puppet … Konfigurationsmanagement“ (KM; englisch configuration
management, CM) ist eine Managementdisziplin, die organisatorische und
verhaltensmäßige Regeln auf den Lebenslauf eines Produkts und seiner
Konfigurationseinheiten von Entwicklung über Herstellung und Betreuung
bis hin zur Entsorgung anwendet.” Wikipedia -
<http://de.wikipedia.org/wiki/Konfigurationsmanagement> , 20.03.2015

Hört sich komisch an, ist aber gar nicht so falsch. Es geht um Server
(Linux/Unix…\[ja, auch Windows, aber wer will das denn schon\])
Konfiguration. Man kennt das ja, man richtet einen neuen Server ein,
dann noch einen und dann noch einen und dann… Immer wieder das Gleiche.
Dann baut man sich irgendwie statische Skripts. Und dann verzweifelt
man, weil es mal wieder nicht so recht will wie man sich das gedacht
hatte… und hier setzt nun Puppet an. Es hilft einem dabei, den
Wunschzustand eines Systems zu definieren und sorgt dann dafür das
dieser hergestellt wird und bleibt. Dynamisch und modular, vielseitig
einsetzbar.

` file { ‘puppet_datengarten.key’:`\
`         ensure   => ‘present’,`\
`         owner    => ‘rwaffen’,`\
`         group     => ‘datengarten’,`\
`         mode     => ‘777’,`\
`         source   => ‘datengarten/mai/puppet_datengarten.key.template’,`\
`         require   => Group[Datengarten],`\
` }`
