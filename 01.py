import multiprocessing

sem = None

def init(s):
    global sem

    sem = s

def passando(direções):
    global sem

    with sem:
        print(f'O carro está passando, indo para o {direções}!')

def main():
    processos = 4
    params = ['Norte', 'Sul', 'Leste', 'Oeste']

    with multiprocessing.Manager() as manager:
        semaforo = manager.Semaphore(1)
        with multiprocessing.Pool(processes=processos, initializer=init, initargs=(semaforo, )) as pool:
            pool.map(passando, params)

if __name__ == '__main__':
    main()
