'''
class Grammar:

    def grammar(Self) -> str:

        _grammar = r"""
        start: statement+ _NEWLINE?

        statement: var_decl
                 | assignment
                 | if_stmt
                 | while_stmt
                 | for_stmt
                 | func_def
                 | func_call 
                 | print_stmt
                 | input_stmt

        var_decl: type ID "=" expr _NEWLINE
        type: "int" | "float" | "str" | "bool" | "char" | list_type
        list_type: "list" "<" type ">"

        assignment: ID "=" expr _NEWLINE

        print_stmt: "print" "(" expr ")" _NEWLINE
        input_stmt: "input" "(" ")" _NEWLINE

        if_stmt: "if" "(" expr ")" "{" statement+ "}" ["else" "{" statement+ "}"]
        while_stmt: "while" "(" expr ")" "{" statement+ "}"
        for_stmt: "for" "(" "int" ID "in" "range" "(" expr ")" ")" "{" statement+ "}"

        func_def: "def" type ID "(" [params] ")" "{" statement+ "return" expr _NEWLINE "}"
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
        start: statement+ _NEWLINE?

        statement: var_decl
                 | assignment
                 | if_stmt
                 | while_stmt
                 | for_stmt
                 | func_def
                 | func_call 
                 | print_stmt
                 | input_stmt

        var_decl: type ID "=" expr _NEWLINE
        type: "int" | "float" | "str" | "bool" | "char" | list_type
        list_type: "list" "<" type ">"

        assignment: ID "=" expr _NEWLINE

        print_stmt: "print" "(" expr ")" _NEWLINE
        input_stmt: "input" "(" ")" _NEWLINE

        if_stmt: "if" "(" expr ")" "{" statement+ "}" ["else" "{" statement+ "}"]
        while_stmt: "while" "(" expr ")" "{" statement+ "}"
        for_stmt: "for" "(" "int" ID "in" "range" "(" expr ")" ")" "{" statement+ "}"

        func_def: "def" type ID "(" [params] ")" "{" statement+ "return" expr _NEWLINE "}"
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
        start: statement+ _NEWLINE?

        statement: var_decl
                 | assignment
                 | if_stmt
                 | while_stmt
                 | for_stmt
                 | func_def
                 | func_call 
                 | print_stmt
                 | input_stmt

        var_decl: type ID "=" expr _NEWLINE
        type: "int" | "float" | "str" | "bool" | "char" | list_type
        list_type: "list" "<" type ">"

        assignment: ID "=" expr _NEWLINE

        print_stmt: "print" "(" expr ")" _NEWLINE
        input_stmt: "input" "(" ")" _NEWLINE

        if_stmt: "if" "(" expr ")" "{" statement+ "}" ["else" "{" statement+ "}"]
        while_stmt: "while" "(" expr ")" "{" statement+ "}"
        for_stmt: "for" "(" ID "in" expr ")" "{" statement+ "}"

        func_def: "def" type ID "(" [params] ")" "{" statement+ "return" expr _NEWLINE "}"
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
        start: (statement _NEWLINE?)+

        statement: var_decl
               | assignment
               | if_stmt
               | while_stmt
               | for_stmt
               | func_def
               | func_call 
               | print_stmt
               | input_stmt
               | return_stmt
          
        
        var_decl: type ID "=" expr _NEWLINE
        type: "int" | "float" | "str" | "bool" | "char" | list_type
        list_type: "list" "<" type ">"

         assignment: ID assignment_op expr _NEWLINE?
         assignment_op: "=" | "+=" | "-=" | "*=" | "/=" | "%="


        print_stmt: "print" "(" expr ")" _NEWLINE?
        input_stmt: "input" "(" ")" _NEWLINE?
        return_stmt: "return" expr _NEWLINE?

        if_stmt: "if" "(" expr ")" "{"  _NEWLINE? statement+ _NEWLINE? "}" ["else" "{"  _NEWLINE? statement+  _NEWLINE? "}"]
        while_stmt: "while" "(" expr ")" "{"  _NEWLINE? statement+  _NEWLINE? "}"  _NEWLINE?
        for_stmt: "for" "(" type ID "in" expr ")" "{" _NEWLINE? statement+ _NEWLINE? "}" _NEWLINE?

        func_def: "def" type ID "(" [params] ")" "{" _NEWLINE? statement+ _NEWLINE? "}"
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

   