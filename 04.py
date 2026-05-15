import multiprocessing
import random

sem = None

def init(s):
    global sem

    sem = s

def processo(esc):
    global sem

    with sem:
        for i in range(2):
            for j in range(3):
                print(f'O carro {i + 1} da escudeira {esc} deu sua {j + 1}º volta em {random.randint(5, 10)} segundos!')

def main():
    processos = 7
    params = [0] * processos

    for n in range(7):
        params[n] = (n + 1)

    with multiprocessing.Manager() as manager:
        semaforo = manager.Semaphore(5)
        with multiprocessing.Pool(processes=processos, initializer=init, initargs=(semaforo, )) as pool:
            pool.map(processo, params)

if __name__ == '__main__':
    main()
