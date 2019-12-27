from django.urls import path
from myapp import views

app_name="myapp"

urlpatterns = [
    path('response/',views.response,name="response"),
    path('demo1/',views.html_demo1,name="demo1"),
    path('demo2/',views.html_demo2,name="demo2"),
    path("topics/",views.display_topics,name="topics"),
    path("form/",views.form_multi_select,name="forms"),
    path('top/',views.topic_form,name="topic_form"),
    path("web/",views.disp_web,name="web_form"),
    path("create_topic/",views.create_topic,name="create_topic"),
    path("create_webpage/",views.create_webpage,name="create_webpage"),
]
