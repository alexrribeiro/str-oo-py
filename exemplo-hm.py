class Funcionario:
    def __init__(self, nome):
        self.nome = nome
    def registra_horas(self, horas):
        print('Horas registradas...')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Alura(Funcionario):
    # def mostrar_tarefas(self):
    #     print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')

class Hipster:
    def __str__(self):
        return f'Hipster, {self.nome}'

class Junior(Alura, Hipster):
    pass

class Pleno(Alura, Caelum, Hipster):
    pass

class Senior(Alura, Caelum, Hipster):
    pass

class Aluno(Hipster):
    def __init__(self, nome):
        self.nome = nome

joao = Junior('Joao')
joao.mostrar_tarefas()
joao.busca_perguntas_sem_resposta()
print(joao)

ana = Pleno('Ana')
ana.mostrar_tarefas()
ana.busca_cursos_do_mes()
ana.busca_cursos_do_mes('agosto')
ana.busca_perguntas_sem_resposta()
print(ana)

claudio = Senior('Claudio')
print(claudio)

yasmin = Aluno('Yasmin')
print(yasmin)