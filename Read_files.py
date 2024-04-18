import glob
import pandas as pd

def process_files_in_folder(folder_path):
    data = []
    filenames = glob.glob(folder_path + "/*.txt")
    for filename in filenames:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            sentiment = folder_path.split('/')[-1]
            data.append({'phrase': text, 'sentiment': sentiment})
    return data

def create_dataset(folder_root, output_filename):
    folder_list = ["negative", "neutral", "positive"]
    all_data = []
    for folder in folder_list:
        folder_path = f"{folder_root}/{folder}"
        folder_data = process_files_in_folder(folder_path)
        all_data.extend(folder_data)
    
    df = pd.DataFrame(all_data)
    df.to_csv(output_filename, index=False)

def generate_train_and_test_datasets():
    create_dataset("data/train", "train_dataset.csv")
    create_dataset("data/test", "test_dataset.csv")

generate_train_and_test_datasets()