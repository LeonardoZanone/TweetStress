from common import tweet_cleaning_for_sentiment_analysis
from fasttext import FastText as fastText

import os.path
import csv
import nltk
nltk.download('punkt')


training_data_path = './TrainingDatasets/Train3Classes.csv'
training_data_path = './TrainingDatasets/Train500.csv'
prepared_data = 'dataset.txt'
test_data_path = './TestDatasets/Test3classes.csv'
prepared_test = 'test_data.txt'
model_path = './'
model_name = 'tweet_model'
sentiments = {'0': 'NEGATIVE', '1': 'POSITIVE', '2': 'NEUTRAL'}

def prepera_data(file, out_file):
    with open(out_file, 'a') as csvoutfile:
        csv_writer = csv.writer(csvoutfile, delimiter=' ', lineterminator='\n')
        with open(file, 'r', newline='') as csvinfile: #,encoding='latin1'
            dataset = []
            csv_reader = csv.reader(csvinfile, delimiter=';', quotechar='"')
            for row in csv_reader:
                if row[3] in ['0', '1', '2']:
                    text = clean_and_prepare_text(row[1], row[3])
                    csv_writer.writerow(text)

def clean_and_prepare_text(text, sentiment):
    output = []
    label = "__label__" + sentiments[sentiment]
    output.append(label)
    #Clean tweet and tokenize it
    output.extend( nltk.word_tokenize(tweet_cleaning_for_sentiment_analysis(text.lower())))
    return output

def train():
    try:
        if not os.path.isfile(prepared_data):
            prepera_data(training_data_path, prepared_data)
        if not os.path.isfile(prepared_test):
            prepera_data(test_data_path, prepared_test)

        hyper_params = {"lr": 0.01,
            "epoch": 20,
            "wordNgrams": 2,
            "dim": 20}     

        # Train the model.
        model = fastText.train_supervised(input=prepared_data, **hyper_params)
        print("Model trained with the hyperparameter \n {}".format(hyper_params))

        # CHECK PERFORMANCE
        result = model.test(prepared_test)
        # DISPLAY ACCURACY OF TRAINED MODEL
        text_line = str(hyper_params) + ",accuracy:" + str(result[1]) + '\n' 
        print(text_line)

        model.save_model(os.path.join(model_path,model_name + ".ftz"))
    except Exception as ex:
        print('Exception' + str(ex))

train()