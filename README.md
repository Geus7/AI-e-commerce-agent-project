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

```date,item_id,total_sales,total_units_ordered```
```2025-06-01,0,309.99,1 ```



### 5. Run the App

```python run.py```

### Output :
### 1. LLM Response
![Sales Output](screenshots/Screenshot%202025-07-22%20121629.png)


![Bar Chart](screenshots/Screenshot%202025-07-22%20121643.png)

### 2. Trend chart
![LLM Output](screenshots/Screenshot%202025-07-22%20121712.png)
