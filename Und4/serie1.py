for i in range(8, 101):
    if i == 8:
        print('8.8')
    else:
        print(float(i)) 
        for n in range(0, 4):
            i += 0.2
            if i > 100:
                break
            print(f'{i:.1f}')