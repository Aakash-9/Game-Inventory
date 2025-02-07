import streamlit as st
import pandas as pd
from db_utils import update_game, delete_game, get_all_games, get_db_connection

def show_update_delete_page():
    st.title("Update or Delete Game")

    # Update Game Section
    st.header("Update Game")
    game_id = st.number_input("Game ID to update", min_value=1, step=1)
    if game_id:
        conn = get_db_connection()
        game = pd.read_sql(f"SELECT * FROM Games WHERE id = {game_id}", conn)
        conn.close()

        if not game.empty:
            with st.form(key='update_game_form'):
                name = st.text_input("Game Name", game['name'][0])
                developer = st.text_input("Developer", game['developer'][0])
                category = st.selectbox("Category", ['Action', 'Adventure', 'Strategy', 'Puzzle', 'RPG'], index=['Action', 'Adventure', 'Strategy', 'Puzzle', 'RPG'].index(game['category'][0]))
                platform = st.selectbox("Platform", ['PlayStation', 'Xbox', 'Nintendo', 'PC'], index=['PlayStation', 'Xbox', 'Nintendo', 'PC'].index(game['platform'][0]))
                price = st.number_input("Price", min_value=0.0, step=0.01, value=game['price'][0])
                release_date = st.date_input("Release Date", value=pd.to_datetime(game['release_date'][0]))

                submit_button = st.form_submit_button(label='Update Game')
                if submit_button:
                    update_game(game_id, name, developer, category, platform, price, release_date)
                    st.success("Game updated successfully!")
        else:
            st.warning("Game not found.")

    # Delete Game Section
    st.header("Delete Game")
    delete_game_id = st.number_input("Game ID to delete", min_value=1, step=1)
    if delete_game_id:
        if st.button("Delete Game"):
            delete_game(delete_game_id)
            st.success("Game deleted successfully!")
