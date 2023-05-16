import streamlit as st
import time
import streamlit_extras.switch_page_button as ste
import pandas as pd
import numpy as np
st.set_page_config(layout="wide")
df = pd.read_csv("Database.csv")
col1,col2 = st.columns([1,1])
with col1:
	st.image("Login logo.jpg")
with col2:
	col3,col4 = st.columns([1,1])
	with col4:
		st.header("Login")
	uname = st.text_input("UserName: ")
	pwd = st.text_input("Password: ",type="password")
	col3,col4 = st.columns([1,1])
	with col4:
		button = st.button("Submit")
	if button:
		ubool = uname in list(df['Name'])
		if(ubool):
			ind = list(df['Name']).index(uname)
			if(pwd==df['pwd'][ind]):
				st.warning('Login Successful', icon="✅")
				time.sleep(2)
				ste.switch_page("Home")
			else:
				st.warning('Wrong username or password', icon="❌")
		else:
			st.warning('Not a registered user', icon="⚠️")
			time.sleep(1)
	col3,col4,col5 = st.columns([8,8,15])
	with col5:
		st.markdown("[Sign Up](Signup)")
df = pd.read_csv("Database.csv")