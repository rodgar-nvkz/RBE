
from django.template import loader, RequestContext
from django.core.paginator import Paginator
from django.conf import settings

from main.decorators import http_response
from RBE.main.models import Post


@http_response
def main_page(request, page=1):

    posts = Post.objects.all()
    paginator = Paginator(posts, settings.POST_PER_PAGE)
    page = paginator.page(page)

    return loader.get_template('main/main_page.html').render(RequestContext(request, {'page': page}))