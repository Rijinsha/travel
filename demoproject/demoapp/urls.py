from . import views
from django.urls import path

urlpatterns = [

    #path('',views.home,name='home1'),
    #path('about/',views.about,name='abt'),
    #path('contact/',views.contact,name='cntct'),
    #path('detail/',views.detail,name='dtls'),
    #path('thanks/',views.thanks,name='thks'),
    #path('',views.calculation,name='calculation'),
   #path('all/',views.result,name='result'),
    path('',views.demo,name="demo")
]










# check thnks fun in view page then the view page go to check thank .html
    # is in templats folder
#crieat path ,chek view page ,here home fun create ,check all others