import sqlite3
import pandas as pd

class DatabaseManager:
    def __init__(self, db_path="data/processed/ecommerce.db"):
        self.conn = None
        self.db_path = db_path
        print("🛠 DatabaseManager initialized")

    async def initialize(self):
        print("🔧 Calling initialize()")
        self.conn = sqlite3.connect(self.db_path)
        self.load_csv("product_eligibility", "data/raw/eligibility.csv")
        self.load_csv("ad_sales_metrics", "data/raw/ad_sales.csv")
        self.load_csv("total_sales_metrics", "data/raw/total_sales.csv")


    def load_csv(self, table, file_path):
        df = pd.read_csv(file_path)
        print(f"✅ Loading table: {table} — Columns: {list(df.columns)}")
        df.to_sql(table, self.conn, if_exists="replace", index=False)


    async def execute_query(self, query: str):
        try:
            cursor = self.conn.cursor()

            # Print out the columns that actually exist in ad_sales_metrics
            if "ad_sales_metrics" in query.lower():
                print("🧪 Running column check:")
                cursor.execute("PRAGMA table_info(ad_sales_metrics)")
                schema_info = cursor.fetchall()
                print("📋 Schema for ad_sales_metrics:")
                for col in schema_info:
                    print(f"  {col[1]}")

            print("🧾 SQL:", query)
            cursor.execute(query)
            return cursor.fetchall()

        except Exception as e:
            print("❌ Query Execution Error:", e)
            raise
