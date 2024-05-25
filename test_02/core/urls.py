from django.urls import path
from core.views import index,prd,cat

app_name ="core"

urlpatterns =[
    path("",index,name="index"),
    path("prd/",prd,name="prd"),
    path("cat/",cat,name="cat"),
]