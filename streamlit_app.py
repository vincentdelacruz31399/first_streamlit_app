#"Commit" means "SAVE" every time "Commit" we can put note on what is the changes #streamlit is a python function like pandas
import streamlit
#title of the streamlit
streamlit.title('My Parents New Healthy Diner')
#Body of the streamlit
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#importing pandas always "" inside pandas.read_csv("")
import pandas 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#pull data into the dataframe using the variable my_fruit_list
streamlit.dataframe(my_fruit_list)

#Create User-Interaction or User interface or UI its called multi select multi select is ("title",list(dataframe.index))
# Separate the title and the list with "," also the list consists of the dataframe with .index 
streamlit.multiselect("Pick Some Fruits:",list(my_fruit_list.index))
#display the table on the page
streamlit.dataframe(my_fruit_list)
