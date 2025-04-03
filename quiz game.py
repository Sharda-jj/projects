import streamlit as st

st.title("Welcome to Fun Quiz")

playing = st.text_input("Do you want to play? (yes/no)").lower()

if playing == "yes":
    st.write("Ok! Let's play ")

    # Question 1
    answer = st.text_input("What is the full form of UPSC you? ")
    if answer:
        if answer.lower() == "union public service commission":
            st.success("CORRECT!")
        else:
            st.error("INCORRECT!")

    # Question 2
    answer = st.text_input("Which state in India is the largest in terms of population? ")
    if answer:
        if answer.lower() == "uttar pradesh":
            st.success("CORRECT!")
        else:
            st.error("INCORRECT!")

    # Question 3
    answer = st.text_input("Who was the first PM of India? ")
    if answer:
        if answer.lower() == "jawaharlal nehru":
            st.success("CORRECT!")
        else:
            st.error("INCORRECT!")

    # Question 4
    answer = st.text_input("How many minutes are in a full week? ")
    if answer:
        if answer.lower() == "10,080":
            st.success("CORRECT!")
        else:
            st.error("INCORRECT!")

    # Question 5
    answer = st.text_input("Which planet has the most moons? ")
    if answer:
        if answer.lower() == "saturn":
            st.success("CORRECT!")
        else:
            st.error("INCORRECT!")

    # Last Question
    answer = st.text_input("How was the quiz? ")
    if answer:
        st.success("Thanks for the feedback!")

else:
    st.write("You chose not to play. See you next time!")

