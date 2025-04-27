import os
import os.path as Pt

class OS:
    
    def Dir_Doc(Self):
        
        try:
            if Pt.isdir(os.getcwd()+"\\"+"Doc"):
                dir_doc = os.getcwd()+"\\"+"Doc"
                return dir_doc
            else:
                return None
        except :
            return None
        
    def Search_File(Self, File):
        
        Dir_doc = Self.Dir_Doc()
        Arq_File = ""
        if Dir_doc != None:
            
            with open(Dir_doc+"\\"+File,'r',encoding='utf-8') as arq:
                Arq_File = arq.read()
                arq.close
                
            return Arq_File