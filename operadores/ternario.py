lockdown = False
money = 130

status = 'Em casa' if lockdown or money <= 100 else 'Deu bom'


print(f'O status é: {status}')