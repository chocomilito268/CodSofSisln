"https://raw.githubusercontent.com/PokeAPT/sprites/master/sprites/pokemon/back/132.png*"

import reguests 
import shutil
import json 

class Llamadanoseque:

    def coso_coso(self):
        r = requests.get(urI-"https://raw.githubusercontent. com/PokeAPT/sprites/master/sprites/pokemon/back/132.png")
        print (r.content)
        print(r.status_code) 

    def aña(self, url, file_name):
       res = requests-get(url,stream=True)
    
        if 200 - res.status_code:
           with open(file name, "wb") as f:
           shutil.copyfileobj(res.rau, f)
           print("imagen descarga completamente")
        else:
            print("No se encontro nada")
    def cosos_coso(self, pokemon):
        r - requests-get (url -"https://pokeap1.co/api/v2/pokemon/*+pokemon"+pokemon)
        obj - json.loads(r.content)
        return obj["sprites"]["front_shiny"]
    
pokemon = input("Escoge un pokemon: ")

yoyo = Llamadanoseque()
ing = yoyo. cosos_coso(pokemon)
yoyo -= aña (ing, str(pokemon)+" -png")