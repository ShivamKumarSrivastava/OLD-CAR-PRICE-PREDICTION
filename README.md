# 🚗 Used Car Price Prediction

A Machine Learning web application that predicts the resale price of used cars based on multiple vehicle features.

## 🔗 Project Links

- 🌐 **Live Demo:** [Click Here](https://old-car-price-prediction-f9pazd7jxc7exqgmsokqqv.streamlit.app/)
- 💻 **GitHub Repository:** [View Code](https://github.com/ShivamKumarSrivastava/OLD-CAR-PRICE-PREDICTION.git)
- 👨‍💼 **LinkedIn:** [Shivam Kumar](www.linkedin.com/in/shivam-srivastava-314153256)

---

This project includes complete ML workflow:

- Data Cleaning
- Feature Engineering
- Model Training
- Model Serialization
- Streamlit Deployment

---

📂 Project Structure

```
OLD-CAR-PRICE-PREDICTION/
│
├── Data/
│   └── Used_Car_Price_Prediction.csv
│
├── Model/
│   └── model.pkl
│
├── Notebook/
│   ├── EDA.ipynb
│   ├── Feature_Scaling.ipynb
│   ├── model.ipynb
│   ├── Cars.csv
│   ├── Final_Data.csv
│   ├── model_file_csv.csv
│   ├── make_model_dict.pkl
│   ├── model_mapping.pkl
│   └── model.pkl
│
├── Streamlit_App.py
├── requirements.txt
├── .gitignore
└── README.md

```

---

🧠 Problem Statement

Predict the selling price of a used car using machine learning techniques based on:

- Year of Manufacture
- Fuel Type
- Kilometers Driven
- Body Type
- Transmission
- Registered State
- Make (Company Name)
- Model
- Total Owners
- Car Rating
- Warranty Availability

---

⚙️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-Learn
- Joblib
- Streamlit
- Matplotlib (EDA)
- Seaborn (EDA)

---

🏗️ ML Pipeline

1️⃣ Exploratory Data Analysis (EDA.ipynb)
2️⃣ Feature Scaling & Encoding
3️⃣ Manual categorical mapping
4️⃣ Model training
5️⃣ Model evaluation
6️⃣ Model saved as .pkl file
7️⃣ Streamlit deployment

---

🎯 Streamlit Application Features

- Interactive user interface
- Dynamic Make → Model selection
- Manual categorical mapping
- Real-time price prediction
- Clean wide layout UI

---

🚀 How to Run Locally

```
git clone https://github.com/ShivamKumarSrivastava/OLD-CAR-PRICE-PREDICTION.git
cd OLD-CAR-PRICE-PREDICTION
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run Streamlit_App.py

```

---

📊 Model Output

The model predicts:
Estimated resale price of the car
Evaluation metrics can be found inside:
Notebook/model.ipynb

---

📈 Future Improvements

- Add XGBoost / Gradient Boosting
- Deploy on Streamlit Cloud
- Add interactive visual dashboard
- Add model comparison section
- Add API version using Flask

---

👨‍💻 Author

Shivam Kumar
Machine Learning & Data Science Enthusiast
India