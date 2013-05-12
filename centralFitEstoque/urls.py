from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'centralFitEstoque.views.home', name='home'),
    # url(r'^centralFitEstoque/', include('centralFitEstoque.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^importOrdersSinceDay/(?P<dateStart>[\w|\W]+)/(?P<dateEnd>[\w|\W]+)', 'salesReport.views.importOrdersSinceDay', name='importOrders'),
    url(r'^someview/(?P<dateStart>[\w|\W]+)/(?P<dateEnd>[\w|\W]+)', 'salesReport.views.some_view', name='some_view'),
)
