import os
import pandas as pd

# Función para leer los archivos y crear un DataFrame
def create_dataset(directory):
    data = []
    for sentiment in os.listdir(directory):
        sentiment_path = os.path.join(directory, sentiment)
        if os.path.isdir(sentiment_path):
            for filename in os.listdir(sentiment_path):
                file_path = os.path.join(sentiment_path, filename)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                    try:
                        phrase = file.read().strip()
                        data.append({'phrase': phrase, 'sentiment': sentiment})
                    except Exception as e:
                        print(f"Error reading file '{file_path}': {e}")
    return pd.DataFrame(data)

# Crear los DataFrames para el conjunto de entrenamiento y prueba
train_df = create_dataset('data/train')
test_df = create_dataset('data/test')

# Guardar los DataFrames como archivos CSV
train_df.to_csv('train_dataset.csv', index=False)
test_df.to_csv('test_dataset.csv', index=False)