"""YYShop URL Configuration

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

from django.urls import path, include
from django.conf.urls import url
import xadmin
from YYShop.settings import MEDIA_ROOT
from django.views.static import serve

from goods.views import GoodsListViewSet, CategoryViewSet, HotSearchsViewset, BannerViewset, IndexCategoryViewset
from users.views import SmsCodeViewSet, UserViewSet
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from user_operation.views import UserFavViewSet

router = DefaultRouter()

# 配置商品
router.register(r'goods', GoodsListViewSet, base_name="goods")
# 配置商品品牌
router.register(r'categorys', CategoryViewSet, base_name="categorys")
# 配置热搜
router.register(r'hotsearchs', HotSearchsViewset, base_name="hotsearchs")
# 轮播图url
router.register(r'banners', BannerViewset, base_name="banners")
# 首页商品系列数据
router.register(r'indexgoods', IndexCategoryViewset, base_name="indexgoods")
# 配置发送验证码
router.register(r'code', SmsCodeViewSet, base_name="code")
# 配置用户
router.register(r'users', UserViewSet, base_name="users")
# 收藏
router.register(r'userfavs', UserFavViewSet, base_name="userfavs")

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^', include(router.urls)),
    url(r'^docs/', include_docs_urls(title="暮学生鲜")),
    # drf自带的token认证
    url(r'^api-token-auth/', views.obtain_auth_token),
    # jwt的认证接口
    url(r'^login/', obtain_jwt_token),
]
