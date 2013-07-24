from django.conf.urls import patterns, include, url
from salesReport.views import importAllProducts, importAllOrders,  exportar, importProductCost, atualizarStatusPedido, SingleOrderInfo, generateCsvFileCronTeste, update_brand
from django.conf import settings
from dashboard.views import home, importar, loginView, logoutView, Faturamento, filtrarFaturamento, cmm, importarQuantidadeEstoque, lista_estoque
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf.urls.static import static
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', login_required(home.as_view()), name='home'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^importOrdersSinceDay/(?P<dateStart>[\w|\W]+)/(?P<dateEnd>[\w|\W]+)/$', 'salesReport.views.importOrdersSinceDay', name='importOrders'),

    url(r'^exportar/$', login_required(exportar), name='exportar'),
    url(r'^cmm/$', login_required(cmm.as_view()), name='cmm'),
    url(r'^listaestoque/$', login_required(lista_estoque.as_view()), name='lista_estoque'),
    url(r'^faturamento/$', login_required(Faturamento.as_view()), name='faturamento'),
    url(r'^importar/$', login_required(importar), name='importar'),
    url(r'^importar/produtos/$', importAllProducts, name='importarProdutos'),
    url(r'^importar/pedidos/$', importAllOrders, name='importarPedidos'),
    url(r'^importar/custos/$', importProductCost, name='atualizarProdutosCusto'),
    url(r'^atualizar/pedido/$', atualizarStatusPedido, name='atualizarPedidosBoleto'),
    url(r'^atualizar/marca/$', update_brand, name='atualizarMarca'),

    url(r'^pedido/detalhes/(?P<order_id>[\w|\W]+)/$', SingleOrderInfo, name='singleOrderInfo'),

    url(r'^salvar/salesReport/$', generateCsvFileCronTeste, name='generateCsvCron'),
    url(r'^filtrar/faturamento/$', filtrarFaturamento, name='filtrarFaturamento'),
    url(r'^importar/quantidadeestoque/$', importarQuantidadeEstoque, name='importarQuantidadeEstoque'),

    url(r'^login/$', loginView, name="login"),
    url(r'^logout/$', logoutView, name="logout"),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
