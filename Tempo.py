hora_inicio = int(input("Digite a hora do início do jogo:"))
min_inicio = int(input("Digite o minuto do início do jogo:"))
hora_final = int(input("Digite a hora final do jogo:"))
min_final = int(input("Digite o minuto final do jogo:"))

if hora_inicio < hora_final:
    hora_total = hora_final - hora_inicio
    if min_inicio < min_final:
        min_total = min_final - min_inicio
    if min_inicio > min_final:
        hora_total = hora_total - 1
        min_total = ((min_inicio - 60)*-1) + min_final
    if min_inicio == min_final:
        min_total = 0
if hora_inicio > hora_final:
    hora_total = (24 - hora_inicio) + hora_final
    if min_inicio < min_final:
        min_total = min_final - min_inicio
    if min_inicio > min_final:
        hora_total = hora_total - 1
        min_total = (60 - min_inicio) + min_final
    if min_inicio == min_final:
        min_total = 0
if hora_inicio == hora_final:
    if min_inicio < min_final:
        min_total = min_final - min_inicio
        hora_total = 0
    if min_inicio > min_final:
        min_total = (60 - min_inicio) + min_final
        hora_total = 23
    if min_inicio == min_final:
        hora_total = 24
        min_total = 0

print("O JOGO DUROU",hora_total,"HORAS E",min_total,"MINUTOS")