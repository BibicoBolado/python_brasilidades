from datetime import date,datetime,timedelta
import time
class Datas_br:
    def __init__(self):
        self.data_cadastro = datetime.today()

    def __str__(self):
        return self.data_cadastro.strftime("%d/%m/%Y : %H:%M")

    def tempo_cadastro(self):
        dias_cadastro = datetime.today() - self.data_cadastro
        print(dias_cadastro)