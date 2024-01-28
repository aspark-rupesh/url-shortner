from django.urls import  path

from shortner.views import  IndexPage, UrlRedirectView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", IndexPage.as_view(), name="index"),
    path("redict-page/<str:slug>/",UrlRedirectView.as_view(),name="url_redirect"),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)