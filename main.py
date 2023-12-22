import sys
from PyQt5.QtWidgets import QApplication
from gui import AppWindow
from openai import OpenAI
import os
from dotenv import load_dotenv
from docx import Document

from PyQt5.QtCore import QObject, QThread, pyqtSignal

class Worker(QObject):
    finished = pyqtSignal(str)  # Signal to indicate completion
    error = pyqtSignal(Exception)  # Signal for errors

    def __init__(self, client, model, query, max_tokens, temperature):
        super().__init__()
        self.client = client
        self.model = model
        self.query = query
        self.max_tokens = max_tokens or 800
        self.temperature = temperature or 0.1

    def run(self):
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": self.query}],
                max_tokens=self.max_tokens,
                temperature=self.temperature
            )
            answer = response.choices[0].message.content
            self.finished.emit(answer)  # Emit the result
        except Exception as e:
            self.error.emit(e)  # Emit the error


class OpenAIChatApp:
    def __init__(self):
        load_dotenv()
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = "gpt-3.5-turbo"  # Model used

        self.app = QApplication(sys.argv)
        self.main_window = AppWindow(self.submit_query,  self.save_response_to_docx)
        self.main_window.show()

        with open("style.css", "r") as f:
            self.app.setStyleSheet(f.read())

    def submit_query(self, query, max_tokens=None, temperature=None):
        # Set default values if None
        max_tokens = max_tokens or 800
        temperature = temperature or 0.1

        # Create a QThread object
        self.thread = QThread()
        self.worker = Worker(self.client, self.model, query, max_tokens, temperature)

        # Move worker to the thread
        self.worker.moveToThread(self.thread)

        # Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.finished.connect(self.handle_response)
        self.worker.error.connect(self.handle_error)

        # Start the thread
        self.thread.start()

    def handle_response(self, answer):
        self.main_window.output_text_edit.setText(answer)
        self.main_window.status_bar.showMessage("Response received")


    def handle_error(self, e):
        print(f"An error occurred: {e}")
        self.main_window.status_bar.showMessage(f"Error: {e}")


    def save_response_to_docx(self, file_path):
        doc = Document()
        doc.add_paragraph(self.main_window.output_text_edit.toPlainText())
        doc.save(file_path)

    def run(self):
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    chat_app = OpenAIChatApp()
    chat_app.run()
