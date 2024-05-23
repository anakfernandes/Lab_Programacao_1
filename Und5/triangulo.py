cont_equi = 0
cont_iso = 0
cont_esc = 0
cont_tri = 0
cont_ntri = 0

while True:
    lados_tri = input().split()
    if lados_tri[0] == 'fim': break
    
    lados_tri[0] = int(lados_tri[0])
    lados_tri[1] = int(lados_tri[1])
    lados_tri[2] = int(lados_tri[2])
    if lados_tri[0] < lados_tri[1] + lados_tri[2] and lados_tri[1] < lados_tri[0] + lados_tri[2] and lados_tri[2] < lados_tri[0] + lados_tri[1]:
        cont_tri += 1
        if lados_tri[0] == lados_tri[1] == lados_tri[2]:
            cont_equi += 1        
        elif lados_tri[0] != lados_tri[1] != lados_tri[2]:
            cont_esc += 1
        elif lados_tri[0] == lados_tri[1] or lados_tri[0] == lados_tri[2] or lados_tri[1] == lados_tri[2] or lados_tri[1] == lados_tri[0] or lados_tri[2] == lados_tri[0] or lados_tri[2] == lados_tri[1]:
            cont_iso += 1
    else:
        cont_ntri += 1
    
if cont_equi != 0:   
  print(f'equilateros: {cont_equi}')
if cont_esc != 0:
  print(f'escaleno: {cont_esc}')
if cont_iso != 0:
  print(f'isoceles: {cont_iso}')
if cont_ntri != 0:
  print(f'nao triangulo: {cont_ntri}')
