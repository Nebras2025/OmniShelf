from flask import Flask, render_template, request
import joblib
import pandas as pd
from sqlalchemy import create_engine

app = Flask(__name__)

# 1. Load the ML assets (Make sure these files are in the SAME folder as app.py)
try:
    model = joblib.load("knn_model.pkl")
    scaler = joblib.load("scaler.pkl")
    print("✅ Model and Scaler loaded successfully!")
except Exception as e:
    print(f"❌ Error loading assets: {e}")

# 2. Database Connection
engine = create_engine("sqlite:///book2.db")

# Pull only relevant data from SQLite
all_books = pd.read_sql("SELECT book_name, Price, Rating FROM book2", engine)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    try:
        # Get input from form
        u_price = float(request.form.get("price"))
        u_rating = float(request.form.get("rating"))

        # Prepare and Scale input
        user_data = pd.DataFrame([[u_price, u_rating]], columns=['Price', 'Rating_in_number'])
        user_scaled = scaler.transform(user_data)

        # Find Neighbors
        distances, indices = model.kneighbors(user_scaled, n_neighbors=5)

   
        
        results = []
        for i in indices[0]:
            results.append(all_books.iloc[i].to_dict())

        return render_template("index.html", results=results)
    
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    app.run(debug=True)
