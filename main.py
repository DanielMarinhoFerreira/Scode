from lark import Lark
from lark import tree



grammar = """
    value: dict
    | list
    | STRING
    | NUMBER
    | "true" | "false" | "null"
    list : "[" [value ("," value)*] "]"
    dict : "{" [pair ("," pair)*] "}"
    pair : STRING ":" value
    
    %import common.ESCAPED_STRING -> STRING
    %import common.SIGNED_NUMBER -> NUMBER
    %import common.WS
    %ignore WS
"""
grammar01 = """
    value: dict
    | list
    | STRING
    | NUMBER
    | "true" -> true
    | "false" -> false
    | "null" -> null

"""


json_parser = Lark(grammar, start='value')

text = '{"key": ["item0", "item1", 3.14]}'
json_parser.parse(text)

code = '{"key": ["item0", "item1", 3.14]}'

parser = Lark(grammar, start='value')
ast = parser.parse(code)

tree.pydot__tree_to_png(ast, 'parse_tree.png')

