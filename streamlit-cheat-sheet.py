import streamlit as st

def sidebar_elements():
    st.sidebar.title("Streamlit Sidebar Elements Cheat Sheet")
    
    st.sidebar.subheader("st.sidebar.button")
    st.sidebar.write("Creates a button in the sidebar. Returns `True` if clicked.")
    if st.sidebar.button('Click Me'):
        st.sidebar.write("Button clicked!")
    
    st.sidebar.subheader("st.sidebar.checkbox")
    st.sidebar.write("Creates a checkbox in the sidebar. Returns `True` if checked.")
    if st.sidebar.checkbox('Check Me'):
        st.sidebar.write("Checkbox checked!")
    
    st.sidebar.subheader("st.sidebar.radio")
    st.sidebar.write("Creates a set of radio buttons in the sidebar. Returns the selected option.")
    radio_option = st.sidebar.radio("Choose an option", ["Option 1", "Option 2", "Option 3"])
    st.sidebar.write(f"Selected option: {radio_option}")
    
    st.sidebar.subheader("st.sidebar.selectbox")
    st.sidebar.write("Creates a dropdown select box in the sidebar. Returns the selected option.")
    selectbox_option = st.sidebar.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"])
    st.sidebar.write(f"Selected option: {selectbox_option}")
    
    st.sidebar.subheader("st.sidebar.multiselect")
    st.sidebar.write("Creates a multi-select box in the sidebar. Returns a list of selected options.")
    multiselect_options = st.sidebar.multiselect("Choose options", ["Option 1", "Option 2", "Option 3"])
    st.sidebar.write(f"Selected options: {multiselect_options}")
    
    st.sidebar.subheader("st.sidebar.slider")
    st.sidebar.write("Creates a slider in the sidebar. Returns the selected value(s).")
    slider_value = st.sidebar.slider("Select a range", 0, 100, (25, 75))
    st.sidebar.write(f"Selected range: {slider_value}")
    
    st.sidebar.subheader("st.sidebar.text_input")
    st.sidebar.write("Creates a text input box in the sidebar. Returns the entered text.")
    text_input = st.sidebar.text_input("Enter some text")
    st.sidebar.write(f"Entered text: {text_input}")
    
    st.sidebar.subheader("st.sidebar.text_area")
    st.sidebar.write("Creates a text area in the sidebar. Returns the entered text.")
    text_area = st.sidebar.text_area("Enter some text")
    st.sidebar.write(f"Entered text: {text_area}")
    
    st.sidebar.subheader("st.sidebar.number_input")
    st.sidebar.write("Creates a number input box in the sidebar. Returns the entered number.")
    number_input = st.sidebar.number_input("Enter a number", 0, 100)
    st.sidebar.write(f"Entered number: {number_input}")
    
    st.sidebar.subheader("st.sidebar.date_input")
    st.sidebar.write("Creates a date input in the sidebar. Returns the selected date.")
    date_input = st.sidebar.date_input("Select a date")
    st.sidebar.write(f"Selected date: {date_input}")
    
    st.sidebar.subheader("st.sidebar.time_input")
    st.sidebar.write("Creates a time input in the sidebar. Returns the selected time.")
    time_input = st.sidebar.time_input("Select a time")
    st.sidebar.write(f"Selected time: {time_input}")
    
    st.sidebar.subheader("st.sidebar.file_uploader")
    st.sidebar.write("Creates a file uploader in the sidebar. Returns the uploaded file.")
    uploaded_file = st.sidebar.file_uploader("Upload a file")
    if uploaded_file is not None:
        st.sidebar.write(f"Uploaded file: {uploaded_file.name}")
    
    st.sidebar.subheader("st.sidebar.color_picker")
    st.sidebar.write("Creates a color picker in the sidebar. Returns the selected color.")
    color = st.sidebar.color_picker("Pick a color", "#00f900")
    st.sidebar.write(f"Selected color: {color}")

def main():
    st.title("Streamlit Sidebar Elements Cheat Sheet")
    st.write("Explore different Streamlit sidebar elements and see how they work.")
    sidebar_elements()

if __name__ == "__main__":
    main()
