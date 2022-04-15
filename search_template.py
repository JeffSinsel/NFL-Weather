import pandas as pd
import re

def search(data,regex):
    searched = []    
    for values in data:
        found = re.search(regex, str(values))
        if found != None:
            searched.append(found.group())
        else:
            searched.append('')
    return searched


