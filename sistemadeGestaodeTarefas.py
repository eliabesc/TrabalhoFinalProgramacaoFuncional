from datetime import datetime, timedelta

# Definição de tipos de dados
class Tarefa:
    def __init__(self, titulo, descricao, data_vencimento, prioridade):
        self.titulo = titulo
        self.descricao = descricao
        self.data_vencimento = data_vencimento
        self.prioridade = prioridade

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def editar_tarefa(self, tarefa_original, tarefa_atualizada):
        for i, tarefa in enumerate(self.tarefas):
            if tarefa == tarefa_original:
                self.tarefas[i] = tarefa_atualizada

    def excluir_tarefa(self, tarefa):
        self.tarefas.remove(tarefa)

# Função para visualizar tarefas ordenadas por data de vencimento
def visualizar_tarefas_por_data(usuario):
    return sorted(usuario.tarefas, key=lambda x: x.data_vencimento)

# Função para visualizar tarefas ordenadas por prioridade
def visualizar_tarefas_por_prioridade(usuario):
    return sorted(usuario.tarefas, key=lambda x: x.prioridade)

# Função para gerar relatório estatístico
def gerar_relatorio(usuario):
    total_tarefas = len(usuario.tarefas)
    return f"Total de tarefas: {total_tarefas}"

# Função de notificação de tarefas próximas ao vencimento
def notificar_tarefas_proximas(usuario):
    hoje = datetime.now()
    return [tarefa for tarefa in usuario.tarefas if (tarefa.data_vencimento - hoje).days <= 1]

# Função lambda para dobrar os valores de uma lista
dobrar_valores = lambda lista: [valor * 2 for valor in lista]

# List comprehension para filtrar tarefas com prioridade maior que 5
filtrar_prioridade_alta = lambda usuario: [tarefa for tarefa in usuario.tarefas if tarefa.prioridade > 5]

# Função de alta ordem para aplicar uma função a cada tarefa
def aplicar_funcao(usuario, funcao):
    return [funcao(tarefa) for tarefa in usuario.tarefas]

# Casos de teste

def test_visualizar_tarefas_por_data():
    """
    Testa a função visualizar_tarefas_por_data, garantindo que as tarefas são ordenadas corretamente por data de vencimento.
    """
    usuario = Usuario("Teste", "teste@teste.com", "senha")
    # Criando tarefas com datas de vencimento distintas
    tarefa1 = Tarefa("Tarefa 1", "Descrição da tarefa 1", datetime.now() + timedelta(days=1), 2)
    tarefa2 = Tarefa("Tarefa 2", "Descrição da tarefa 2", datetime.now() + timedelta(days=3), 1)
    tarefa3 = Tarefa("Tarefa 3", "Descrição da tarefa 3", datetime.now() + timedelta(days=2), 3)
    
    # Adicionando tarefas ao usuário
    usuario.adicionar_tarefa(tarefa1)
    usuario.adicionar_tarefa(tarefa2)
    usuario.adicionar_tarefa(tarefa3)
    
    # Testando a função de ordenação por data de vencimento
    tarefas_ordenadas = visualizar_tarefas_por_data(usuario)
    assert tarefas_ordenadas == [tarefa1, tarefa3, tarefa2], "As tarefas não foram ordenadas corretamente por data de vencimento."

def test_visualizar_tarefas_por_prioridade():
    """
    Testa a função visualizar_tarefas_por_prioridade, garantindo que as tarefas são ordenadas corretamente por prioridade.
    """
    usuario = Usuario("Teste", "teste@teste.com", "senha")
    # Criando tarefas com prioridades distintas
    tarefa1 = Tarefa("Tarefa 1", "Descrição da tarefa 1", datetime.now(), 2)
    tarefa2 = Tarefa("Tarefa 2", "Descrição da tarefa 2", datetime.now(), 1)
    tarefa3 = Tarefa("Tarefa 3", "Descrição da tarefa 3", datetime.now(), 3)
    
    # Adicionando tarefas ao usuário
    usuario.adicionar_tarefa(tarefa1)
    usuario.adicionar_tarefa(tarefa2)
    usuario.adicionar_tarefa(tarefa3)
    
    # Testando a função de ordenação por prioridade
    tarefas_ordenadas = visualizar_tarefas_por_prioridade(usuario)
    assert tarefas_ordenadas == [tarefa2, tarefa1, tarefa3], "As tarefas não foram ordenadas corretamente por prioridade."
