def nota_quices(codigo: str, nota1: int, nota2: int, nota3: int, nota4: int, nota5: int) -> str:
    
   notaBaja = min(nota1, nota2, nota3, nota4, nota5)
   
   promedio = (nota1 + nota2 + nota3 + nota4 + nota5 - notaBaja)/4
   
   promedioReal = round(promedio/20, 3)
   
   promedioReal2 = str(round(promedioReal, 2))
    
   return "El promedio ajustado del estudiante {} es: {}".format(codigo, promedioReal2)

print(nota_quices("AAA", 40, 50, 39, 76, 96))
print(nota_quices("6456", 19, 90, 38, 55, 68))
print(nota_quices("fgdfg", 37, 10, 50, 19, 79))
print(nota_quices("dfgdf", 45, 46, 33, 74, 22))
print(nota_quices("dfg", 57, 100, 87, 93, 21))
print(nota_quices("dfgf", 5, 14, 76, 91, 5))