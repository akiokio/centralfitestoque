# -*- coding: utf-8 -*-
__author__ = 'akiokio'

# -*- coding: utf-8 -*-
__author__ = 'akiokio'

def find_key(dic, val):
    """
    return the key of dictionary dic given the value
    Source: http://www.daniweb.com/software-development/python/code/217019
    """
    return [k for k, v in dic.iteritems() if v == val][0]

## {{{ http://code.activestate.com/recipes/534109/ (r8)
import re
import xml.sax.handler

def xml2obj(src):
    """
    A simple function to converts XML data into native Python object.
    """

    non_id_char = re.compile('[^_0-9a-zA-Z]')
    def _name_mangle(name):
        return non_id_char.sub('_', name)

    class DataNode(object):
        def __init__(self):
            self._attrs = {}    # XML attributes and child elements
            self.data = None    # child text data
        def __len__(self):
            # treat single element as a list of 1
            return 1
        def __getitem__(self, key):
            if isinstance(key, basestring):
                return self._attrs.get(key,None)
            else:
                return [self][key]
        def __contains__(self, name):
            return self._attrs.has_key(name)
        def __nonzero__(self):
            return bool(self._attrs or self.data)
        def __getattr__(self, name):
            if name.startswith('__'):
                # need to do this for Python special methods???
                raise AttributeError(name)
            return self._attrs.get(name,None)
        def _add_xml_attr(self, name, value):
            if name in self._attrs:
                # multiple attribute of the same name are represented by a list
                children = self._attrs[name]
                if not isinstance(children, list):
                    children = [children]
                    self._attrs[name] = children
                children.append(value)
            else:
                self._attrs[name] = value
        def __str__(self):
            return self.data or ''
        def __repr__(self):
            items = sorted(self._attrs.items())
            if self.data:
                items.append(('data', self.data))
            return u'{%s}' % ', '.join([u'%s:%s' % (k,repr(v)) for k,v in items])

    class TreeBuilder(xml.sax.handler.ContentHandler):
        def __init__(self):
            self.stack = []
            self.root = DataNode()
            self.current = self.root
            self.text_parts = []
        def startElement(self, name, attrs):
            self.stack.append((self.current, self.text_parts))
            self.current = DataNode()
            self.text_parts = []
            # xml attributes --> python attributes
            for k, v in attrs.items():
                self.current._add_xml_attr(_name_mangle(k), v)
        def endElement(self, name):
            text = ''.join(self.text_parts).strip()
            if text:
                self.current.data = text
            if self.current._attrs:
                obj = self.current
            else:
                # a text only node is simply represented by the string
                obj = text or ''
            self.current, self.text_parts = self.stack.pop()
            self.current._add_xml_attr(_name_mangle(name), obj)
        def characters(self, content):
            self.text_parts.append(content)

    builder = TreeBuilder()
    if isinstance(src,basestring):
        xml.sax.parseString(src, builder)
    else:
        xml.sax.parse(src, builder)
    return builder.root._attrs.values()[0]
## end of http://code.activestate.com/recipes/534109/ }}}

def call_url(url, method='get', values=None):
    '''
    Call some external URL. It uses urllib and is a Shortcut
    @param String url: the full url with protocol (without get data. If you need, use as 'values')
    @param String method: the method between 'get' and 'post'
    @param Dict values: an dict containing the data to send
    @return: string Full content from url
    '''
    import urllib
    import urllib2

    if values is not None:
        # convert values to url defaults
        values = urllib.urlencode(values)

        if method == 'get':
            # if method is get, add values to url
            url = url + "?" + values
            req = urllib2.Request(url)

        elif method == 'post':
            # if method is post, add user agent to request
            user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
            headers = { 'User-Agent' : user_agent }
            req = urllib2.Request(url, values, headers)

        else:
            # if not in conditions return null value
            return None

    # if no value to send
    else:
        req = urllib2.Request(url)

    # open url using requested object
    response = urllib2.urlopen(req)

    # return page's content
    return response.read()

def digits_only(string):
    '''
    This function get all numbers from a string and creates an Integer with it
    Indicated to prices and adresses
    @return Int number: the number from string
    '''
    return int(''.join(i for i in string if i.isdigit()))

def correios_frete(nCdEmpresa='', sDsSenha='', nCdServico=None,sCepOrigem='99999999', sCepDestino='99999999',
                  nVlPeso='1', nCdFormato=1, nVlComprimento=0, nVlAltura=0, nVlLargura=0, nVlDiametro=0,
                  sCdMaoPropria='N', nVlValorDeclarado=0, sCdAvisoRecebimento='N', StrRetorno='XML'):
    '''
    Este método utiliza a API dos correios enviando os dados via POST e recebendo um XML com as informações.
    Todos os dados são obrigatórios no formato da declaração.
    @param String nCdEmpresa: Seu código administrativo junto à ECT. O código está disponível no corpo do
                              contrato firmado com os Correios.
    @param String sDsSenha: Senha para acesso ao serviço, associada ao seu código administrativo.
                            A senha inicial corresponde aos 8 primeiros dígitos do CNPJ informado no contrato.
                            A qualquer momento, é possível alterar a senha no endereço

http://www.corporativo.correios.com.br/encomendas/servicosonline/recuperaSenha.

    @param List nCdServico: código de serviço para o cálculo seguindo a seguinte tabela(Pode ser mais de um
                            numa consulta separados por vírgula):
                            40010 : SEDEX sem contrato
                            40045 : SEDEX a Cobrar, sem contrato
                            40126 : SEDEX a Cobrar, com contrato
                            40215 : SEDEX 10, sem contrato
                            40290 : SEDEX Hoje, sem contrato
                            40096 : SEDEX com contrato
                            40436 : SEDEX com contrato
                            40444 : SEDEX com contrato
                            40568 : SEDEX com contrato
                            40606 : SEDEX com contrato
                            41106 : PAC sem contrato
                            41068 : PAC com contrato
                            81019 : e-SEDEX, com contrato
                            81027 : e-SEDEX Prioritário, com conrato
                            81035 : e-SEDEX Express, com contrato
                            81868 : (Grupo 1) e-SEDEX, com contrato
                            81833 : (Grupo 2) e-SEDEX, com contrato
                            81850 : (Grupo 3) e-SEDEX, com contrato
    @param String sCepOrigem: CEP de Origem sem hífen.Exemplo: 05311900
    @param String sCepDestino: CEP de Destino Sem hífem
    @param String nVlPeso: Peso da encomenda, incluindo sua embalagem. O peso deve ser informado em quilogramas.
                           Máximo de 30kg. Ex.: 0.300, 1, 2, 3
    @param Int nCdFormato: Formato da encomenda (incluindo embalagem). Valores possíveis:
                           1: Formato caixa/pacote - 2: Formato rolo/prisma
    @param Int nVlComprimento: Comprimento da encomenda (incluindo embalagem), em centímetros.
    @param Int nVlAltura: Altura da encomenda (incluindo embalagem), em centímetros.
    @param Int nVlLargura: Largura da encomenda (incluindo embalagem), em centímetros.
    @param Int nVlDiametro: Diâmetro da encomenda (incluindo embalagem), em centímetros. (somente para rolo/prisma)
    @param String sCdMaoPropria: Indica se a encomenda será entregue com o serviço adicional mão própria.
                                 Valores possíveis: S ou N (S – Sim, N – Não)
    @param Int nVlValorDeclarado: Indica se a encomenda será entregue com o serviço adicional valor declarado.
                                  Neste campo deve ser apresentado o valor declarado desejado, em Reais.
    @param String sCdAvisoRecebimento: Indica se a encomenda será entregue com o serviço adicional aviso de recebimento.
                                       Valores possíveis: S ou N (S – Sim, N – Não)
    @param String StrRetorno: Indica a forma de retorno da consulta. XML  Resultado em XML Popup 
                              Resultado em uma janela popup   Resultado via post em uma página do requisitante
    @return String: Conteúdo vindo da página dos correios como retorno da chamada
    '''
    url_correios = 'http://ws.correios.com.br/calculador/CalcPrecoPrazo.aspx'

    # Apesar da documentação oficial declarar que a chamada deve ser via POST os dados são enviados via GET
    method='get'

    # ajusta valores em um dicionário
    values = {
              'nCdEmpresa':nCdEmpresa,
              'sDsSenha':sDsSenha,
              'nCdServico':nCdServico,
              'sCepOrigem':sCepOrigem,
              'sCepDestino':sCepDestino,
              'nVlPeso':nVlPeso,
              'nCdFormato':nCdFormato,
              'nVlComprimento':nVlComprimento,
              'nVlAltura':nVlAltura,
              'nVlLargura':nVlLargura,
              'nVlDiametro':nVlDiametro,
              'sCdMaoPropria':sCdMaoPropria,
              'nVlValorDeclarado':nVlValorDeclarado,
              'sCdAvisoRecebimento':sCdAvisoRecebimento,
              'StrRetorno':StrRetorno
              }

    # busca o conteúdo da URL gerada
    return call_url(url=url_correios,method=method, values=values)
# End correios_frete

def correios_frete_simples(cep_origem, cep_destino, comprimento, largura, altura, peso,
                           metodos='sedex, pac',codigo='', senha=''):
    '''
    Este método faz a chamada de página dos correios com as informações mais comuns e retorna um dicionário com os valores
    @param String cep_origem: cep de origem sem hifens. Caso haja hifens eles serão retirados
    @param String cep_destino: cep de destino sem hifens. Caso haja hifens eles serão retirados
    @param Int comprimento: comprimento da caixa em cm
    @param Int largura: largura da caixa em cm
    @param Int altura: altura da caixa em cm
    @param String peso: peso da encomenda em Kg(0.300, 1, 2, 3)
    @param String metodos: listagem dos serviços para calculo do frete. Use somente minusculas e palavras separadas por hifens.
                           Separe os métodos com vírgulas. Insira '-c' nos serviços com contrato (sedex-c, sedex-hoje-c)
    @param String codigo: codigo de servico caso exista
    @param Srtring senha: senha de servico caso exista
    @
    @return: Dict: dicionario de dados de metodos de entrega
    '''
    # códigos dos métodos para associação
    c_metodos = {
                 'sedex' : '40010',
                 'sedex-c' : '40096',
                 'sedex-a-cobrar' : '40045',
                 'sedex-a-cobrar-c' : '40126',
                 'sedex-10' : '40215',
                 'sedex-hoje' : '40290',
                 'pac' : '41106',
                 'pac-c' : '41068',
                 'e-sedex' : '81019',
                 'e-sedex-c' : '81035',
                 }

    # remove espaços da string com os métodos
    metodos = metodos.replace(' ', '').split(',')

    # verifica se existem dados para o cálculo
    if len(metodos) < 1:
        return None

    # varre o métodos enviados deixando somente os métodos válidos
    v_metodos = []

    for m in metodos:
        if m in c_metodos.keys():
            v_metodos.append(str(c_metodos[m]))

    # se nenhum metodo válido é encontrado retorna nulo
    if len(v_metodos) < 1:
        return None

    # faz a consulta de valores e adiciona para uma variavel
    v_metodos=','.join(v_metodos)
    cep_origem = digits_only(cep_origem)
    cep_destino = digits_only(cep_destino)
    xml_correios = correios_frete(nCdEmpresa=codigo, sDsSenha=senha, nCdServico=v_metodos, sCepOrigem=cep_origem, sCepDestino=cep_destino, nVlPeso=peso, nCdFormato=1, nVlComprimento=comprimento, nVlAltura=altura, nVlLargura=largura, nVlDiametro=0, sCdMaoPropria='N', nVlValorDeclarado=0, sCdAvisoRecebimento='N', StrRetorno='XML')

    # verifica se há dados da consulta aos correios
    if xml_correios is not None:
        #transforma a resposta (pagina XML) em DOM
        data = xml2obj(xml_correios)

        if data:
            # cria um array limpo com os dados retornados
            data = data['cServico']
            retorno = {}
            for d in data:
                retorno[find_key(c_metodos, d['Codigo'])] = {'valor':d['Valor']}
            return retorno

    return None