def copy_matrix(matrix):
    return [row.copy() for row in matrix]

def print_matrix(matrix):
    for row in matrix:
        print(row)

def is_reflexive(relation_matrix):
    # Перевірка властивості рефлексивності
    for i in range(len(relation_matrix)):
        if relation_matrix[i][i] != 1:
            return False
    return True

def is_symmetric(relation_matrix):
    # Перевірка властивості симетричності
    for i in range(len(relation_matrix)):
        for j in range(len(relation_matrix[0])):
            if relation_matrix[i][j] != relation_matrix[j][i]:
                return False
    return True

def is_transitive(relation_matrix):
    # Перевірка властивості транзитивності
    n = len(relation_matrix)
    for i in range(n):
        for j in range(n):
            if relation_matrix[i][j]:
                for k in range(n):
                    if relation_matrix[j][k] and relation_matrix[i][k] != 1:
                        return False
    return True

def check_properties(relation_matrix):
    # Перевірка властивостей відношення
    is_equivalence = is_reflexive(relation_matrix) and is_symmetric(relation_matrix) and is_transitive(relation_matrix)
    is_partial_order = is_reflexive(relation_matrix) and is_transitive(relation_matrix)
    is_strict_order = ~is_reflexive(relation_matrix) and is_transitive(relation_matrix)

    print("Властивості відношення:")
    print(f"Еквівалентність: {is_equivalence}")
    print(f"Частковий порядок: {is_partial_order}")
    print(f"Строгий порядок: {is_strict_order}")

def closure_reflexive(relation_matrix):
    # Замикання відношення за рефлексивністю
    n = len(relation_matrix)
    reflexive_closure = copy_matrix(relation_matrix)
    for i in range(n):
        reflexive_closure[i][i] = 1
    return reflexive_closure

def closure_symmetric(relation_matrix):
    # Замикання відношення за симетричністю
    n = len(relation_matrix)
    symmetric_closure = copy_matrix(relation_matrix)
    for i in range(n):
        for j in range(n):
            if symmetric_closure[i][j] == 1:
                symmetric_closure[j][i] = 1
    return symmetric_closure

def closure_transitive(relation_matrix):
    # Замикання відношення за транзитивністю
    n = len(relation_matrix)
    transitive_closure = copy_matrix(relation_matrix)
    for i in range(n):
        for j in range(n):
            if transitive_closure[j][i] == 1:
                for k in range(n):
                    if transitive_closure[i][k] == 1 and transitive_closure[j][k] != 1:
                        transitive_closure[j][k] = 1
    return transitive_closure

def calculate_power(relation_matrix, exponent):
    n = len(relation_matrix)
    result_matrix = [row.copy() for row in relation_matrix]

    for _ in range(exponent - 1):
        temp_matrix = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    temp_matrix[i][j] |= (result_matrix[i][k] and relation_matrix[k][j])

        result_matrix = temp_matrix

    return result_matrix


my_matrix = [
    [1,0,1,0,1],
    [0,0,1,1,1],
    [0,1,1,0,0],
    [0,0,0,1,1],
    [0,0,0,0,1],
]
# print(is_symmetric(my_matrix))
# print(is_reflexive(my_matrix))
# print(is_transitive(my_matrix))

check_properties(my_matrix)

print("\nЗамикання за рефлексивністю:")
print_matrix(closure_reflexive(my_matrix))
print("\nЗамикання за симетричністю:")
print_matrix(closure_symmetric(my_matrix))
print("\nЗамикання за транзитивністю:")
print_matrix(closure_transitive(my_matrix))
print(is_transitive(closure_transitive(my_matrix)))

print('Друга степінь:')
print_matrix(calculate_power(my_matrix, 2))
print('Третя степінь:')
print_matrix(calculate_power(my_matrix, 3))