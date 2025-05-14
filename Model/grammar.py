'''
class Grammar:

    def grammar(Self) -> str:

        _grammar = r"""
        start: value+ 

        value: var_decl
                 | assignment
                 | if
                 | while
                 | for
                 | func_def
                 | func_call 
                 | print
                 | input

        var_decl: type ID "=" expr _NEWLINE
        type: "int" | "float" | "str" | "bool" | "char" | list_type
        list_type: "list" "<" type ">"

        assignment: ID "=" expr _NEWLINE

        print: "print" "(" expr ")" _NEWLINE
        input: "input" "(" ")" _NEWLINE

        if: "if" "(" expr ")" "{" value+ "}" ["else" "{" value+ "}"]
        while: "while" "(" expr ")" "{" value+ "}"
        for: "for" "(" "int" ID "in" "range" "(" expr ")" ")" "{" value+ "}"

        func_def: "def" type ID "(" [params] ")" "{" value+ "return" expr _NEWLINE "}"
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
             | ESCAPED_STRING                -> string
             | CHAR_LITERAL                  -> char
             | "True"                        -> true
             | "False"                       -> false
             | ID                            -> var
             | func_call
             | list_access                   -> list_access
             | list_literal                  -> list_literal
             | "(" expr ")"

        list_access: ID "[" expr "]"
        list_literal: "{" [expr ("," expr)*] "}"

        ID: /[a-zA-Z_]\w*/
        NUMBER: /\d+(\.\d+)?/
        CHAR_LITERAL: /'[^']'/

        _NEWLINE: /(\r?\n)+/

        %import common.ESCAPED_STRING
        %import common.WS_INLINE
        %ignore WS_INLINE
        """

        return _grammar

class Grammar:

    def grammar(Self) -> str:

        _grammar = r"""
        start: value+ 

        value: var_decl
                 | assignment
                 | if
                 | while
                 | for
                 | func_def
                 | func_call 
                 | print
                 | input

        var_decl: type ID "=" expr _NEWLINE
        type: "int" | "float" | "str" | "bool" | "char" | list_type
        list_type: "list" "<" type ">"

        assignment: ID "=" expr _NEWLINE

        print: "print" "(" expr ")" _NEWLINE
        input: "input" "(" ")" _NEWLINE

        if: "if" "(" expr ")" "{" value+ "}" ["else" "{" value+ "}"]
        while: "while" "(" expr ")" "{" value+ "}"
        for: "for" "(" "int" ID "in" "range" "(" expr ")" ")" "{" value+ "}"

        func_def: "def" type ID "(" [params] ")" "{" value+ "return" expr _NEWLINE "}"
        params: param ("," param)*
        param: type ID

        func_call: ID "(" [args] ")"
        args: expr ("," expr)*

        ?expr: logic_or
             | list_access  -> list_access

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
             | ESCAPED_STRING                -> string
             | CHAR_LITERAL                  -> char
             | "True"                        -> true
             | "False"                       -> false
             | ID                            -> var
             | func_call
             | list_access                   -> list_access
             | list_literal                  -> list_literal
             | "(" expr ")"

        list_access: ID "[" expr "]"
        list_literal: "{" [expr ("," expr)*] "}"

        ID: /[a-zA-Z_]\w*/
        NUMBER: /\d+(\.\d+)?/
        CHAR_LITERAL: /'[^']'/

        

        %import common.ESCAPED_STRING
        %import common.NEWLINE -> _NEWLINE
        %import common.WS_INLINE
        %ignore WS_INLINE
        """

        return _grammar

class Grammar:

    def grammar(Self) -> str:

        _grammar = """
        start: value+ 

        value: var_decl
                 | assignment
                 | if
                 | while
                 | for
                 | func_def
                 | func_call 
                 | print
                 | input

        var_decl: type ID "=" expr _NEWLINE
        type: "int" | "float" | "str" | "bool" | "char" | list_type
        list_type: "list" "<" type ">"

        assignment: ID "=" expr _NEWLINE

        print: "print" "(" expr ")" _NEWLINE
        input: "input" "(" ")" _NEWLINE

        if: "if" "(" expr ")" "{" value+ "}" ["else" "{" value+ "}"]
        while: "while" "(" expr ")" "{" value+ "}"
        for: "for" "(" ID "in" expr ")" "{" value+ "}"

        func_def: "def" type ID "(" [params] ")" "{" value+ "return" expr _NEWLINE "}"
        params: param ("," param)*
        param: type ID

        func_call: ID "(" [args] ")"
        args: expr ("," expr)*

        ?expr: logic_or
             | index_expr
             | list_access  -> list_access

        index_expr: atom "[" expr "]" -> list_access

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
             | ESCAPED_STRING                -> string
             | CHAR_LITERAL                  -> char
             | "True"                        -> true
             | "False"                       -> false
             | ID                            -> var
             | func_call
             | list_literal                  -> list_literal
             | "(" expr ")"

        list_access: ID "[" expr "]"
        list_literal: "{" [expr ("," expr)*] "}"

        ID: /[a-zA-Z_]\w*/
        NUMBER: /\d+(\.\d+)?/
        CHAR_LITERAL: /'[^']'/

        %import common.NEWLINE -> _NEWLINE
        %import common.ESCAPED_STRING
        %import common.WS_INLINE
        %ignore WS_INLINE
        """

        return _grammar
'''
class Grammar:

    def grammar(Self) -> str:

        _grammar = """
        start: (value)+

        value: var_decl
               | assignment
               | if
               | while
               | for
               | func_def
               | func_call 
               | print
               | input
               | return
          
        
        var_decl: type ID "=" expr
        type: "int" | "float" | "str" | "bool" | "char" | list_type
        list_type: "list" "<" type ">"

        assignment: ID assignment_op expr
        assignment_op: "=" | "+=" | "-=" | "*=" | "/=" | "%="

        print: "print" "(" expr ")" 
        input: "input" "(" ")" 
        return: "return" expr 

        if: "if" "(" expr ")" "{" value+ "}" ["else" "{" value+ "}"]
        while: "while" "(" expr ")" "{" value+ "}"  
        for: "for" "(" type ID "in" expr ")" "{" value+ "}" 

        func_def: "def" type ID "(" [params] ")" "{" value+ "}"
        params: param ("," param)*
        param: type ID

        func_call: ID "(" [args] ")"
        args: expr ("," expr)*

        ?expr: logic_or
             | index_expr
             | list_access  -> list_access

        index_expr: atom "[" expr "]" -> list_access

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
             | ESCAPED_STRING                -> string
             | CHAR_LITERAL                  -> char
             | "True"                        -> true
             | "False"                       -> false
             | ID                            -> var
             | func_call
             | list_literal                  -> list_literal
             | "(" expr ")"

        list_access: ID "[" expr "]"
        list_literal: "{" [expr ("," expr)*] "}"

        ID: /[a-zA-Z_]\w*/
        NUMBER: /\d+(\.\d+)?/
        CHAR_LITERAL: /'[^']'/


        %import common.ESCAPED_STRING
        %import common.WS
        %ignore WS
        
        """

        return _grammar

   