from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as dt

# Create your views here.

#Function to display the welcome page
def welcome (request):
    return render ( request, 'welcome.html')


#Function to display photos that have been posted today.
def todays_pics(request): 
    date = dt.date.today()

    return render (request, 'all-photos/recent_pics.html',{"date":date})  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 

#Function to redirect to photos posted in the past
def past_pics (request, past_date):
    #Convert date from the url string
    
    try:
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        raise Http404()
        assert False
    
    if date ==dt.date.today():
        return redirect(todays_pics)

    return render(request, 'all-photos/past_pics.html', {"date": date})




