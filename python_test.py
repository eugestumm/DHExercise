import os
import tkinter as tk
from tkinter import filedialog
import platform
import subprocess

class MarkdownConverter(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Markdown Converter")
        self.pack(padx=20, pady=20)

        self.info_label = tk.Label(self, text="This program converts Markdown files to PDF and PPTX.")
        self.info_label.pack(pady=10)

        self.pdf_button = tk.Button(self, text="Convert to PDF", command=self.convert_to_pdf)
        self.pdf_button.pack(side="left", padx=10)

        self.pptx_button = tk.Button(self, text="Convert to PPTX", command=self.convert_to_pptx)
        self.pptx_button.pack(side="right", padx=10)

    def convert_to_pdf(self):
        file_path = filedialog.askopenfilename()
        base_name = os.path.splitext(file_path)[0]
        pdf_path = base_name + ".pdf"

        if platform.system() == "Windows":
            # Windows-specific command to run pandoc
            subprocess.run(f"pandoc.exe {file_path} -o {pdf_path}")
        else:
            # Linux and macOS command to run pandoc
            subprocess.run(f"pandoc {file_path} -o {pdf_path}", shell=True)

    def convert_to_pptx(self):
        file_path = filedialog.askopenfilename()
        base_name = os.path.splitext(file_path)[0]
        pptx_path = base_name + ".pptx"

        if platform.system() == "Windows":
            # Windows-specific command to run pandoc
            subprocess.run(f"pandoc.exe {file_path} -o {pptx_path} --slide-level=2")
        else:
            # Linux and macOS command to run pandoc
            subprocess.run(f"pandoc {file_path} -o {pptx_path} --slide-level=2", shell=True)

if __name__ == "__main__":
    root = tk.Tk()
    markdown_converter = MarkdownConverter(master=root)
    markdown_converter.mainloop()
