#importing required modules
import PyPDF2
def PDFmerge(pdfs,output):
    #creating pdf file merger object
    pdfMerger=PyPDF2.PdfFileMerger()
    #appending pdfs one by one
    for pdf in pdfs:
        with open(pdf,'rb')as f:
             pdfMerger.append(f)

    #writting combined pdf to output pdf file
    with open(output,'wb')as f:
           pdfMerger.write(f)

def main():
    #pdf files to merge
    pdfs=['mobile.pdf','mobile2.pdf']

    #output pdf file name
    output='mobile3.pdf'
    PDFmerge(pdfs=pdfs,output=output)
if __name__=="__main__":
    #calling the main function
    main()
