from django.urls import path

# from . import views

# urlpatterns = [
#     path('', views.index, name='intro'),

# ]
#prueba de botones de control de tesis
# from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='in'),
    path('intro/', views.index, name='intro'),
    path('control/', views.motors, name='controles'),
    path('<int:z>/', views.calibracion, name='limits'),
    path('var/<int:y>/', views.vari, name='vari'),
    path('move/<int:z>/', views.move, name='const'),
    path("<int:pk>/<w>/", views.motors, name="moveCW"),
    
    path('goodbye/', views.fin, name='salir'),
]
