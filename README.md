# KNNmovie-reccomedation-system
# 🎬 Movie Recommendation System

A **Movie Recommendation System** built using **Natural Language Processing (NLP)** and **Machine Learning** that suggests similar movies based on the movie summary.
The application is developed with **Python, Scikit-learn, and Streamlit** and provides an interactive web interface for users to discover recommended movies.

---

## 🚀 Project Overview

This project analyzes movie descriptions using **TF-IDF Vectorization** and finds similar movies using the **K-Nearest Neighbors (KNN)** algorithm.

Users can simply enter a movie name, and the system will recommend similar movies along with their ratings and release year.

---

## ✨ Features

* 🎬 Movie Recommendation based on **NLP**
* 🔎 Search movies by name
* ⭐ Display movie **ratings and release year**
* 🖼️ Option to show **movie posters**
* 📊 Data preprocessing and visualization
* 🌐 Interactive **Streamlit web application**

---

## 🧠 Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Streamlit**
* **Matplotlib**
* **TF-IDF Vectorizer**
* **K-Nearest Neighbors (KNN)**

---

## 📂 Project Structure

```
Movie-Recommendation-System
│
├── app.py
├── movies.csv
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit app

```bash
streamlit run app.py
```

Then open the browser and go to:

```
http://localhost:8501
```

---

## 📊 How It Works

1. The dataset containing movie information is loaded.
2. Movie summaries are preprocessed and cleaned.
3. **TF-IDF Vectorization** converts text data into numerical vectors.
4. **K-Nearest Neighbors (KNN)** finds movies with similar summaries.
5. The system returns the most relevant movie recommendations.

---

## 📸 Example Output

Input Movie:

```
Animal
```

Recommended Movies:

```
Kabir Singh
Arjun Reddy
Pushpa
KGF
Jersey
```

---

## 📌 Future Improvements

* 🎨 Netflix-style UI
* 🎬 Movie posters using TMDB API
* 🔎 Dropdown search for movie names
* 📊 Movie rating visualization
* ☁️ Deployment on Streamlit Cloud

---

## 👨‍💻 Author

**Sundaram dubey**
Data Analyst

Python | SQL | Excel | Power BI | Data Visualization

sundaramsundaramdubey@gmail.com
📞 9026667150

---

⭐ If you like this project, consider giving it a **star on GitHub**!
