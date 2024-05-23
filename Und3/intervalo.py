
primeiro = int(input())
segundo = int(input())
terceiro = int(input())

if (terceiro >= primeiro) and (terceiro <= segundo):
    print('dentro')

elif (terceiro < primeiro):
    print('antes')

else:
    print('depois')
