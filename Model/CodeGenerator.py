from lark import Tree, Token

class CodeGenerator:
    def __init__(self):
        self.code = []
        self.indent_level = 1  # Dentro do main()

    def indent(self):
        return "    " * self.indent_level

    def get_type_name(self, node):
        # Extrai o nome do tipo (ex: "int" ou "list<int>")
        if isinstance(node.children[0], Token):
            return node.children[0].value
        elif isinstance(node, Tree):
            if node.children[0].data == "list_type":
                inner_type = self.get_type_name(node.children[0].children[0])
                return f"list<{inner_type}>"
            else:
                # Outros casos, se houver
                return "unknown_type"
        else:
            return "unknown_type"

    def generate(self, tree):
        self.code = ["#include <stdio.h>", "int main() {"]
        self.visit(tree)
        self.code.append("    return 0;")
        self.code.append("}")
        return "\n".join(self.code)

    def visit(self, node):
        if isinstance(node, Tree):
            if node.data == "var_decl":
                type_node = node.children[0]  # tipo pode ser Token ou Tree
                var_type = self.get_type_name(type_node)
                var_name = node.children[1].value  # ID é sempre Token
                expr = self.expr_to_str(node.children[2])
                self.code.append(f"{self.indent()}{var_type} {var_name} = {expr};")

            elif node.data == "assignment":
                var_name = node.children[0].value  # ID Token
                op = node.children[1].data
                expr = self.expr_to_str(node.children[2])
                self.code.append(f"{self.indent()}{var_name} {op} {expr};")

            elif node.data == "print":
                expr = self.expr_to_str(node.children[0])
                self.code.append(f'{self.indent()}printf("%s\\n", {expr});')

            elif node.data == "input":
                self.code.append(f'{self.indent()}scanf("%s"); // ajustar variável depois')

            elif node.data == "if":
                cond = self.expr_to_str(node.children[0])
                self.code.append(f"{self.indent()}if ({cond}) {{")
                self.indent_level += 1
                for stmt in node.children[1:-1]:
                    self.visit(stmt)
                self.indent_level -= 1
                self.code.append(f"{self.indent()}}}")
                if len(node.children) > 2:
                    self.code.append(f"{self.indent()}else {{")
                    self.indent_level += 1
                    self.visit(node.children[-1])
                    self.indent_level -= 1
                    self.code.append(f"{self.indent()}}}")

            elif node.data == "while":
                cond = self.expr_to_str(node.children[0])
                self.code.append(f"{self.indent()}while ({cond}) {{")
                self.indent_level += 1
                for stmt in node.children[1:]:
                    self.visit(stmt)
                self.indent_level -= 1
                self.code.append(f"{self.indent()}}}")

            elif node.data == "for":
                # Exemplo simplificado: for (int i in range(5))
                id_name = node.children[1].value
                range_expr = self.expr_to_str(node.children[3])
                self.code.append(f"{self.indent()}for (int {id_name} = 0; {id_name} < {range_expr}; {id_name}++) {{")
                self.indent_level += 1
                for stmt in node.children[4:]:
                    self.visit(stmt)
                self.indent_level -= 1
                self.code.append(f"{self.indent()}}}")

            elif node.data == "return":
                expr = self.expr_to_str(node.children[0])
                self.code.append(f"{self.indent()}return {expr};")

            elif node.data == "func_def":
                ret_type = self.get_type_name(node.children[0])
                func_name = node.children[1].value
                self.code.append(f"{ret_type} {func_name}() {{")
                self.indent_level += 1
                for stmt in node.children[2:-1]:
                    self.visit(stmt)
                self.visit(node.children[-1])  # normalmente return
                self.indent_level -= 1
                self.code.append("}")

            else:
                for child in node.children:
                    self.visit(child)

    def expr_to_str(self, expr):
        if isinstance(expr, Token):
            return expr.value
        elif isinstance(expr, Tree):
            if expr.data == "number":
                return expr.children[0].value
            elif expr.data == "string":
                return expr.children[0].value
            elif expr.data == "char":
                return expr.children[0].value
            elif expr.data == "var":
                return expr.children[0].value
            elif expr.data == "value":
                return expr.children[0].children[0].children[0].value
            elif expr.data == "list_literal":
                elementos = [self.expr_to_str(child) for child in expr.children]
                return "{" + ", ".join(elementos) + "}"
            elif expr.data == "add":
                return f"{self.expr_to_str(expr.children[0])} + {self.expr_to_str(expr.children[1])}"
            elif expr.data == "sub":
                return f"{self.expr_to_str(expr.children[0])} - {self.expr_to_str(expr.children[1])}"
            elif expr.data == "mul":
                return f"{self.expr_to_str(expr.children[0])} * {self.expr_to_str(expr.children[1])}"
            elif expr.data == "div":
                return f"{self.expr_to_str(expr.children[0])} / {self.expr_to_str(expr.children[1])}"
            elif expr.data == "eq":
                return f"{self.expr_to_str(expr.children[0])} == {self.expr_to_str(expr.children[1])}"
            elif expr.data == "gt":
                return f"{self.expr_to_str(expr.children[0])} > {self.expr_to_str(expr.children[1])}"
            elif expr.data == "lt":
                return f"{self.expr_to_str(expr.children[0])} < {self.expr_to_str(expr.children[1])}"
            else:
                return "EXPR"
        return "EXPR"
