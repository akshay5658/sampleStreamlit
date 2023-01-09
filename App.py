# import module
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import streamlit.components.v1 as com\

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
st.markdown(hidemenu,unsafe_allow_html=True)
# with st.sidebar:
selected1 = option_menu(
	menu_title=None,
	options=["Home","Product","Contact"],
	icons = ["house","basket3","envelope"],
	menu_icon="cast",
	default_index = 0,
	orientation="horizontal",
	)

dataframe = pd.read_excel("C:\\Users\\tejas\\Downloads\\reboschdataanalystinterview\\Ertiga 1.4 Generation I NOT COMPLETED.xlsx",sheet_name="Sheet1")
# print(dataframe)
# st.write(dataframe.columns)
st.markdown("<h2 style='text-align: center; color: black;'>Periodic Maintenance Shedule </h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: black;'>A responsive website created to display maintenance of a passenger car </h4>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
	o1 = st.selectbox('Select a Brand',
	list(dataframe["Make"].unique()),key = "154")
	# st.write('You selected:', o1)

with col2:
	o2 = st.selectbox('Select a Model',
	list(dataframe["Model"].unique()),key = "155")
	# st.write('You selected:', o2)

col3, col4,col5 = st.columns(3)


with col3:
	o3 = st.selectbox('Mileage (x1000 Kms)',
	list(dataframe["Km(x1000)"].unique()),key = "156")
	# st.write('You selected:', o3)

with col4:
	o4 = st.selectbox('Select a fuel type',
	list(dataframe["Fuel"].unique()),key = "157")
	# st.write('You selected:', o4)

with col5:
	o5 = st.selectbox('Select a fuel type',
	list(dataframe["Month"].unique()),key = "158")
	# st.write('You selected:', o5)

# st.table(dataframe)

# com.html(dataframe.to_html(render_links=True, escape=False))

# option1 = st.selectbox(
# 	'How would you like to be contacted?',
# 	list(dataframe["Main Component"].unique()))

# st.write('You selected:', option)
# Title
