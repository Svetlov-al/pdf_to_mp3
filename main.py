from gtts import gTTS
import PyPDF2

filepath = 'Path to pdf_file'


def extract_text_from_pdf(path):
    with open(filepath, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
            print("File was readed succesfully")
        return text


def main():
    try:
        text = extract_text_from_pdf(filepath)
        language = 'en'
        my_audio = gTTS(text=text, lang=language, slow=False)
        print("Trying save file!")
        my_audio.save('my_audio.mp3')
        print("Work was finished!")
    except Exception as ex:
        print(f"Something went wrong! Error : {ex}")


if __name__ == '__main__':
    main()
