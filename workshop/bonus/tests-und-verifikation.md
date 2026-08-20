# Bonus: Tests und Verifikation

## Kurze Theorie

Agenten können Tests schnell erzeugen, aber eine große Testmenge ist nicht automatisch aussagekräftig. Gute Tests beweisen fachliches Verhalten, scheitern bei einer Regression und bleiben unabhängig von unwichtigen Implementierungsdetails.

## Aufgabe

Bitte den Agenten, die bisherige Testabdeckung gegen Fachlichkeit und Akzeptanzkriterien zu prüfen. Lass ihn anschließend gezielte Tests ergänzen, soweit sie noch fehlen.

Prüfe jeden vorgeschlagenen Test:

1. Ist das fachliche Verhalten deutlich erkennbar?
2. Würde der Test beim entsprechenden Fehler wirklich rot werden?
3. Ist er unabhängig von anderen Tests und lokalen Daten?
4. Testet er Verhalten statt interne Implementierungsdetails?

Lass den Agenten danach die komplette Suite ausführen. Verändere testweise lokal eine zentrale Bedingung, beobachte einen passenden fehlschlagenden Test und verwirf nur diese absichtliche Veränderung wieder.

## Fertig, wenn …

- du mindestens einen Test kontrolliert rot und wieder grün gesehen hast,
- Anwendung und Tests dieselbe fachliche Erwartung ausdrücken,
- der abschließende Git-Diff nur beabsichtigte Änderungen enthält.

## Reflexion

- Welcher Test hätte den ursprünglichen Workshop-Bug früh erkannt?
- Welche vom Agenten vorgeschlagenen Prüfungen waren redundant oder zu technisch?
- Welche Evidenz würdest du zusätzlich vor einem Merge verlangen?
