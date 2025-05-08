from lark import Lark, UnexpectedInput
from lark import tree
from Model.TestScode import TesteScode, TesteLexicoScode
from Model.SistemaOperacional import Sistema_Operacional
from Model.grammar import Grammar



Teste = TesteScode()
TesteLexico = TesteLexicoScode()

Dir_Img = Sistema_Operacional()

parser = Lark(Grammar().grammar(),parser="lalr", start="start")

#Teste Tipos Basicos 
parsed_tree_TesteTiposBasicos = parser.parse(Teste.TesteTiposBasicos())
tree.pydot__tree_to_png(parsed_tree_TesteTiposBasicos,filename=Dir_Img.Dir_Img()+"\\"+"Img_teste_Validos"+"\\"+"TesteTiposBasicos.png")

#Teste Condicional
parsed_tree_TesteListas = parser.parse(Teste.TesteCondicional())
tree.pydot__tree_to_png(parsed_tree_TesteListas,filename=Dir_Img.Dir_Img()+"\\"+"Img_teste_Validos"+"\\"+"TesteCondicional.png")

#Teste Lista
parsed_tree_TesteListas = parser.parse(Teste.TesteListas())
tree.pydot__tree_to_png(parsed_tree_TesteListas,filename=Dir_Img.Dir_Img()+"\\"+"Img_teste_Validos"+"\\"+"TesteListas.png")

#Teste Loop For
parsed_tree_TesteListas = parser.parse(Teste.TesteLoopFor())
tree.pydot__tree_to_png(parsed_tree_TesteListas,filename=Dir_Img.Dir_Img()+"\\"+"Img_teste_Validos"+"\\"+"TesteLoopFor.png")

#Teste Loop while
parsed_tree_TesteListas = parser.parse(Teste.TesteLoopWhile())
tree.pydot__tree_to_png(parsed_tree_TesteListas,filename=Dir_Img.Dir_Img()+"\\"+"Img_teste_Validos"+"\\"+"TesteLoopWhile.png")

#Teste Loop Funções
parsed_tree_TesteListas = parser.parse(Teste.TesteFuncoes())
tree.pydot__tree_to_png(parsed_tree_TesteListas,filename=Dir_Img.Dir_Img()+"\\"+"Img_teste_Validos"+"\\"+"TesteFuncoes.png")

#Teste Lexico Condicional
try:    
    parsed_tree_TesteListas = parser.parse(TesteLexico.TesteCondicional())
    tree.pydot__tree_to_png(parsed_tree_TesteListas)
except UnexpectedInput as u:
    print(u.token)
    print(u.expected)
    print(u.line)
    print(u.column)
    exit(0)