import math
# seno cosseno e tangente

angulo=float(input("Digite o angulo que você deseja:"))
seno=math.sin(math.radians(angulo))
cos=math.cos(math.radians(angulo))
tan=math.tan(math.radians(angulo))
print("O angulo de {} tem o SENO de {:.2f} o Cosseno de {:.2f} e a tangente de {:.2f} ".format(angulo,seno,cos,tan))