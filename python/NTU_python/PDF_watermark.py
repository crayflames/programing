#! /usr/bin/python3.5
import PyPDF2
import os
os.chdir(r'/home/roger/Downloads')

pdfFile = open('ror.pdf', 'rb')

reader = PyPDF2.PdfFileReader(pdfFile)
writer = PyPDF2.PdfFileWriter()

watermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))

watermark = watermarkReader.getPage(0)
# 給每張加上浮水印
for pageNum in range(reader.numPages):
    page = reader.getPage(pageNum)
    page.mergePage(watermark)
    writer.addPage(page)

outputPdf = open('all_watermark_ror.pdf', 'wb')
writer.write(outputPdf)
outputPdf.close()
