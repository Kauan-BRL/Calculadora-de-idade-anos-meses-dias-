from datetime import datetime,date
from dateutil.relativedelta import relativedelta

class Calculadora:
    def __init__(self, data_nascimento):
        self._data_nascimento = data_nascimento

    def calcular_idade(self):
        data_hoje = date.today()
        data_nascimento = datetime.strptime(self._data_nascimento, '%d/%m/%Y').date()
        diferença_dias = (data_hoje - data_nascimento).days
        idade_exata = relativedelta(data_hoje, data_nascimento)

        if diferença_dias < 0 :
            return False
        
        if idade_exata.years == 0:
            if idade_exata.months == 0:
                if idade_exata.days == 0:
                    print('\nVocê nasceu hoje! Parabéns\n')
                else:
                    print(f'\nSua idade é de exatos {idade_exata.days} dias.\n')
            else:
                print(f'\nSua idade é de exatos {idade_exata.months} meses e {idade_exata.days} dias.\n')
        else:
            print(f'\nSua idade é de exatos {idade_exata.years} anos, {idade_exata.months} meses e {idade_exata.days} dias.\n')

while True:
    print(f'{20*'='} CALCULADORA DE IDADE EXATA {20*'='}')
    nascimento = Calculadora(input('Digite suas data de nascimento (DD/MM/AAAA): ')) 
    calcular_idade = nascimento.calcular_idade()

    if calcular_idade == False:
        print('\nVocê digitou uma data do futuro, digite uma data válida\n')
    else:
        break
