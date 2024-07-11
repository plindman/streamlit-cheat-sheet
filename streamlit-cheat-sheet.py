import streamlit as st

# Load the configuration
from config_loader import load_config
config = load_config('config.json')

def init_page():
    if 'button_clicked_count' not in st.session_state:
        st.session_state.button_clicked_count = 0
        st.session_state.checkbox_selected = False

def button_elements():
    # st.sidebar.subheader("st.sidebar.button")
    if st.sidebar.button('Click Me'):
        st.session_state.button_clicked_count += 1

    color = config.colors.positive if st.session_state.button_clicked_count > 0 else config.colors.negative

    st.subheader("st.sidebar.button")
    st.markdown(f"Button returns `True` if clicked and increments click count. Button clicked <span style='color: {color};'>{st.session_state.button_clicked_count} times</span>.", unsafe_allow_html=True)    

def checkbox_elements():
    # st.sidebar.subheader("st.sidebar.checkbox")
    if st.sidebar.checkbox('Check Me'):
        st.session_state.checkbox_selected = True
    else:
        st.session_state.checkbox_selected = False

    color = config.colors.positive if st.session_state.checkbox_selected else config.colors.negative

    st.subheader("st.sidebar.checkbox")
    st.markdown(f"Creates a checkbox in the sidebar. Returns `True` if checked. Checkbox selected: <span style='color: {color};'>{st.session_state.checkbox_selected}</span>.", unsafe_allow_html=True)    

def radio_elements():
    # st.sidebar.subheader("st.sidebar.radio")
    radio_option = st.sidebar.radio("Choose an option", ["Option 1", "Option 2", "Option 3"],
                                    horizontal=True)

    color = getattr(config.colors.radios, radio_option or "default")

    st.subheader("st.sidebar.radio")
    st.markdown(f"Creates a set of radio buttons in the sidebar. Returns the selected option. Selected radio: <span style='color: {color};'>{radio_option}</span>.", unsafe_allow_html=True)    

def select_elements():
    # st.sidebar.subheader("st.sidebar.selectbox")
    selectbox_option = st.sidebar.selectbox("Choose an option", ["Select 1", "Select 2", "Select 3"])

    color = getattr(config.colors.select, selectbox_option or "default")

    st.subheader("st.sidebar.selectbox")
    st.markdown(f"Creates a dropdown select box in the sidebar. Returns the selected option. Selected option: <span style='color: {color};'>{selectbox_option}</span>.", unsafe_allow_html=True) 

def multiselect_elements():
    # st.sidebar.subheader("st.sidebar.multiselect")
    multiselect_options = st.sidebar.multiselect("Choose options", ["Multi 1", "Multi 2", "Multi 3"])

    st.subheader("st.sidebar.multiselect")
    st.markdown(f"Creates a multi-select box in the sidebar. Returns a list of selected options. Selected options: {multiselect_options}", unsafe_allow_html=True) 

def sidebar_elements():
    st.sidebar.title("Streamlit Sidebar Elements Cheat Sheet")

    button_elements()
    checkbox_elements()
    radio_elements()
    select_elements()
    multiselect_elements()
    
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
    
    init_page()

    st.title("Streamlit Sidebar Elements Cheat Sheet")
    st.write("Explore different Streamlit sidebar elements and see how they work.")
    sidebar_elements()

if __name__ == "__main__":
    main()
