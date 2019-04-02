from validate_docbr import CPF,CNPJ

class Documento:

    @staticmethod
    def criarNovo(doc):
        docStr = str(doc)
        if len(docStr) == 14:
            return DocCnpj(docStr)
        if len(docStr) == 11:
            return DocCpf(docStr)
        else:
            raise ValueError("Quantidade de caracteres inválida")

class DocCpf:
    def __init__(self,cpf):
        if self.valida(cpf):
            self.cpf = cpf
        else:
            raise ValueError("CPF inválido")

    def __str__(self):
        return self.formata(self.cpf)

    def valida(self,cpf):
        valida_cpf = CPF()
        return valida_cpf.validate(cpf)

    @staticmethod
    def formata(cpf):
        mascara_cpf = CPF()
        return mascara_cpf.mask(cpf)


class DocCnpj:
    def __init__(self, cnpj):
        if self.valida(cnpj):
            self.cnpj = cnpj
        else:
            raise ValueError("CNPJ Inválido")

    def __str__(self):
        return self.formata(self.cnpj)

    def valida(self, cnpj):
        valida_cnpj = CNPJ()
        return valida_cnpj.validate(cnpj)

    @staticmethod
    def formata(cnpj):
        mascara_cnpj = CNPJ()
        return mascara_cnpj.mask(cnpj)

cnpj = Documento.criarNovo(20881175000162)
cpf  = Documento.criarNovo(15316264754)
print(cpf)
print(cnpj)