import multiprocessing
import random
import time

sem = None

def init(s):
    global sem

    sem = s

def processo(id, passos):
    global sem

    caminham(id, passos)
    time.sleep(random.randint(1, 2))
    with sem:
        abrir(id)

def caminham(id, passos):
    c = 0

    while (c < passos):
        print(f'A pessoa {id} deu um passo!')
        c = c + 1

def abrir(id):
    print(f'A pessoa {id} cruzou a porta!')

def main():
    processos = 4
    params = [0] * processos

    for n in range(4):

        id = n + 1
        velocidade = random.randint(4, 6)
        passos = 200//velocidade
        params[n] = (id, passos)

    with multiprocessing.Manager() as manager:
        semaforo = manager.Semaphore(1)
        with multiprocessing.Pool(processes=processos, initializer=init, initargs=(semaforo, )) as pool:
            pool.starmap(processo, params)

if __name__ == '__main__':
    main()
