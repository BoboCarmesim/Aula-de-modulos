import random

num_ale=random.random()#Numeró aleatório entre 0 e 1
print(num_ale)

print(50*"-")

#nm_aule=random.seed(10)-> mantem um numéro aleatório,uma seed

num_ale=random.randrange(0,100)#Numeró entre 0 e 100
print(num_ale)

print(50*"-")

num_ale=random.randrange(0,100,5) # Numeró aleatório de 5 em 5
print(num_ale)

print(50*"-")

lista=["Pão","Arroz","Ovo","Batata"]# Escolhe um
print(random.choice(lista))

print(50*"-")

lista=["Pão","Arroz","Ovo","Batata"]
print(random.choices(lista,k=2))

# Faça um sorteio da megacena