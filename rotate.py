import PyPDF2
def PDFrotate(original,new,rotation):
    # Creating a pdf File object of original Pdf
    pdfFileObj=open(original,'rb')
    #Creating a pdf Reader object
    pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
    #creating a pdf writer Object for new pdf
    pdfWriter=PyPDF2.PdfFileWriter()
    # rotating each page
    for page in range(pdfReader.numPages):
        #creating rotated page object
        pageObj=pdfReader.getPage(page)
        pageObj.rotateClockwise(rotation)

        #adding rotated page object to pdf writer
        pdfWriter.addPage(pageObj)

    #new pdf file object
    newFile=open(new,'wb')
    #writing rotated pages to new file
    pdfWriter.write(newFile)
    #closing the original pdf file object
    pdfFileObj.close()
    #closing the new pdf file object
    newFile.close()

def main():
     
        original="mobile.pdf"
        new="mobile2.pdf"
        rotation=270
        PDFrotate(original,new,rotation)

if __name__=="__main__":
    main()
    
    
