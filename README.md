# AI E-Commerce Agent Project

An intelligent, interactive API-based analytics agent for e-commerce businesses — powered by FastAPI, Gemini (Google) LLM, Plotly, and Matplotlib.

---

## 🚀 Features

- ✅ Natural language Q&A using LLM (Gemini 2.5)
- ✅ Automagically generates SQL queries
- ✅ Answers business questions like:
  - "What is my total sales?"
  - "Which product had the highest CPC?"
- ✅ Sales data visualizations:
  - 📈 **Line chart** (Matplotlib PNG)
  - 📊 **Interactive bar chart** (Plotly)
- ✅ Clean RESTful FastAPI endpoints with Swagger docs

---

## ⚙️ Quick Start

### 1. Activate Virtual Environment

**Windows:**

```venv\Scripts\activate```


### 2. Install Dependencies


```pip install -r requirements.txt```


### 3. Add Your `.env` 


Create a `.env` file in the root directory:

```GEMINI_API_KEY=your-google-gemini-api-key-here```


### 4. Prepare Your Sales Data

Save your dataset as `data/raw/total_sales.csv` with this format:

```date,item_id,total_sales,total_units_ordered
2025-06-01,0,309.99,1
...```


### 5. Run the App

```python run.py```

### Output :
<img width="1910" height="930" alt="Screenshot 2025-07-22 121712" src="https://github.com/user-attachments/assets/a67468ae-f86b-4e81-b217-bcad8032feea" />
<img width="884" height="417" alt="Screenshot 2025-07-22 121643" src="https://github.com/user-attachments/assets/daa18a70-2a8a-42b0-9e3d-5416a81e6542" />
<img width="988" height="750" alt="Screenshot 2025-07-22 121629" src="https://github.com/user-attachments/assets/421c7922-b634-4c30-91d7-a8535340ea3a" />

