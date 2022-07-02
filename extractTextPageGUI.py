import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

from pjeutils.extractTextPage import extractPDF


# # create the root window
# root = tk.Tk()
# root.title('Tkinter Open File Dialog')
# root.resizable(False, False)
# root.geometry('300x150')
#
#



# def openPDF():
filetypes = (
    ('Arquivos Adobe PDF', '*.pdf'),
    ('Todos os arquivos', '*.*')
)

filename = fd.askopenfilename(
    title='Abrir arquivo',
    initialdir='G:\Meu Drive\Gabinete',
    filetypes=filetypes)

extractPDF(filename)


# # open button
# open_button = ttk.Button(
#     root,
#     text='Open a File',
#     command=openPDF()
# )
#
# open_button.pack(expand=True)
#
#
# # run the application
# root.mainloop()
#
