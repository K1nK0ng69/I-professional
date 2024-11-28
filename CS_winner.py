import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

train_file_path = r'C:\Users\Ivan\Downloads\train.csv'
test_file_path = r'C:\Users\Ivan\Downloads\test.csv'
output_file_path = r'C:\Users\Ivan\Downloads\SampleSubmission.csv'

train_data = pd.read_csv(train_file_path)
test_data = pd.read_csv(test_file_path)

if 'roundNum' not in test_data.columns:
    raise ValueError("Столбец 'roundNum' отсутствует в тестовых данных!")

combined_data = pd.concat([train_data, test_data], axis=0)

categorical_columns = ['mapName', 'ctTeam', 'tTeam', 'ctBuyType', 'tBuyType']

for column in categorical_columns:
    label_encoder = LabelEncoder()
    combined_data[column] = label_encoder.fit_transform(combined_data[column])

train_data = combined_data.iloc[:len(train_data)].copy()
test_data = combined_data.iloc[len(train_data):].copy()

X_train = train_data.drop(columns=['winnerSide', 'roundNum'])
y_train = train_data['winnerSide']
X_test = test_data.drop(columns=['winnerSide', 'roundNum'], errors='ignore')

if X_test.empty:
    raise ValueError("Тестовый набор данных пустой или обработан некорректно!")

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)

if 'roundNum' not in test_data.columns:
    raise ValueError("Столбец 'roundNum' отсутствует в тестовых данных после обработки!")

output = pd.DataFrame({'winnerSide': predictions.astype(int)})
output.to_csv(output_file_path, index=False)

print(f"Результаты сохранены в файл: {output_file_path}")
