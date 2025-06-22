from lark import Tree, Token

class Symbol:
    def __init__(self, name, var_type):
        self.name = name
        self.type = var_type

class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = {}

    def analyze(self, tree):
        self.visit(tree)

    def visit(self, node):
        if isinstance(node, Tree):
            if node.data == "declaration":
                var_type = node.children[0].value
                var_name = node.children[1].value
                if var_name in self.symbol_table:
                    print(f"SemanticError: variável '{var_name}' já declarada.")
                else:
                    self.symbol_table[var_name] = Symbol(var_name, var_type)
            elif node.data == "assignment":
                var_name = node.children[0].value
                if var_name not in self.symbol_table:
                    print(f"SemanticError: variável '{var_name}' não declarada antes do uso.")
            for child in node.children:
                self.visit(child)