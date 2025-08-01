# 🎥 YouTube Video Summarizer with Gemini AI

This Streamlit app allows users to **summarize YouTube videos** using the **video transcript** and **Google Gemini (Gemini 1.5 Pro)**.

Just paste a YouTube video URL and get a concise summary in seconds!

---

## 🚀 Features

- 🔗 Input any YouTube URL
- 🧠 Retrieves the transcript (in English or Hindi)
- ✨ Summarizes the video content using **Gemini 2.5 Pro**
- ⚠️ Handles missing transcripts gracefully
- 🌐 Easy-to-use web interface powered by Streamlit

---

## 📸 Demo

![demo-screenshot](https://user-images.githubusercontent.com/your-screenshot.png)

---

## 🛠️ Installation

### 1. Clone the Repo

```bash
git clone https://github.com/UtkarshaKakulte/youtube-gemini-summarizer.git
cd youtube-gemini-summarizer
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

> Requirements:

```txt
streamlit
google-generativeai
youtube-transcript-api
```

### 3. Run the App

```bash
streamlit run app.py
```

---

## 🔑 Setup Gemini API Key

Before running the app, set your **Gemini API key**:

You can set it in the code:

```python
genai.configure(api_key="YOUR_API_KEY")
```

Or securely using an environment variable:

```bash
export GOOGLE_API_KEY=your_key_here  # for Linux/macOS
set GOOGLE_API_KEY=your_key_here     # for Windows
```

Update code to:

```python
import os
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
```

---

## 📁 File Structure

```
📦 youtube-gemini-summarizer/
├── app.py                  # Streamlit app script
├── requirements.txt        # Python dependencies
├── README.md               # You're here!
```

---

## ⚠️ Limitations

* Only works with videos that have transcripts available in **English or Hindi**
* API usage is based on Gemini quotas (check limits)
* Doesn't work for YouTube Shorts or Livestreams without transcripts

---

## 📚 Example Use Case

| YouTube URL                             | Summary Output                   |
| --------------------------------------- | -------------------------------- |
| `https://youtube.com/watch?v=abc123xyz` | “This video discusses how AI...” |

---

## ✨ Credits

* Built with [Streamlit](https://streamlit.io/)
* Powered by [Google Generative AI](https://ai.google.dev/)
* Transcripts via [youtube-transcript-api](https://pypi.org/project/youtube-transcript-api/)

---

## 📜 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 🙌 Created By

**[@UtkarshaKakulte](https://github.com/UtkarshaKakulte)**
✨ Empowering search, learning, and video content digestion with AI!
