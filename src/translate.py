import sys
import time

from deep_translator import GoogleTranslator
import requests
from tqdm import tqdm
from lxml import etree
from urllib3 import HTTPSConnectionPool



def chunks(lst, size):
    for i in range(0, len(lst), size):
        yield lst[i:i + size]


def translate_phrases(phrases, source_lang, target_lang, batch_size, sleep_sec):
    total_phrases = len(phrases)
    translated_count = 0
    failed_batches = 0
    
    try:
        translator = GoogleTranslator(source=source_lang, target=target_lang)
    except Exception as e:
        print(f"❌ Translator initialization error: {e}")
        sys.exit(1)
    
    with tqdm(total=total_phrases, desc="Translation of phrases", unit="phrase") as pbar:
        for batch in chunks(phrases, batch_size):
            texts = [p.text.strip() if p.text else "" for p in batch]
            
            # protect for lost '}'
            texts_for_translation = []
            for text in texts:
                text = text.replace('{', '[[$').replace('}', '$]]')
                texts_for_translation.append(text)
            
            # Skip
            if not any(texts):
                for phrase in batch:
                    pbar.update(1)
                continue
            
            try:
                while True: # BAD
                    try:
                        translated = translator.translate_batch(texts)
                        break
                    except requests.exceptions.ConnectionError:
                        print("Connection error. Try again in 5 seconds. (CNTR + C for Exit)")
                        time.sleep(5)
                        
                time.sleep(sleep_sec)
                
                texts_translation = []
                for text in translated:
                    text = text.replace('[[&', '{').replace('$]]', '}')
                    texts_translation.append(text)
                    
                for phrase, t_text in zip(batch, texts_translation):
                    if t_text:  # Checking that the translation is not empty
                        phrase.text = etree.CDATA(t_text)
                    pbar.update(1)
                
                translated_count += len(batch)
                
            except Exception as e:
                failed_batches += 1
                tqdm.write(f"⚠️ Batch translation error: {e}")
                time.sleep(5)  # Pause on error
                
                # skip phrases in the erroneous batch
                for _ in batch:
                    pbar.update(1)
                continue
    
    return translated_count, failed_batches