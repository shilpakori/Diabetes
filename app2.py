import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sidebar title
st.sidebar.title("Diabetes Data App")

# Load dataset
df = pd.read_csv("diabetes.csv")

# Sidebar options
option = st.sidebar.selectbox(
    "Choose an option:",
    ("Display Data", "Top 5 Glucose Values", "Plot Outcome Count")
)

# Button
if st.sidebar.button("Submit"):
    st.write(f"You selected: {option}")
    
    # 1. Display full dataset
    if option == "Display Data":
        st.write(df)
    
    # 2. Top 5 highest glucose values
    if option == "Top 5 Glucose Values":
        top_glucose = df.nlargest(5, 'Glucose')
        st.write(top_glucose)
    
    # 3. Plot Outcome distribution
    if option == "Plot Outcome Count":
        outcome_counts = df['Outcome'].value_counts()
        
        fig, ax = plt.subplots()
        outcome_counts.plot(kind='bar', ax=ax)
        
        ax.set_title("Diabetes Outcome Count")
        ax.set_xlabel("Outcome (0 = No, 1 = Yes)")
        ax.set_ylabel("Count")
        
        st.pyplot(fig)