

# Delhi House Price Prediction Model

This project is a **Delhi House Price Prediction** tool built using a **Linear Regression** model. It takes various input features like the number of BHKs, bathrooms, area, parking, etc., and predicts the price of a house in Delhi. The model is deployed as a web application using **Flask**.

## Features

- Predicts house prices based on input features:
  - Number of BHKs (Bedrooms, Hall, Kitchen)
  - Number of bathrooms
  - Area of the house (in square feet)
  - Parking spaces
  - Other important factors
- Simple and user-friendly web interface.
- Powered by a Linear Regression model.

## Tech Stack

- **Python**: Core programming language.
- **Pandas & NumPy**: For data handling and preprocessing.
- **Scikit-learn**: For building and training the Linear Regression model.
- **Flask**: For creating the web application.
- **HTML/CSS**: For front-end UI.

## Model Training

1. The dataset used for training the Linear Regression model includes features such as:
   - Number of BHKs
   - Bathrooms
   - Area in square feet
   - Parking spaces
   - Location data, etc.

2. The model is trained using **Scikit-learn's Linear Regression** algorithm. The training dataset is preprocessed to handle missing values, scale the features, and encode categorical data.

## How It Works

1. **Input Form**: The user enters details like BHK, area, bathrooms, and parking spaces into the form.
2. **Prediction**: Once the user submits the form, the input is processed and fed into the trained Linear Regression model.
3. **Output**: The predicted house price is displayed on the webpage.

## Future Enhancements

- Integrate more features to improve model accuracy, such as:
  - Nearby amenities (schools, hospitals, etc.)
  - Age of the property
  - Distance from key landmarks
- Implement an API endpoint for the prediction model.
- Add data visualizations to the web interface.
