from django.http import HttpResponse

def home(request):
    html_content = """
    <html>
    <head>
        <title>University of Sulaimani</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {
                font-family: Arial, sans-serif;
                padding: 50px;
            }
            h1 {
                left-align: right;
            }
             h2 {
                left-align: right;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to University of Sulaimani</h1>
        <h2>Created by Heshwan Adnan</h2>
    </body>
    </html>
    """
    return HttpResponse(html_content)