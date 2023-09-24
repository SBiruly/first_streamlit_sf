import streamlit
import pandas
import snowflake.connector
import requests
from urllib.error import URLError
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.title("My Parents New Healthy Dinner")

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
  
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
# streamlit.dataframe(my_fruit_list)
#--------------------------------------------------------------------------
# Let's put a pick list here so they can pick the fruit they want to include
fruits_selected=streamlit.multiselect("Pick some fruits:",list(my_fruit_list. index), ['Avocado' , 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
# -------------------------------------------------------------------------
# streamlit.header("Fruityvice Fruit Advice!")
# # To Display fruityvice api response
# fruit_choice = streamlit.text_input('What fruit would you like information about?','Apple')
# streamlit.write('The user entered ', fruit_choice)
# # import requests
# fruity_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
# # streamlit.text(fruity_response.json())
# ---------------------------------------------------------------------------
# -------------------------------------------------------------------------
# streamlit.header("Fruityvice Fruit Advice!")
# To Display fruityvice api response
#--------------------------------------------------------------------------------
# try:
#   fruit_choice = streamlit.text_input('What fruit would you like information about?')
#   if not fruit_choice:
#     streamlit.error("Please select a fruit to get information.")
#   else:
#     fruity_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
#     fruityvice_normalized = pandas.json_normalize(fruity_response.json())
#     streamlit.dataframe(fruityvice_normalized)
# except URLError as e:
#   streamlit.error()
#-----------------------------------------------------------------------------------------
def get_fruitvice_data(this_fruit_choice):
  fruity_response = requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruity_response.json())
  return fruityvice_normalized
  # streamlit.dataframe(fruityvice_normalized)
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruitvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)

except URLError as e:
  streamlit.error()
#-----------------------------------------------------------------------------------------
# # import requests
# fruity_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
# # streamlit.text(fruity_response.json())
# ---------------------------------------------------------------------------
# write your own comment -what does the next line do? 
# fruity_response.json() will converts the JSON data from the response into a Python dictionary
# pandas.json_normalize is used to flatten and normalize nested JSON data into a tabular format
# fruityvice_normalized = pandas.json_normalize(fruity_response.json())
# ----------------------------------------------------------------------------

# write your own comment - what does this do?
# It will view fruityvice_normalized in tabular form(dataframe)
# streamlit.dataframe(fruityvice_normalized)
# streamlit.stop()
#-----------------------------------------------------------------------------
# import snowflake.connector

# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_data_row = my_cur.fetchone()
# streamlit.text("Hello from Snowflake:")
# streamlit.text(my_data_row)
# #-----------------------------------------------------------------------------
# my_cnx = snowflake. connector. connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("select * from fruit_load_list")
# my_data_row = my_cur.fetchone()
# streamlit.header("The fruit load contains:")
# streamlit.dataframe(my_data_row)
# #-------------------------------------------------------------------------------
# my_data_rows = my_cur.fetchall()
# streamlit.header("The fruit load list contains:")
# streamlit.dataframe(my_data_rows)
#-------------------------------------------------------------------------------
streamlit.header("The fruit load list contains:")
#Snowf1ake-re1ated functions
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list")
    return my_cur.fetchall()
# Add a button to load the fruit
if streamlit.button( 'Get Fruit Load List'):
  my_cnx = snowflake.connector. connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  streamlit.dataframe(my_data_rows)
# streamlit.stop()
# #-------------------------------------------------------------------------------
# streamlit.header("What fruit would you like to add")
# # To Display fruityvice api response
# fruit_choice = streamlit.text_input('What fruit would you like information about?','Jackfruit')
# streamlit.write('Thanks for adding ', fruit_choice)
# # -----------------------------------------------------------------------------
#-------------------------------------------------------------------------------
# Allow the end user to add a fruit to the
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values ('from streamlit' ) ")
    return "Thanks for adding " + new_fruit

add_my_fruit = streamlit.text_input(' What fruit would you like to add?')
if streamlit.button('Add a Fruit to the List'):
  my_cnx = snowflake. connector.connect(**streamlit.secrets["snowflake"])
  back_from_function =  insert_row_snowflake(add_my_fruit)
  streamlit.text(back_from_function)
streamlit.stop()
# -----------------------------------------------------------------------------
my_cur.execute("insert into fruit_load_list values ('from streamlit')")   



