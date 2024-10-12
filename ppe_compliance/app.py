import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Data for PPE Compliance
data = {
    'Compliance Item': ['Helmet', 'Vest', 'Safety Shoes', 'Machine Guard', 'Emergency Gate'],
    'Total Employees': [200, 200, 200, 50, 10],
    'Compliant Employees': [180, 160, 190, 45, 8],
    'Compliance Percentage': [90, 80, 95, 90, 80]
}
df = pd.DataFrame(data)

# Expanded Data for Departments and Factories
department_data = {
    'Department/Factory': ['Department A', 'Department B', 'Factory X', 'Factory Y'],
    'Helmet Compliance (%)': [85, 90, 88, 92],
    'Vest Compliance (%)': [80, 75, 85, 90],
    'Safety Shoes Compliance (%)': [90, 88, 92, 94],
    'Machine Guard Compliance (%)': [92, 85, 91, 89],
    'Emergency Gate Compliance (%)': [78, 80, 82, 85]
}
df_departments = pd.DataFrame(department_data)

# Data for Compliance Over Time
time_data = {
    'Time Period': ['Week 1', 'Week 2', 'Week 3', 'Week 4'],
    'Helmet Compliance (%)': [85, 88, 87, 90],
    'Vest Compliance (%)': [78, 80, 82, 84],
    'Safety Shoes Compliance (%)': [92, 94, 93, 95],
    'Machine Guard Compliance (%)': [90, 92, 91, 93],
    'Emergency Gate Compliance (%)': [80, 83, 85, 87]
}
df_time = pd.DataFrame(time_data)

# Data for Compliance Prediction
prediction_data = {
    'Month': ['July', 'August', 'September', 'October'],
    'Predicted Compliance (%)': [89, 90, 91, 92]
}
df_prediction = pd.DataFrame(prediction_data)

# Data for Shift-Based Comparison
shift_data = {
    'Shift': ['Morning', 'Evening', 'Night'],
    'Helmet Compliance (%)': [90, 85, 80],
    'Vest Compliance (%)': [85, 80, 75],
    'Safety Shoes Compliance (%)': [95, 90, 85]
}
df_shifts = pd.DataFrame(shift_data)

# App Title
st.title("PPE Compliance Visualization App")

# Navigation for different sections
section = st.sidebar.radio("Navigate to", (
    "PPE Combined Compliance Score", "PPE Compliance Across Different Safety Measures", "PPE Compliance Comparison Across Departments and Factories",
    "PPE Compliance Over Time", "PPE Compliance Target vs. Actual", "PPE Compliance Prediction", "PPE Improvement Trends",
    "PPE Shift-Based Comparison", "PPE Compliance Performance Rating", "PPE Violation Cost Analysis",
    "PPE Sentiment Analysis", "PPE Compliance Gap Analysis"
))

# PPE Combined Compliance Score
if section == "PPE Combined Compliance Score":
    st.header("PPE Combined Compliance Score")
    st.write("The combined compliance score gives an overview of how well the factories are complying with PPE requirements.")
    st.write("**Combined Compliance Score:** 89%")
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = 89,
        title = {'text': "Combined Compliance Score"},
        gauge = {'axis': {'range': [0, 100]}, 'bar': {'color': "green"}}
    ))
    st.plotly_chart(fig)

# PPE Compliance Across Different Safety Measures
elif section == "PPE Compliance Across Different Safety Measures":
    st.header("PPE Compliance Across Different Safety Measures")
    st.write("This section shows compliance across various safety measures like helmets, vests, safety shoes, etc.")
    st.dataframe(df)
    fig = px.bar(df, x='Compliance Item', y='Compliance Percentage', title="PPE Compliance Across Safety Measures")
    st.plotly_chart(fig)

# PPE Compliance Comparison Across Departments and Factories
elif section == "PPE Compliance Comparison Across Departments and Factories":
    st.header("PPE Compliance Comparison Across Departments and Factories")
    st.write("Comparison of compliance scores across different departments and factories.")
    st.dataframe(df_departments)
    fig = px.bar(df_departments, x='Department/Factory', y=['Helmet Compliance (%)', 'Vest Compliance (%)', 'Safety Shoes Compliance (%)', 'Machine Guard Compliance (%)', 'Emergency Gate Compliance (%)'], title="PPE Compliance Comparison Across Departments and Factories")
    st.plotly_chart(fig)

# PPE Compliance Over Time
elif section == "PPE Compliance Over Time":
    st.header("PPE Compliance Over Time")
    st.write("This section shows how compliance has changed over weeks, months, and years.")
    st.dataframe(df_time)
    fig = px.line(df_time, x='Time Period', y=['Helmet Compliance (%)', 'Vest Compliance (%)', 'Safety Shoes Compliance (%)', 'Machine Guard Compliance (%)', 'Emergency Gate Compliance (%)'], title="PPE Compliance Over Time")
    st.plotly_chart(fig)

# PPE Compliance Target vs. Actual
elif section == "PPE Compliance Target vs. Actual":
    st.header("PPE Compliance Target vs. Actual")
    st.write("A gap analysis showing the difference between the target compliance and the current compliance.")
    gap_data = df.copy()
    gap_data['Target Compliance (%)'] = 100
    gap_data['Compliance Gap (%)'] = gap_data['Target Compliance (%)'] - gap_data['Compliance Percentage']
    st.dataframe(gap_data)
    fig = px.bar(gap_data, x='Compliance Item', y=['Compliance Percentage', 'Compliance Gap (%)'], title="PPE Compliance Target vs. Actual")
    st.plotly_chart(fig)

# PPE Compliance Prediction
elif section == "PPE Compliance Prediction":
    st.header("PPE Compliance Prediction")
    st.write("Prediction of future compliance based on past violation data.")
    st.dataframe(df_prediction)
    fig = px.line(df_prediction, x='Month', y='Predicted Compliance (%)', title="PPE Compliance Prediction")
    st.plotly_chart(fig)

# PPE Improvement Trends
elif section == "PPE Improvement Trends":
    st.header("PPE Improvement Trends")
    st.write("Improvement trends across different factories and departments.")
    improvement_data = df_time.copy()
    fig = px.area(improvement_data, x='Time Period', y=['Helmet Compliance (%)', 'Vest Compliance (%)', 'Safety Shoes Compliance (%)', 'Machine Guard Compliance (%)', 'Emergency Gate Compliance (%)'], title="PPE Improvement Trends")
    st.plotly_chart(fig)

# PPE Shift-Based Comparison
elif section == "PPE Shift-Based Comparison":
    st.header("PPE Shift-Based Comparison")
    st.write("Comparison of compliance during different shifts: morning, evening, and night.")
    st.dataframe(df_shifts)
    fig = px.bar(df_shifts, x='Shift', y=['Helmet Compliance (%)', 'Vest Compliance (%)', 'Safety Shoes Compliance (%)'], title="PPE Shift-Based Comparison")
    st.plotly_chart(fig)

# PPE Compliance Performance Rating
elif section == "PPE Compliance Performance Rating":
    st.header("PPE Compliance Performance Rating")
    st.write("Performance ratings categorized as high, moderate, or low.")
    performance_data = df.copy()
    performance_data['Performance Rating'] = np.where(performance_data['Compliance Percentage'] >= 90, 'High', 
                                                     np.where(performance_data['Compliance Percentage'] >= 80, 'Moderate', 'Low'))
    st.dataframe(performance_data)
    fig = px.pie(performance_data, names='Performance Rating', title="PPE Compliance Performance Rating")
    st.plotly_chart(fig)

# PPE Violation Cost Analysis
elif section == "PPE Violation Cost Analysis":
    st.header("PPE Violation Cost Analysis")
    st.write("Cost analysis of violations across different PPE modules.")
    cost_data = df.copy()
    cost_data['Violation Cost ($)'] = (cost_data['Total Employees'] - cost_data['Compliant Employees']) * 100
    st.dataframe(cost_data)
    fig = px.bar(cost_data, x='Compliance Item', y='Violation Cost ($)', title="PPE Violation Cost Analysis")
    st.plotly_chart(fig)

# PPE Sentiment Analysis
elif section == "PPE Sentiment Analysis":
    st.header("PPE Sentiment Analysis")
    st.write("Sentiment analysis based on feedback provided by stakeholders.")
    sentiment_data = {'Sentiment': ['Positive', 'Neutral', 'Negative'], 'Count': [50, 20, 30]}
    df_sentiment = pd.DataFrame(sentiment_data)
    st.dataframe(df_sentiment)
    fig = px.pie(df_sentiment, names='Sentiment', values='Count', title="PPE Sentiment Analysis")
    st.plotly_chart(fig)

# PPE Compliance Gap Analysis
elif section == "PPE Compliance Gap Analysis":
    st.header("PPE Compliance Gap Analysis")
    st.write("Analysis of the gap between current compliance and target compliance.")
    gap_data = df.copy()
    gap_data['Target Compliance (%)'] = 100
    gap_data['Compliance Gap (%)'] = gap_data['Target Compliance (%)'] - gap_data['Compliance Percentage']
    st.dataframe(gap_data)
    fig = px.bar(gap_data, x='Compliance Item', y='Compliance Gap (%)', title="PPE Compliance Gap Analysis")
    st.plotly_chart(fig)

# Footer
st.sidebar.write("\n\nApp developed for PPE compliance visualization.")