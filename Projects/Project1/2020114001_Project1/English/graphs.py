import re
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import pos_tag
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer

nltk.download('punkt')
nltk.download('words')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
nltk.download('wordnet')

eng_words = set(nltk.corpus.words.words())
eng_stopwords = set(nltk.corpus.stopwords.words('english'))

def crawl(url):
    res = requests.get(url)
    html_page = res.content

    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.find_all(text=True)

    output = ''
    extractlist = ['p','h2','em','i','strong']

    for t in text:
        if t.parent.name in extractlist:
            output += " " + format(t)
    
    output = re.sub(r'\s+', " ", output.replace("\n"," ").replace('`', "'")).replace('``',"\"")
    
    return output


def next_crawl(url,n):
           
    output = crawl(url)
    
    res = requests.get(url)
    html_page = res.text
    soup = BeautifulSoup(html_page, 'html.parser')
    
    urls = []
    
    for s in soup.find_all("p"):
        for t in s.find_all("a",href=True,src=False):
            link = t.get('href')
            
            if len(link) > 0 and link[0] == '/':
                link = url + link
            elif link[-4:] == 'html':
                link = url[0:-n] + link

            if link not in urls and link[:4] == 'http':
               #print("link " + link)
               urls.append(link)
    
    for link in urls:
        output += " " + crawl(link)
        
    return output

### Crawling ###
print("Scraping \"Alice in Wonderland\"")
url_alice = "https://www.cs.cmu.edu/~rgs/alice-table.html"
raw_alice = next_crawl(url_alice,16)
sentences_alice = sent_tokenize(raw_alice)[2:] #1541 sentences
print("Done")

print("Scraping \"Jungle Book\"")
url_jungle = "https://www.cs.cmu.edu/~rgs/jngl-table.html"
raw_jungle = next_crawl(url_jungle,15)
sentences_jungle = sent_tokenize(raw_jungle)[1:] #2980 sentences
print("Done")

print("Scraping \"The Wizard of Oz\"")
url_oz = "https://www.cs.cmu.edu/~rgs/wizoz10.html"
raw_oz = next_crawl(url_oz,12)
sentences_oz = sent_tokenize(raw_oz)[6:] #2245 sentences
print("Done")

print("Scraping \"The Adventures of Tom Sawyer\"")
url_tom = "https://www.cs.cmu.edu/~rgs/sawyr-table.html"
raw_tom = next_crawl(url_tom,16)
sent = sent_tokenize(raw_tom)
sentences_tom = [sent[0][158:]] + sent[1:] #4885 sentences
print("Done")

sentences = sentences_alice + sentences_jungle + sentences_tom + sentences_oz #11651 sentences
raw = " ".join(sentences)
### Now a list of sentences is obtained. ###

### File Writing and Reading ###
with open('raw.txt','w') as r:
    print(raw, file=r)

filename = input("Enter name of file with raw data: ")
with open(filename,'r') as rawfile:
    raw = rawfile.read()
### The raw data is now ready to be processed. ###

print("Raw data ready")

### Word tokenisation ###
words = word_tokenize(raw)
sentences = sent_tokenize(raw)
### Now a list of sentences and a list of words are obtained. The wordlist is to be cleaned. ###

print("Data tokenised")

### Cleaning ###
cleaned_words = [w.lower() for w in words if w.lower() in eng_words] # words with punctuation etc removed
### Now we have a list of words without punctuation, abbreviation, symbols or foreign words. ###

print("Data cleaned")

### Removing Stopwords ###
unstop_words = [w for w in cleaned_words if not w in eng_stopwords]
### Now we have a list without stopwords ###

print("Stopwords removed")

### POS Tagging ###
tagged_raw = nltk.pos_tag(words)
tagged_unstop = [(word,tag) for word,tag in tagged_raw if not word in eng_stopwords]
### Now the wordlist is tagged. ###

print("Data tagged")

### Stemming and Lemmatisation ###
stems = [PorterStemmer().stem(word) for word in unstop_words]
lemmata = [WordNetLemmatizer().lemmatize(word,tag[0].lower()) for (word,tag) in tagged_unstop if tag[0] in ['A','N','R','V']]
### Now we have a list of stems and lemmata. ###

print("Data stemmed and lemmatised")

fd_words = nltk.FreqDist(words)
fd_words.plot(20, title="Unprocessed Wordlist Frequencies")

fd_cleaned = nltk.FreqDist(cleaned_words)
fd_cleaned.plot(20, title="Cleaned Wordlist Frequencies")

fd_unstop = nltk.FreqDist(unstop_words)
fd_unstop.plot(20, title="Unstop Wordlist Frequences")

fd_tags_raw = nltk.FreqDist(pair[1] for pair in tagged_raw)
fd_tags_raw.plot(20, title="Raw Taglist Frequencies")

fd_tags_unstop = nltk.FreqDist(pair[1] for pair in tagged_unstop)
fd_tags_unstop.plot(20, title="Unstop Taglist Frequencies")

fd_stems = nltk.FreqDist(stems)
fd_stems.plot(20, title="Stem Frequencies")

fd_lemmata = nltk.FreqDist(lemmata)
fd_lemmata.plot(20, title="Lemmata Frequencies")

with open('mostcommon.txt','w') as m:
    for w,f in fd_lemmata.most_common(50):
        print(w + ' - ' + str(f), file=m)
