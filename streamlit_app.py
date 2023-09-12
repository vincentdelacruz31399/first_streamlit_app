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

#filter the table data will put the selected fruits into a variable called "fruits_selected". then ask our app 
#to use the fruits in our fruits_selected list to pull rows from the full dataset(and assigned that data to a variable 
#called fruits_to_show).Finally, we'll ask the app to use the data in fruits_to_show in the dataframe it displays on the page
fruits_selected = streamlit.multiselect("Pick Some Fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
streamlit.dataframe(my_fruit_list)
#use myfruitlist dataframe then put inside [fruit_selected]
fruits_to_show = my_fruit_list.loc[fruits_selected]
#pull data into the dataframe using the variable my_fruit_list use now the fruits_to_show dataframe for selected 
#streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)

#New Section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")

#import python function "REQUEST" with "Get" function and text function
#import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response.json()) # just writes the data to the screen

#take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output it in the screen as table
streamlit.dataframe(fruityvice_normalized)
