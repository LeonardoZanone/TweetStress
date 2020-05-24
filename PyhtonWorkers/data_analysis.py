from common import read_csv, get_files_paths, get_current_folder_path, move_file, tweet_cleaning_for_sentiment_analysis
from constants import RAW_FILES, PROCESSED_FILES, MODEL_PATH, FINAL_FILE, API

import fasttext
import time
import requests

def fix_strings(region):
    fixes = {
        "Amapa": "Amapá",
        "Destrito Federal": "Distrito Federal",
        "Espirito Santo": "Espírito Santo",
        "Mato Grosso so Sul": "Mato Grosso do Sul",
    }

    return fixes.get(region, region)

def store_result(region, sentiment):
    region = fix_strings(region)
    data = {"Estado": region, "Sentimento": sentiment}
    _ = requests.put(url=API, params=data)

def predict_sentiment(tweet):
    try:
        tweet = tweet_cleaning_for_sentiment_analysis(tweet)
        model = fasttext.load_model(MODEL_PATH)
        predict = model.predict(tweet)
        return predict[0][0].replace('__label__', '')
    except Exception as e:
        print(f"Error: {str(e)}")
        return 'NEUTRAL'


def get_sentiments_from_csv():
    return read_csv(f"{FINAL_FILE}/final_file.csv", ("region", "positive", "neutral", "negative"))

def processing_data(data):
    for line in data:
        sentiment = predict_sentiment(line['tweet'])
        store_result(line["region"], sentiment)

def move_twitter_file(file_name):
    current_path = f"{get_current_folder_path()}/{RAW_FILES}/{file_name}"
    new_path = f"{get_current_folder_path()}/{PROCESSED_FILES}/{file_name}"
    move_file(current_path, new_path)

def main():
    print("Processing files!")
    while True:
        try:
            file_names = get_files_paths(f"{get_current_folder_path()}/{RAW_FILES}")
            for file_name in file_names:
                path = f"{get_current_folder_path()}/{RAW_FILES}/{file_name}"
                data = read_csv(path, ("region", "tweet"))
                processing_data(data)
                move_twitter_file(file_name)
                print(f"processed: {file_name}")
        except Exception as e:
            print(f"Error: {str(e)}")
            raise e
        finally:
            print("Sleeping")
            minutes = 1
            time.sleep(minutes*60)
            print("Proccessing again")

if __name__ == "__main__":
    main()
