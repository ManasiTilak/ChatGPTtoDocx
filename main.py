# main.py
import sys
from PyQt5.QtWidgets import QApplication
from gui import AppWindow
from openai import OpenAI
import os
from dotenv import load_dotenv
from docx import Document


class OpenAIChatApp:
    def __init__(self):
        load_dotenv()
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = "gpt-3.5-turbo"  # Adjust model as needed

        self.app = QApplication(sys.argv)
        self.main_window = AppWindow(self.submit_query,  self.save_response_to_docx)
        self.main_window.show()

        with open("style.css", "r") as f:
            self.app.setStyleSheet(f.read())

    def submit_query(self, query, max_tokens=None, temperature=None):
        # Set default values if None
        max_tokens = max_tokens or 100  # Default max_tokens
        temperature = temperature or 0.7  # Default temperature

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": query}],
                max_tokens=max_tokens,
                temperature=temperature
            )
            answer = response.choices[0].message.content
        except Exception as e:
            answer = f"An error occurred: {e}"

        self.main_window.output_label.setText(answer)

    def save_response_to_docx(self, file_path):
        doc = Document()
        doc.add_paragraph(self.main_window.output_label.text())
        doc.save(file_path)

    def run(self):
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    chat_app = OpenAIChatApp()
    chat_app.run()
