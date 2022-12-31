import pandas
import streamlit as st


col1, col2 = st.columns(2)

with col1:
    st.image("image/photo.jpg")

with col2:
    st.title("Niki Patel")
    content = """
    Hello !! My self Niki patel. I am python developer. My master completed at ignou in 2015. I graduated in 2012 at m.s. university.
    I married with Brijesh Patel. He is production engineer. He worked in sai industry as a sr manager at kheda. I have one kids. His name Hetansh Patel. He is only 3.5 Year old. 
    """
    st.info(content)

content2 = """ Below you can find some of the apps i have built in python. Feel free to contect me. """
st.write(content2)

col3 , col4 = st.columns(2)
df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:11].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[11:].iterrows():
        st.header(row["title"])

