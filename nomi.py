'''
    creare la list comprension che crei la lista con solo i nomi con g o h
'''



l = ["gauss", "conway", "eulero", "Hilbent"]
l_gh = [nome for nome in l if nome[0]=='g'or nome[0]=='h'or nome[0]=='H'or nome[0]=='G']
print(l_gh)