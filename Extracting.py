#importing required modules
import PyPDF2
#Creating a pdf file object
pdfFileObj=open('mobile.pdf','rb')
#creating a pdf reader object
pdfReade=PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReade.numPages)
pageObj=pdfReade.getPage(0)
print(pageObj.extractText())
pdfFileObj.close()
