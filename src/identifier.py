import re

def identifier(id):
    if id.isidentifier() and len(id) >= 1 and len(id) <= 6:
        return "Valido"
    else:
        return "Invalido"
 
#print(identifier("a$%@"))