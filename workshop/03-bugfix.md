# Übung 3: Einen Bug agentisch bearbeiten

**Richtzeit:** 30 Minuten

## Kurze Theorie

Bei einem Bug sollte der Agent zuerst das Problem reproduzieren und die Ursache erklären. Erst danach entscheidest du über den Fix. So trennst du Diagnose von Umsetzung und kannst fachliches Sollverhalten bewusst bestätigen.

## Fehlerbeschreibung

Ein Nutzer meldet:

> Auf den Hof-Detailseiten fehlt ein Teil der Inspektionshistorie. Besonders nach erfolgreichen Inspektionen wirkt die Historie unvollständig.

Fachlich gilt: Die Historie soll alle gespeicherten Inspektionen unabhängig vom Ergebnis enthalten und neueste Einträge zuerst anzeigen.

## Aufgabe

1. Reproduziere das Symptom selbst in der laufenden Anwendung.
2. Bitte den Agenten, das Problem zu untersuchen und dir **zunächst nur** Ursache, betroffene Fälle und einen Fix-Vorschlag zu erklären.
3. Prüfe die Diagnose an Code, Daten und dokumentierter Fachlichkeit.
4. Beauftrage den Agenten anschließend mit dem kleinsten passenden Fix.
5. Lass den Agenten einen gezielten Regressionstest ergänzen, der eine vollständige Historie mit unterschiedlichen Ergebnissen prüft.
6. Prüfe den Diff, starte die Tests und verifiziere die Detailseiten im Browser.
7. Committe den funktionierenden Bugfix auf deinem Branch.

## Fertig, wenn …

- erfolgreiche und problematische Inspektionen sichtbar sind,
- die Reihenfolge weiterhin neu nach alt ist,
- ein Test die vollständige Historie absichert,
- die vorhandenen Tests grün bleiben,
- keine fachlich unabhängigen Änderungen im Diff enthalten sind.

## Reflexion

- Welche Werkzeuge hat der Agent für die Diagnose verwendet?
- Hätte ein grüner Testlauf den ursprünglichen Bug ausgeschlossen?
- Welche zusätzliche Prüfung würde eine Wiederkehr des Fehlers verhindern?
