import streamlit as st

st.title("💬 Chatbot")

if "name" not in st.session_state:
    st.session_state.name = None

if "interest" not in st.session_state:
    st.session_state.interest = None

user_input = st.text_input("You:")

if user_input:
    user_input = user_input.lower()

    if "hi" in user_input or "hello" in user_input:
        st.write("Chatbot: Hello! 😊 What's your name?")

    elif "my name is" in user_input:
        st.session_state.name = user_input.split("my name is")[-1].strip()
        st.write(f"Chatbot: Nice to meet you {st.session_state.name}! What are you interested in?")

    elif "i like" in user_input:
        st.session_state.interest = user_input.split("i like")[-1].strip()
        st.write(f"Chatbot: Wow! I like {st.session_state.interest} too 😄")

    elif "what is my name" in user_input:
        if st.session_state.name:
            st.write(f"Chatbot: Your name is {st.session_state.name}")
        else:
            st.write("Chatbot: I don't know your name yet.")

    elif "what do i like" in user_input:
        if st.session_state.interest:
            st.write(f"Chatbot: You like {st.session_state.interest}")
        else:
            st.write("Chatbot: I don't know your interest yet.")

    else:
        st.write("Chatbot: Sorry, I didn't understand that.")