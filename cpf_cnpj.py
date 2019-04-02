from validate_docbr import CPF,CNPJ

class DocFactory:
    @staticmethod
    def factory(doc):
        docStr = str(doc)
        if len(docStr) == 14:
            return DocCnpj(docStr)
        if len(docStr) == 11:
            return DocCpf(docStr)
        else:
            raise ValueError("Quantidade de caracteres inválida")

class DocCpf:
    def __init__(self,cpf):
        if self.validaCpf(cpf):
            self.cpf = cpf
        else:
            raise ValueError("CPF inválido")

    def __str__(self):
        return self.formatCpf(self.cpf)

    def validaCpf(self,cpf):
        valida_cpf = CPF()
        return valida_cpf.validate(cpf)

    @staticmethod
    def formatCpf(cpf):
        mascara_cpf = CPF()
        return mascara_cpf.mask(cpf)


class DocCnpj:
    def __init__(self, cnpj):
        if self.validaCnpj(cnpj):
            self.cnpj = cnpj
        else:
            raise ValueError("CNPJ Inválido")

    def __str__(self):
        return self.formatCnpj(self.cnpj)

    def validaCnpj(self, cnpj):
        valida_cnpj = CNPJ()
        return valida_cnpj.validate(cnpj)

    @staticmethod
    def formatCnpj(cnpj):
        mascara_cnpj = CNPJ()
        return mascara_cnpj.mask(cnpj)

cpfRodrigo = DocFactory.factory(20881175000162)
print(cpfRodrigo)