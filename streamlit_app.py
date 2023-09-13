#"Commit" means "SAVE" every time "Commit" we can put note on what is the changes #streamlit is a python function like pandas
import streamlit
#importing pandas always "" inside pandas.read_csv("")
import pandas 
#add snowflake connector
import snowflake.connector
#import python function "REQUEST" with "Get" function and text function
import requests
#import library that will help in control of flow changes
from urllib.error import URLError


#title of the streamlit
streamlit.title('My Parents New Healthy Diner')
#Body of the streamlit
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


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
#fruit_choice = streamlit.text_input('What fruit would you like information about?', 'KIWI') #text , example output the 'KIWI' is the example output
#streamlit.write('The user entered', fruit_choice) #shows the text then the variable since we store the output inside the variable fruit_choice

#create a repeatable function and move the output here of requesting data from fruityvice.com always starts function with name "DEF"
#inside the function is a variable always end with ":"
def get_fruityvice_data(this_fruit_choice):
        fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice) #added + variable where we store the output of the selected choice in text inpu
#streamlit.text(fruityvice_response.json()) # just writes the data to the screen
#take the json version of the response and normalize it
        fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
        return fruityvice_normalized #always with return action in a function

#put the fruity choice advice to a try-except(with nested if-else)
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
         streamlit.error("Please select a fruit to get information.") #error message if not part of fruit list 
  else:
       back_from_function = get_fruityvice_data(fruit_choice) #create new variable which value is function get_fruityvice_data which inside is (fruit_choice)variable which connects with users selection
       #output it in the screen as table
       streamlit.dataframe(back_from_function) # shows on dataframe the back_from_function variable

except URLError as e:
    streamlit.error()
#Introducing this structure allows us to separate the code that is loaded once from the code that should be repeated each time a new value is entered.
#Notice there are three lines of code under the ELSE. These are important steps we will be repeating. We can pull them out into a separate bit of code called a function. We'll do that next. 

  
#don't run anything past here while we troubleshoot
#stereamlit.stop()

#header
streamlit.header("The fruit load list contain:")
#snowflake-related functions
def get_fruit_load_list():
        with my_cnx.cursor() as my_cur: #with function means getting my_cnx.cursor to a variable name called as "my_cur"
             my_cur.execute("SELECT * from fruit_load_list")   #execute select * command from the list
             return my_cur.fetchall() #return all value inside my_cur variable if only one the function is fetchone() if all fetchall

#Add a button to load the fruit table
if streamlit.button('Get Fruit Load List'):
        my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])  #Query trial account Metadata
        my_data_row = get_fruit_load_list() #store the value of get_fruit_load_list function to a variable called my_data_row
        streamlit.dataframe(my_data_row) #call variable my_data_row as dataframe  using streamlit
        
#don't run anything past here while we troubleshoot        
#stereamlit.stop()

#allows to add user in the frame
def insert_row_snowflake(new_fruit): #create new function to add the fruit name submissions to the snowflake table
        with my_cnx.cursor() as my_cur:
                my_cur.execute("insert into fruit_load_list values ('from streamlit')") #function that will insert value into the snowflake table
                return "Thanks for adding" +  new_fruit     #return a word + the new value that inserted in snowflake
                
add_my_fruit = streamlit.text_input('What fruit would you like to add?') #text , example output the 'KIWI' is the example output
if streamlit.button('Add a Fruit to the List'):
        my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"]) #if the button is click then connect the variable to the secret account
        back_from_function = insert_row_snowflake(add_my_fruit) #call new variable which value is function insert_row_function with add_my_fruit inside which is input button where user type what fruit they want to add
        streamlit.text(back_from_function)


#streamlit.write('Thanks for adding', add_my_fruit) #shows the text then the variable since we store the output inside the variable fruit_choice
#import python function "REQUEST" with "Get" function and text function
#import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + add_my_fruit) #added + variable where we store the output of the selected choice in text input
#streamlit.text(fruityvice_response.json()) # just writes the data to the screen

#my_cur.execute("update fruit_load_list set fruit_name = ('from streamlit') where fruit_name = ('test')") 
#this will not work pa just do it!
#my_cur.execute("insert into fruit_load_list values ('from streamlit')")

