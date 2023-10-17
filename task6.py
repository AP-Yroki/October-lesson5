n = int(input())
square = [[*map(int, input().split())] for i in range(n)]
m_const = n * (1 + n ** 2) // 2
print(('Квадрат обычный', 'Квадрат магический')[all(sum(el) == m_const for x in (((square[i][i] for i in range(n)), (square[i][~i] for i in range(n))), square, zip(*square)) for el in x) and set(sum(square, [])) == set(range(1, n ** 2 + 1))])
