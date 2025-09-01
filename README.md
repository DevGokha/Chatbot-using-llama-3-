# 🧠 Smart Study Buddy

A web application built with Streamlit and powered by the Google Gemini API to help you study more effectively.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)]

## ✨ Features

- **Text Summarization:** Paste in a large block of text and get a concise, bulleted summary.
- **Quiz Generation:** Automatically create multiple-choice questions based on your study material to test your knowledge.
- **Key Concept Explanations:** Identify and explain the most important concepts from your text in simple terms.

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **Language:** Python
- **LLM API:** Google Gemini API

## 🚀 Deployment

This application is deployed and live on Streamlit Community Cloud.

**Live App:** [https://zy3dpav8y6lkfhnncqwnus.streamlit.app/]

## ⚙️ Setup and Local Run

To run this project on your local machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/DevGokha/Smart-Study-Buddy-with-Gemini-.git]
    cd Smart-Study-Buddy-with-Gemini-
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv myenv
    source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create your secrets file:**
    - Create a folder named `.streamlit` in the main project directory.
    - Inside that folder, create a file named `secrets.toml`.
    - Add your API key to this file:
      ```toml
      GOOGLE_API_KEY = "AIzaSyBZUaNaMC5GOT5h6AqaHX3-Q_SRZy*****"
      ```

5.  **Run the app:**
    ```bash
    streamlit run main.py
    ```
