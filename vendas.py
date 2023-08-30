listaprodutos = ["IPhone - R$10.000", "MacBook - R$25.000", "IPad - R$4.000"]
for produtos in listaprodutos:
    print(produtos)
    
vendas = 40000
if vendas > 25000:
    print("Ganhou Bônus")
else:
    print("Não Ganhou Bônus")
    
custo = 10000
lucro = vendas - custo
print("O Lucro do mês foi de:", lucro)
