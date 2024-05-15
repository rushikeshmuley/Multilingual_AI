import streamlit as st
from src.helper import voice_input, llm_model_object, text_to_speech
import base64

def main():
    st.title("🎙️ Multilingual AI Voice Assistant 🤖")
    if st.button("🗣️ Ask me anything"):
        with st.spinner("👂 Listening..."):
            try:
                text = voice_input()
                st.text("🎤 Speech Recognition thinks you said: " + text)
                response = llm_model_object(text)
                text_to_speech(response)

                st.text_area("📋 Response:", value=response)

                with open("audio.mp3", "rb") as audio_file:
                    audio_bytes = audio_file.read()
                st.audio(audio_bytes, format="audio/mp3")

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
