import streamlit as st
from googletrans import Translator
from gtts import gTTS
from tempfile import NamedTemporaryFile
from streamlit_option_menu import option_menu

# Function to translate text
def translate_text(text, dest_lang):
    translator = Translator()
    translated_text = translator.translate(text, src='en', dest=dest_lang)
    return translated_text.text

# Function to convert text to audio
def convert_to_audio(text, lang):
    tts = gTTS(text=text, lang=lang)
    temp_file = NamedTemporaryFile(delete=False)
    tts.save(temp_file.name)
    return temp_file.name

# Function to display a cool title
def cool_title(title_text):
    st.markdown(
        f"""
        <div style="background-color:#f63366;padding:10px;border-radius:10px;font-family: 'Times New Roman', Times, serif;">
        <h1 style="color:white;text-align:center;">{title_text}</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Main Function
def main():
    cool_title("💖 Love Story Translator")
    st.header("Enter Your Love Story and Translate It into Multiple Languages!")

    # Menu for language selection
    selected = option_menu(
        menu_title="Select Language",
        options=["English", "Hindi", "Punjabi", "Marathi", "Telugu"],
        menu_icon="globe",
        default_index=0,
        orientation="horizontal"
    )

    # User inputs a love story
    love_story = st.text_area("Enter your love story in English:", height=200)

    if st.button("Translate & Generate Audio"):
        if love_story.strip() == "":
            st.warning("Please enter a love story before translating.")
        else:
            with st.spinner("Translating your love story..."):

                # Translations
                hindi_text = translate_text(love_story, "hi")
                punjabi_text = translate_text(love_story, "pa")
                marathi_text = translate_text(love_story, "mr")
                telugu_text = translate_text(love_story, "te")

                # Display translated text and audio
                if selected == "English":
                    st.subheader("Original Love Story in English")
                    st.write(love_story)
                    st.audio(convert_to_audio(love_story, "en"), format='audio/mp3')

                elif selected == "Hindi":
                    st.subheader("❤️ Love Story in Hindi")
                    st.write(hindi_text)
                    st.audio(convert_to_audio(hindi_text, "hi"), format='audio/mp3')

                elif selected == "Punjabi":
                    st.subheader("💖 Love Story in Punjabi")
                    st.write(punjabi_text)
                    st.audio(convert_to_audio(punjabi_text, "pa"), format='audio/mp3')

                elif selected == "Marathi":
                    st.subheader("💘 Love Story in Marathi")
                    st.write(marathi_text)
                    st.audio(convert_to_audio(marathi_text, "mr"), format='audio/mp3')

                elif selected == "Telugu":
                    st.subheader("💕 Love Story in Telugu")
                    st.write(telugu_text)
                    st.audio(convert_to_audio(telugu_text, "te"), format='audio/mp3')

if __name__ == "__main__":
    main()