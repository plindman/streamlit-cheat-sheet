import streamlit as st
import json

def json_to_st_table(data):
    column_widths = (1, 2, 3)
    columns = st.columns(column_widths)
    fields = ["Title", "Description", "Link"]
    for col, field_name in zip(columns, fields):
        # header
        col.write(field_name)

    for i, item in enumerate(data):
        title, description, link = item['title'], item['description'], item['link']

        col1, col2, col3 = st.columns(column_widths)
        col1.write(title)
        col2.write(description)

        if link.startswith("http"):
            clickable_link = f'<a href="{link}" target="_blank" rel="noopener noreferrer">{title}</a>'
            col3.write(clickable_link, unsafe_allow_html=True)
        else:
            col3.page_link(link, label=title)

# Load the data from the JSON file
with open('cheat-sheet.json') as f:
    cheat_sheet_data = json.load(f)

st.title("Streamlit Cheat Sheet")
st.write("Explore different Streamlit elements and see how they work.")

# Generate markdown table
json_to_st_table(cheat_sheet_data)
