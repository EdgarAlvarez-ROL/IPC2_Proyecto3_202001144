from contextlib import ContextDecorator
from xml.etree.ElementTree import ProcessingInstruction
from matplotlib.pyplot import text, xlim
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import re


from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY

# c = canvas.Canvas("hola-mundo.pdf")
# c.save()
import time



def recibirText():
    file = 'BackEnd0\\textPDF.txt'


    archivo = open(file, 'r') # abre el archivo datos.txt
    text = archivo.readlines()
    # print(archivo.readline())
    archivo.close()

    xo = ''
    for x in text:
        pa = x.replace("\n", "<br />")
        xo += pa
        # xo += "<br />"
    
    
    print('Generando PDF')
    # print(xo)

    doc = SimpleDocTemplate(
    "PDF Proyecto3.pdf",
    pagesize=A4
    )
    paragraph = Paragraph(
        xo,
        ParagraphStyle(
            "ps1",
            fontName="Times-Roman",
            fontSize=11
        )
    )
    doc.build([paragraph])

    # x = text[0].replace(">", "><br />") #">\n"

    # w, h = A4
    # c = canvas.Canvas("PDF Proyecto3.pdf", pagesize=A4)
    # c.drawString(50, h - 50, x)
    # c.showPage()
    # c.save()

# recibirText()