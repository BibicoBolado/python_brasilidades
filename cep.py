import requests

class BuscaEndereco:
    def __init__(self,cep):
        if self.validaCep(str(cep)):
            self.cep = str(cep)
        else:
            raise NameError('CEP inválido')

    def __str__(self):
        return '{}-{}'.format(self.cep[:5],self.cep[5:])

    def validaCep(self,cep):
        if len(cep)==8:
            return True
        else:
            return False

    def acessaViaCep(self):
        url     = 'https://viacep.com.br/ws/{}/json'.format(self.cep)
        r       =  requests.get(url)
        dados   =  r.json()

        return dados['bairro'], dados['localidade'], dados['uf']