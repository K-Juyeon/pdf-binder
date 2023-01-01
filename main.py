from tkinter import *
import os
from tkinter import filedialog
from PyPDF2 import PdfFileReader, PdfFileWriter

window = Tk()
window.title("PDF 분할")
window.geometry('300x150')
window.resizable(False, False)

def clicked_1():
    window.dir_path = filedialog.askopenfilename(parent=window, title='파일 선택',
                                                 filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
    Label(window, text=window.dir_path).pack()

def clicked_2():
    pdf_name = window.dir_path

    fname = os.path.splitext(pdf_name)[0]

    pdf = PdfFileReader(pdf_name)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
        output = f'{fname}_{page + 1}.pdf'

        with open(output, 'wb') as out:
            pdf_writer.write(out)

Label(window, text=" ").pack()
button = Button(window, text="파일선택", bg="gray", fg="white", command=clicked_1).pack()
Label(window, text=" ").pack()
button = Button(window, text="분할실행", bg="gray", fg="white", command=clicked_2).pack()
Label(window, text=" ").pack()

window.mainloop()