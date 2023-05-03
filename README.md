# simple_pdfreader

This is a simple Python script that reads a PDF file and converts its text content into audio using the pyttsx3 library.

To use this script, follow these steps:

Install Python on your computer (if you haven't already).
Install the required libraries - pyttsx3 and PyPDF2 - by running the following commands in your terminal:
pip install pyttsx3
pip install PyPDF2
Download the script and the PDF file that you want to listen to.
Edit the script by replacing the file path in the 'with open()' statement with the path to your PDF file.
Run the script in your terminal by typing: python main.py
The audio output will be played on your default audio output device.
Note: The script uses the default pyttsx3 voice, which can be changed by modifying the 'audio_reader.setProperty("voice", ...)' line in the script.