# PNG zu ICO Converter

Ein einfaches GUI-Tool zum Konvertieren von PNG-Bildern in ICO-Format für Windows-Icons.

## Features

- Benutzerfreundliche grafische Oberfläche
- Auswahl mehrerer Icon-Größen (16x16, 32x32, 48x48, 64x64, 128x128, 256x256)
- Batch-Konvertierung mehrerer PNG-Dateien
- Fortschrittsanzeige
- Automatische Erstellung von Multi-Size ICO-Dateien

## Voraussetzungen

- Python 3.x
- PIL (Pillow)
- ttkbootstrap

## Installation

1. Klone das Repository:
   ```bash
   git clone <repository-url>
   cd png-to-ico-converter
   ```

2. Installiere die erforderlichen Pakete:
   ```bash
   pip install pillow ttkbootstrap
   ```

## Verwendung

1. Starte die Anwendung:
   ```bash
   python icon.py
   ```

2. Wähle den Eingabeordner mit PNG-Dateien aus
3. Wähle den Ausgabeordner für die ICO-Dateien
4. Wähle die gewünschten Icon-Größen aus
5. Klicke auf "Konvertieren"

## Kompilierung zu EXE

Die Anwendung kann mit PyInstaller zu einer ausführbaren EXE-Datei kompiliert werden:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed icon.py
```

## Lizenz

[Hier Lizenz angeben]
