#!/usr/bin/env python3
"""
Simple NLTK Setup Script
Run this to download required NLTK data
"""

import ssl

# Handle SSL certificate issues
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# Import NLTK
import nltk

def download_nltk_data():
    """Download required NLTK datasets"""
    
    datasets = ['punkt', 'stopwords', 'wordnet', 'omw-1.4']
    
    print("Downloading NLTK data...")
    
    for dataset in datasets:
        try:
            print(f"Downloading {dataset}...")
            nltk.download(dataset)
            print(f"✓ {dataset} downloaded successfully")
        except Exception as e:
            print(f"✗ Failed to download {dataset}: {e}")
    
    print("\nTesting NLTK imports...")
    
    try:
        from nltk.tokenize import sent_tokenize, word_tokenize
        from nltk.corpus import stopwords
        from nltk.stem import WordNetLemmatizer
        
        # Test functionality
        test_text = "Hello world. This is a test."
        sentences = sent_tokenize(test_text)
        words = word_tokenize(test_text)
        stop_words = stopwords.words('english')
        lemmatizer = WordNetLemmatizer()
        
        print("✓ All NLTK functions working!")
        print(f"  Sentences: {sentences}")
        print(f"  Words: {words[:5]}...")
        print(f"  Stop words count: {len(stop_words)}")
        
    except Exception as e:
        print(f"✗ NLTK test failed: {e}")

if __name__ == "__main__":
    download_nltk_data()