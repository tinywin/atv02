# Atividade 2 (To-do List)

Esta aplicação de lista de tarefas é uma ferramenta de linha de comando simples, mas poderosa, desenvolvida em Python. Ela permite aos usuários gerenciar suas tarefas diárias de forma eficaz, adicionando tarefas à lista, marcando tarefas como concluídas e removendo tarefas da lista. O objetivo deste projeto é fornecer uma interface simples e intuitiva para gerenciamento de tarefas, utilizando operações de arquivo para persistência de dados.

## Funcionalidades Desenvolvidas

Adicionar Tarefa: Os usuários podem adicionar novas tarefas à lista, cada uma com uma descrição única. Uma vez adicionada, a tarefa é armazenada em um arquivo de texto (`tasks.txt`), permitindo persistência entre as execuções do programa.
  
Marcar Tarefa Como Feita: Esta funcionalidade permite aos usuários marcar uma tarefa específica como concluída. Ao marcar uma tarefa como feita, o status da tarefa é atualizado no arquivo de persistência.
  
Excluir Tarefa: Os usuários podem remover tarefas específicas da lista, utilizando o ID da tarefa como referência. Ao excluir uma tarefa, a entrada correspondente é removida do arquivo de persistência.

Verificar as Tarefas pendentes: O usuário verifica se existem tarefas ainda não concluídas no arquivo.

## Tecnologias Utilizadas

Linguagem de Programação: Python

Armazenamento de Dados: Arquivo de texto (`tasks.txt`)

## Como Usar

1. Clone o repositório do projeto para o seu computador local.
2. Navegue até o diretório do projeto através do terminal.
3. Execute o programa com o comando `python todo_app.py`.
4. Siga as instruções no menu de linha de comando para gerenciar suas tarefas.
