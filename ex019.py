# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa
# que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random

alunos = ['Felipe', 'Jorge', 'Gabriela', 'Manuela']
sorteioAluno = random.choice(alunos)

print(f'O aluno sorteado foi: {sorteioAluno}')
