import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
import google.generativeai as genai
import re

# Configure Gemini API
genai.configure(api_key="AIzaSyCKxZNq-OljRT__R6tVggAst-_5fAURlzY")

st.title("🎥 YouTube Video Summarizer with Gemini AI")
st.markdown("Paste a YouTube video URL below to get a summarized version of the video content using Gemini AI.")

video_url = st.text_input("🔗 YouTube Video URL")

def extract_video_id(url):
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url)
    return match.group(1) if match else None

if video_url:
    video_id = extract_video_id(video_url)
    if video_id:
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en', 'hi'])
            transcript_text = " ".join([entry['text'] for entry in transcript])
            st.success("✅ Transcript retrieved successfully!")

            # Use correct Gemini model and method
            model = genai.GenerativeModel("models/gemini-2.5-pro")

            st.markdown("📋 **Summary:**")
            with st.spinner("Generating summary..."):
                response = model.generate_content(f"Summarize this YouTube video transcript:\n\n{transcript_text}")
                st.write(response.text)

        except (TranscriptsDisabled, NoTranscriptFound):
            st.error("❌ Transcript not available for this video in English or Hindi.")
        except Exception as e:
            st.error(f"❌ Error generating summary: {e}")
    else:
        st.error("❌ Invalid YouTube URL.")