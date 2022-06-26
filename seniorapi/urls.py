from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    
    #number api
    #http://127.0.0.1:8000/api/number_List/
    path('number_List/', views.number_List.as_view()),

    # register api
    #http://127.0.0.1:8000/api/register_List/
    path('register_List/', views.register_List.as_view()),

    #stream api
    #http://127.0.0.1:8000/api/stream_api/  
    #user enter without ""
    path('stream_api/', views.stream_api),

    #car api
    #http://127.0.0.1:8000/api/car_List/ 
    path('car_List/', views.car_List.as_view()),

    #all patterns api
    #http://127.0.0.1:8000/api/patternsid/<int:pk>
    path('patternsid/<int:pk>', views.patternsid),

    ##show information of user by cluster  
    #http://127.0.0.1:8000/api/clusterid/<int:pk> 
    path('clusterid/<int:pk>', views.clusterid),

    #test of table pattern
    path('pat_ref_List/', views.pat_ref_List.as_view()),

    #show information user by user id from table car and user and number 
    path('informationid/<int:pk>', views.informationid),

    #dashbord_all
    path('dashbord_all/', views.dashbord_all),

    #dashbord_all information by id 
    path('dashbord_all_id/<int:pk>', views.dashbord_all_id),

    #edit activate api
    path('editactive/<int:pk>', views.editactive.as_view()),

    #all stream of id 
    path('streamofid/<int:pk>', views.streamofid),
    #all stream of time 
    path('streamoftime/<time>', views.streamoftime),
    
    path('idandtime/<int:pk>/<time>', views.idandtime),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)