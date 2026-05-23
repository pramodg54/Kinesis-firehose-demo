import streamlit as st
import pandas as pd
import random
import time
from datetime import datetime

st.title("Kinesis Firehose Streaming Demo")
data = []
placeholder = st.empty()

for i in range(30):
    new_data = {

        "device_id": random.randint(1000, 9999),

        "temperature": random.randint(20, 40),

        "humidity": random.randint(40, 90),

        "location": random.choice(["Pune", "Mumbai", "Delhi"]),

        "time": datetime.now().strftime("%H:%M:%S"),
        
        "Status": random.choice(["Cloudy", "Clear Sky", "Sunny", "Rain"])

    }
    data.append(new_data) 
    df = pd.DataFrame(data)
    placeholder.dataframe(df)
    

    chart.add_rows(

        pd.DataFrame(

            {

                "temperature": [new_data["temperature"]],

                "humidity": [new_data["humidity"]]

            }

        )

    )

 

    # Alerts

    if new_data["temperature"] > 35:

        st.warning("High Temperature Alert!")

 

    time.sleep(1)

 

# Download CSV Report

csv = full_df.to_csv(index=False)

 

st.download_button(

    label="Download Report",

    data=csv,

    file_name="streaming_report.csv",

    mime="text/csv"

)
