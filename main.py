import pyttsx3
import PyPDF2

with open('storeBook/RDPD.pdf', 'rb') as file: #add the pdf file you want to listen here int first parameter
    pdf_reader = PyPDF2.PdfReader(file)

    audio_reader = pyttsx3.init()
    audio_reader.setProperty("rate", 130)

    for page in range(len(pdf_reader.pages)):
        next_page = pdf_reader.pages[page]
        content = next_page.extract_text()

        audio_reader.say(content)
        audio_reader.runAndWait()
