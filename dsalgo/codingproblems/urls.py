from django.conf.urls import url 
from codingproblems import views 
from django.urls import path
urlpatterns = [
    url(r'section1', views.section1, name='section1'),
    url(r'section2', views.section2, name='section2'),
    url(r'miscellaneous', views.miscellaneous, name='miscellaneous'),
    url(r'newproblem', views.newproblem, name='newproblem'),
    path(r'newsolution/<int:pk>/', views.newsolution, name='newsolution'),
    path(r'updatesolution/<int:pk>/', views.updatenewsolution, name='updatesolution'),
    path(r'deletesolution/<int:pk>/', views.deletenewsolution, name='deletenewsolution'),
    path(r'problem/<int:pk>/', views.problem, name='problem'),
    path(r'solution/<int:pk>/', views.solution, name='solution'),
]