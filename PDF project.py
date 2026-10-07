from pathlib import Path
import fitz
import tkinter as tk
from tkinter import filedialog


def inspect_pdf(path: str):
    print(f"Inspecting PDF: {path}")
    pdf = fitz.open(path)

    print(f"Pages: {len(pdf)}")

    for page_number, page in enumerate(pdf):

        drawings = page.get_drawings()
        text = page.get_text("text")

        print(
            f"Page {page_number + 1}: "
            f"{len(drawings)} vector objects, "
            f"{len(text)} text characters"
        )


if __name__ == "__main__":

    root = tk.Tk()
    root.withdraw()

    pdf_path = filedialog.askopenfilename(
        title="Select Architectural PDF",
        filetypes=[
            ("PDF files", "*.pdf"),
            ("All files", "*.*")
        ]
    )

    if not pdf_path:
        print("No PDF selected.")
    else:
        inspect_pdf(pdf_path)