# Domänenmodell

Die Hof-App ist ein fiktives Betriebswerkzeug. Sie bietet eine kleine, in sich stimmige Fachdomäne, mit der sich eine unbekannte Codebase erkunden lässt, ohne branchenspezifisches Vorwissen zu benötigen.

## Höfe

Ein Hof steht für einen Betriebsstandort.

| Attribut | Bedeutung |
| --- | --- |
| `code` | Stabiler, menschenlesbarer Identifikator wie `YRD-001` |
| `name` | Anzeigename des Standorts |
| `city` | Fiktive Stadt zur Orientierung |
| `status` | Aktueller Betriebszustand |

Unterstützte Hof-Status sind:

- `active`: Der Standort ist regulär in Betrieb.
- `maintenance`: Der Standort ist vorübergehend durch Wartungsarbeiten beeinträchtigt.
- `inactive`: Der Standort ist derzeit nicht in Betrieb.

Der Status wird unabhängig von Inspektionen gepflegt. Das Erfassen einer neuen Inspektion ändert den Status eines Hofs nicht automatisch.

## Inspektionen

Eine Inspektion gehört zu genau einem Hof und dokumentiert eine abgeschlossene Prüfung. Sie enthält Datum, Name der prüfenden Person, Ergebnis und einen optionalen Kommentar.

Unterstützte Ergebnisse sind:

- `passed`: Die Inspektion wurde ohne handlungsbedürftiges Problem abgeschlossen.
- `issues_found`: Die Inspektion hat mindestens ein Problem festgestellt.

Die Hof-Detailseite soll die vollständige Inspektionshistorie anzeigen, einschließlich aller unterstützten Ergebnisse, sortiert von den neuesten zu den ältesten Einträgen.

## Fachliche Regeln

- Hof-Codes sind eindeutig.
- Eine Inspektion kann nicht ohne Hof existieren.
- Namen prüfender Personen müssen mindestens zwei Zeichen enthalten.
- Kommentare dürfen bis zu 500 Zeichen enthalten.
- Alle Beispielpersonen, -standorte und -ereignisse sind fiktiv.
