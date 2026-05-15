import multiprocessing
import random

x: int = 0

def init(val):
    global x

    x = val

def threads(id, saltos):
    global x

    s = 0
    print(f'Deu largada o sapo {id}!')
    
    for salto in saltos:
        print(f'O sapo {id} deu um salto de {salto} cm de distância')
        
        s = s + salto
        print(f'O sapo {id} percorreu {s} cm até agora')

    x.value = x.value + 1
    print(f'O sapo {id} chegou ao final em {x.value}º colocado!!!')

def main():
    processos = 5
    parametros = [0] * processos

    for n in range(5):

        vet = [0] * 30
        id = n + 1
        saltos = 0
        i = -1

        while (saltos < 30):

            i = i + 1
            vet[i] = random.randint(1, 5)
            saltos = saltos + vet[i]

        parametros[n] = (id, vet[:i])

    valor = multiprocessing.Value('i', 0)

    with multiprocessing.Pool(processes=processos, initializer=init, initargs=(valor, )) as pool:
        pool.starmap(threads, parametros)

if __name__ == '__main__':
    main()
