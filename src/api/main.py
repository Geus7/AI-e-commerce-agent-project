# src/api/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import StreamingResponse, HTMLResponse
from src.database.manager import DatabaseManager
from src.llm.text_to_sql import GeminiTextToSQL
import traceback
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import io
import json

app = FastAPI()

# Initialize database and LLM
db = DatabaseManager()
llm = GeminiTextToSQL()

class Question(BaseModel):
    question: str

@app.on_event("startup")
async def startup_event():
    await db.initialize()

@app.get("/")
def read_root():
    return {"message": "AI E-commerce Agent running 🚀"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/ask")
async def ask_question(user_input: Question):
    question = user_input.question.strip()
    print("🧠 User asked:", question)
    try:
        sql = await llm.convert_to_sql(question)
        print("🧾 Generated SQL:", sql)
        rows = await db.execute_query(sql)
        print("📊 Query Result:", rows)

        if not rows:
            return {"answer": "I couldn't find any results.", "sql": sql, "raw": []}

        if len(rows[0]) == 1:
            values = [row[0] for row in rows]
            return {
                "answer": f"The result is: {', '.join(map(str, values))}",
                "sql": sql,
                "raw": rows
            }
        else:
            return {
                "answer": f"I found {len(rows)} records. Here's the first one: {rows[0]}",
                "sql": sql,
                "raw": rows
            }
    except Exception as e:
        print("❌ Error:", e)
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/matplotlib_sales_trend")
async def matplotlib_sales_trend():
    df = pd.read_csv("data/raw/total_sales.csv")
    fig, ax = plt.subplots()
    ax.plot(df["date"], df["total_sales"], marker="o", color="teal")
    ax.set_title("Total Sales Trend")
    ax.set_xlabel("Date")
    ax.set_ylabel("Total Sales")
    fig.autofmt_xdate()
    plt.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plt.close(fig)
    return StreamingResponse(buf, media_type="image/png")
from fastapi.responses import HTMLResponse
import pandas as pd
import plotly.express as px

@app.get("/plotly_sales_html", response_class=HTMLResponse)
async def plotly_sales_html():
    df = pd.read_csv("data/raw/total_sales.csv")
    fig = px.bar(df, x="item_id", y="total_sales", title="Total Sales by Item")
    chart_json = fig.to_json()

    html = f"""
    <html>
    <head>
        <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
        <title>Plotly Sales Chart</title>
    </head>
    <body style="margin:0">
        <h2 style="text-align:center">Plotly – Total Sales by Item</h2>
        <div id="chart" style="width:100%;height:600px;"></div>
        <script>
            var chartObj = {chart_json};
            Plotly.newPlot('chart', chartObj.data, chartObj.layout);
        </script>
    </body>
    </html>
    """

    return HTMLResponse(content=html)
