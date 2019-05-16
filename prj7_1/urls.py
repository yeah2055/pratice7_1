"""prj7_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import pratice7_1.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',pratice7_1.views.pratice7_1,name='pratice7_1'),
]
#path('',pratice7_1(앱이름).views(뷰스 안에 있는 함수를 경로에 알려주기 위함 안에는 탬플릿에 있는 html파일도 있음).pratice7_1(이걸 한번 더 쓰는 이유는 무엇인가?),name='pratice7_1'),