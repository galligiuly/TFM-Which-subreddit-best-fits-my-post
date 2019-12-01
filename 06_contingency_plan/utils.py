
# Whit text_processing we can decide to call the functios:
## clean_text (only basical cleaning)
## pre_process (only tokenization and stopwords)
## text_process (cleaning, tokenization and stopwords)

# needed downloads
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.lang.en import English
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords

import re

parser = English()
stemmer = SnowballStemmer(language='english')



# Cleaning the text
## remove urls
def remove_urls(text):
    clean = re.compile(r'http\S+')
    return re.sub(clean, '', str(text))

## remove line endings
def remove_line_endings (text):
    clean = re.compile(r'\n')
    return re.sub(clean, '', str(text))

## remove symbols
def remove_symbols (text):
    clean = re.compile(r"[^a-zA-Z0-9' ]") 
    return re.sub(clean, '', str(text))

def clean_text(text):
    return remove_urls(remove_line_endings(remove_symbols(text.lower())))

# Tokenization and stemming
## tokenization
def tokenize(text):
    return parser(text)

## stopwords
def remove_stopwords(tokenized):
    without_stopwords = []
    from spacy.lang.en.stop_words import STOP_WORDS
    from spacy.lang.en import English
    for token in tokenized:
        if token.text not in STOP_WORDS:
            without_stopwords.append(token.text)
    return without_stopwords

## stemming
def stem(words):
    stemmed_words = []
    for word in words:
        stemmed_words.append(stemmer.stem(word))
    return stemmed_words

def pre_process (text):
    return stem(remove_stopwords(tokenize(text)))


## Text processing
def text_process (text):
    return pre_process(clean_text(text))


# cleaning text for keras model
REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
STOPWORDS = set(stopwords.words('english'))

def clean_text_keras(text):
    """
        text: a string
        
        return: modified initial string
    """
    text = text.lower()
    text = REPLACE_BY_SPACE_RE.sub(' ', text)
    text = BAD_SYMBOLS_RE.sub('', text)
    # tring to remove double white spaces...
    #    text = re.sub(r'\W+', '', text)
    text = text.replace('x', '')
    text = ' '.join(word for word in text.split() if word not in STOPWORDS)
    return text




# Dictionary of Subreddits names whit the corresponding label encoded
## dict for labels
def label_encoder(subreddit_name):
    dict_labels = {
        "Fitness":0,
        "IAmA":1,
        "atheism":2,
        "aww":3,
        "europe":4,
        "funny":5,
        "gaming":6,
        "movies":7,
        "nba":8,
        "politics":9,
        "science":10,
        "technology":11,
        "todayilearned":12,
        "worldnews":13,
    }
    
    return dict_labels[subreddit_name]

# Dictionary of Subreddits names whit the corresponding label encoded
## dict for labels
def label_decoder(subreddit_id):
    dict_labels = {
        0:"Fitness",
        1:"atheism",
        2:"aww",
        3:"europe",
        4:"gaming",
        5:"movies",
        6:"nba",
        7:"politics",
        8:"science",
        9:"technology"
    }
    
    return dict_labels[subreddit_id]