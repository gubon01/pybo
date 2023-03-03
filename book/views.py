from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import IsbnForm
import requests
import json


api_key = '037bb2f4f94e2f88cfde974658af3b9e'
header = {'Authorization': 'KakaoAK ' + api_key}
url = "https://dapi.kakao.com/v3/search/book?target=isbn"


def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = IsbnForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            isbn_for_search = form.cleaned_data['isbn']
            isbn = {'query' : isbn_for_search}
            response = requests.get(url, headers=header, params=isbn)
            tokens = response.json()
            author_list = tokens['documents'][0]['authors']
            author_comma = ', '.join(author_list)
            contents = tokens['documents'][0]['contents']
            datetime = tokens['documents'][0]['datetime'][0:10]
            publisher = tokens['documents'][0]['publisher']
            title = tokens['documents'][0]['title']
            thumbnail = tokens['documents'][0]['thumbnail']
            return render(request, 'book/book_info.html', {'author_comma' : author_comma, 'contents' : contents, 'datetime' : datetime, 'publisher' : publisher, 'title' : title, 'thumbnail' : thumbnail})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = IsbnForm(request.POST)

    return render(request, 'book/book_info.html', {'form': form})











