import streamlit as st
import requests
import pandas as pd

API = "http://127.0.0.1:5000"

st.title("📄 AI Resume Analyzer")

# Upload section
st.header("Upload Resume")

name = st.text_input("Candidate Name")
resume_text = st.text_area("Paste Resume Text")

if st.button("Analyze Resume"):
    response = requests.post(f"{API}/analyze", json={
        "name": name,
        "text": resume_text
    })

    if response.status_code == 200:
        result = response.json()
        st.success("Analysis Complete!")

        st.write("### Skills Found")
        st.write(result["skills"])

        st.write("### Score")
        st.metric("Resume Score", result["score"])

# Dashboard
st.header("📊 Resume Database")

res = requests.get(f"{API}/resumes")

if res.status_code == 200:
    df = pd.DataFrame(res.json())

    if not df.empty:
        st.dataframe(df)

        st.bar_chart(df["score"])
    else:
        st.info("No data yet")