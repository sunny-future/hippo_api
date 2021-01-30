from django.urls import path,include,re_path
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [

    re_path(r'^login/', obtain_jwt_token),

]
