from django.urls import path
from . import views

app_name = 'tempapps'
urlpatterns = [ 
    path('', views.index, name='index'),
    path('template.filter/', views.templateFilter, name="my_filter"),
    #path('template.tag/', views.templatetag, name="my_tag"),
    #path('form.create/', views.formCreate, name="formCreate"),
    #path('thanks/', views.thanks),
]