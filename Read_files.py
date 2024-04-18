import glob
import pandas as pd

def process_directory(directory):
    data = []
    for file_path in glob.glob(directory + '/**/*.txt', recursive=True):
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
            sentiment = file_path.split('/')[-2]
            data.append({'phrase': text, 'sentiment': sentiment})
    return data

# Procesar directorios de entrenamiento y prueba
train_data = process_directory('train')
test_data = process_directory('test')

# Convertir a DataFrames
train_df = pd.DataFrame(train_data)
test_df = pd.DataFrame(test_data)

# Renombrar la columna 'sentiment' a 'target'
train_df.rename(columns={'sentiment': 'target'}, inplace=True)
test_df.rename(columns={'sentiment': 'target'}, inplace=True)

# Guardar como archivos CSV
train_df.to_csv('train_dataset.csv', index=False)
test_df.to_csv('test_dataset.csv', index=False)