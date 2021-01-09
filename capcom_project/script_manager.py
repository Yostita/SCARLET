import random
import numpy as np
from datetime import datetime

def script_response(script):
    if script == "script_hora":
        return ("Son las" + datetime.time())
    
    if script == "script_numero_aleatorio":
        return str(random.randrange(100))
