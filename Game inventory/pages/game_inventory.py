import streamlit as st
from db_utils import get_all_games

def show_game_inventory_page():
    st.title("Game Inventory")
    games_df = get_all_games()
    st.dataframe(games_df)
