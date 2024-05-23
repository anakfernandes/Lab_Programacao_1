# Extensão ordenada

# Implemente a função extensao_ordenado(nums, novos) que insere os elementos da lista
# novos na lista nums. Contudo, a função deve implementar o algoritmo de inserção ordenada
# simulando o uso de um array e cada elemento inserido deve ser adicionado à lista nums
# através de um único append() seguido do reposicionamento do elemento na lista até a
# posição válida para manter a ordem, usando apenas operações de atribuição de itens.
# Observe que os dados em novos não necessariamente estarão ordenados.

def extensao_ordenado(nums, novos):  # nums é uma lista ordenada
    for elemento in novos:
        nums.append(elemento)
        j = len(nums) - 1  # índice do novo elemento

        while j > 0 and nums[j - 1] > nums[j]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1  # quando o elemento troca de posição, ele assume o índice do seu vizinho da esquerda


nums = [10, 20, 30, 40]
novos = [15, 54]
extensao_ordenado(nums, novos)
assert nums == [10, 15, 20, 30, 40, 54]

nums1 = []
novos1 = [15, 54]
extensao_ordenado(nums1, novos1)
assert nums1 == [15, 54]

nums2 = [15, 54]
novos2 = []
extensao_ordenado(nums2, novos2)
assert nums2 == [15, 54]

nums3 = []
novos3 = [54, 15]
extensao_ordenado(nums3, novos3)
assert nums3 == [15, 54]