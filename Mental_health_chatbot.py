import streamlit as st
from groq import Groq
import base64
import os

st.set_page_config(page_title = "Mental Health Chatbot")

#def get_base64(background):
#    with open(background,"rb") as f:
#        data = f.read()
#    return base64.b64encode(data).decode()

#bin_str = get_base64("background.png")


#st.markdown(f"""
#        <style>
#            .main{{
#            background-image:url("data:image/png;base64,{bin_str}");
#            background-style: cover;
#            background-position: center;
#            background-repeat: no-repeat;

#            }}
#        </style>
#        """,unsafe_allow_html = True)

st.session_state.setdefault('conversation_history',[])

def generate_response(user_input):

    client = Groq(api_key="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")

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_input,
            }
        ],
        model="llama-3.1-8b-instant",
    )

    return chat_completion.choices[0].message.content


def generate_affirmation():
    prompt = "provide a positive affirmation to encourage someone who is feeling \n            stressed or overwhelmed"
    client = Groq(api_key="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")

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_message,
            }
        ],
        model="llama-3.1-8b-instant",
    )

    return chat_completion.choices[0].message.content

def generate_meditation_guide():
    prompt = "Provide a 5-min guided meditation script to help someone relax and \n reduce     stress"
    client = Groq(api_key="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")

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_message,
            }
        ],
        model="llama-3.1-8b-instant",
    )

    return chat_completion.choices[0].message.content

st.title("Mental Health Support Agent")

for msg in st.session_state['conversation_history']:
    roles = 'You' if msg['role'] == 'user' else 'AI'
    st.markdown(f"**{msg['role']}:** {msg['content']}")

user_message = st.text_input("How can I help you today?")

#if user_message:
#    with st.spinner("Thinking...."):
#        ai_response = generate_response(user_message)
#        st.markdown(f"**AI:** {ai_response}")

col1 , col2 = st.columns(2)

with col1:
    if st.button('Give me a positive Affirmation'):
        affirmation = generate_affirmation()
        st.markdown(f"**Affirmation:** {affirmation}")

with col2:
    if st.button("Give me a guided meditation"):
        meditation_guide = generate_meditation_guide()
        st.markdown(f"**Guided Meditation:** {meditation_guide}")
        
    










