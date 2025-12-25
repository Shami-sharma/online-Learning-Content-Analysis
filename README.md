# 📊 Learning Content Analysis Dashboard

A beginner-friendly **Python data analysis project** that analyzes online learning content engagement using **Pandas, Matplotlib, and Gradio**.

The app allows users to **upload their own dataset** or automatically analyzes an **existing dataset** using **OS-based file handling**.

---

## 🚀 Features

- 📁 Upload your own CSV dataset  
- 🗂️ Automatically uses existing dataset if no file is uploaded  
- 📊 Generates **study insights**:
  - Total views, likes, comments  
  - Average content duration  
  - Most viewed content type  
  - Most popular course  
- 📈 Visualizations:
  - Bar chart: Views by content type  
  - Line chart: Upload trend over time  
- 🖥️ Interactive UI using **Gradio**

---

## 🧠 Project Logic (Simple)

1. If user uploads a CSV → analyze uploaded file  
2. If user does NOT upload a CSV → check if dataset exists using `os.path.exists()`  
3. If dataset exists → analyze it  
4. If no dataset exists → show error  

✔ No hard-coded default functions  
✔ Real-world OS file handling logic  

---

## 📁 Dataset Format

The CSV file should contain the following columns:

