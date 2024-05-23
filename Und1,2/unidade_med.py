medmetro = float(input())

mdmetro =  medmetro / 100

mdjarda = 109.361
mdpe = 328.084
mdpolegada = 3937.008

jarda = mdmetro * 109.361
pe = mdmetro * 328.084
polegada = mdmetro * 3937.008

print(f'Jardas: {jarda:.3f} yd')
print(f'Pés: {pe:.3f} ft')
print(f'Polegadas: {polegada:.3f} in')
