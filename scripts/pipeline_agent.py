import sqlalchemy
import pandas as pd
import os

# Define the database and paths
DB_PATH = 'sqlite:///data/sales.db'
QUERY_FILE = 'scripts/query.sql'
OUTPUT_DIR = 'output'
OUTPUT_FILE = os.path.join(OUTPUT_DIR, 'query_result.csv')

def execute_sql(query):
    try:
        engine = sqlalchemy.create_engine(DB_PATH)
        with engine.connect() as conn:
            df = pd.read_sql_query(query, conn)
        return df
    except Exception as e:
        print("❌ Error executing SQL:", e)
        return None

if __name__ == "__main__":
    print(f"📄 Reading SQL from {QUERY_FILE}...\n")

    with open(QUERY_FILE, 'r') as file:
        sql_query = file.read()

    print("🔍 SQL Query:\n", sql_query)

    df = execute_sql(sql_query)

    if df is not None:
        print("\n📊 Query Results:\n")
        print(df)

        # Ensure output directory exists
        os.makedirs(OUTPUT_DIR, exist_ok=True)

        # Save to CSV
        df.to_csv(OUTPUT_FILE, index=False)
        print(f"\n✅ Results saved to {OUTPUT_FILE}")
    else:
        print("⚠️ Query failed. Check your SQL syntax.")
