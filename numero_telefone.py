import re
class telefone_br:
    def __init__(self,telefone=''):
        if self.validaTelefone(str(telefone)):
            self.telefone = str(telefone)
        else:
            raise ValueError('Número de telefone inválido')

    def __str__(self):
        return self.mascaraTelefone(self.telefone)

    def validaTelefone(self,telefone):
        padrao   = "([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao,telefone)
        if resposta:
            return True
        else:
            return False

    @staticmethod
    def mascaraTelefone(telefone):
        padrao = "([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao,telefone)
        return "({}){}-{}".format(resposta.group(1), resposta.group(2), resposta.group(3))