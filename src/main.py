#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
XenForo XML Phrase Translator
Author: Goleks8 (https://github.com/Goleks8)
Description: Translate XenForo 2.2 language XML files
"""

import sys
import argparse
from pathlib import Path
from lxml import etree
from deep_translator import GoogleTranslator

from config import load_config
from translate import translate_phrases

def parse_arguments():
    parser = argparse.ArgumentParser(
        description='XenForo XML Phrase Translator by Goleks8',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples of use:
  python translator.py language.xml
  python translator.py language.xml -c custom_config.yml
  python translator.py language.xml --no-cdata
        '''
    )
    
    parser.add_argument(
        '-i','--input_file',
        help='Path to the XML file with phrases XenForo'
    )
    
    parser.add_argument(
        '--update-title',
        action='store_true',
        help='Change language title'
    )
    
    return parser.parse_args()

def update_language_title(root, new_title):
    root.set('title', new_title)
    print(f"✅ Language title changed to: {new_title}")



def main():
    print("=" * 60)
    print("🚀 XenForo XML Phrase Translator")
    print("👤 Author: Goleks8 (https://github.com/Goleks8)")
    print("=" * 60)
    
    args = parse_arguments()
    
    config = load_config()
    
    SOURCE_LANG      = config.get('source_lang', 'en')
    TARGET_LANG      = config.get('target_lang', 'ru')
    LANGUAGE_TITLE   = config.get('language_title', 'Russian (RU)')
    BATCH_SIZE       = config.get('batch_size', 20)
    SLEEP_SEC        = config.get('sleep_sec', 1.0)
    
    path = args.input_file
    if(path is None):
        path = input("📄Path to .xml: ")
    
    input_path = Path(path)
    output_path = Path(f"{input_path.stem}-{TARGET_LANG}{input_path.suffix}")
    
    print(f"\n📁 Input file: {input_path}")
    print(f"📁 Output file: {output_path}")
    print(f"🌐 Translation: {SOURCE_LANG} -> {TARGET_LANG}")
    print(f"📦 Batch size: {BATCH_SIZE}")
    print(f"⏱️ Pause: {SLEEP_SEC} сек")
    print("-" * 60)
    
    try:
        parser = etree.XMLParser(remove_blank_text=False, recover=True)
        tree = etree.parse(str(input_path), parser)
        root = tree.getroot()
        
        if args.update_title:
            update_language_title(root, LANGUAGE_TITLE)
        
        phrases = root.findall(".//phrase")
        total_phrases = len(phrases)
        
        if total_phrases == 0:
            print("⚠️ Phrases not found in XML file!")
            sys.exit(1)
        
        print(f"📊 Phrases found for translation: {total_phrases}")
        
        translated, failed = translate_phrases(
            phrases, SOURCE_LANG, TARGET_LANG, BATCH_SIZE, SLEEP_SEC
        )
        
        tree.write(
            str(output_path),
            encoding="utf-8",
            xml_declaration=True,
            pretty_print=True
        )
        
        print("\n" + "=" * 60)
        print("✅ Translation completed!")
        print(f"📊 Statistics:")
        print(f"   - Total phrases: {total_phrases}")
        print(f"   - Translated: {translated}")
        print(f"   - Errors: {failed}")
        print(f"📁 The result is saved: {output_path}")
        print("=" * 60)
        
    except etree.XMLSyntaxError as e:
        print(f"❌ Parsing error XML: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exit...")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
        sys.exit(1)
    input("Press Enter to exit...")