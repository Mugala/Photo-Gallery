from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

# Create your views here.

#Function to display the welcome page
def welcome (request):
    return HttpResponse ('Welcome to My Photo Gallery!')

def todays_pics(request): #Function to display photos that have been posted today.
    date = dt.date.today()

    html = f'''
        <html>
            <body>
                <h1> {date.day}-{date.month}-{date.year} </h1>
            </body>
        </html>
            '''
    return HttpResponse(html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
