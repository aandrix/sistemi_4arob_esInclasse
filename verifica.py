def leggiFile(nome_file):
    file=open(nome_file, "r")
    lista_righe= file.readlines()
    print(lista_righe)
    file.close()
    
    diz_mat={"data":[], "cognome":[], "quota":[]} #id sono numeri, nomi sono stringhe 
    #print(diz_mat)
    #exit()
    SOMMATOT=2200
    SOMMAPTOT=100
    sommaP=0
    somma=0
    for riga in lista_righe[:]:
        if(riga[-1]=="\n"):
            riga_senza_linefeed=riga[:-1] #senza \n
        else: riga_senza_linefeed=riga
        #print(riga_senza_linefeed)
        lista_campi=riga_senza_linefeed.split(";")
        #print(lista_campi)
        data=lista_campi[0]
        cognome=lista_campi[1]
        quota=int(lista_campi[2])
        #print(id, nome)
        diz_mat["data"].append(data)
        diz_mat["cognome"].append(cognome)
        diz_mat["quota"].append(quota)
        somma+=quota
        if(cognome=="Abello"):
            sommaP+=quota

    #print(somma)
    if somma==SOMMATOT:
        print(f"totale corretto")
    else:
        if somma>SOMMATOT: 
            print(f"sono presenti {somma-SOMMATOT} euro in più")   
        else: print(f"sono presenti {SOMMATOT-somma} euro in meno")
    #quota personale
    if(sommaP==SOMMAPTOT): print(f"Abello ha pagato tutta la quota")
    else: print(f"controllare la quota versata di Abello")   

    return diz_mat

def trovaIndice(lista_cognome1, k):
    for count, c in enumerate(lista_cognome1):
        if c==k: return count 


def pagamento(diz):
    lista_cognome=diz["cognome"]
    lista_quota=diz["quota"]
    lista_cognome1=[]
    lista_quota1=[]
    
    c=0
    for cogn, qu in zip(lista_cognome, lista_quota):
        if not cogn in lista_cognome1: 
            lista_cognome1.append(cogn)
            lista_quota1.append(qu)
        else:
            i=trovaIndice(lista_cognome1, cogn)
            lista_quota1[i]+=qu

    for cogn, qu in zip(lista_cognome1, lista_quota1):
        if qu!=100: 
            print(f"{cogn}, {qu} --> da controllare")
        else: 
            print(f"{cogn}, {qu}")

def main():
    diz=leggiFile("4AROB_GITA.csv")
    #print(diz)
    pagamento(diz)

if _name_ =="_main": #"_" = Dunder
    main()