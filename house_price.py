import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("house_data.csv")

X = data[['sqft', 'bedrooms', 'bathrooms']]
y = data['price']

# Split data into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction Function
def predict_price():
    sqft = int(input("Enter Square Foot: "))
    bed = int(input("Enter Bedrooms: "))
    bath = int(input("Enter Bathrooms: "))

    predicted = model.predict([[sqft, bed, bath]])
    print("\n🏠 Estimated House Price = ₹", int(predicted[0]))

# Run Program
print("HOUSE PRICE PREDICTION SYSTEM")
predict_price()
