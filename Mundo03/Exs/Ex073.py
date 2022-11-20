times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athetico-PR', 'Atletico-MG',
'Fortaleza', 'Sao Paulo', 'America-MG', 'Botafogo', 'Santos', 'Goias', 'Bragantino', 'Coritiba', 'Cuiaba', 'Ceara SC',
'Atletico-GO', 'Avai', 'Juventude')

print('-' * 150)
print(f'Lista de times: {times}')
print('-' * 150)
print(f'Cinco primeiros: {times[0:5]}')
print('-' * 150)
print(f'Quatro ultimos: {times[-4:]}')
print('-' * 150)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-' * 150)
print(f'Sao Paulo esta na {times.index("Sao Paulo") + 1}° posicao')
