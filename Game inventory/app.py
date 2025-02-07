import streamlit as st
from pages.add_game import show_add_game_page
from pages.update_delete_game import show_update_delete_page
from pages.game_inventory import show_game_inventory_page

st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to", ["Game Inventory", "Add Game", "Update/Delete Game"])

if page == "Game Inventory":
    show_game_inventory_page()
elif page == "Add Game":
    show_add_game_page()
elif page == "Update/Delete Game":
    show_update_delete_page()
