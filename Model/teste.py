from lark import Lark, UnexpectedInput
from grammar import Grammar

def test_grammar():
    try:
        grammar_str = Grammar().grammar()
        print("Compilando a gramática...\n")

        parser = Lark(grammar_str, parser="lalr", start="start")
        print("✅ Gramática compilada com sucesso!")

        # Código de exemplo para testar o parser
        exemplo = '''
            int x = 5
            float y = 3.14
            if (x > 3) {
                print(x)
            } else {
                print(y)
            }
        '''
        print("\nAnalisando código de exemplo...\n")
        tree = parser.parse(exemplo)
        print("✅ Código de exemplo analisado com sucesso!")
        print("\nÁrvore Sintática:\n")
        print(tree.pretty())

    except UnexpectedInput as e:
        print("❌ Erro de parsing:")
        print(e)
    except Exception as e:
        print("❌ Erro ao compilar a gramática:")
        print(e)

if __name__ == "__main__":
    test_grammar()
