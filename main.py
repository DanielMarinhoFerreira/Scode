from lark import Lark, UnexpectedInput, UnexpectedToken, UnexpectedCharacters
from lark import tree
from Model.TestScode import TesteScode, TesteLexicoScode, TesteSintatico
from Model.SistemaOperacional import Sistema_Operacional
from Model.SyntaxError import ErrorMaper
from Model.grammar import Grammar



Teste = TesteScode()
TesteLexico = TesteLexicoScode()
TesteSintarico = TesteSintatico()

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

#Teste sintatico Condicional
_ErrorMaper = ErrorMaper()
_ErrorMaper.MaperParser(parser=parser)

#Erro atribuição
try:
    parsed_tree_TesteListas = parser.parse(TesteSintarico.TesteAtribuicao())
    tree.pydot__tree_to_png(parsed_tree_TesteListas)
except UnexpectedToken as e:
    expected = ", ".join(_ErrorMaper.traduz_token(t) for t in e.expected)
    print(f"\nSyntaxError at line {e.line}, column {e.column}: Unexpected token '{e.token}' (type: {e.token.type}). Expected one of: {expected}.")

#Erro Operacao
try:
    parsed_tree_TesteListas = parser.parse(TesteSintarico.TesteErroUsoIncorretoOpe())
    tree.pydot__tree_to_png(parsed_tree_TesteListas)
except UnexpectedToken as e:
    expected = ", ".join(_ErrorMaper.traduz_token(t) for t in e.expected)
    print(f"\nSyntaxError at line {e.line}, column {e.column}: Unexpected token '{e.token}' (type: {e.token.type}). Expected one of: {expected}.")

#Erro colchete
try:
    parsed_tree_TesteListas = parser.parse(TesteSintarico.TesteFaltaColchete())
    tree.pydot__tree_to_png(parsed_tree_TesteListas)
except UnexpectedToken as e:
    expected = ", ".join(_ErrorMaper.traduz_token(t) for t in e.expected)
    print(f"\nSyntaxError at line {e.line}, column {e.column}: Unexpected token '{e.token}' (type: {e.token.type}). Expected one of: {expected}.")


#Erro parametros
try:
    parsed_tree_TesteListas = parser.parse(TesteSintarico.TesteFaltaParentese())
    tree.pydot__tree_to_png(parsed_tree_TesteListas)
except UnexpectedToken as e:
    expected = ", ".join(_ErrorMaper.traduz_token(t) for t in e.expected)
    print(f"\nSyntaxError at line {e.line}, column {e.column}: Unexpected token '{e.token}' (type: {e.token.type}). Expected one of: {expected}.")

#Erro loop
try:
    parsed_tree_TesteListas = parser.parse(TesteSintarico.TesteSintaticoLoop())
    tree.pydot__tree_to_png(parsed_tree_TesteListas)
except UnexpectedToken as e:
    expected = ", ".join(_ErrorMaper.traduz_token(t) for t in e.expected)
    print(f"\nSyntaxError at line {e.line}, column {e.column}: Unexpected token '{e.token}' (type: {e.token.type}). Expected one of: {expected}.")

