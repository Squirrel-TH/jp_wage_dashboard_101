import plotly.express as px
import numpy as np
import pandas as pd
import streamlit as st
import pydeck as pdk

st.title('日本の賃金データダッシュボード')

df_jp_category = pd.read_csv('./csv_data/雇用_医療福祉_一人当たり賃金_全国_大分類.csv', encoding='shift_jis')
df_pref_ind = pd.read_csv('./csv_data/雇用_医療福祉_一人当たり賃金_都道府県_全産業.csv', encoding='shift_jis')
df_pref_category = pd.read_csv('./csv_data/雇用_医療福祉_一人当たり賃金_都道府県_大分類.csv', encoding='shift_jis')