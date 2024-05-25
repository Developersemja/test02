from django.urls import path
from core.views import index,prd,cat,cat_view

app_name ="core"

urlpatterns =[
    path("",index,name="index"),
    path("prd/",prd,name="prd"),
    path("cat/",cat,name="cat"),
    path("cat/<cid>/",cat_view,name="catls")
]