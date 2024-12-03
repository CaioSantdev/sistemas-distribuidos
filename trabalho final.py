from mpi4py import MPI
import numpy as np
from time import time
import matplotlib.pyplot as plt

# Função da integral
def f(x):
    return 5 * x**3 + 3 * x**2 + 4 * x + 20

# Método do trapézio para um intervalo
def trapezoidal_chunk(a, b, n):
    h = (b - a) / n
    x = a + h
    soma = 0
    for _ in range(1, n):
        soma += f(x)
        x += h
    return h * soma

# Implementação onde o mestre processa
def mestre_processa(a, b, n):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    h = (b - a) / n
    chunk_size = n // size

    if rank == 0:
        results = np.zeros(size)

        for i in range(1, size):
            comm.send((a + i * chunk_size * h, a + (i + 1) * chunk_size * h, chunk_size), dest=i)

        results[0] = trapezoidal_chunk(a, a + chunk_size * h, chunk_size)
        for i in range(1, size):
            results[i] = comm.recv(source=i)

        total = h * ((f(a) + f(b)) / 2) + np.sum(results)
        return total
    else:
        a_local, b_local, chunk_size = comm.recv(source=0)
        result = trapezoidal_chunk(a_local, b_local, chunk_size)
        comm.send(result, dest=0)

# Implementação método Butterfly
def butterfly_method(a, b, n):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    h = (b - a) / n
    chunk_size = n // size
    local_a = a + rank * chunk_size * h
    local_b = local_a + chunk_size * h

    local_result = trapezoidal_chunk(local_a, local_b, chunk_size)

    step = 1
    while step < size:
        if rank % (2 * step) == 0:
            if rank + step < size:
                temp = comm.recv(source=rank + step)
                local_result += temp
        elif rank % (2 * step) == step:
            comm.send(local_result, dest=rank - step)
            break
        step *= 2

    if rank == 0:
        total = h * ((f(a) + f(b)) / 2) + local_result
        return total

# Função principal
def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    # Definições do problema
    a = 0
    b = 1000000
    n = 10000000

    # Calcular tempo de execução e resultados
    start = time()
    if rank == 0:
        print("Calculando com Mestre...")
    resultado_mestre = mestre_processa(a, b, n)
    if rank == 0:
        print(f"Resultado Mestre: {resultado_mestre}")
        print(f"Tempo Mestre: {time() - start} segundos")

    comm.Barrier()

    start = time()
    if rank == 0:
        print("\nCalculando com Butterfly...")
    resultado_butterfly = butterfly_method(a, b, n)
    if rank == 0:
        print(f"Resultado Butterfly: {resultado_butterfly}")
        print(f"Tempo Butterfly: {time() - start} segundos")

# Início do programa
if __name__ == "__main__":
    main()
