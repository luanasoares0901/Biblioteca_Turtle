import turtle

def desenhar(ang,tam,qtd_lado):
    for i in range(qtd_lado):
        desenhista.forward(tam)#tamanho da linha
        desenhista.left(ang)#angulo

num_lados=int(input("Digite o numero de lados: "))
angulo=360/num_lados

tela=turtle.Screen()
tela.bgcolor("pink")

desenhista= turtle.Turtle()

desenhar(angulo,100,num_lados)


tela.exitonclick()