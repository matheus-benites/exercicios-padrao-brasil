from datetime import datetime


class DatasBr:

    def __init__(self):
        self.momento_cadastro = datetime.today()

    def mes_cadastro(self):
        meses_do_ano = [
            '','janeiro', 'fevereiro', 'março',
            'abril', 'maio', 'junho', 'julho',
            'agosto', 'setembro', 'outubro',
            'novembro', 'dezembro'
        ]
        mes_cadastro = self.momento_cadastro.month
        return meses_do_ano[mes_cadastro]


    def dia_cadastro(self):
        dias_da_semana = [
            'segunda', 'terça', 'quarta',
            'quinta', 'sexta', 'sábado', 'domingo'
        ]
        dia_cadastro = self.momento_cadastro.weekday()
        return dias_da_semana[dia_cadastro]

    def formata_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada
