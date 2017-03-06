from django.http import HttpResponse


def index(request):
    content = [

    ]
    return HttpResponse(
        '''
        <html><head><title>Test Czarcie</title></head>
        <body>
        <h1> Test Czarcie </h1>
        <h2> Hello, world!! </h2>
        </body>
        </html>'''
    )