INFORMAÇÕES PARA EXECUÇÃO DO PROGRAMA

Para realizar a execução do programa, é necessário descompactar o arquivo TP1.zip. Uma vez descompactado, basta
acessar o diretório em que o programa foi armazenado:

$   cd <diretoriodestino>

Agora, é necessário executar o problema com as informações na linha de comando. O primeiro parâmetro deverá ser
uma letra representando o algoritmo utilizado, seguido da configuração da entrada (as 3 linhas do 8 puzzle em
sequência, usando o número 0 para representar o espaço vazio). E, opcionalmente, um último parâmetro (PRINT)
indicando se os passos até a solução devem ser impressos.

A seguir, mostra-se a sigla usada para cada algoritmo:
A -> A* search
B -> Breadth-first search
G -> Greedy best-first search
H -> Hill Climbing
I -> Iterative deepening search
U -> Uniform-cost search

A seguir a instrução de execução:
$   python3 TP1.py <algoritmo> <configuração inicial> <PRINT-opcional>

Um exemplo de chamada para o algoritmo Hill Climbing seria:
$   python3 TP1.py H 1 2 3 4 5 6 7 8 0 PRINT

O programa retornará o número de estados percorridos até encontrar a solução, se houver.
Caso o parâmetro PRINT seja usado, mostrará em seguida, todos esses estados intermediários.