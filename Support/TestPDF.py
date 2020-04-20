#ResumeBuilder
#Evangellos Wiegers
#April 17, 2020

from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.platypus import (SimpleDocTemplate, Paragraph, PageBreak)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import LETTER
from reportlab.platypus import HRFlowable
from reportlab.lib.colors import gray, lightgrey, black
import shutil

#just a simple test of reportlab PDF generation

if __name__ == '__main__':
    file_name = "test.pdf"
    doc = SimpleDocTemplate(file_name, pagesize=LETTER)

    styles = getSampleStyleSheet()
    print(styles.list())
    elements = []
    elements.append(Paragraph("Title", styles["Title"]))
    elements.append(Paragraph("BodyText", styles["BodyText"]))
    elements.append(Paragraph("Bullet", styles["Bullet"]))
    elements.append(Paragraph("Code", styles["Code"]))
    elements.append(Paragraph("Definition", styles["Definition"]))

    elements.append(HRFlowable(width="100%", thickness=2, lineCap='round', color=black, spaceBefore=2,
                               spaceAfter=2, hAlign='CENTER', vAlign='BOTTOM', dash=None))

    elements.append(Paragraph("Heading1", styles["Heading1"]))
    elements.append(Paragraph("Heading2", styles["Heading2"]))
    elements.append(Paragraph("Heading3", styles["Heading3"]))
    elements.append(Paragraph("Heading4", styles["Heading4"]))
    elements.append(Paragraph("Heading5", styles["Heading5"]))
    elements.append(Paragraph("Heading6", styles["Heading6"]))
    # elements.append(Paragraph("Hello", styles["OrderedList"]))

    elements.append(Paragraph("Italic", styles["Italic"]))
    elements.append(Paragraph("<b>Normal Bold</b>", styles["Normal"]))
    elements.append(Paragraph("Normal Normal", styles["Normal"]))
    elements.append(PageBreak())
    elements.append(Paragraph("You are in page 2", styles["Normal"]))

    doc.build(elements)


    shutil.move(file_name, "..")
