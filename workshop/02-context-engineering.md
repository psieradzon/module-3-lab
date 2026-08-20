# Übung 2: Kontext finden statt Prompt aufblasen

**Richtzeit:** 25 Minuten

## Kurze Theorie

Gute Zusammenarbeit mit einem Agenten bedeutet nicht, möglichst viel Text in einen Prompt zu kopieren. Auffindbaren technischen Kontext kann der Agent recherchieren. Nicht dokumentierte Ziele, Entscheidungen und fachliche Erwartungen muss der Mensch ergänzen.

## Aufgabe

Untersuche dieselbe Frage in zwei neuen Chat-Sitzungen:

> Wie wird sichergestellt, dass Beispieldaten nur in eine leere Datenbank geladen werden, und wie wird das in Tests isoliert?

### Variante B: Dateien referenzieren

Gib nur gezielt ausgewählte Dateien als Kontext mit und stelle die Frage.

### Variante C: Kontext suchen lassen

Gib nur Ziel und gewünschtes Ergebnis vor. Bitte den Agenten, relevante Implementierung und Tests selbst zu finden und seine Erklärung mit Fundstellen zu belegen.

Vergleiche anschließend:

- Aufwand für dich,
- Vollständigkeit und Präzision,
- verwendete Quellen,
- falsche oder unnötige Annahmen,
- Nachvollziehbarkeit der Antwort.

## Fertig, wenn …

- du die beiden Antworten vergleichen kannst,
- du mindestens eine fehlende oder unnötige Kontextinformation identifiziert hast,
- du eine kurze eigene Regel formuliert hast, wann du Kontext mitgibst und wann du ihn suchen lässt.

## Reflexion

- Hat mehr Kontext automatisch zu einer besseren Antwort geführt?
- Welcher Kontext war fachlich wichtig, aber nicht aus Code allein ableitbar?
- Wie würdest du den Prompt für eine reale, größere Codebase verändern?
