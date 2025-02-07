import streamlit as st
from db_utils import add_game

def show_add_game_page():
    st.title("Add New Game")
    with st.form(key='add_game_form'):
        name = st.text_input("Game Name")
        developer = st.text_input("Developer")
        category = st.selectbox("Category", ['Action', 'Adventure', 'Strategy', 'Puzzle', 'RPG'])
        platform = st.selectbox("Platform", ['PlayStation', 'Xbox', 'Nintendo', 'PC'])
        price = st.number_input("Price", min_value=0.0, step=0.01)
        release_date = st.date_input("Release Date")

        submit_button = st.form_submit_button(label='Add Game')

        if submit_button:
            add_game(name, developer, category, platform, price, release_date)
            st.success("Game added successfully!")
