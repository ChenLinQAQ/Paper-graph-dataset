# coding:utf-8
import fitz
import re
import os


def pdf2image(path, pic_path):
    checkIM = r"/Subtype(?= */Image)"
    pdf = fitz.open(path)
    lenXREF = pdf.xref_length()
    print(lenXREF)
    count = 1
    for i in range(1, lenXREF):
        text = pdf.xref_object(i)
        # print(text)
        isImage = re.search(checkIM, text)
        if not isImage:
            continue
        print(checkIM)
        print("==============")
        print(text)
        print("is image")
        pix = fitz.Pixmap(pdf, i)
        new_name = f"img_{count}.png"
        print(new_name)
        print(pix)
        pix.save(os.path.join(pic_path, new_name))
        count += 1
        pix = None


pdf2image("pdf_set/3.pdf", "graph")
