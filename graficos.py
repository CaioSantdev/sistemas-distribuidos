import pandas as pd
import matplotlib.pyplot as plt

# Dados fornecidos
processes = [1, 2, 4, 8, 16]
tempo_mestre = [4.276822805404663, 2.174808979034424, 1.132521152496338, 0.5868945121765137, 0.5937068462371826]
tempo_butterfly = [4.262850522994995, 2.152575969696045, 1.1049814224243164, 0.5631165504455566, 0.6866543292999268]
resultados_mestre = [1.2500009994861482e+24, 1.2500009371811437e+24, 1.2500007185938882e+24, 1.2500002343014266e+24, 1.249999242151596e+24]
resultados_butterfly = [1.2500009994861482e+24, 1.2500009371811437e+24, 1.2500007185938882e+24, 1.2500002343014266e+24, 1.2499992421515956e+24]

# Criar tabela
data = {
    "Nº Processos": processes,
    "Tempo Mestre (s)": tempo_mestre,
    "Tempo Butterfly (s)": tempo_butterfly,
    "Resultado Mestre": resultados_mestre,
    "Resultado Butterfly": resultados_butterfly,
}

df = pd.DataFrame(data)

# Exibir a tabela no terminal
print(df)

# Gerar gráficos
plt.plot(processes, tempo_mestre, label='Tempo Mestre', marker='o')
plt.plot(processes, tempo_butterfly, label='Tempo Butterfly', marker='o')
plt.xlabel('Número de Processos')
plt.ylabel('Tempo de Execução (s)')
plt.title('Tempo de Execução vs Número de Processos')
plt.legend()
plt.grid()
plt.show()
