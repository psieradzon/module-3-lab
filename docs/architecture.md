# Architektur- und Entwicklungsleitfaden

## Überblick

Die Anwendung ist ein serverseitig gerenderter FastAPI-Dienst. HTTP-Routen nehmen Eingaben entgegen, Services führen Datenbankabfragen oder -befehle aus, und Jinja2-Templates erzeugen HTML. SQLModel bildet die Domänenmodelle auf SQLite-Tabellen ab.

```text
Browser → FastAPI route → service → SQLModel session → SQLite
                     ↘ Jinja2 template → HTML response
```

## Projektstruktur

- `app/routes/` übersetzt HTTP-Anfragen und -Antworten.
- `app/services/` enthält Anwendungsabfragen und -befehle.
- `app/models/` definiert Domänen-Enumerationen und SQLModel-Tabellen.
- `app/database/` erzeugt Sessions und lädt `data/seed.json` in eine leere Datenbank.
- `app/templates/` und `app/static/` stellen die serverseitig gerenderte Oberfläche bereit.
- `tests/` enthält Tests für Routen, Persistenz und Initialisierung.

`app.main.create_app()` ist die Application Factory. Jede Anwendung besitzt ihre Datenbank-Engine über `app.state.engine`. So können Tests isolierte SQLite-Datenbanken erzeugen, ohne die Produktionskonfiguration zu ändern.

## HTTP-Schnittstelle

| Methode | Pfad | Zweck |
| --- | --- | --- |
| `GET` | `/` | Weiterleitung zur Übersicht |
| `GET` | `/yards` | Rendert alle Höfe |
| `GET` | `/yards/{yard_id}` | Rendert einen Hof und seine Inspektionshistorie |
| `GET` | `/yards/{yard_id}/inspections/new` | Rendert das Inspektionsformular |
| `POST` | `/yards/{yard_id}/inspections` | Validiert und speichert eine Inspektion |

## Lokale Entwicklung

Installiere die festgeschriebenen Abhängigkeiten:

```bash
uv sync --locked
```

Starte die Anwendung:

```bash
uv run uvicorn app.main:app --reload
```

Führe die Tests aus:

```bash
uv run pytest
```

Die Standarddatenbank ist `data/yard_management.db`. Setze `DATABASE_URL`, um eine andere Datenbank-URL zu verwenden. Die SQLite-Datei wird von Git ignoriert und kann gelöscht werden, damit beim nächsten Start der Anwendung die ursprünglichen Beispieldaten erneut geladen werden.

## Designvorgaben

- Halte HTTP-Belange in den Routen und Datenbankverhalten in den Services.
- Belasse die Anwendung serverseitig gerendert; ein JavaScript-Buildsystem ist nicht erforderlich.
- Bewahre die dokumentierten Enum-Werte, weil Templates und persistierte Datensätze davon abhängen.
- Behandle Tests und direkte Browserprüfung als sich ergänzende Nachweise.
