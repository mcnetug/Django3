
from django.conf.urls import url
from form3app.views import costView
from . import views

app_name = 'form3app'
urlpatterns = [
	#url(r'^$', views.get, name='get'),
    url(r'^$', views.costView, name='cost'),
	# url(r'^$', costView.as_view(), name='cost'),
]
