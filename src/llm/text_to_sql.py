import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env
load_dotenv()


class GeminiTextToSQL:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise EnvironmentError("❌ GEMINI_API_KEY not set in .env file.")
        
        # Configure the Gemini client
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    async def convert_to_sql(self, question: str) -> str:
        # Define the structured prompt for SQL generation
        prompt = f"""
You are an AI assistant trained to convert natural language questions into valid, strict SQLite SQL queries.

✅ Rules:
- ONLY return raw SQL — no explanations, markdown, or comments.
- Always include a FROM clause.
- Use the exact table and column names provided in the schema.
- Never make up table or column names.

📊 SCHEMA:
- total_sales_metrics(date, item_id, total_sales, total_units_ordered)
- ad_sales_metrics(date, item_id, ad_sales, impressions, ad_spend, clicks, units_sold)
- product_eligibility(eligibility_datetime_utc, item_id, eligibility, message)

❓ QUESTION:
{question}

💬 Your SQL response:
"""
        try:
            # Call Gemini API
            response = self.model.generate_content(prompt)

            sql_text = response.text.strip()

            # Optional: debug print
            # print("🔎 Gemini Response:\n", sql_text)

            # Return only the first line that starts with SELECT
            lines = sql_text.splitlines()
            for line in lines:
                if line.strip().lower().startswith("select"):
                    return line.strip()

            # Return full response if SELECT not found
            return sql_text

        except Exception as e:
            raise RuntimeError("❌ Error while calling Gemini API: " + str(e))
