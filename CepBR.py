import requests

class CepBr:

    def __init__(self, cep):
        cep = str(cep)
        if self.valida_cep(cep):
            self.cep = cep
        else:
            raise ValueError("CEP inválido!")

    def __str__(self):
        return self.format_cep()

    def valida_cep(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format_cep(self):
        return '{}-{}'.format(self.cep[:5], self.cep[5:])

    def api_via_cep(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json/"
        r = requests.get(url)
        dados_cep = r.json()
        return (
            dados_cep['cep'],
            dados_cep['logradouro'],
            dados_cep['bairro'],
            dados_cep['localidade'],
            dados_cep['uf']
        )



