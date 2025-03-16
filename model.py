# %%
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# %%
# Load the dataset
data = pd.read_csv("data/ml_input.csv")

# %%
# Define the predictor features and target variable
features = ['npi', 'code', 'proc_hour']
target = 'true_oopsie_cost'

# %%
X = data[features]
y = data[target]

# %%
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# %%
# Preprocessor for categorical features using OneHotEncoder
categorical_transformer = OneHotEncoder(handle_unknown='ignore')

preprocessor = ColumnTransformer(
    transformers=[
        ('cat', categorical_transformer, features)
    ]
)

# %%
# Create a pipeline that first transforms the data and then fits the RandomForestRegressor
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(random_state=42))
])

# %%
# Define a parameter grid for hyperparameter tuning
param_grid = {
    'regressor__n_estimators': [100, 200, 300],
    'regressor__max_depth': [None, 10, 20, 30],
    'regressor__min_samples_split': [2, 5, 10],
    'regressor__min_samples_leaf': [1, 2, 4]
}

# %%
# Use GridSearchCV to find the best hyperparameters using 5-fold cross-validation
grid_search = GridSearchCV(
    pipeline, param_grid, cv=5,
    scoring='neg_mean_squared_error', n_jobs=-1, verbose=1
)

# %%
grid_search.fit(X_train, y_train)

print("Best parameters:", grid_search.best_params_)
print("Best CV score (negative MSE):", grid_search.best_score_)

# Retrieve the best model from grid search and evaluate on the test set
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Test Mean Squared Error: {mse:.2f}")
print(f"Test R^2 Score: {r2:.2f}")

# %%
