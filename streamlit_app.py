import streamlit as st

pg = st.navigation([st.Page("streamlit-cheat-sheet.py"),
                    st.Page("streamlit-sidebar-elements.py"), 
                    st.Page("streamlit-data-page.py")])
pg.run()
