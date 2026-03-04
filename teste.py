from requests import get


def endpoint_pack(id_pack: int) -> str:

        url= f'https://api.mercadolibre.com/packs/{id_pack}'
        return url

def endpoint_order(id_venda: int) -> str:
    
    url = f'https://api.mercadolibre.com/orders/{id_venda}'
    return url

def extraindo_custos():

    comissaofrete = []
    id_venda = 2000015077524812 

    url_order: str = endpoint_order(id_venda=id_venda)

    access_token_ml = 'APP_USR-7778911123425720-021813-7cdcdfd52f8d39a24f69e175047f4e00-790037830'
    headers: dict[str, str] = {
            'Authorization' : f'Bearer {access_token_ml}',
            'Accept' : 'application/json'
        }
    response_order = get(url=url_order, headers=headers)
    json_response_order = response_order.json()
    id_pack: int = json_response_order['pack_id']
    url_pack: str = endpoint_pack(id_pack=id_pack)
    response_pack = get(url=url_pack, headers=headers)
    json_response_pack = response_pack.json()
    ids_venda = json_response_pack['orders']
    for item in ids_venda:
        id = item['id']
        url_venda = endpoint_order(id_venda=id)
        response_id = get(url=url_venda, headers=headers)
        print(response_id.text)

custo = extraindo_custos()

'''
Conclusão: Quando em uma venda há mais de um item o bling pega o primeiro código de venda do Mercado Livre,
           e com isso não conseguimos todos os dados de frete e comissão pois o Mercado Livre cria um Pack Id
           para que seja armazenado os dois itens do pacote. Com isso quando há mais de um item na venda devemos
           fazer uma requisição para o id do Mercado Livre que o Bling nos da, com o retorno conseguimos o
           Pack ID e devemos enviar uma requisição para a endpoint com o Pack ID e lá conseguiremos os Ids das
           duas vendas, ai então conseguiremos os custos das duas vendas.

'''