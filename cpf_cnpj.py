from validate_docbr import CPF,CNPJ

class cpf_cnpj_br:
    def __init__(self,doc="",tipo_doc=""):
        self.tipo_doc   = tipo_doc.lower()
        self.doc        = self.determinaValorDoc(str(doc))

    def __str__(self):
        if self.tipo_doc=='cnpj':
            mascara_cnpj = CNPJ()
            return mascara_cnpj.mask(self.doc)
        else:
            mascara_cpf = CPF()
            return mascara_cpf.mask(self.doc)


    def validaCpf(self,cpf):
        if cpf:
            valida_cpf = CPF()
            return valida_cpf.validate(cpf)
        else:
            return False

    def validaCnpj(self,cnpj):
        if cnpj:
            valida_cnpj = CNPJ()
            return valida_cnpj.validate(cnpj)
        else:
            return False

    def determinaValorDoc(self,doc):
        if self.tipo_doc   == 'cnpj':
            if self.validaCnpj(doc):
                return doc
            else:
                print("CNPJ inválido")
        elif self.tipo_doc == 'cpf':
            if self.validaCpf(doc):
                return doc
            else:
                print("CPF Inválido")
        else:
            print("Tipo de documento Inválido")