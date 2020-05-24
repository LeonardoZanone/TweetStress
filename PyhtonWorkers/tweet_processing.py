from common import get_current_folder_path, generate_file_name, write_csv, move_file, get_twitter_api, BRAZILIAN_STATES
from constants import PROCESSED_FILES, RAW_FILES, WRITING_FILES
import time

from datetime import datetime

import sys, traceback

since_id = ""

def get_twitter_data():
    api = get_twitter_api()
    data = []

    for state in BRAZILIAN_STATES:
        query = f"q=place%3A{state['twitter_id']}&since_id={state['since_id']}&count=100"
        
        result = api.GetSearch(raw_query=query)

        for tweet in result:
            value = {
                "region": state["name"],
                "tweet": tweet.AsDict()["text"]
            }
            data.append(value)
        state["since_id"] = result[-1].AsDict()["id_str"]

    return data

def write_twitter_data(data):
    file_name = generate_file_name(extension="csv")
    file_path = f"{get_current_folder_path()}/{WRITING_FILES}/{file_name}"
    write_csv(data, file_path, ("region", "tweet"))
    return file_name

def move_twitter_file(file_name):
    current_path = f"{get_current_folder_path()}/{WRITING_FILES}/{file_name}"
    new_path = f"{get_current_folder_path()}/{RAW_FILES}/{file_name}"
    move_file(current_path, new_path)

def main():
    print("Processing tweets!")
    while True:
        try:
            data = get_twitter_data()
            file_name = write_twitter_data(data)
            move_twitter_file(file_name)
            print("Proccessed with success")
        except Exception:
            with open("errors.txt", "a") as f:
                traceback.print_exc(file=f)
                f.writelines("\n------------------NEW ERROR------------------\n")
            print("Error")
        finally:
            print("Sleeping")
            minutes = 1
            time.sleep(minutes*60)
            print("Proccessing again")

if __name__ == '__main__':
    main()