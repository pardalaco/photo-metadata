from PIL import Image
from PIL.ExifTags import TAGS


def metadatos(ruta):
        

    #Leemos la imagen

    mi_imagen = Image.open(ruta)

    #Extraemos los metadatos

    exif_data = mi_imagen.getexif()

    #Iteramos para sacar todos los metadatos

    dataEncontrada=False

    i=0

    for tagId in exif_data:
        #Obtenemos la etiqueta nombre
        tag = TAGS.get(tagId, tagId)
        data = exif_data.get(tagId)

        
        print(f"{tag:16} {data}")

    



metadatos("ruta")