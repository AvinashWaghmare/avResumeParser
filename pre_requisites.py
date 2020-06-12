import os
import nltk

# Install SpaCy Dependencies
os.system('python -m SpaCy download en_core_web_sm')


nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
