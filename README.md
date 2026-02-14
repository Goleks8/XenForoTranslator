# XenForo XML Phrase Translator
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Windows](https://img.shields.io/badge/platform-Windows-brightgreen)](https://github.com/Goleks8/xenforo-phrase-translator)

Automatically translate phrases XenForo 1.* - 2.* language XML files using Google Translate.

## Features

- ✨ Batch translation of XenForo phrases
- 📊 Progress bar with real-time status
- 🔄 Error handling with automatic retries


## Quick Start 

1. Installation
    - Download the latest `zip` from Releases
    - Unzip in any folder
    - `config.yml` is included in the archive - edit it as needed

2. Export XML from XenForo:
    - Go to Appearance → Languages
    - Click "Export" on your target language
    - Recommended: translate one addon at a time

3. Translate:
    - Run XenForoTranslator.exe
    - Drag and drop your XML file onto XenForoTranslator.exe

## Installation

### Option 1: Standalone EXE (Windows)

1. Download the latest `XenForoTranslator.exe` from Releases
2. Place the EXE in any folder
3. `config.yml` is included in the archive - edit it as needed

### Option 2: Python Source Code

#### Requirements
- Python 3.8 or higher
- pip

#### Steps
```bash
git clone https://github.com/Goleks8/XenForoTranslator.git
cd xenforo-phrase-translator
pip install -r requirements.txt
```

## Usage

### Basic Usage
```bash
XenForoTranslator.exe -i language.xml

python translator.py -i language.xml
```
### Interactive Mode (asks for file path)
```bash
XenForoTranslator.exe

python translator.py
```
### Options

| Option | Description |
|--------|-------------|
| `-i, --input_file` | Path to XML file |
| `--update-title` | Change language title (uses config) |

### Examples
```bash
XenForoTranslator.exe -i language.xml
XenForoTranslator.exe -i language.xml --update-title
XenForoTranslator.exe
```
## Configuration (config.yml)

The archive includes `config.yml`. Edit it to your needs:

```yaml
# Language settings
source_lang: "en"               # Source language
target_lang: "ru"               # Target language
language_title: "Russian (RU)"  # New language title (used with --update-title)

# Batch processing
batch_size: 20                  # Phrases per batch
sleep_sec: 1.0                  # Pause between batches
```

## Output File

The translated file is saved in the same folder as input:
- `language.xml` → `language-ru.xml`
- `addon-phrases.xml` → `addon-phrases-ru.xml`

## Requirements

- Windows 7/8/10/11 (for EXE version)
- Internet connection for Google Translate
- Python 3.8+ (for source version)

## License

MIT License - free to use and modify.
