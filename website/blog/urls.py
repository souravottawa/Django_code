from django.conf.urls import patterns,include,url
from django.views.generic import ListView
from blog.models import Post

urlpatterns=patterns('',
                     url(r'^',ListView.as_view(
					         queryset=Post.objecs.all()order_by("-date")[:10],
							 template_name="blog.html")),
)
							  