import os
import pyttsx3
from PyPDF2 import PdfReader

# Replace 'file.pdf' with the path to your PDF file
pdfreader = PdfReader(open('file.pdf', 'rb'))

reader = pyttsx3.init()

# Set the output path to the Downloads folder
output_path = os.path.join(os.path.expanduser("~"), "Downloads")

# Use len(reader.pages) instead of reader.numPages
for page in range(len(pdfreader.pages)):
    text = pdfreader.pages[page].extract_text()
    legible_text = text.strip().replace('\n', ' ')
    print(legible_text)
    reader.say(legible_text)

    # Save the audio file to the Downloads folder
    reader.save_to_file(legible_text, os.path.join(output_path, 'Olgierd.mp3'))

reader.runAndWait()
reader.stop()
