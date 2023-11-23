import streamlit as st

def login():
    st.title("Sign In")

    # Get username and password from the user
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Sign In"):
        if authenticate_user(username, password):
            st.success("Sign In Successful!")

            # Set a session state variable to switch pages
            st.session_state.page = "main"
        else:
            st.error("Invalid Credentials")

def authenticate_user(username, password):
    # Replace this with your authentication logic
    return username == "123" and password == "123"

def main_page():
    st.title("Welcome to the Main Page")
    st.write("Select:")

    # user_input = st.text_input("User Input")

    # if st.button("Submit"):
    #     st.success("Form Submitted!")

    st.button("Upload Surgery List")
    st.button("Activate Surgeries")
    st.button("Settings")

def main():
    # Takes back to login page
    if "page" not in st.session_state:
        st.session_state.page = "login"

    if st.session_state.page == "login":
        login()
    elif st.session_state.page == "main":
        main_page()

# Run the app
if __name__ == "__main__":
    main()
