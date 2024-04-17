import os
import pandas as pd

def process_directory(directory):
    data = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    text = f.read()
                    sentiment = os.path.basename(root)
                    data.append({'phrase': text, 'target': sentiment})
    return data

# Procesar directorios de entrenamiento y prueba
train_data = process_directory('train')
test_data = process_directory('test')

# Convertir a DataFrames
train_df = pd.DataFrame(train_data)
test_df = pd.DataFrame(test_data)

# Guardar como archivos CSV
train_df.to_csv('train_dataset.csv', index=False)
test_df.to_csv('test_dataset.csv', index=False)


import os
import pandas as pd

def process_directory(directory):
    data = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    text = f.read()
                    sentiment = os.path.basename(os.path.dirname(os.path.join(root, file)))
                    data.append({'phrase': text, 'sentiment': sentiment})
    return data

# Procesar directorios de entrenamiento y prueba
train_data = process_directory('train')
test_data = process_directory('test')

# Convertir a DataFrames
train_df = pd.DataFrame(train_data)
test_df = pd.DataFrame(test_data)

# Guardar como archivos CSV
train_df.to_csv('train_dataset.csv', index=False)
test_df.to_csv('test_dataset.csv', index=False)