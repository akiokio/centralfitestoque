from django.conf.urls import patterns, include, url
from salesReport.views import home, importAllProducts, importAllOrders, importar, loginView, logoutView, exportar, Faturamento
from django.contrib.auth.decorators import login_required

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', login_required(home.as_view()), name='home'),
    # url(r'^centralFitEstoque/', include('centralFitEstoque.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^importOrdersSinceDay/(?P<dateStart>[\w|\W]+)/(?P<dateEnd>[\w|\W]+)/$', 'salesReport.views.importOrdersSinceDay', name='importOrders'),
    url(r'^exportar/$', login_required(exportar), name='exportar'),
    url(r'^faturamento/$', login_required(Faturamento.as_view()), name='faturamento'),
    url(r'^importar/$', login_required(importar), name='importar'),
    url(r'^importar/produtos/$', importAllProducts, name='importarProdutos'),
    url(r'^importar/pedidos/$', importAllOrders, name='importarPedidos'),
    url(r'^login/$', loginView, name="login"),
    url(r'^logout/$', logoutView, name="logout"),
)
