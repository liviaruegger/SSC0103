"""
File:   agenda.py
Author: Ana Lívia Ruegger Saldanha (N.USP 8586691)
Brief:  SSC0103 - Programação Orientada a Objetos
        Exercícios sobre herança e polimorfismo
        Exercício 01: Agenda de contatos
"""


from pessoa import Pessoa, PessoaJuridica


"""
Crie uma agenda de contatos. Nessa agenda, contatos podem ser adicionados,
removidos, ou pesquisados por nome ou por CPF/CNPJ. Deve ser possível, também,
visualizar todos os contatos da agenda.
"""


class Agenda:

    def __init__(self) -> None:
        self.contatos = []


    def adicionar_pessoa_fisica(self) -> None:
        CPF          = str(input("Digite o CPF: "))
        nome         = str(input("Digite o nome: "))
        endereco     = str(input("Digite o endereço: "))
        nasc         = str(input("Digite a data de nascimento: "))
        email        = str(input("Digite o email: "))
        estado_civil = str(input("Digite o estado civil: "))

        nova_pessoa = Pessoa(CPF, nome, endereco, nasc, email, estado_civil)
        self.contatos.append(nova_pessoa)


    def adicionar_pessoa_juridica(self) -> None:
        CNPJ      = str(input("Digite o CNPJ: "))
        nome      = str(input("Digite o nome: "))
        endereco  = str(input("Digite o endereço: "))
        email     = str(input("Digite o email: "))
        inscricao = str(input("Digite a inscrição estadual: "))
        razao_soc = str(input("Digite a razão social: "))

        nova_pessoa = PessoaJuridica(CNPJ, nome, endereco, email, inscricao, razao_soc)
        self.contatos.append(nova_pessoa)


    def __get_indice_por_id(self, id: str) -> int:
        for i in range(len(self.contatos)):
            if self.contatos[i].get_id() == id:
                return i
        return -1

    
    def __get_indice_por_nome(self, nome: str) -> int:
        for i in range(len(self.contatos)):
            if self.contatos[i].get_nome() == nome:
                return i
        return -1


    def remover_contato(self, chave: str) -> None:
        if chave.isnumeric():
            indice = self.__get_indice_por_id(chave)
        else:
            indice = self.__get_indice_por_nome(chave)
        
        if indice != -1:
            self.contatos.pop(indice)
    

    def pesquisar_contato(self, chave: str) -> None:
        if chave.isnumeric():
            indice = self.__get_indice_por_id(chave)
        else:
            indice = self.__get_indice_por_nome(chave)

        if indice != -1:
            self.contatos[indice].imprimir()
        else:
            print("Contato não encontrado!")


    def visualizar_contatos(self) -> None:
        for contato in self.contatos:
            contato.imprimir()
            print()