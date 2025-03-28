import streamlit as st

st.title("Welcome to Love Quiz 😎")

playing = st.text_input("Do you want to play? (yes/no)").lower()

if playing == "yes":
    st.write("Ok! Let's play 😊")

    # Question 1
    answer = st.text_input("Who is the most beautiful girl for you? 🤔")
    if answer:
        if answer.lower() == "shraddha":
            st.success("CORRECT! 🤗")
        else:
            st.error("INCORRECT! 😡")

    # Question 2
    answer = st.text_input("Do you love Shraddha/Sharda? ❤️")
    if answer:
        if answer.lower() == "yes":
            st.success("CORRECT! ❤️")
        else:
            st.error("INCORRECT! 💔")

    # Question 3
    answer = st.text_input("Which is her favourite sweet? 🍬")
    if answer:
        if answer.lower() == "chumchum":
            st.success("CORRECT! 🤤")
        else:
            st.error("INCORRECT 🤢!")

    # Question 4
    answer = st.text_input("What is her favourite hobby? 🎤")
    if answer:
        if answer.lower() == "to talk and gossip with mayuresh":
            st.success("CORRECT! 🤥")
        else:
            st.error("ITNA BHI NAHI PATA! 😱")

    # Question 5
    answer = st.text_input("What does she want to achieve in life? 🌠")
    if answer:
        if answer.lower() == "peace and to watch northern lights":
            st.success("CORRECT! 🎇")
        else:
            st.error("YOU BETTER ASK HER! 🤨")

    # Last Question
    answer = st.text_input("What is your life without her? ❤️")
    if answer:
        st.success("CORRECT! ❤️ 😍😘")

else:
    st.write("You chose not to play. See you next time! 👋")

