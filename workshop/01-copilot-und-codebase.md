# Übung 1: Copilot kennenlernen und die Codebase verstehen

**Richtzeit:** 25 Minuten

## Kurze Theorie

GitHub Copilot bietet verschiedene Interaktionen für unterschiedliche Aufgaben:

- **Ask** recherchiert und erklärt, ohne Änderungen auszuführen.
- **Plan** untersucht eine Aufgabe und erstellt vor der Umsetzung einen abstimmbaren Plan.
- **Agent** darf Dateien bearbeiten, Kommandos ausführen und anhand der Ergebnisse iterieren.

Ein Coding Agent kann Dateien suchen und vorhandene Dokumentation mit Code abgleichen. Deine Aufgabe ist nicht, ihm jeden Dateipfad zu nennen, sondern Ziel und Perspektive deutlich zu machen.

## Aufgabe

1. Prüfe, dass Copilot und Copilot Chat in VS Code aktiv sind.
2. Bitte Copilot in **Ask**, die Struktur und den Zweck des Repositories kurz zu erklären. Gib zunächst keine Dateien manuell als Kontext mit.
3. Lass dir erklären, wie Anwendung und Tests gestartet werden. Vergleiche die Antwort mit dem Root-README.
4. Starte Anwendung und Tests mit den dokumentierten Kommandos.
5. Bleib in **Ask** und wähle **eine** der beiden Perspektiven:

### Entwicklerinnen und Entwickler

Bitte Copilot, den Request-Fluss für das Anlegen einer Inspektion zu verfolgen. Die Erklärung soll HTTP-Eingabe, Validierung, Persistenz und die anschließende Antwort umfassen und ihre Aussagen mit Fundstellen belegen.

Stelle danach **eine** Rückfrage, zum Beispiel zur Isolation der Testdatenbank oder zu den Grenzen zwischen Route und Service.

### Projektmanagerinnen und Projektmanager

Bitte Copilot, die Anwendung ausschließlich fachlich zu erklären: Möglichkeiten für Nutzende, Status und Ergebnisse, erkennbare Regeln sowie fachliche Risiken.

Bitte anschließend um Fundstellen für **eine** zentrale Aussage, ohne eine detaillierte Code-Erklärung anzufordern.

## Fertig, wenn …

- die Hof-Übersicht im Browser sichtbar ist,
- die vorhandenen Tests grün sind,
- du den Ablauf einer Benutzeraktion in eigenen Worten wiedergeben kannst,
- mindestens eine Agentenaussage direkt an einer Fundstelle überprüft wurde.

## Reflexion

- Welche Informationen hat Copilot selbst gefunden?
- Wie verändert die genannte Rolle die Antwort?
- Welche fachliche Information könnte der Agent nicht selbst wissen, wenn sie nirgendwo dokumentiert wäre?
