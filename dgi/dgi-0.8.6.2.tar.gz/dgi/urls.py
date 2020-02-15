"""
URLs identificadas de cada um dos serviços utilizados pelo dgi-dumps
"""

URL_LOGIN = "http://www.dgi.inpe.br/catalogo/login.php"
URL_CARINHO = "http://www.dgi.inpe.br/catalogo/addtocart.php?ACTION=CART&INDICE={}"
URL_CONFIRMA_PEDIDO = "http://www.dgi.inpe.br/catalogo/cartAddress.php?userid={}&nItens=1&sesskey={}&mediaCD=&total=0&action=Prosseguir"
URL_FECHA_PEDIDO = "http://www.dgi.inpe.br/catalogo/cartAddress.php?action=Fechar+Pedido&sesskey={}&userid={}&nItens={}&total=0&mediaCD="
URL_BUSCA = "http://www.dgi.inpe.br/catalogo/buscarimagens.php?p=1&pg={}&TRIGGER=BTNINTERFACE&CQA=CA&SATELITE={}&SENSOR={}&DATAINI={}&DATAFIM={}&Q1={}&Q2={}&Q3={}&Q4={}&LAT={}&LON={}&TAMPAGINA=20"
URL_BUSCA_RETANGULO = "http://www.dgi.inpe.br/catalogo/buscarimagens.php?p=1&pg={}&TRIGGER=BTNREGIAO&CQA=CA&SATELITE={}&SENSOR={}&DATAINI={}&DATAFIM={}&Q1={}&Q2={}&Q3={}&Q4={}&NORTE={}&SUL={}&LESTE={}&OESTE={}&TAMPAGINA=20"
