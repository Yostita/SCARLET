import random
import numpy as np
from files_manager import get_valor
from datetime import datetime

def script_response(script):
    if script == "script_hora":
        return (f"Son las {datetime.now().hour}:{datetime.now().minute}")
    
    if script == "script_numero_aleatorio":
        return str(random.randrange(100))
    
    if script == "script_estado_animico":
        sentimiento = get_valor("sentimientos")

        if(sentimiento > 0):
            return (f"Si por como estoy te refieres a en que % se encuentra mi variable, me encuentro un {sentimiento}% alegre")
        if (sentimiento == 0):
            return (f"Si por como estoy te refieres a en que % se encuentra mi variable, me encuentro en un estado neutro")
        if(sentimiento < 0):
            return (f"Si por como estoy te refieres a en que % se encuentra mi variable, me encuentro un {abs(sentimiento)}% enfadada")
