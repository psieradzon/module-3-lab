# Übung 4: Ein Feature planen und umsetzen

**Richtzeit:** 40 Minuten

## Kurze Theorie

Plan eignet sich, wenn mehrere Schichten betroffen sein können oder Anforderungen vor der Änderung geprüft werden sollen. Der Plan soll technische Auswirkungen und Verifikation klären, ohne bereits Code zu verändern. Erst ein akzeptierter Plan wird an Agent übergeben.

## Anforderung

Nutzende möchten die Hof-Übersicht nach dem aktuellen Status filtern.

### Akzeptanzkriterien

- Ohne Filter zeigt `/yards` weiterhin alle Höfe.
- `GET /yards?status=active`, `maintenance` oder `inactive` zeigt nur passende Höfe.
- Die Oberfläche bietet eine serverseitige Filterauswahl und zeigt den aktiven Wert nach dem Absenden weiterhin an.
- Eine unbekannte Statusangabe liefert HTTP 400 mit einer verständlichen Fehlermeldung.
- Die Anwendung bleibt vollständig server-gerendert und benötigt kein JavaScript.

## Aufgabe

1. Öffne eine neue Sitzung mit **Plan** und übergib Anforderung und Akzeptanzkriterien.
2. Lass den Agenten das Repository untersuchen und einen Implementierungs- und Testplan erstellen.
3. Prüfe, ob der Plan Datenfluss, Fehlerbehandlung, UI und Rückwärtskompatibilität abdeckt. Kläre Rückfragen und verfeinere ihn bei Bedarf.
4. Übergib den akzeptierten Plan an **Agent**.
5. Beobachte die ausgeführten Schritte und genehmige nur nachvollziehbare Kommandos.
6. Lass den Agenten gezielte Tests ergänzen für:
   - unveränderte Hof-Übersicht ohne Filter,
   - jeden gültigen Statusfilter,
   - eine ungültige Statusangabe,
   - die sichtbare Auswahl des aktiven Filters.
7. Prüfe die Änderung mit Browser, direkten Requests, Tests und Git-Diff.

## Fertig, wenn …

- alle fünf Akzeptanzkriterien nachweisbar erfüllt sind,
- die genannten Filterszenarien automatisiert geprüft werden,
- bestehende URLs ohne Query-Parameter unverändert funktionieren,
- keine zusätzliche Frontend-Toolchain eingeführt wurde,
- der vollständige Testlauf grün ist.

## Reflexion

- Welche Entscheidung wurde im Plan sichtbar, bevor Code entstand?
- Wo musstest du den Agenten während der Umsetzung nachsteuern?
- Welche Verifikation lieferte den stärksten Nachweis für das Feature?
