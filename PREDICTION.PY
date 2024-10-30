import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset to inspect its structure and preview the data
file_path = 'HousingData.csv'
data = pd.read_csv(file_path)

# Display basic information and the first few rows
data_info = data.info()
data_head = data.head()

#print(data_info, data_head)
# Filling missing values with the mean of each column
data_filled = data.fillna(data.mean())

# Verify if all missing values are handled
missing_values = data_filled.isnull().sum()

print(missing_values)
# Define feature variables (all columns except 'MEDV') and target variable ('MEDV')
X = data_filled.drop(columns='MEDV')
y = data_filled['MEDV']

# Split the data into 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Linear Regression model
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = linear_model.predict(X_test)

# Evaluate the model using MSE and R² score
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("mean squared error:" + str(mse))
print("r2:" + str(r2))