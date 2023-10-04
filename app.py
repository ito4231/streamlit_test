import streamlit as st
from PIL import Image
import sqlite3
import pandas as pd

st.title("アプリ")
st.caption("これはテストあぷりです。")

image = Image.open("./キャプチャ.PNG")
st.image(image,width=200)

with sqlite3.connect("./test.db") as conn:
    sql = """
        select * from 'test'
    """
    
    df = pd.read_sql(sql,conn)

st.write(df)