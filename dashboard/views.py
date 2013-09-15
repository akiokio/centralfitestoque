# -*- coding: utf-8 -*-
__author__ = 'akiokio'
from django.http import HttpRequest, HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from salesReport.models import order as orderNaBase, orderItem, brands, item as itemNaBase
import datetime
from salesReport.models import order, orderItem, item as itemObject
from django.views.generic import TemplateView, FormView, CreateView, UpdateView, ListView, DetailView, DeleteView
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from xlrd import open_workbook
from django.shortcuts import redirect
from django.contrib import messages
from zipfile import ZipFile
import xml.etree.ElementTree as ET
from xml_helper import XmlDictConfig, XmlListConfig
from tempfile import TemporaryFile
from xlwt import Workbook
import math

def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                return HttpResponseRedirect(reverse('home'))
            else:

                return render_to_response('registration/login.html',
                                          {'error': 'Usuario ou senha incorreta'},
                                          context_instance=RequestContext(request))
                # Return a 'disabled account' error message
        else:
            return render_to_response('registration/login.html',
                                          {'error': 'Usuario ou senha incorreta'},
                                          context_instance=RequestContext(request))
            # Return an 'invalid login' error message.
    else:
        return render_to_response('registration/login.html',
                          {'status': 'ok'},
                          context_instance=RequestContext(request))

def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

class home(TemplateView):
    template_name = 'index.html'

    def get(self, *args, **kwargs):
        context = self.get_context_data()
        #Em caso dos filtros
        if self.request.GET.get('dataInicio') and self.request.GET.get('dataFim'):
            dateInicio = datetime.datetime.strptime(self.request.GET.get('dataInicio'), '%d-%m-%Y') - datetime.timedelta(days=1)
            dateFim = datetime.datetime.strptime(self.request.GET.get('dataFim'), '%d-%m-%Y')
        else:
            dateInicio = datetime.datetime.today() - datetime.timedelta(days=30) - datetime.timedelta(hours=3)
            dateFim = datetime.datetime.today()

        #Cria a tabela da dashboard limpa
        pedidoArray = []
        qtd_linhas = dateFim.date() - dateInicio.date()
        tempData = dateFim
        for day in range(0, qtd_linhas.days):
            pedidoArray.append([
                str(tempData.day) + '-' + str(tempData.month), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
            ])
            tempData -= datetime.timedelta(days=1)
        pedidoArray.append(['TOTAL', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        #Preenche a tabela com os pedidos
        for orderInPeriod in order.objects.filter(created_at__range=[dateInicio.date(), dateFim.date()]):
            #Ajuste de UTC para GMT-3
            orderInPeriod.created_at -= datetime.timedelta(hours=3)
            diferencaDias = dateFim.date() - orderInPeriod.created_at.date()

            #Soma a coluna de dias
            pedidoArray[diferencaDias.days][orderInPeriod.created_at.hour + 1] += 1
            pedidoArray[diferencaDias.days][25] += 1

            #Soma a coluna Totais
            pedidoArray[-1][orderInPeriod.created_at.hour + 1] += 1
            pedidoArray[-1][25] += 1
        context['tabelaPedidos'] = pedidoArray
        context['usuario'] = self.request.user
        return self.render_to_response(context)


def getFaturamentoForDay(date, totalArr):
    inicioDoDia = date.replace(hour=0, minute=0, second=0) - datetime.timedelta(hours=3)
    fimDoDia = date.replace(hour=23, minute=59, second=59) - datetime.timedelta(hours=3)

    orders = orderNaBase.objects.filter(updated_at__range=[inicioDoDia, fimDoDia]).filter(status__in=['complete', 'complete2'])
    today = str(date.day) + '-' + str(date.month),


    numeroDePedidos = len(orders)
    valorBrutoFaturado = 0
    receitaFrete = 0
    valorDesconto = 0
    valorBonificado = 0
    valorBonificadoPedido = 0
    valorLiquidoProdutos = 0
    custoProdutos = 0
    valorFrete = 0
    valorTaxaCartao = 0
    somatoriaProdutos = 0

    #Não existem pedidos nesse dia
    if len(orders) == 0:
        return [today[0],0,0,0,0,0,0,0,0,0,0,0,0,0]


    for order in orders:
        valorBrutoFaturado += order.valorBrutoFaturado
        receitaFrete += order.receitaFrete
        valorDesconto += order.valorDesconto
        custoProdutos += order.custoProdutos
        valorBonificado += order.valorBonificado
        valorBonificadoPedido += order.valorBonificadoPedido
        somatoriaProdutos += order.somatoriaProdutos
        valorLiquidoProdutos += order.valorLiquidoProdutos
        valorFrete += order.valorFrete
        valorTaxaCartao += order.valorTaxaCartao

    margemBrutaSoProdutos = (1 - (custoProdutos / valorLiquidoProdutos)) * 100
    margemBrutaCartaoFrete = (1 - ((custoProdutos + valorFrete + valorTaxaCartao) / (valorLiquidoProdutos + receitaFrete))) * 100
    ticketMedio = valorLiquidoProdutos / numeroDePedidos
    nuemroPedidosProdutos = round(somatoriaProdutos / numeroDePedidos, 2)

    totalArr[1] += numeroDePedidos
    totalArr[2] += round(valorBrutoFaturado, 2)
    totalArr[3] += round(receitaFrete, 2)
    totalArr[4] += round(valorDesconto, 2)
    totalArr[5] += round(valorBonificado, 2)
    totalArr[6] += round(valorLiquidoProdutos, 2)
    totalArr[7] += round(custoProdutos, 2)
    totalArr[8] += round(valorFrete, 2)
    totalArr[9] += round(valorTaxaCartao, 2)
    totalArr[10] = (totalArr[10] + round(margemBrutaSoProdutos, 2)) /2
    totalArr[11] = (totalArr[11] + round(margemBrutaCartaoFrete, 2)) /2
    totalArr[12] = (totalArr[12] + round(ticketMedio, 2)) / 2
    totalArr[13] += somatoriaProdutos

    return [
        today[0],
        numeroDePedidos,
        round(valorBrutoFaturado, 2),
        round(receitaFrete, 2),
        round(valorDesconto, 2),
        round(valorBonificado, 2),
        round(valorLiquidoProdutos, 2),
        round(custoProdutos, 2),
        round(valorFrete, 2),
        round(valorTaxaCartao, 2),
        round(margemBrutaSoProdutos, 2),
        round(margemBrutaCartaoFrete, 2),
        round(ticketMedio, 2),
        nuemroPedidosProdutos
    ]

class Faturamento(TemplateView):
    template_name = 'faturamento.html'

    def get_context_data(self, **kwargs):
        context = super(Faturamento, self).get_context_data(**kwargs)
        #Cria a tabela da dashboard limpa
        tabela = []
        totalArr = ['TOTAL',0,0,0,0,0,0,0,0,0,0,0,0,0]

        today = datetime.datetime.now()
        #range define a quantidade de dia que a tabela deve ter
        for day in range(0, 90):
            tabela.append(getFaturamentoForDay(today, totalArr))
            today -= datetime.timedelta(days=1)

        #Finaliza linha de totais
        if totalArr[1]:
            totalArr[13] = totalArr[13] / float(totalArr[1])
         #Arredonda os valores
        totalArr[1] = round(totalArr[1], 2)
        totalArr[2] = round(totalArr[2], 2)
        totalArr[3] = round(totalArr[3], 2)
        totalArr[4] = round(totalArr[4], 2)
        totalArr[5] = round(totalArr[5], 2)
        totalArr[6] = round(totalArr[6], 2)
        totalArr[7] = round(totalArr[7], 2)
        totalArr[8] = round(totalArr[8], 2)
        totalArr[9] = round(totalArr[9], 2)
        totalArr[10] = round(totalArr[10], 2)
        totalArr[11] = round(totalArr[11], 2)
        totalArr[12] = round(totalArr[12], 2)
        totalArr[13] = round(totalArr[13], 2)
        tabela.append(totalArr)

        context['tabelaFaturamento'] = tabela
        return context

def importar(request):
    return render_to_response('importar.html',
                          {'status': 'ok'},
                          context_instance=RequestContext(request))

def daterange(start_date, end_date):
    dateRange = end_date - start_date
    if dateRange.days == 0:
            dateRange += datetime.timedelta(days=1)
    for n in range(int (dateRange.days)):
        yield start_date + datetime.timedelta(n)

@csrf_exempt
def filtrarFaturamento(request):
    if request.method == 'POST':
        tabela = []
        totalArr = ['TOTAL',0,0,0,0,0,0,0,0,0,0,0,0,0]

        dataInicio = datetime.datetime.strptime(request.POST.get('dataInicio'), '%d-%m-%Y')
        dataFim = datetime.datetime.strptime(request.POST.get('dataFim'), '%d-%m-%Y')
        dataFim += datetime.timedelta(days=1)

        for single_date in daterange(dataInicio, dataFim):
            print single_date
            tabela.append(getFaturamentoForDay(single_date, totalArr))

        #Finaliza linha de totais
        totalArr[13] = totalArr[13] / float(totalArr[1])
        #Arredonda os valores
        totalArr[1] = round(totalArr[1], 2)
        totalArr[2] = round(totalArr[2], 2)
        totalArr[3] = round(totalArr[3], 2)
        totalArr[4] = round(totalArr[4], 2)
        totalArr[5] = round(totalArr[5], 2)
        totalArr[6] = round(totalArr[6], 2)
        totalArr[7] = round(totalArr[7], 2)
        totalArr[8] = round(totalArr[8], 2)
        totalArr[9] = round(totalArr[9], 2)
        totalArr[10] = round(totalArr[10], 2)
        totalArr[11] = round(totalArr[11], 2)
        totalArr[12] = round(totalArr[12], 2)
        totalArr[13] = round(totalArr[13], 2)

        tabela.append(totalArr)
        return HttpResponse(simplejson.dumps(tabela))

class cmm(TemplateView):
    template_name = 'cmm.html'


    def get(self, *args, **kwargs):
        context = self.get_context_data()
        itens = itemObject.objects.all().order_by('sku')

        #Filtros
        if self.request.GET.get('sku'):
            itens = itens.filter(sku=self.request.GET.get('sku'))

        if self.request.GET.get('nome'):
            itens = itens.filter(name__icontains=self.request.GET.get('nome'))

        if self.request.GET.get('marca'):
            itens = itens.filter(brand__name__icontains=self.request.GET.get('marca'))
        #Filter Only for status
        if self.request.GET.get('status'):
            itens = itens.filter(status=self.request.GET.get('status'))

        #ordenacao
        if self.request.GET.get('order_by'):
            itens = itens.order_by(self.request.GET.get('order_by'))

        self.request.session['product_list'] = itens

        #paginacao
        paginator = Paginator(itens, 300)
        page = self.request.GET.get('page')
        try:
            itens = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            itens = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            itens = paginator.page(paginator.num_pages)

        context['itens'] = itens

        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(cmm, self).get_context_data(**kwargs)
        return context

    def post(self, *args, **kwargs):
        produto = itemObject.objects.get(sku=self.request.POST.get('sku'))

        if self.request.POST.get('cmm_novo'):
            produto.cmm = ((produto.cmm * produto.estoque_atual) + (float(self.request.POST.get('cmm_novo').replace(',','.')) * float(self.request.POST.get('qtd_a_posicionar')))) \
                          / (float(produto.estoque_atual) + float(self.request.POST.get('qtd_a_posicionar')))

        if self.request.POST.get('qtd_a_posicionar'):
            produto.estoque_atual += int(self.request.POST.get('qtd_a_posicionar'))
            produto.estoque_disponivel += int(self.request.POST.get('qtd_a_posicionar'))
        produto.save()

        get_attr = self.request.META.get('HTTP_REFERER').split('?')[-1]
        return HttpResponseRedirect(reverse('cmm') + "?%s" % get_attr)

def importarQuantidadeEstoque(request):
    if request.method == "POST":
        file = request.FILES['docfile']
        wb = open_workbook(file_contents=file.read())
        for s in wb.sheets():
            for row in range(s.nrows):
                values = []
                for col in range(s.ncols):
                    values.append(s.cell(row, col).value)
                try:
                    if values[0] != 0:
                        produto = itemNaBase.objects.get(sku=values[0])

                        # produto.price = values[2]
                        produto.specialPrice = values[2]
                        produto.estoque_atual = values[4]
                        #o que estiver com estoque zero, deve ficar com custo zero tbm ok?
                        if int(values[3]) == 0:
                            produto.cost = 0
                        else:
                            produto.cost = values[3]
                        produto.cmm = produto.cost
                        produto.margem = 1 - (float(produto.cost) / float(produto.specialPrice))

                        dateMinus8 = datetime.datetime.today() - datetime.timedelta(days=8)
                        qtd_produtos_comprometidos = len(orderItem.objects.filter(item__sku=values[0]).filter(order__status='holded').filter(created_at__gt=dateMinus8))
                        produto.estoque_empenhado = qtd_produtos_comprometidos
                        produto.estoque_disponivel = int(values[4]) - qtd_produtos_comprometidos
                        produto.save()
                except Exception as e:
                    print e

        return redirect(reverse('cmm'))
    else:
        return HttpResponseForbidden()

class lista_estoque(TemplateView):
    template_name = 'lista_estoque.html'


    def get(self, *args, **kwargs):
        context = self.get_context_data()
        itens = itemObject.objects.all().order_by('sku')

        #Filtros
        if self.request.GET.get('sku'):
            itens = itens.filter(sku=self.request.GET.get('sku'))

        if self.request.GET.get('nome'):
            itens = itens.filter(name__icontains=self.request.GET.get('nome'))

        if self.request.GET.get('marca'):
            itens = itens.filter(brand__name__icontains=self.request.GET.get('marca'))
        #Filter Only for status
        if self.request.GET.get('status'):
            itens = itens.filter(status=self.request.GET.get('status'))

        #ordenacao
        if self.request.GET.get('order_by'):
            itens = itens.order_by(self.request.GET.get('order_by'))

        #Lista para possivel exportacao
        self.request.session['product_list'] = itens

        paginator = Paginator(itens, 300)
        page = self.request.GET.get('page')
        try:
            itens = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            itens = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            itens = paginator.page(paginator.num_pages)

        context['itens'] = itens
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(lista_estoque, self).get_context_data(**kwargs)
        return context

    def post(self, *args, **kwargs):
        produto = itemObject.objects.get(sku=self.request.POST.get('sku'))


        if self.request.POST.get('qtd_a_posicionar'):
            produto.estoque_atual = int(self.request.POST.get('qtd_a_posicionar'))
            produto.estoque_disponivel = int(self.request.POST.get('qtd_a_posicionar')) - len(orderItem.objects.filter(item__sku=produto.sku).filter(order__status='holded'))
        if self.request.POST.get('price'):
            produto.price = self.request.POST.get('price').replace(',', '.')
        if self.request.POST.get('specialPrice'):
            produto.specialPrice = self.request.POST.get('specialPrice').replace(',', '.')
        if self.request.POST.get('cmm'):
            produto.cmm = self.request.POST.get('cmm').replace(',', '.')
            produto.margem = 1 - (float(produto.cmm) / float(produto.specialPrice))
        produto.save()

        get_attr = self.request.META.get('HTTP_REFERER').split('?')[-1]
        return HttpResponseRedirect(reverse('lista_estoque') + "?%s" % get_attr)

def exportar_lista_produto(request):
    return generateXLS(request.session.get('product_list'), 'lista_produto')

def exportar_lista_produto_fornecedor(request):
    return generateXLS(request.session.get('product_list'), 'exportar_lista_produto_fornecedor')

def generateXLS(modelData, type):
    from django.http import HttpResponse
    import xlwt


    book = xlwt.Workbook(encoding='utf8')
    sheet = book.add_sheet('product_list')

    default_style = xlwt.Style.default_style
    datetime_style = xlwt.easyxf(num_format_str='dd/mm/yyyy hh:mm')
    date_style = xlwt.easyxf(num_format_str='dd/mm/yyyy')

    # Add the header type
    # TODO make headers and values_list dinamicaly
    if type == 'lista_produto':
        headers = ['sku', 'name', 'specialPrice', 'cmm', 'estoque_atual']
        values_list = modelData.values_list('sku', 'name', 'specialPrice', 'cmm', 'estoque_atual')
    elif type == 'exportar_lista_produto_fornecedor':
        headers = ['sku', 'name', 'brand__name', 'estoque_disponivel', 'cmm', 'vmd', 'margem', 'quantidade_excedente', 'quantidade_faltante']
        values_list = modelData.values_list('sku', 'name', 'brand__name', 'estoque_disponivel', 'cmm', 'vmd', 'margem', 'quantidade_excedente', 'quantidade_faltante')
    else:
        headers = []
        values_list = modelData.values_list()

    values_list = [headers] + list(values_list)

    for row, rowdata in enumerate(values_list):
        for col, val in enumerate(rowdata):
            if isinstance(val, datetime.datetime):
                style = datetime_style
            elif isinstance(val, datetime.date):
                style = date_style
            else:
                style = default_style

            sheet.write(row, col, val, style=style)

    response = HttpResponse(mimetype='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=export.xls'
    book.save(response)
    return response


class expedicao(TemplateView):
    template_name = 'expedicao.html'


    def get_context_data(self, **kwargs):
        context = super(expedicao, self).get_context_data(**kwargs)
        return context

    def post(self, *args, **kwargs):
        uploaded_file = self.request.FILES['docfile']

        #Parse o xml e retorna uma lista de dicionarios das nfes
        xmlDict = []
        headerList = ['RAZAO SOCIAL REMETENTE', 'CNPJ REMETENTE', 'NOME DO ARQUIVO', 'CODIGO DE BARRAS',
                      'CODIGO DO PACOTE', 'NUMERO DA NOTA', 'SERIE DA NOTA', 'DATA EMISSÃO', 'PESO BALANÇA',
                      'PESO CUBADO', 'NATUREZA OPERACAO', 'CFOP NOTA', 'AD VALOREM', 'VALOR DA MERCADORIA',
                      'VALOR TOTAL DA NOTA', 'ICMS', 'CODIGO PRODUTO CLIENTE', 'NOME DESTINATARIO', 'ENDERECO',
                      'NUMERO', 'COMPLEMENTO', 'BAIRRO', 'CEP', 'CIDADE', 'ESTADO', 'E-MAIL', 'CPF / CNPJ', 'TELEFONE',
                      'CELULAR', 'DICA DE ENTREGA']
        root = ZipFile(uploaded_file, 'r')
        for file in root.namelist():
            xml_root = ET.fromstring(root.open(file).read().replace('http://www.portalfiscal.inf.br/nfe', ''))
            xmlDict.append(XmlDictConfig(xml_root))

        #Manipula as nfes gera um excel para o cliente fazer download
        book = Workbook(encoding='utf-8')
        sheet1 = book.add_sheet('ListaExpedicao')

        for count, header in enumerate(headerList):
            sheet1.write(0, count, header)

        for count, nfe in enumerate(xmlDict):
            count += 1
            #Monta a tabela
            sheet1.write(count, 0, nfe['NFe']['infNFe']['emit']['xNome'])
            sheet1.write(count, 1, nfe['NFe']['infNFe']['emit']['CNPJ'])
            sheet1.write(count, 2, nfe['NFe']['infNFe']['Id'])
            sheet1.write(count, 3, '')
            sheet1.write(count, 4, '')
            sheet1.write(count, 5, nfe['NFe']['infNFe']['ide']['nNF'])
            sheet1.write(count, 6, nfe['NFe']['infNFe']['ide']['serie'])
            sheet1.write(count, 7, nfe['NFe']['infNFe']['ide']['dEmi'])
            sheet1.write(count, 8, '')
            sheet1.write(count, 9, '')
            sheet1.write(count, 10, nfe['NFe']['infNFe']['ide']['natOp'])
            sheet1.write(count, 11, nfe['NFe']['infNFe']['det']['prod']['CFOP'])
            sheet1.write(count, 12, nfe['NFe']['infNFe']['total']['ICMSTot']['vTotTrib'])
            sheet1.write(count, 13, nfe['NFe']['infNFe']['total']['ICMSTot']['vProd'])
            sheet1.write(count, 14, nfe['NFe']['infNFe']['total']['ICMSTot']['vNF'])
            sheet1.write(count, 15, nfe['NFe']['infNFe']['total']['ICMSTot']['vICMS'])
            sheet1.write(count, 16, '')
            sheet1.write(count, 17, nfe['NFe']['infNFe']['dest']['xNome'])
            sheet1.write(count, 18, nfe['NFe']['infNFe']['dest']['enderDest']['xLgr'])
            sheet1.write(count, 19, nfe['NFe']['infNFe']['dest']['enderDest']['nro'])
            if 'xCpl' in nfe['NFe']['infNFe']['dest']['enderDest']:
                sheet1.write(count, 20, nfe['NFe']['infNFe']['dest']['enderDest']['xCpl'])
            else:
                sheet1.write(count, 20, u'')
            sheet1.write(count, 21, nfe['NFe']['infNFe']['dest']['enderDest']['xBairro'])
            sheet1.write(count, 22, nfe['NFe']['infNFe']['dest']['enderDest']['CEP'])
            sheet1.write(count, 23, nfe['NFe']['infNFe']['dest']['enderDest']['xMun'])
            sheet1.write(count, 24, nfe['NFe']['infNFe']['dest']['enderDest']['UF'])
            sheet1.write(count, 25, '')
            if 'CPF' in nfe['NFe']['infNFe']['dest']:
                sheet1.write(count, 26, nfe['NFe']['infNFe']['dest']['CPF'])
            else:
                sheet1.write(count, 26, nfe['NFe']['infNFe']['dest']['CNPJ'])
            if 'fone' in nfe['NFe']['infNFe']['dest']['enderDest']:
                sheet1.write(count, 27, nfe['NFe']['infNFe']['dest']['enderDest']['fone'])
            else:
                sheet1.write(count, 27, u'')
            sheet1.write(count, 28, '')
            sheet1.write(count, 29, '')

        book.save('centralFitEstoque/media/expedicao/%s.xls' % (uploaded_file.name[:-4]))
        messages.add_message(self.request, messages.INFO, "Arquivo Gerado com sucesso: %s.xls" % uploaded_file.name[:-4])
        messages.add_message(self.request, messages.INFO, "Link para download: /media/expedicao/%s.xls" % uploaded_file.name[:-4])
        return redirect(reverse('expedicao'))

class pedidos(TemplateView):
    template_name = 'pedidos.html'

    def get_context_data(self, **kwargs):
        context = super(pedidos, self).get_context_data(**kwargs)
        return context

    def get(self, *args, **kwargs):
        context = self.get_context_data()
        itens = itemObject.objects.all().order_by('sku')

        #ordenacao
        if self.request.GET.get('order_by'):
            itens = itens.order_by(self.request.GET.get('order_by'))

        #Filtros
        if self.request.GET.get('marca'):
            itens = itens.filter(brand__name__icontains=self.request.GET.get('marca'))

        if self.request.GET.get('sku'):
            itens = itens.filter(sku=self.request.GET.get('sku'))

        if self.request.GET.get('nome'):
            itens = itens.filter(name__icontains=self.request.GET.get('nome'))

        if self.request.GET.get('status'):
            itens = itens.filter(status=self.request.GET.get('status'))

        #Lista para possivel exportacao
        self.request.session['product_list'] = itens

        #paginacao
        paginator = Paginator(itens, 50)
        page = self.request.GET.get('page')
        try:
            itens = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            itens = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            itens = paginator.page(paginator.num_pages)

        context['itens'] = itens

        context['brands'] = brands.objects.all()

        return self.render_to_response(context)

class abc(TemplateView):
    template_name = 'abc.html'

    def get_context_data(self, **kwargs):
        context = super(abc, self).get_context_data(**kwargs)
        return context

    def get(self, *args, **kwargs):
        context = self.get_context_data()
        # itens = sorted(itemObject.objects.all(), key=lambda a: a.valor_faturado_do_dia, reverse=True)
        itens = itemObject.objects.all().order_by('-valor_faturado_do_dia')
        total_itens_na_base = len(itens)

        total_faturado_no_dia = 0
        pedido_no_periodo = order.objects.filter(created_at__range=[datetime.datetime.today().replace(hour=0, minute=0, second=0) - datetime.timedelta(days=30) - datetime.timedelta(hours=3), datetime.datetime.today().replace(hour=23, minute=59, second=59) - datetime.timedelta(hours=3)])
        for pedido in pedido_no_periodo:
            total_faturado_no_dia += pedido.grand_total

        for count, item in enumerate(itens):
            percentage = (float(count) / float(total_itens_na_base)) * 100
            if percentage <= 65.00:
                item.abc_letter = "A"
            elif percentage > 65.00 and percentage <= 90.00:
                item.abc_letter = "B"
            elif percentage > 90.00:
                item.abc_letter = "C"

        #ordenacao
        if self.request.GET.get('order_by'):
            itens = itens.order_by(self.request.GET.get('order_by'))

        #Filtros
        if self.request.GET.get('marca'):
            itens = itens.filter(brand__name__icontains=self.request.GET.get('marca'))

        if self.request.GET.get('sku'):
            itens = itens.filter(sku=self.request.GET.get('sku'))

        if self.request.GET.get('nome'):
            itens = itens.filter(name__icontains=self.request.GET.get('nome'))

        if self.request.GET.get('status'):
            itens = itens.filter(status=self.request.GET.get('status'))


        #paginacao
        paginator = Paginator(itens, 50)
        page = self.request.GET.get('page')
        try:
            itens = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            itens = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            itens = paginator.page(paginator.num_pages)


        context['itens'] = itens
        context['total_faturado_no_dia'] = total_faturado_no_dia
        context['brands'] = brands.objects.all()

        return self.render_to_response(context)