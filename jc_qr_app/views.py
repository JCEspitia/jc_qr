from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home(request):
    html = f'''
        <html>
            <body>
                <h1>JC QR</h1>
            </body>
        </html>
        '''
    return HttpResponse(html)
