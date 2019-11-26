# from aula09 import somar, subtrair
# from unittest import TestCase, main
#
# class Testes(TestCase):
#     def test_soma(self):
#         self.assertEqual(somar(5, 5), 10) # testa se 5 + 5 é igual a 10
#         self.assertLess(somar(5, 5), 11) # testa se 5 + 5 é menor que 11
#
#     def test_subtracao(self):
#         self.assertEqual(subtrair(5, 5), 10) # testa se 5 - 5 é igual a 10
#         self.assertLessEqual(subtrair(15, 5), 10) # testa se 15 - 5 é menor igual a 10
#
# if __name__ == "__main__":
#     main()
#
# Normalmente você cria um arquivo apenas para teste e importa o código do arquivo original
# para que você possa realizar os testes, igual fizemos aqui:
# estamos importando as funções do arquivo aula09 para realizar os testes no arquivo aula09_testes
# importamos também, do unittest, o TestCase e o main, para realizar os testes.

# Criando um TDD
from unittest import TestCase, main
from aula09 import validar_par

class Teste(TestCase):
    def test_par(self):
        self.assertEqual(validar_par(4), True)
        self.assertEqual(validar_par(1000), True)
    
    def test_impar(self):
        self.assertEqual(validar_par(5), False)
        self.assertEqual(validar_par(1001), False)

    def test_string(self):
        self.assertEqual(validar_par('102'), True)
        self.assertEqual(validar_par('1059'), False)
        self.assertEqual(validar_par('string'), None)

if __name__ == "__main__":
    main()