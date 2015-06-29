from django.conf.urls import patterns, include, url
from django.contrib import admin

from trips.views import hello_world
from trips.views import home
from trips.views import post_detail

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(網址"的樣子", 去哪個View)
    #^:開頭 $:結尾
    #r:raw string(字串，個輸字不當特殊字元)

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello_world),
    url(r'^home/$', home),
    #name --> Template要用到的({% url %})
    #?p<取出的東西，傳給view的東西> \d數字 +一個以上 ?0或1 *0或多個
    url(r'^post/(?P<id>\d+)/$', post_detail, name='post_detail'),
)
