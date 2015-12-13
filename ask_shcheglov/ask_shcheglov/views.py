from django.http import HttpResponse
from django.utils.html import escape

def hi(request):

    data = "Hello world! </br>"
    get_data = request.GET
    post_data = request.POST
    output = data + "</br>GET data: </br>" +  get_data.urlencode() + "</br>POST data: </br>"  + post_data.urlencode()
    return HttpResponse((output))
