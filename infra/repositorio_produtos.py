from infra.executa_database import consultadb, consultadb_com_parametros, updatecredentdb, consultageral
import logging
from datetime import datetime, date
import typing
logger = logging.getLogger('lucroadmin.infra.produtos')

class Produtos:

    def consulta_custo (self, SKU):
        logger.info('Produtos Repo | Iniciando consulta do preço de custo')
        query = 'SELECT preco_custo FROM produtos WHERE sku = %s'
        preco_custo = consultadb_com_parametros(execute=query, params=(SKU,))
        return preco_custo

