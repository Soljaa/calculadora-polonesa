'''
Neste exemplo, iremos criar uma classe ContaBancaria. Nela, teremos o método construtor __init__
que instancia o objeto, dado os parâmetros recebidos por eles. Esses parâmetros são passados como 
atributos do objeto instanciado.
'''

class ContaBancaria:

    # Definindo um contador para a classe, de forma que a cada nova conta instanciada ela terá um
    # registro. Esse é um atributo de classe, que será comum a todos os objetos ContaBancaria. Ele
    # será incrementado a cada objeto instanciado. Note que os atributos de classe são definidos
    # FORA do método construtor
    contador = 1000

    # No método construtor da classe, definimos os atributos de instância, ou seja, do objeto. 
    # Utilizamos '__' antes do atributo para defini-lo como privado, ou seja, só conseguimos
    # acessá-lo dentro da classe, e assim temos mais segurança nos dados.
    def __init__(self, nome, saldo):
        # incrementamos o contador para que o próximo objeto instanciado receba um novo registro
        ContaBancaria.contador += 1
        self.__registro = ContaBancaria.contador # note que para referenciar 
        self.__nome = nome
        self.__saldo = saldo

    # Os métodos que definiremos serão relativos ao objeto que estamos instanciando. São funções
    # que realizam alguma tarefa com o objeto. OBS: quando definimos o TIPO do parâmetro passado
    # para a função, podemos fazer um controle do uso correto do código, tratando os erros.
    def saque(self, valor_saque: float):
        '''Verifica se o saque é válido, e retira o valor do saldo do cliente.
        :param valor_saque: valor a ser retirado da conta
        :return: novo saldo
        '''
        if type(valor_saque) != float:
            return print(f'\nValor incorreto. Tente novamente.')
        else:
            if valor_saque <= 0:
                return print(f'\nSaque inválido.')
            elif valor_saque > self.__saldo:
                return print(f'\nSaldo insuficiente.')
            else:
                self.__saldo -= valor_saque
                return print(f'\nSaque concluído com sucesso!')

    # Sabemos que queremos um método que fará um depósito na conta, mas como ainda estamos
    # desenvolvendo o código, colocamos apenas o 'pass', que permite que o método exista
    # antes que façamos a definição do que ele faz.
    def deposito(self, valor_deposito: float):
        pass

    def extrato(self):
        '''Imprime o extrato da conta bancária.
        :return: extrato com as informações da conta
        '''
        return print(f'\n{30 * "-"} EXTRATO {30 * "-"}\n'
                f'NÚMERO DA CONTA: {self.__registro}\n'
                f'NOME: {self.__nome}\n'
                f'SALDO: R$ {self.__saldo:.2f}\n{69 * "-"}')

    # Definimos um método de classe, que vai referenciar a atributos de classe, ou a nenhum
    # atributo. Ele recebe o decorator @classmethod.
    @classmethod
    def quantos_usuarios(cls):
        '''Informa quantos usuarios da ContaBancaria existem'''
        return print(f'\nAtualmente existem {ContaBancaria.contador - 1_000} usuários.')
    

# Instanciando 3 objetos do tipo ContaBancaria
u1 = ContaBancaria('Maria', 1_000.00)
u2 = ContaBancaria('João', 4_000.00)
u3 = ContaBancaria('Mônica', 290_000.00)

# Testando o método de classe
ContaBancaria.quantos_usuarios()

# Vamos fazer um saque na conta da Maria e forçar um erro TypeError, inserindo um inteiro
print(f'Tentando sacar um valor inteiro da conta da Maria')
u1.saque(150)
# Note que esse erro foi tratado no código

# Vamos agora tentar fazer um saque na conta do João de um valor que ele não possuí
print(f'\nTentando sacar um valor além do limite da conta do João')
u2.saque(30_000.00)

# Vamos simular um saque bem sucedido na conta da Mônica
print(f'\nTentando sacar um valor da conta da Mônica')
u3.saque(145_093.87)

# Vamos verificar o extrato da conta da Mônica
u3.extrato()
