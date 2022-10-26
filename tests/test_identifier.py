
#from src.identifier import identifier
import sys
sys.path.append('src/')
from identifier import identifier

class TestesIdentifier:

    def teste1(self):
        assert identifier("q") == "Valido"
    
    def teste2(self):
        assert identifier("") == "Invalido"
    
    def teste3(self):
        assert identifier("q45876") == "Valido"
    
    def teste4(self):
        assert identifier("q1234567") == "Invalido"

    def teste5(self):
        assert identifier("a@%6") == "Invalido"

    def teste6(self):
        assert identifier("9") == "Invalido"