
# OpenAI GPT-3.5 Chat Interface

This Python-based graphical user interface (GUI) application facilitates interaction with OpenAI's GPT-3.5 model. Leveraging PyQt5, it provides a sleek, user-friendly platform for querying the AI model and viewing its responses. It features customizable query parameters and the ability to export conversations to a Word document.

## Features
- **Interactive Chat Interface**: Engage with OpenAI's GPT-3.5 model in a conversational manner.
- **Customizable Query Parameters**: Tailor AI responses by adjusting settings like maximum tokens and response temperature.
- **Save Conversations**: Export AI responses to a Word document for documentation and sharing.

## Installation

Ensure Python is installed on your system. This application depends on several libraries, including PyQt5, OpenAI, and python-docx.

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ManasiTilak/ChatGPTtoDocx
   cd GPTtoDocs

2. **Install the Required Packages**
   ```bash
   pip install -r requirements.txt

## Usage

Set up your OpenAI API key before running the application.

1. **API Key Configuration:**

   Create a .env file in the project directory and add your OpenAI API key:
   ```bash
   OPENAI_API_KEY=your_api_key_here

2. **Run the Application**

   ```bash
   python main.py


## Interacting with the Application

Enter your query in the input area and press 'Submit' to receive a response from GPT-3.5.

## Customize Settings:

Adjust 'Max Tokens' and 'Temperature' to explore different types of responses.

## Save the Conversation:

Use the 'Save to .docx' button to save the dialogue to a Word document.
## Screenshots

![Main Window](https://github.com/ManasiTilak/ChatGPTtoDocx/blob/main/Screenshots/mainwindow.png)
![Saving to .Doc](https://github.com/ManasiTilak/ChatGPTtoDocx/blob/main/Screenshots/savetodoc.png)
## Contributing

Contributions are welcome. Please fork the repository and submit a pull request with your changes.