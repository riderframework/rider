from rider.views import HtmlView
from rider.templates import render


@HtmlView('GET', 'POST')
def deep_render_get_post(request):
    return render('template.html', {'params': request.params})
