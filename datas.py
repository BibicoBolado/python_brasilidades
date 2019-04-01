from datetime import date,datetime,timedelta
import time

class Datas_br:
    def __init__(self):
        self.data_cadastro = datetime.today()

    def __str__(self):
        return self.mascaraData(self.data_cadastro)

    def tempoCadastro(self):
        dias_cadastro = datetime.today() - self.data_cadastro
        print(dias_cadastro)

    @staticmethod
    def mascaraData(data):
        return data.strftime("%d/%m/%Y : %H:%M")

    def diaCadastro(self):
        dias=['segunda-feira','terça-feira','quarta-feira',
              'quinta-feira','sexta-feira','sabado','domingo']
        return dias[self.data_cadastro.weekday()]

    def mesCadastro(self):
        #mes = 'posicao0 janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro'
        #mes_lista = mes.split(' ')
        #return mes_lista[self.data_cadastro.month]
        return self.data_cadastro.strftime('%B')