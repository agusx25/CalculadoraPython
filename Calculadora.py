class EqSolver():
    def __init__(self):
        self.terminos = []
        self.operations = []
    def resolve(self, equation):
        self.terminos = equation.replace('-',' -').replace('+',' ').split()
        for i in equation:
            if i == '+' or i == '-':
                self.operations.append(i)
    def multiply(self, equation):
        for termino_index in range(len(self.terminos)):
            if '*' in self.terminos[termino_index]:
                pass
                

if __name__ == '__main__':
    eqsol = EqSolver()
    print("hola")
# def resolve(equation):
#     for i in equation:
#     separarN = self.terminos[i].replace('*',' ').replace('/',' ')
#           for i in equation:
#             if i == '*' or i == '/':
#                 separarO.append(i)
# "1*2*3*4*5/6/6*4/3"

# 6/2(1+2)
