from os import listdir
from os.path import isfile, join
from shutil import move

import csv
import os
import uuid
import re
import emoji
import itertools
from bs4 import BeautifulSoup

def get_files_paths(folder_path):
    """
    Search for the files inside a folder_path
    """
    return [f for f in listdir(folder_path) if isfile(join(folder_path, f))]

def move_file(current_path, new_path):
    """
    Move files accross folders
    """
    move(current_path, new_path)

def generate_file_name(extension=None):
    """
    Generates a file name with the given extension
    """
    name = str(uuid.uuid4())
    if extension:
        name += f".{extension}"
    return name

def write_csv(lines, file_path, field_names):
    """
    Receives a list of dictionaries, the file_path (with the file name)
    and the field names to gene generates a csv.
    """
    if not lines:
        raise Exception("No lines")
    with open(file_path, 'w', encoding='utf8', newline='') as f:
        fc = csv.DictWriter(f, fieldnames=field_names)
        fc.writerows(lines)

def read_csv(file_path, field_names):
    """
    Reads the csv file and returns a dict list
    """
    with open(file_path, "r") as f:
        lines = []
        for line in csv.DictReader(f, fieldnames=field_names):
            lines.append(line)
        return lines

def get_current_folder_path():
    """
    Returns the full path of the current folder
    """
    return os.getcwd()


def load_dict_smileys():
    return {
        ":‑)":"sorriso",
        ":-]":"sorriso",
        ":-3":"sorriso",
        ":->":"sorriso",
        "8-)":"sorriso",
        ":-}":"sorriso",
        ":)":"sorriso",
        ":]":"sorriso",
        ":3":"sorriso",
        ":>":"sorriso",
        "8)":"sorriso",
        ":}":"sorriso",
        ":o)":"sorriso",
        ":c)":"sorriso",
        ":^)":"sorriso",
        "=]":"sorriso",
        "=)":"sorriso",
        ":-))":"sorriso",
        ":‑D":"sorriso",
        "8‑D":"sorriso",
        "x‑D":"sorriso",
        "X‑D":"sorriso",
        ":D":"sorriso",
        "8D":"sorriso",
        "xD":"sorriso",
        "XD":"sorriso",
        ":‑(":"triste",
        ":‑c":"triste",
        ":‑<":"triste",
        ":‑[":"triste",
        ":(":"triste",
        ":c":"triste",
        ":<":"triste",
        ":[":"triste",
        ":-||":"triste",
        ">:[":"triste",
        ":{":"triste",
        ":@":"triste",
        ">:(":"triste",
        ":'‑(":"triste",
        ":'(":"triste",
        ":‑P":"divertido",
        "X‑P":"divertido",
        "x‑p":"divertido",
        ":‑p":"divertido",
        ":‑Þ":"divertido",
        ":‑þ":"divertido",
        ":‑b":"divertido",
        ":P":"divertido",
        "XP":"divertido",
        "xp":"divertido",
        ":p":"divertido",
        ":Þ":"divertido",
        ":þ":"divertido",
        ":b":"divertido",
        "<3":"amor"
        }

def tweet_cleaning_for_sentiment_analysis(tweet):
    
    #Escaping HTML characters
    tweet = BeautifulSoup(tweet, features="html.parser").get_text()
   
    #Special case not handled previously.
    tweet = tweet.replace('\x92',"'")
    
    #Removal of hastags/account
    tweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|(#[A-Za-z0-9]+)", " ", tweet).split())
    
    #Removal of address
    tweet = ' '.join(re.sub("(\w+:\/\/\S+)", " ", tweet).split())
    
    #Lower case
    tweet = tweet.lower()
    
    # Standardizing words
    tweet = ''.join(''.join(s)[:2] for _, s in itertools.groupby(tweet))
    
    #Deal with emoticons source: https://en.wikipedia.org/wiki/List_of_emoticons
    SMILEY = load_dict_smileys()  
    words = tweet.split()
    reformed = [SMILEY[word] if word in SMILEY else word for word in words]
    tweet = " ".join(reformed)
    
    #Deal with emojis
    tweet = emoji.demojize(tweet)

    #Removal of Punctuation
    tweet = ' '.join(re.sub("[\.\,\!\?\:\;\-\=]", " ", tweet).split())

    tweet = tweet.replace(":"," ")
    tweet = ' '.join(tweet.split())

    return tweet

def create_folder_structure(path):
    """
    Create a folder structure
    """
    if not os.path.isdir(path):
        os.makedirs(path)

def get_twitter_api():
    import twitter
    api = twitter.Api(consumer_key=,
                  consumer_secret=,
                  access_token_key=,
                  access_token_secret=)
    return api

BRAZILIAN_STATES =  [
        {
            "name": "Acre",
            "twitter_id": "3c42576594e748ff", 
            "since_id": "1259633531598356482" 
        },
        {
            "name": "Alagoas",
            "twitter_id": "35caf3cf30eba1ad", 
            "since_id": "1259633531598356482" 
        },
        {
            "name": "Amapá",
            "twitter_id": "72c1b85a11f23685", 
            "since_id": "1259633531598356482" 
        },
        {
            "name": "Amazonas",
            "twitter_id": "049e74831110e731", 
            "since_id": "1259633531598356482" 
        },
        {
            "name": "Bahia",
            "twitter_id": "8ee88bd36514f636", 
            "since_id": "1259633531598356482" 
        },
        {
            "name": "Ceará",
            "twitter_id": "7a0985d843b92380", 
            "since_id": "1259633531598356482" 
        },
        {
            "name": "Distrito Federal",
            "twitter_id": "23bf863bd278c0e4", 
            "since_id": "1259633531598356482" 
        },
        {
            "name": "Espírito Santo",
            "twitter_id": "ca1ac90b0cff479a", 
            "since_id": "1259633531598356482" 
        },
        {
            "name": "Goiás",
            "twitter_id": "c42167e3bba1e99d", 
            "since_id": "1259633531598356482" 
        },
        {
            "name": "Maranhão",
            "twitter_id": "d9e7a568db83d7e6", 
            "since_id": "1259633531598356482" 
        },
        {
            "name": "Mato Grosso",
            "twitter_id": "31c646c9d2b0efbb", 
            "since_id": "1259633531598356482" 
        },
        {
            "name": "Mato Grosso do Sul",
            "twitter_id": "292dedf68951e239", 
            "since_id": "1259633531598356482" 
        },
        {
            "name": "Minas Gerais",
            "twitter_id": "ce0385aee84dbdf9", 
            "since_id": "1259633531598356482" 
        },
        {
            "name": "Pará",
            "twitter_id": "f2e8609f44d80bc7", 
            "since_id": "1259633531598356482" 
        },
        {
            "name": "Paraíba",
            "twitter_id": "b9999f7f6f548ce7", 
            "since_id": "1259633531598356482" 
        },
        {
            "name": "Paraná",
            "twitter_id": "c0d0b98719f1c884", 
            "since_id": "1259633531598356482" 
        },
        {
            "name": "Pernambuco",
            "twitter_id": "6f6c3cc945b95a32", 
            "since_id": "1259633531598356482" 
        },
        {
            "name": "Piauí",
            "twitter_id": "6a8eb83785196df9", 
            "since_id": "1259633531598356482" 
        },
        {
            "name": "Rio de Janeiro",
            "twitter_id": "e433fbca595f29e5", 
            "since_id": "1259633531598356482" 
        },
        {
            "name": "Rio Grande do Norte",
            "twitter_id": "d219658b53f37d2d", 
            "since_id": "1259633531598356482" 
        },
        {
            "name": "Rio Grande do Sul",
            "twitter_id": "a4b227ce2060cf5e", 
            "since_id": "1259633531598356482" 
        },
        {
            "name": "Rondônia",
            "twitter_id": "074042a860d58d75", 
            "since_id": "1259633531598356482" 
        },
        {
            "name": "Roraima",
            "twitter_id": "dcfd7d224dcf9668", 
            "since_id": "1259633531598356482" 
        },
        {
            "name": "Santa Catarina",
            "twitter_id": "f82af1e2ebdb0f2e", 
            "since_id": "1259633531598356482" 
        },
        {
            "name": "São Paulo",
            "twitter_id": "8cd72e7876a6c73d", 
            "since_id": "1259633531598356482" 
        },
        {
            "name": "Sergipe",
            "twitter_id": "ec32cf627c142984", 
            "since_id": "1259633531598356482" 
        },
        {
            "name": "Tocantins",
            "twitter_id": "9c0db54ac37eb12e",
            "since_id": "1259633531598356482"
        }
    ]