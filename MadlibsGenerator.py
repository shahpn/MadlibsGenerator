# mad_libs_web.py

import streamlit as st

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
if st.button("Generate Story"):
    if all([name, place, animal, emotion, action]):
        story = (
            f"One day, {name} went to {place} and found a giant {animal} 🐾!\n\n"
            f"It was {action} around and looked very {emotion}.\n\n"
            f"So {name} ran away screaming, 'I’ll never go to {place} again!'"
        )
        st.markdown("### 🎉 Here's your story:")
        st.success(story)
    else:
        st.warning("⚠️ Please fill in all the blanks before generating your story.")

st.markdown("---")
st.caption("Made with 💻 and 😄 using Streamlit")
