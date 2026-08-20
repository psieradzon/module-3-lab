# Modul 3 Lab: Hof-App

Dieses Repository ist die gemeinsame Übungsumgebung für Modul 3 des Workshops. An einer kleinen, vollständig fiktiven Hof-App lernst du, wie du GitHub Copilot zum Verstehen, Planen, Implementieren und Verifizieren von Änderungen einsetzt.

Die Anwendung ist bewusst überschaubar, verhält sich aber wie ein echtes kleines Softwareprojekt: Sie besitzt eine Datenbank, serverseitig gerenderte Seiten, fachliche Regeln, Tests und dokumentierten Projektkontext.

## Voraussetzungen

- Visual Studio Code
- GitHub Copilot und GitHub Copilot Chat für VS Code
- Git
- [uv](https://docs.astral.sh/uv/) und Python 3.12

Alternativ kannst du das Repository in GitHub Codespaces öffnen. Der Devcontainer installiert Python, uv und die benötigten VS-Code-Erweiterungen automatisch.

## Anwendung starten

```bash
uv sync --locked
uv run uvicorn app.main:app --reload
```

Öffne anschließend <http://127.0.0.1:8000>. Beim ersten Start wird `data/yard_management.db` aus den fiktiven Beispieldaten in `data/seed.json` erzeugt.

## Tests ausführen

```bash
uv run pytest
```

Die vorhandene Test-Suite muss zu Beginn vollständig grün sein.

## Workshop starten

Beginne mit [workshop/README.md](workshop/README.md). Der Pflichtpfad ist ein Halbtag von 9:00 bis 13:00 Uhr mit zwei kurzen Pausen. Der Ausgangspunkt ist `main` bzw. der Tag `workshop-start`.

## Technischer Kontext

- [Domain model](docs/domain.md)
- [Architecture and development guide](docs/architecture.md)

Die Workshop-Anleitungen und die Benutzeroberfläche sind auf Deutsch. Code, Bezeichner, Formularfelder, Enum-Werte und technische Projektdokumentation bleiben auf Englisch.

## Lizenz

Dieses Projekt steht unter der [MIT License](LICENSE).
