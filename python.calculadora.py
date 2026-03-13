nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2  

print(f"A média do aluno é {media:.2f}")

if media >= 7:
   print ("A média é maior ou igual a 7, então o aluno está aprovado.")
   
else:
   print ("A média é menor que 7, então o aluno está reprovado.")
   
   