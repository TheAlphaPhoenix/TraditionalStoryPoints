import streamlit as st

def calculate_story_points(technical, integration, implementation, testing, uncertainty):
    fibonacci = [1, 2, 3, 5, 8, 13, 21]
    total_score = technical + integration + implementation + testing + uncertainty
    story_points = next((num for num in fibonacci if num >= total_score), 21)
    return story_points

st.title("Story Points Calculator")
st.write("Select values for each category:")

technical = st.selectbox("Technical Complexity", [1, 2, 3], index=0, format_func=lambda x: ["Low", "Medium", "High"][x-1])
integration = st.selectbox("Integration Complexity", [1, 2, 3], index=0, format_func=lambda x: ["Low", "Medium", "High"][x-1])
implementation = st.selectbox("Implementation Effort", [1, 2, 3], index=0, format_func=lambda x: ["Low", "Medium", "High"][x-1])
testing = st.selectbox("Testing Effort", [1, 2, 3], index=0, format_func=lambda x: ["Low", "Medium", "High"][x-1])
uncertainty = st.selectbox("Uncertainty", [1, 2, 3], index=0, format_func=lambda x: ["Low", "Medium", "High"][x-1])

if st.button("Calculate Story Points"):
    story_points = calculate_story_points(technical, integration, implementation, testing, uncertainty)
    st.subheader(f"Story Points: {story_points}")
