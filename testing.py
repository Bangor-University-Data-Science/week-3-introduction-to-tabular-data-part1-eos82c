import pandas as pd

mock_df = pd.DataFrame(data={
    'Sex': ['male', 'female', 'female', 'male'],
    'Embarked': ['S', 'C', 'S', 'Q']
})
categorical_features = mock_df.columns.tolist()

unique_values = {}
for i in categorical_features:
    unique_values[i] = mock_df[i].unique().tolist()

print(unique_values)