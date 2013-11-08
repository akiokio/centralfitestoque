from django.conf.urls import patterns, include, url
from salesReport.views import importAllProducts, importAllOrders,  exportar, importProductCost, atualizarStatusPedido,\
    SingleOrderInfo, generateCsvFileCronTeste, update_brand, teste_update_item_detail
from django.conf import settings
from dashboard.views import home, importar, loginView, logoutView, Faturamento, filtrarFaturamento, cmm,\
    importarQuantidadeEstoque, lista_estoque, exportar_lista_produto, expedicao, pedidos, exportar_lista_produto_fornecedor, \
    abc, resumo
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic import RedirectView
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', login_required(home.as_view()), name='home'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^importOrdersSinceDay/(?P<dateStart>[\w|\W]+)/(?P<dateEnd>[\w|\W]+)/$', 'salesReport.views.importOrdersSinceDay', name='importOrders'),

    url(r'^exportar/$', login_required(exportar), name='exportar'),
    url(r'^cmm/$', login_required(cmm.as_view()), name='cmm'),
    url(r'^resumo/$', login_required(resumo.as_view()), name='resumo'),
    url(r'^abc/$', login_required(abc.as_view()), name='abc'),
    url(r'^listaestoque/$', login_required(lista_estoque.as_view()), name='lista_estoque'),
    url(r'^faturamento/$', login_required(Faturamento.as_view()), name='faturamento'),
    url(r'^importar/$', login_required(importar), name='importar'),
    url(r'^pedidos/$', login_required(pedidos.as_view()), name='pedidos'),

    url(r'^expedicao/$', login_required(expedicao.as_view()), name='expedicao'),
    url(r'^importar/produtos/$', importAllProducts, name='importarProdutos'),
    url(r'^importar/pedidos/$', importAllOrders, name='importarPedidos'),
    url(r'^importar/custos/$', importProductCost, name='atualizarProdutosCusto'),
    url(r'^atualizar/pedido/$', atualizarStatusPedido, name='atualizarPedidosBoleto'),
    url(r'^atualizar/marca/$', update_brand, name='atualizarMarca'),

    url(r'^exportar/lista_produtos/$', exportar_lista_produto, name='exportar_lista_produto'),
    url(r'^exportar/lista_produto_fornecedores/$', exportar_lista_produto_fornecedor, name='exportar_lista_produto_fornecedor'),

    url(r'^pedido/detalhes/(?P<order_id>[\w|\W]+)/$', SingleOrderInfo, name='singleOrderInfo'),

    url(r'^salvar/salesReport/$', generateCsvFileCronTeste, name='generateCsvCron'),
    url(r'^filtrar/faturamento/$', filtrarFaturamento, name='filtrarFaturamento'),
    url(r'^importar/quantidadeestoque/$', importarQuantidadeEstoque, name='importarQuantidadeEstoque'),
    url(r'^teste/updateItemDetail/$', teste_update_item_detail, name='teste_update_item_detail'),

    url(r'^login/$', loginView, name="login"),
    url(r'^logout/$', logoutView, name="logout"),
    url(r'^favicon\.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'favicon.ico'))
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
