
print()
print(" CALCULADORA ".center(60, '#'))
print()

while True:
      print()
      print(" OPERAÇÕES: ".center(60, '*'))
      print()
      print("[1]Soma [2]Subtração [3]Multiplicação [4]Divisão [5]Sair \n")
      print("".center(60, '*'))
      print()
      operacao_escolhida = int(input("Digite qual a operação: "))
      print()
        
      operacoes_validas = [1, 2, 3, 4, 5]

      while operacao_escolhida not in operacoes_validas:
                  print("Operação Inválida, Digite 1, 2, 3, 4 ou 5.")
                  operacao_escolhida = int(input("Digite qual a peração: "))
                  print()

      if operacao_escolhida == 5:
            print("Encerrando.")
            break    

      primeiro_numero = float(input("Primeiro Valor: "))
      segundo_numero = float(input("Segundo Valor: "))
      print()

                  

      if operacao_escolhida == 1:
                  print("Resultado: ", primeiro_numero + segundo_numero)
                 

      elif operacao_escolhida == 2:
                  print("Resultado: ", primeiro_numero - segundo_numero)
                  

      elif operacao_escolhida == 3:
                  print("Resultado: ", primeiro_numero * segundo_numero)
                  

      elif operacao_escolhida == 4:
            if segundo_numero == 0:
                        print("Divisão por zero não permitida")
            else:
                        print("Resultado: ", primeiro_numero / segundo_numero)
                       
                        
                 
            