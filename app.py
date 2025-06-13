import streamlit as st
import pandas as pd
import sqlalchemy
import os
import io

# Set database path
DB_PATH = 'sqlite:///data/sales.db'
QUERY_FILE = 'scripts/query.sql'
OUTPUT_FILE = 'output/query_result.csv'

def run_query(query):
    try:
        engine = sqlalchemy.create_engine(DB_PATH)
        with engine.connect() as conn:
            df = pd.read_sql_query(query, conn)
        return df
    except Exception as e:
        st.error(f"❌ SQL Error: {e}")
        return None

# Streamlit app UI
st.set_page_config(page_title="InsightNarrator-SQL", layout="centered")
st.title("💡 InsightNarrator-SQL")
st.markdown("Run and view SQL query results with one click!")

# Read the SQL from file
if os.path.exists(QUERY_FILE):
    with open(QUERY_FILE, 'r') as file:
        default_query = file.read()
else:
    default_query = ""

# SQL text area
user_query = st.text_area("✍️ Edit your SQL query:", value=default_query, height=200)

# Run button
if st.button("🚀 Run SQL Query"):
    if user_query.strip():
        df = run_query(user_query)
        if df is not None:
            st.success("✅ Query executed successfully!")
            st.dataframe(df)

            # Debug: show column names
            st.write("🧾 Columns in result:", df.columns.tolist())

            # Optional bar chart if expected columns are present
            if "region" in df.columns and "total_revenue" in df.columns:
                st.subheader("📊 Revenue by Region")
                st.bar_chart(data=df, x="region", y="total_revenue")

            # Save CSV
            os.makedirs("output", exist_ok=True)
            df.to_csv(OUTPUT_FILE, index=False)
            st.download_button(
                label="📥 Download CSV",
                data=df.to_csv(index=False),
                file_name="query_result.csv",
                mime="text/csv"
            )

            # Save to Excel and offer download
            excel_buffer = io.BytesIO()
            with pd.ExcelWriter(excel_buffer, engine='openpyxl') as writer:
                df.to_excel(writer, index=False, sheet_name='QueryResults')
            excel_data = excel_buffer.getvalue()

            st.download_button(
                label="📥 Download Excel (.xlsx)",
                data=excel_data,
                file_name="query_result.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

            st.success(f"✅ Results saved to: {OUTPUT_FILE}")
    else:
        st.warning("⚠️ Please enter a valid SQL query.")
