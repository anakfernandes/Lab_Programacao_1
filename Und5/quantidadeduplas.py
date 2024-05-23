quantidade_dupla = int(input())
soma = maior = 0
duplas = []
for i in range(quantidade_dupla):
    nums = input().split()
    duplas.append(nums)

for e in range(len(duplas)):
    for j in nums:
        if nums[0] > nums[1]:
            maior = nums[0]
        else:
            maior = nums[1]
        soma += int(maior)
print(f'soma maior {soma}')
