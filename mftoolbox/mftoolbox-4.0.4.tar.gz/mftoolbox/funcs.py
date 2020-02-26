def num_ptb2us(str_number):
    """
    Trasnforma um número do formato brasileiro (0.000,00 ou 0.000,00%) para o formato americano (0,000.00).
    :param str_number: string com o número no formato brasileiro que será transformado
    :return: número (inteiro ou float) transformado. Se número for uma porcentagem, retorna o resultado dividido por 100
    """
    try:
        number_to_return = float(str_number.upper().replace('R$ ','').replace('.','').replace(',','.').replace('\n','').replace('%','').strip())
        if str_number.find('%') != -1:
            number_to_return = number_to_return / 100
    except Exception as e:
        number_to_return = 0
    return number_to_return

def clean_text(str_text):
    """
    Remove de uma string espaços em branco nas pontas e '\n'
    :param str_text: texto a ser formatado
    :return: texto formatado (se o parâmetro de origem era uma string), o próprio valor passado como parâmetro (se o parâmetro não for uma string) ou uma string vazia ('') se o parâmetro passado for nulo
    """

    if str_text is None:
        return ''
    try:
        text_to_return = str_text.replace('\n','').strip()
    except:
        text_to_return = str_text
    return text_to_return

def find_keys_by_val(_dict, _value):
    """
    Encontra o nome de uma chave em um dicionário a partir de seu valor.
    Referência: https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary
    :param _dict: dicionário com chaves e valores
    :param _value: valor da chave
    :return: chave
    """
    try:
        key_2_return = list(_dict.keys())[list(_dict.values()).index(_value)]
    except:
        key_2_return = ''
    return key_2_return

def formata_fone(str_fone):
    """
    Formata no padrão brasileiro uma string contendo um telefone
    Se for um número celular, o formato final será +55 (DDD) #-####-####.
    Se for um número fixo, o formato final será +55 (DDD) ####-####.
    :param str_fone: string contendo um número de telefone
    :return: string formatada com o número de telefone no padrão brasileiro
    """
    str_fone = str_fone.strip().replace(' ', '').replace('-', '').replace('+','').replace('.','').replace('(','').replace(')','')
    if len(str_fone) == 8: #assumindo que é um número fixo sem DDD e DDI
        str_fone = '+55 (11) ' + str_fone[:4] + '-' + str_fone[4:]
    elif len(str_fone) == 9: #assumindo que é um número de celular sem DDD e DDI
        str_fone = '+55 (11) ' + str_fone[:5] + '-' + str_fone[5:]
    elif len(str_fone) == 10: #assumindo que é um número fixo com DDD e sem DDI
        str_fone = '+55 (' + str_fone[:2] + ') ' + str_fone[2:6] + '-' + str_fone[6:]
    elif len(str_fone) == 11: #assumindo que é um número de celular com DDD e sem DDI
        str_fone = '+55 (' + str_fone[:2] + ') ' + str_fone[2:3] + '-' + str_fone[3:7] + '-' + str_fone[7:]
    elif len(str_fone) == 12:  # assumindo que é um número fixo com DDD e DDI
        str_fone = '+' + str_fone[:2] + ' (' + str_fone[2:4] + ') ' + str_fone[4:8] + '-' + str_fone[8:12]
    elif len(str_fone) == 13:  # assumindo que é um número celular com DDD e DDI
        str_fone = '+' + str_fone[:2] + ' (' + str_fone[2:4] + ') ' + str_fone[4:5] + '-' + str_fone[5:9] + '-' + str_fone[9:13]
    return str_fone

def formata_url(str_url):
    """
    Formata no padrão https://url uma string contendo uma url
    :param str_url: url
    :return: url formatada
    """
    str_url = str_url.lower().replace('https','').replace('http','').replace('://','')
    return 'https://' + str_url

def formata_email(str_email):
    """
    Formata email no padrão lestras minúsculas e garante que tenho um '@'. ainda não valida formato dos domínios.
    :param str_email: email
    :return: email formatado
    """
    if str_email.find('@') < 0:
        return 'email com formato errado. Faltou \'@\''
    else:
        return clean_text(str_email).lower()

def formata_cnpj(str_cnpj):
    """
    Formata uma string contendo um CNPJ. Não checa se é um CNPJ válido.
    :param str_cnpj: string com o CNPJ
    :return: string formatada. Se a string não puder ser formatada (quantidade menor de dígitos), retorna mensagem de erro: 'CNPJ 'zzzzz' não pode ser formatado', onde zzzzzz é a string passada como parâmetro.
    """
    _temp_cnpj = clean_text(str_cnpj).replace('.', '').replace('/', '').replace('-', '')
    if not _temp_cnpj.isdigit() or len(_temp_cnpj) != 14:
        return 'CNPJ \'' + str_cnpj + '\' não pode ser formatado'
    else:
        return _temp_cnpj[:2] + '.' + _temp_cnpj[2:5] + '.' + _temp_cnpj[5:8] + '/' + _temp_cnpj[8:12] + '-' + _temp_cnpj[12:14]