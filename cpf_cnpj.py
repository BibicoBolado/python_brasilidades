from validate_docbr import CPF

class DocCpf:
    def __init__(self,cpf):
        cpf_str = str(cpf)
        if self.validaCpf(cpf_str):
            self.cpf = cpf_str
        else:
            raise ValueError("CPF inválido")

    def __str__(self):
        return self.formataCpf(self.cpf)

    def validaCpf(self,cpf):
        valida_cpf = CPF()
        return valida_cpf.validate(cpf)

    @staticmethod
    def formataCpf(cpf):
        mascara_cpf = CPF()
        return mascara_cpf.mask(cpf)


cpf = DocCpf(15316264754)
print(cpf)