nota = float(input('Informe a nota do aluno: '))
comportado = True if input('Comportado (y/n): ') == 'y' else False

if nota >= 8.5 and comportado:
    print('Parabéns você foi aprovado!')
    print('Você participa do quadro de honra')
elif nota >= 7 and  comportado == False:
    print('Você foi aprovado mas não é comportado!')
elif nota <= 5:
    print('Você esta de recuperação')
else:
    print('Você foi reprovado!!!!!!')

print(f'Sua nota final foi: {nota}')
