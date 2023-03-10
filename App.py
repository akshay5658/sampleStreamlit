# import module
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import streamlit.components.v1 as com
import numpy as np

# st.set_page_config(layout="wide")
hidemenu="""
<style>
#MainMenu{
	visibility:hidden;

}
footer{
	visibility:hidden;

}
<style>
"""
# st.markdown(hidemenu,unsafe_allow_html=True)

# headers Provided for selection
selected1 = option_menu(
	menu_title=None,
	options=["Home","Product","Contact"],
	icons = ["house","basket3","envelope"],
	menu_icon="cast",
	default_index = 0,
	orientation="horizontal",
	)
# readding the data converted to excel format
dataframe = pd.read_excel("Ertiga 1.4 Generation I NOT COMPLETED.xlsx",sheet_name="Sheet1")
# print(dataframe)
# st.write(dataframe.columns)
# Writing headings
st.markdown("<h2 style='text-align: center; color: black;'>Periodic Maintenance Shedule </h2>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: black;'>A responsive website created to display maintenance of a passenger car </h5>", unsafe_allow_html=True)

# creating 2 dropdown and adding options to it.
col1, col2 = st.columns(2)

with col1:
	o1 = st.selectbox('Select a Brand',
	["--select--"]+list(dataframe["Make"].unique()),key = "154")
	

with col2:
	dataframe1 = dataframe[(dataframe["Make"]==str(o1))]
	o2 = st.selectbox('Select a Model',
	["--select--"]+list(dataframe1["Model"].unique()),key = "155")
	
# creating 2 dropdown and adding options to it.
col3, col4 = st.columns(2)


with col3:
	dataframe2 = dataframe1[ (dataframe1["Model"]==str(o2))]
	o3 = st.selectbox('Mileage (x1000 Kms)',
	[0]+list(dataframe2["Km(x1000)"].unique()),key = "156")
	# st.write('You selected:', o3)


with col4:
	dataframe3 = dataframe2[ (dataframe2["Km(x1000)"]==int(o3))]
	o4 = st.selectbox('Select a Month from purchase(Optional)',
	[0]+list(dataframe3["Month"].unique()),key = "157")

# creating 2 dropdown and adding options to it.
col5, col6 = st.columns(2)

with col5:
	# if 
	if o4:
		dataframe4 = dataframe3[ (dataframe3["Month"]==int(o4))]
		o5 = st.selectbox('Select a fuel type',
		["--select--"]+list(dataframe4["Fuel"].unique()),key = "159")
	else:
		dataframe4 = dataframe3[ (dataframe3["Km(x1000)"]==int(o3))]
		o5 = st.selectbox(' Select Fuel',
		[0]+list(dataframe3["Fuel"].unique()),key = "160")
		


with col6:
	dataframe5 = dataframe4[(dataframe4["Fuel"]==str(o5))]
	o6 = st.selectbox('Select a Main Group',
	["--select--"]+list(dataframe4["Main Component"].unique()),key = "158")


final = dataframe5[(dataframe5["Main Component"]==str(o6))].dropna()
final = final.reset_index(drop=True)
final.index = np.arange(1, len(final) + 1)



col1, col2, col3 , col4, col5 = st.columns(5)

with col1:
    pass
with col2:
    pass
with col4:
    pass
with col5:
    pass
with col3 :
    submitbutton = st.button('Submit')

if submitbutton:
	st.table(final[["Sub Group",'Components To Insepect/Replace','Action']])
