# mad_libs_web.py
import os
import openai
import streamlit as st
from dotenv import load_dotenv


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Mad Libs Generator", page_icon="🧠")

st.title("🧠 Mad Libs Generator")
st.markdown("Fill in the blanks below to create your own silly story!")

# Input fields
name = st.text_input("Enter a name")
place = st.text_input("Enter a place")
animal = st.text_input("Enter an animal")
emotion = st.text_input("Enter an emotion")
action = st.text_input("Enter a verb ending in -ing")

# Generate story on button press
# if st.button("Generate Story"):
#     if all([name, place, animal, emotion, action]):
#         story = (
#             f"One day, {name} went to {place} and found a giant {animal} 🐾!\n\n"
#             f"It was {action} around and looked very {emotion}.\n\n"
#             f"So {name} ran away screaming, 'I’ll never go to {place} again!'"
#         )
#         st.markdown("### 🎉 Here's your story:")
#         st.success(story)
#     else:
#         st.warning("⚠️ Please fill in all the blanks before generating your story.")

if st.button("Generate Story"):
    if all([name, place, animal, emotion, action]):
        with st.spinner("Generating your story... ✨"):

            prompt = (
                f"Create a fun and silly Mad Libs-style short story using the following words:\n"
                f"- Name: {name}\n"
                f"- Place: {place}\n"
                f"- Animal: {animal}\n"
                f"- Emotion: {emotion}\n"
                f"- Action (verb ending in -ing): {action}\n\n"
                f"The story should be no more than 5 sentences and written like a children's story."
            )

            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a playful storyteller."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.9
                )

                story = response['choices'][0]['message']['content'].strip()
                st.markdown("### 🎉 Here's your AI-generated story:")
                st.success(story)

            except Exception as e:
                st.error(f"Something went wrong: {e}")

    else:
        st.warning("⚠️ Please fill in all the blanks before generating your story.")

st.markdown("---")
st.caption("Made with 💻 and 😄 using Streamlit")
