# streamlit run EXERCISES\MODULE-01\exercise-04\app.py
import streamlit as st

image_path = 'EXERCISES/MODULE-01/exercise-04/2-object-detection/image/kitten-dog.jpg'

# Câu 1
with st.expander('Câu 1'):
    st.markdown("**:blue[st.text]**")
    st.text('Hello World!')

    st.markdown("**:blue[st.image]**")
    st.image(image_path)

    st.markdown("**:blue[st.selectbox]**")
    selected_option = st.selectbox(
        'Select an option', ['Option 1', 'Option 2', 'Option 3'])
    st.write('Selected option:', selected_option)

    st.markdown("**:blue[st.slider]**")
    selected_value = st.slider(
        'Select a value', min_value=0, max_value=100, value=50)
    st.write('Selected value:', selected_value)

# Câu 2
with st.expander('Câu 2'):
    st.markdown("**:blue[st.multiselect]**")
    options = st.multiselect('Your favorite colors:', [
                             'Green', 'Yellow', 'Red', 'Blue'], ['Yellow', 'Red'])
    st.write('Your selected:', options)

# Câu 3
with st.expander('Câu 3'):
    st.markdown("**:blue[st.text_input]**")
    name = st.text_input('Enter your name')
    st.write('Your name is:', name)

# Câu 4
with st.expander('Câu 4'):
    st.markdown("**:blue[st.image(image_path, caption, width, channels)]**")
    st.image(image_path, caption='A cat', width=100, channels='RGB')
    st.image(image_path, caption='A cat', width=None, channels='BGR')


# Câu 6
with st.expander('Câu 6'):
    st.markdown("**:blue[st.session_state]**")

    st.write(st.session_state)

    with st.form('my_form_6'):
        if 'username' not in st.session_state:
            st.text_input('Enter your name', key='username')
        submitted = st.form_submit_button('Submit')
        if submitted:
            st.write('Hello,', st.session_state['username'])

    if st.button('Clear All Session State in Question 6'):
        st.session_state.clear()
        st.write('All session state in Question 6 cleared.')

# Câu 7
with st.expander('Câu 7'):
    st.markdown("**:blue[st.columns]**")
    with st.form('my_form_7'):
        col1, col2 = st.columns(2)
        f_name = col1.text_input('First Names')
        l_name = col2.text_input('Last Name')
        submitted = st.form_submit_button('Submit')
        if submitted:
            st.write('First Name: ', f_name, ' Last Name: ', l_name)

# Câu 8
with st.expander('Câu 8'):
    st.markdown(
        "**:blue[st.file_uploader('Choose files', accept_multiple_files=True]**")
    uploađe_files = st.file_uploader(
        'Choose files', accept_multiple_files=True)

# Câu 9
with st.expander('Câu 9'):
    st.markdown("**:blue[code example:]**")
    code_example = """
    def greet(name):
        print(f"Hello, {name}!")
    """
    st.text(code_example)

    st.markdown("**:blue[st.code(code_string, language)]**")
    st.code(code_example, language="python")

    st.markdown("**:blue[st.echo]**")
    with st.echo():
        def greet(name):
            print(f"Hello, {name}!")

    st.markdown("**:blue[st.markdown]**")
    st.markdown(code_example)

