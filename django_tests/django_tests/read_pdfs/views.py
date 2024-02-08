from django.shortcuts import render
# from arelle import ModelManager, Cntlr
import PyPDF2 



# Create your views here.


def read_pdf(request):
    template_name = "read_pdfs/pdf.html"

    # start_text = '9900'
    start_text = '9087'

    pdf_path = './read_pdfs/files/fosfari.pdf'

    text = ""

    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            page_text = page.extract_text()

            text += page_text

            # Search for the start_text in the page
            start_index = page_text.find(start_text)
            if start_index != -1:
                # Extract the data point following the start_text (adjust the range as needed)
                data_point = page_text[start_index : start_index + 25]
                # print(data_point.strip())  # Trim leading and trailing spaces
                data_point = data_point.split('\n')
                data_point = data_point[0].split(' ')

                print(data_point)
                

    

    
    context = {
        'text' : text

    }
    

    return render(request, context=context, template_name=template_name)


def read_xbrl(request):
    template_name = "read_pdfs/xbrl.html"

    print('start')

    xbrl_file_path = './read_pdfs/files/colruyt.xbrl'
    

    # model_xbrl = Cntlr.Cntlr().modelManager.load(xbrl_file_path)
    

    # # model_manager = ModelManager.initialize(cntlr)
    # # model_xbrl = model_manager.load(xbrl_file_path)

    # # for fact in model_xbrl.facts:
    # #     print(fact)
    
    # print(model_xbrl.facts)

    
    # model_xbrl.close()

    

    xbrl_parser = XBRLParser()
    xbrl = xbrl_parser.parse(file_path)

    # Iterate through facts and extract data
    for fact in xbrl.facts:
        print(fact.name, fact.value)


    # xbrl = Cntlr.Cntlr().modelManager.load('https://www.sec.gov/Archives/edgar/data/101984/000010198416000062/ueic-20151231.xml')
    # for fact in xbrl.facts:
    #     print(fact) 

    context = {

    }
    

    return render(request, context=context, template_name=template_name)


