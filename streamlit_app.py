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
#set fruit name column as the index of the data
my_fruit_list = my_fruit_list.set_index('Fruit')

#Create User-Interaction or User interface or UI its called multi select multi select is ("title",list(dataframe.index))
# Separate the title and the list with "," also the list consists of the dataframe with .index 
#let's put pre-pick list to set a good example so they can pick the fruit they want to include
#just put "," in the list after the index then ['',''] separate it with ","
streamlit.multiselect("Pick Some Fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
#pull data into the dataframe using the variable my_fruit_list
streamlit.dataframe(my_fruit_list)


