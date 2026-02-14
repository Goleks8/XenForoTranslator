[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Windows](https://img.shields.io/badge/platform-Windows-brightgreen)](https://github.com/Goleks8/xenforo-phrase-translator)

## Features

- ✨ Batch translation of XenForo phrases via Google Translate
- 📊 Progress bar with real-time status
- ⚙️ Flexible YAML configuration
- 🏷️ Automatic language title update
- 🛡️ Error handling with automatic retries



## Quick Start
1. Install
   - Download the latest `XenForoTranslator.zip` from [Releases](https://github.com/Goleks8/xenforo-phrase-translator/releases)
   - Unzip in any folder (e.g., `C:\XenForoTranslator`)
   - Change the params of the `config.yml` if necessary([more](#Configuration (config.yml))).  
  
2. Export XML from XenForo:
  - Go to Appearance → Languages
  - Click "Export" on your target language (Recommended: translate one addon at a time)

3. Run the translator:
   - Run `XenForoTranslator.exe`
   - Drag and drop your `XML` file onto `XenForoTranslator.exe`
   - Output file: original-name_ru.xml (configurable)

## Installation Python Source Code

#### Requirements
- Python 3.8 or higher
- pip

#### Steps
```bash
git clone https://github.com/Goleks8/XenForoTranslator.git
```
```bash
cd XenForoTranslator
```
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage
```bash
XenForoTranslator.exe -i language.xml
```
or
```bash
python translator.py -i language.xml
```

### Interactive Mode (asks for file path)
```bash
XenForoTranslator.exe
```
or
```bash
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
source_lang: "en"           # Source language
target_lang: "ru"           # Target language
language_title: "Russian (RU)"  # New language title (used with --update-title)

# Batch processing
batch_size: 20              # Phrases per batch
sleep_sec: 1.0              # Pause between batches
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
