from rider.views import HtmlView
from rider.templates import render

@HtmlView
def hello(request):
    return render('hello.html')
