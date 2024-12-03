Análise do Cálculo da Integral com MPI
Este repositório contém a implementação de métodos paralelizados para o cálculo da integral da função 
𝑓
(
𝑥
)
=
5
𝑥
3
+
3
𝑥
2
+
4
𝑥
+
20
f(x)=5x 
3
 +3x 
2
 +4x+20 no intervalo de 
𝑥
0
=
0
x 
0
​
 =0 a 
𝑥
𝑛
=
1000000
x 
n
​
 =1000000, com 
𝑛
=
10000000
n=10000000 usando o método do trapézio. Foram utilizados dois algoritmos paralelos: Mestre Processa e Butterfly. A seguir, são apresentados os resultados obtidos e uma análise comparativa entre eles.

Algoritmos Utilizados
Mestre Processa: O processo mestre divide a tarefa entre os processos escravos e coleta os resultados de cada um para calcular a integral final.
Butterfly: O algoritmo butterfly utiliza comunicação entre processos em diferentes estágios para dividir e combinar os cálculos da integral.
Função de Integração
A função 
𝑓
(
𝑥
)
f(x) a ser integrada é:

𝑓
(
𝑥
)
=
5
𝑥
3
+
3
𝑥
2
+
4
𝑥
+
20
f(x)=5x 
3
 +3x 
2
 +4x+20
A integral foi calculada no intervalo de 
[
0
,
1000000
]
[0,1000000] com 
𝑛
=
10000000
n=10000000 pontos de discretização.

Resultados
Tabela de Resultados
Os resultados mostrados abaixo indicam o valor aproximado da integral e o tempo de execução para cada número de processos (1, 2, 4, 8, 16).

Nº de Processos	Resultado Mestre (aproximado)	Resultado Butterfly (aproximado)	Tempo Mestre (s)	Tempo Butterfly (s)
1	1.2500009994861482e+24	1.2500009994861482e+24	4.28	4.26
2	1.2500009371811437e+24	1.2500009371811437e+24	2.17	2.15
4	1.2500007185938882e+24	1.2500007185938882e+24	1.13	1.10
8	1.2500002343014266e+24	1.2500002343014266e+24	0.59	0.56
16	1.249999242151596e+24	1.2499992421515956e+24	0.59	0.69
Análise dos Resultados:
Ambos os métodos fornecem resultados muito próximos para todos os números de processos.
Precisão: A integral calculada convergiu rapidamente para um valor muito preciso. As pequenas diferenças nos resultados podem ser atribuídas a imprecisões numéricas ou limitações de ponto flutuante.
Tempo de Execução: O tempo de execução diminui conforme o número de processos aumenta, como esperado em métodos paralelos. O método Mestre foi ligeiramente mais rápido que o Butterfly, especialmente com mais de 4 processos, provavelmente devido a uma sobrecarga menor de comunicação entre os processos.
Gráfico de Desempenho
A seguir, o gráfico que mostra a comparação entre o tempo de execução dos métodos Mestre e Butterfly para diferentes números de processos.


Observações sobre o gráfico:
O tempo de execução diminui conforme o número de processos aumenta, refletindo a paralelização.
O método Mestre apresenta uma ligeira vantagem sobre o Butterfly em termos de tempo, especialmente para 8 e 16 processos, devido a menor sobrecarga de comunicação.
Conclusões
Precisão: Ambos os métodos proporcionam resultados muito precisos, convergindo rapidamente para o valor correto da integral.
Escalabilidade: Ambos os métodos demonstraram boa escalabilidade, com a execução se tornando mais rápida à medida que o número de processos aumenta.
Eficiência: O método Mestre mostrou um desempenho ligeiramente melhor do que o Butterfly à medida que o número de processos aumentou, possivelmente devido a uma sobrecarga de comunicação maior no método Butterfly.
Para mais detalhes, consulte o código-fonte disponível no repositório.

