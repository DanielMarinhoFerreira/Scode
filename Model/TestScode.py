from Model import SistemaOperacional as OS

class TesteScode:
    
    def TesteListas(Self):
        
        _OS = OS.Sistema_Operacional()
        _Dir = _OS.Dir_Doc()
        
        if _Dir != None:
            _File = _OS.Search_File("Caso_de_teste_validos"+"\\"+"TesteListas.txt")
        
        return _File

    def TesteTiposBasicos(Self):
        
        _OS = OS.Sistema_Operacional()
        _Dir = _OS.Dir_Doc()
        
        if _Dir != None:
            _File = _OS.Search_File("Caso_de_teste_validos"+"\\"+"TiposBasicos.txt")
        
        return _File
    
    def TesteLoopFor(Self):
        
        _OS = OS.Sistema_Operacional()
        _Dir = _OS.Dir_Doc()
        
        if _Dir != None:
            _File = _OS.Search_File("Caso_de_teste_validos"+"\\"+"TesteLoopFor.txt")
        
        return _File
    
    def TesteLoopWhile(Self):
        
        _OS = OS.Sistema_Operacional()
        _Dir = _OS.Dir_Doc()
        
        if _Dir != None:
            _File = _OS.Search_File("Caso_de_teste_validos"+"\\"+"TesteLoopWhile.txt")
        
        return _File
    
    def TesteCondicional(Self):
        
        _OS = OS.Sistema_Operacional()
        _Dir = _OS.Dir_Doc()
        
        if _Dir != None:
            _File = _OS.Search_File("Caso_de_teste_validos"+"\\"+"TesteCondicional.txt")
        
        return _File
    
    def TesteFuncoes(Self):
        
        _OS = OS.Sistema_Operacional()
        _Dir = _OS.Dir_Doc()
        
        if _Dir != None:
            _File = _OS.Search_File("Caso_de_teste_validos"+"\\"+"TesteFuncoes.txt")
        
        return _File


    