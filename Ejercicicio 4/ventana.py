class Ventana:
    __titulo = ''
    __xsuperior = 0
    __ysuperior = 0
    __xinferior = 0
    __yinferior = 0
    def __init__(self,titulo = '',  xsuperior=0, ysuperior=0, xinferior=0, yinferior=0):
        self.__titulo = titulo
        self.__xsuperior = max(0,xsuperior)
        self.__ysuperior = max(0,ysuperior)
        self.__xinferior = min(500,xinferior)
        self.__yinferior = min(500,yinferior)
    def mostrar(self):
        print ('Ventana: {}\t Superior: (X:{}, Y:{})\tInferior: (X:{},Y:{})'.format(self.__titulo, self.__xsuperior, self.__ysuperior, self.__xinferior, self.__yinferior))    
    def getTitulo (self):
        return self.__titulo
    def alto(self):
        return (self.__yinferior - self.__ysuperior)
    def ancho(self):
        return (self.__xinferior - self.__xsuperior)
    def moverDerecha(self, numero):
        if self.__xinferior + numero > 500:
            numero = 500 - self.__xinferior
        self.__xsuperior += numero
        self.__xinferior += numero
    def moverIzquierda (self, numero):
        if self.__xsuperior - numero < 0:
            numero = self.__xsuperior
        self.__xsuperior -= numero
        self.__xinferior -= numero
    def subir (self, numero=0):
        if self.__ysuperior - numero < 0:
            numero = self.__ysuperior
        self.__ysuperior -= numero
        self.__yinferior -= numero
    def bajar (self, numero=0):
        if self.__yinferior + numero > 500:
            numero = 500 - self.__yinferior
        self.__ysuperior += numero
        self.__yinferior += numero        


