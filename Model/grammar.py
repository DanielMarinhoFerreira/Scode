grammar = """
start: statement+

statement: var_decl
         | assignment
         | if_stmt
         | while_stmt
         | for_stmt
         | func_def
         | func_call ";"
         | "print" "(" expr ")" ";"
         | "input" "(" ")" ";"

var_decl: type ID "=" expr ";"
type: "int" | "float" | "str" | "bool" | list_type
list_type: "list" "<" type ">"

assignment: ID "=" expr ";"

if_stmt: "if" "(" expr ")" "{" statement+ "}" ["else" "{" statement+ "}"]
while_stmt: "while" "(" expr ")" "{" statement+ "}"
for_stmt: "for" "(" "int" ID "in" "range" "(" expr ")" ")" "{" statement+ "}"

func_def: "def" type ID "(" [params] ")" "{" statement+ "return" expr ";" "}"
params: param ("," param)*
param: type ID

func_call: ID "(" [args] ")"
args: expr ("," expr)*

?expr: logic_or

?logic_or: logic_and
         | logic_or "or" logic_and   -> or_expr

?logic_and: equality
          | logic_and "and" equality -> and_expr

?equality: comparison
         | equality "==" comparison  -> eq

?comparison: term
           | comparison ">" term     -> gt
           | comparison ">=" term    -> ge
           | comparison "<" term     -> lt
           | comparison "<=" term    -> le

?term: factor
     | term "+" factor               -> add
     | term "-" factor               -> sub

?factor: unary
       | factor "*" unary            -> mul
       | factor "/" unary            -> div
       | factor "%" unary            -> mod

?unary: "not" unary                  -> not_expr
      | "-" unary                    -> neg_expr
      | atom

?atom: NUMBER                        -> number
     | ESCAPED_STRING               -> string
     | "True"                       -> true
     | "False"                      -> false
     | ID                           -> var
     | func_call
     | list_access
     | "(" expr ")"

list_access: ID "[" expr "]"

ID: /[a-zA-Z_]\w*/
NUMBER: /\d+(\.\d+)?/

%import common.ESCAPED_STRING
%import common.WS
%ignore WS

"""