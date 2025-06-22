from lark import Lark, UnexpectedToken, tree
from Model.TestScode import TesteScode, TesteLexicoScode, TesteSintatico
from Model.SistemaOperacional import Sistema_Operacional
from Model.grammar import Grammar
from Model.SemanticAnalyzer import SemanticAnalyzer
from Model.CodeGenerator import CodeGenerator

Teste = TesteScode()
TesteLexico = TesteLexicoScode()
TesteSintarico = TesteSintatico()
Dir_Img = Sistema_Operacional()
grammar = Grammar().dir_grammar()
parser = Lark(grammar, parser="lalr", start="start")
semantic = SemanticAnalyzer()
generator = CodeGenerator()

def processar(nome, codigo):
    try:
        tree_parsed = parser.parse(codigo)
        semantic.analyze(tree_parsed)
        codigo_c = generator.generate(tree_parsed)
        
        print("[CÓDIGO GERADO]\n")
        print(codigo_c)

        with open(f"saida_{nome}.c", "w") as f:
            f.write(codigo_c)
        tree.pydot__tree_to_png(tree_parsed, filename=Dir_Img.Dir_Img()+"\\Img_teste_Validos\\" + f"{nome}.png")
    except UnexpectedToken as e:
        expected = ", ".join(e.expected)
        print(f"SyntaxError at line {e.line}, column {e.column}: Unexpected token '{e.token}' (type: {e.token.type}). Expected one of: {expected}.")

#processar("TesteTiposBasicos", Teste.TesteTiposBasicos())
processar("TesteCondicional", Teste.TesteCondicional())
processar("TesteListas", Teste.TesteListas())
processar("TesteLoopFor", Teste.TesteLoopFor())
processar("TesteLoopWhile", Teste.TesteLoopWhile())
processar("TesteFuncoes", Teste.TesteFuncoes())