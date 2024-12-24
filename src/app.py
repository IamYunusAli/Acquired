import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import nbformat

def load_notebook_data(notebook_path):
    with open(notebook_path) as f:
        nb = nbformat.read(f, as_version=4)
    code_cells = [cell['source'] for cell in nb.cells if cell.cell_type == 'code']
    exec_globals = {}
    for code in code_cells:
        exec(code, exec_globals)
    return exec_globals

def main():
    st.title("Company Analysis Dashboard")
    notebook_path = 'notebooks/company_analysis.ipynb'
    data = load_notebook_data(notebook_path)
    df = data.get('df')
    
    if df is not None:
        st.subheader("Data Overview")
        st.dataframe(df)
        st.subheader("Data Insights")
        st.write("Summary Statistics:")
        st.write(df.describe())
        st.subheader("Visualizations")
        st.line_chart(df['Total DL (Bytes)']) 
        st.subheader("Data Insights")
        st.write("Summary Statistics:")
        st.write(df.describe())
        st.subheader("Visualizations")
        fig, ax = plt.subplots()
        ax.plot(df['Total DL (Bytes)']) 
        st.pyplot(fig)
        
    else:
        st.error("No data found in the notebook.")

if __name__ == "__main__":
    main()