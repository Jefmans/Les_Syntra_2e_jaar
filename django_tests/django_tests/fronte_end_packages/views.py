from django.shortcuts import render

import pandas as pd

import plotly.graph_objects as go
import plotly.express as px

# Create your views here.

def ___(request):
    template_name = "fronte_end_packages/____.html"

    
    context = {

    }
    

    return render(request, context=context, template_name=template_name)



def overview(request):
    template_name = "fronte_end_packages/overview.html"

    my_bar_data = go.Bar(y=[2, 1, 3, 6])

    fig = go.Figure(
        data=[my_bar_data],
        layout_title_text="Our data object"
    )

    bar_graph = fig.to_html()


    df = px.data.iris()

    fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                    title="Using The add_trace() method With A Plotly Express Figure")

    fig.add_trace(
        go.Scatter(
            x=[2, 4],
            y=[4, 8],
            mode="lines",
            line=go.scatter.Line(color="gray"),
            showlegend=False)
    )
    
    iris_scatter = fig.to_html()

    # Read data from a csv
    z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')

    fig = go.Figure(data=[go.Surface(z=z_data.values)])

    fig.update_layout(title='Mt Bruno Elevation', autosize=False,
                    width=500, height=500,
                    margin=dict(l=65, r=50, b=65, t=90))

    three_d_chart = fig.to_html()

    context = {
        'bar_graph' : bar_graph,
        'iris_scatter' : iris_scatter,
        'three_d_chart' : three_d_chart,
    }
    

    return render(request, context=context, template_name=template_name)




from PIL import Image
import pytesseract
import cv2
from django.templatetags.static import static


def tesseract_view(request):
    # pytesseract.pytesseract.tesseract_cmd = r'C:/Users/Echos Bv/Desktop/github_repos/Les_Syntra_2e_jaar/django_tests/venv/Scripts/pytesseract.exe'

    pytesseract.pytesseract.tesseract_cmd = (r'C:/Program Files/Tesseract-OCR')

    template_name = "fronte_end_packages/tesseract.html"
    # image_path = ('images/test.png')
    # print(image_file)
    # image_path = "django_tests\django_tests/fronte_end_packages\static\images/test.png"
    image_path = r"C:\Users\Echos Bv\Desktop\github_repos\Les_Syntra_2e_jaar\django_tests\django_tests\fronte_end_packages\static\images\test.png".replace('\\', '/')
    print(image_path)
    # Image.open(image_path)


    image = cv2.imread(image_path)

    # # print(image)
    custom_config = r'--oem 3 --psm 6'
    result = pytesseract.image_to_string(image, config=custom_config)
    
    context = {
        'result' : result,
        # 'image' : image,
    }
    

    return render(request, context=context, template_name=template_name)

