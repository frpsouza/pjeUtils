import re, os, csv

import PyPDF2


def bookmark_dict(bookmark_list):
    result = {}
    for item in bookmark_list:
        if isinstance(item, list):
            # recursive call
            result.update(bookmark_dict(item))
        else:
            try:
                result[reader.getDestinationPageNumber(item) + 1] = item.title
            except:
                pass
    return result


def extractPDF(filename):
    with open(filename, 'rb') as pdf_file:
        reader = PyPDF2.PdfFileReader(pdf_file)
        metadata = reader.getDocumentInfo()
        outlines = reader.getOutlines()
        numPages = reader.getNumPages()

        print(metadata)
        print(numPages)
        print(outlines)

        os.chdir('C:/Users/frpso/PycharmProjects/pythonProject/pjeutils')
        with open('output.csv', 'a') as f:
            write = csv.writer(f)

            for bkm in outlines[1:10]:
                write.writerow(bkm)


                line = ""
                print("\n")
                print("Title=", bkm.title)
                numPage = reader.getDestinationPageNumber(bkm)
                print("Page ", numPage)

                pdfPage = reader.getPage(numPage)

                text = pdfPage.extractText()

                re1 = re.compile("(Assinado eletronicamente por: )")
                re2 = re.compile(
                    r"(https...pje.trt4.jus.br.segundograu.Processo.ConsultaDocumento.listView.seam.nd=\d{29})")

                b = re.search(re1, text)
                e = re.search(re2, text)

                if not (b is None or e is None):
                    line = text[b.start():e.start()].rstrip()
                    line = line[30:]
                    print(line)
                    m = re.match(
                        r"(?P<signatario>([A-Z]+\s){2,})-\s(?P<data>((\d{2}/){2}\d{4}))\s(?P<hora>\d{2}:\d{2})\s-\s(?P<ID>[0-f]{7})",
                        line)
                    print(m.groupdict())

                    # pageDict = {'signatario': 'Advogado', 'data': '10/11/2010', 'hora': '04:20', 'ID': 'C0FFEE',
                    #             'url': 'https://pje.trt4.jus.br', 'processo': '0012345-dd.20yy.5.04.vvvv',
                    #             'doc': '01234567890123456789012345678'}
