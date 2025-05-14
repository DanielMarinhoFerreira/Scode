

class ErrorMaper:
    
    @classmethod
    def MaperParser(self, parser):
        self.parser = parser

    def mapear_tokens_anonimos(self):
        """dicionário com mapeamento de tokens __ANON_x."""
        anonimos = {}
        
        for term in self.parser.parser.lexer_conf.terminals:
            if term.name.startswith("__ANON_"):
                regex = term.pattern.value
                
                # Remove as barras e grupos, ex: /\+/ → +
                simbolo = regex.replace("\\", "")
                anonimos[term.name] = simbolo
        
        return anonimos

    def traduz_token(self, token_name):
        
        anonimos_map = self.mapear_tokens_anonimos()
        
        return anonimos_map.get(token_name, token_name)