import PyPDF2
def add_watermark(wmFile,pageobj)
    #opening watermark pdf file
    wmFileObj=open(wmFile,'rb')
    #creating pdf reader object of watermark pdf file
    pdfReader=PyPDF2.PdfFileReader(wmFileObj)
    #merging watermark pdf's first page with passed page object.
    pageObj.mergePage(pdfReader.getPage(0))
    #closing the watermark pdf file object
    wmFileObj.close()
    #returning watermarked page object
    return pageObj

def main():
    #watermark pdf file name
    mywatermark='mobile.pdf'
    #original pdf file name
    origFileName='mobile2.pdf'
    newFileName='mobile4.pdf'
    pdfFileObj=open(origFileName,'rb')
    pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
    pdfWriter=PyPDF2.PdfFileWriter()

    for page in range
    
