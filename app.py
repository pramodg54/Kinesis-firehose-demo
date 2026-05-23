import streamlit as st
import pandas as pd
import random
import time
from datetime import datetime

st.title("Kinesis Firehose Analytics Dashboard")

df = pd.DataFrame(columns=["temperature", "humidity"])
chart = st.line_chart(df)

data = []

table_placeholder = st.empty()

st.subheader("Location-wise Average Temperature")
location_chart_placeholder = st.empty()

for i in range(30):
    new_data = {
        "device_id": random.randint(1000, 9999),
        "temperature": random.randint(20, 40),
        "humidity": random.randint(40, 90),
        "time": datetime.now().strftime("%H:%M:%S"),
        "status": random.choice(["Cloudy", "Clear Sky", "Sunny", "Rain"]),
        "location": random.choice(["Pune", "Mumbai", "Delhi"])
    }

    data.append(new_data)

    full_df = pd.DataFrame(data)

    table_placeholder.dataframe(full_df)

    chart.add_rows(
        pd.DataFrame({
            "temperature": [new_data["temperature"]],
            "humidity": [new_data["humidity"]]
        })
    )

    location_avg = full_df.groupby("location")["temperature"].mean().reset_index()

    location_chart_placeholder.bar_chart(
        location_avg,
        x="location",
        y="temperature"
    )

    if new_data["temperature"] > 35:
        st.warning("High Temperature Alert!")

    time.sleep(1)

csv = full_df.to_csv(index=False)

st.download_button(
    label="Download Report",
    data=csv,
    file_name="streaming_report.csv",
    mime="text/csv"
)
