from django.contrib import admin
from django.urls import path
import blogapp.views
import portfolio.views
import accounts.views
##
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    #블로그
    path('admin/', admin.site.urls),
    path('blog/home', blogapp.views.home, name = "home"),
    path('blog/<int:blog_id>', blogapp.views.detail, name = "detail"),
    path('blog/new/', blogapp.views.new, name = "new"),
    path('blog/create', blogapp.views.create, name = "create"),
    path('blog/<int:blog_id>', blogapp.views.update, name = "update"),
    path('blog/update_page/<int:blog_id>', blogapp.views.update_page, name = "update_page"),
    path('blog/delete/<int:blog_id>', blogapp.views.delete, name = "delete"),

    #포트폴리오 
    path('portfolio', portfolio.views.portfolio, name = "portfolio"),
    path('portfolio/<int:portfolio_id>', portfolio.views.detail_port, name = "detail_port"),

    #회원가입, 로그인
    path('signup/', accounts.views.signup, name="signup"),
    path('', accounts.views.login, name="login"),
    path('logout/', accounts.views.logout, name="logout"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)