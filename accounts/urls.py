from django.urls import path

from accounts.views import kakao_login, kakao_callback, KakaoLogin

app_name = 'accounts'

urlpatterns = [
    path('kakao/login', kakao_login, name='kakao_login'),
    path('kakao/callback/', kakao_callback, name='kakao_callback'),
    path('kakao/login/finish/', KakaoLogin.as_view(), name='kakao_login_todjango'),
]
