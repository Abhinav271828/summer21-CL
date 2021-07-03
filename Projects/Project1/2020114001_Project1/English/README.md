# Computational Linguistics
## Summer 2021, IIIT Hyderabad
## Project 1 – Wordcloud Generation

## Running
The project scrapes the Internet for 10,000 sentences in English and generates

* frequency graphs of the top 20 most commonly occurring tokens at each stage of processing (tokenised raw data, cleaned data, tagged data, data without stopwords, stemmed data and lemmatised data)
* a wordcloud of the top 50 most commonly occurring words in the data without stopwords  

Please run the following commands before running the code:

    pip install re
    pip install requests
    pip install bs4
    pip install nltk
    
Please note that the `wordcloud` library is not available for Python 3.7 and above. If you are using these versions of Python, please run the following command:

    python3 graphs.py

In case your Python version is compatible with the library, you can run the following:
    
    pip install wordcloud
    python3 wordcloud.py

## Output
The codes intermittently print the status of the processing on the command line, at each stage.

Both codes generate the frequency graphs as popups. They can be saved to disk manually. Note that each one will pop up only after the previous one is closed; thus until the "Unprocessed Wordlist Frequencies" graph is closed, the "Cleaned Wordlist Frequencies" will not appear, and so on. Further, the wordcloud will not be generated until the last graph (lemmata) is closed.

`wordcloud.py` generates the wordcloud and stores it as `cloud.png` in the same directory.
Both `wordcloud.py` and `graphs.py` write the 50 most common lemmata, along with their frequencies, into a file `mostcommon.txt` in the same directory.
