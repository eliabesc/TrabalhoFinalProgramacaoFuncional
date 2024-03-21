# TrabalhoFinalProgramacaoFuncional

Documento de Requisitos:

1. Requisitos Funcionais:

1.1. Cadastro de Usuários:

Descrição: O sistema deve permitir que os usuários se cadastrem fornecendo um nome, um email e uma senha.
Codificação: A função cadastrar_usuario receberá como entrada os dados do usuário e os armazenará em uma estrutura de dados adequada.
1.2. Login de Usuários:

Descrição: O sistema deve permitir que os usuários façam login utilizando o email e a senha cadastrados.
Codificação: A função login_usuario verificará se o email e a senha fornecidos correspondem a um usuário cadastrado.
1.3. Adição de Tarefas:

Descrição: Os usuários devem ser capazes de adicionar novas tarefas ao sistema, informando título, descrição, data de vencimento e prioridade.
Codificação: A função adicionar_tarefa receberá os dados da tarefa e a adicionará à lista de tarefas do usuário.
1.4. Visualização de Tarefas:

Descrição: Os usuários podem visualizar suas tarefas, ordenadas por data de vencimento ou prioridade.
Codificação: As funções visualizar_tarefas_por_data e visualizar_tarefas_por_prioridade ordenarão a lista de tarefas do usuário de acordo com os critérios especificados.
1.5. Edição de Tarefas:

Descrição: Os usuários podem editar suas tarefas, modificando título, descrição, data de vencimento ou prioridade.
Codificação: A função editar_tarefa receberá a tarefa original e a tarefa atualizada, realizando as modificações necessárias.
1.6. Exclusão de Tarefas:

Descrição: Os usuários podem excluir suas tarefas do sistema.
Codificação: A função excluir_tarefa removerá a tarefa especificada da lista de tarefas do usuário.
1.7. Relatório Estatístico:

Descrição: O sistema deve fornecer relatórios estatísticos sobre o progresso das tarefas.
Codificação: A função gerar_relatorio calculará e retornará estatísticas sobre as tarefas do usuário.
1.8. Notificações de Tarefas Próximas ao Vencimento:

Descrição: O sistema deve notificar os usuários sobre tarefas próximas ao vencimento.
Codificação: A função notificar_tarefas_proximas identificará as tarefas com data de vencimento próxima e as retornará para notificação.
2. Requisitos Não-funcionais:

2.1. Implementação em Python:

Descrição: O sistema deve ser implementado na linguagem de programação Python.
Codificação: Todo o código será escrito em Python.
2.2. Segurança:

Descrição: O sistema deve garantir a segurança dos dados dos usuários.
Codificação: Serão adotadas práticas de segurança, como hash de senhas, para proteger as informações dos usuários.
2.3. Usabilidade:

Descrição: O sistema deve ser intuitivo e de fácil utilização.
Codificação: A interface do usuário será desenvolvida de forma amigável e com mensagens claras de feedback.
2.4. Performance:

Descrição: O sistema deve ter uma boa performance, mesmo com grandes volumes de dados.
Codificação: Serão adotadas estratégias de otimização de código para garantir uma execução eficiente.

Casos de testes:

Teste test_visualizar_tarefas_por_data:

Descrição: Este teste verifica se a função visualizar_tarefas_por_data ordena corretamente as tarefas por data de vencimento.
Cenário de Teste: São criadas três tarefas com datas de vencimento distintas e são adicionadas ao usuário. As datas de vencimento são definidas para 1, 2 e 3 dias no futuro, respectivamente. Em seguida, a função visualizar_tarefas_por_data é chamada para ordenar as tarefas por data de vencimento.
Resultado Esperado: As tarefas devem ser ordenadas corretamente por data de vencimento, com a primeira tarefa sendo a que vence mais cedo, seguida pela segunda tarefa e assim por diante.
Teste test_visualizar_tarefas_por_prioridade:

Descrição: Este teste verifica se a função visualizar_tarefas_por_prioridade ordena corretamente as tarefas por prioridade.
Cenário de Teste: São criadas três tarefas com prioridades distintas e são adicionadas ao usuário. As prioridades das tarefas são definidas como 2, 1 e 3, respectivamente. Em seguida, a função visualizar_tarefas_por_prioridade é chamada para ordenar as tarefas por prioridade.
Resultado Esperado: As tarefas devem ser ordenadas corretamente por prioridade, com a primeira tarefa sendo a de menor prioridade, seguida pela segunda tarefa e assim por diante.
Esses casos de teste garantem que as funções visualizar_tarefas_por_data e visualizar_tarefas_por_prioridade funcionam corretamente, ordenando as tarefas conforme esperado. Esses testes são importantes para garantir que o sistema de gestão de tarefas esteja funcionando corretamente e atendendo aos requisitos especificados.