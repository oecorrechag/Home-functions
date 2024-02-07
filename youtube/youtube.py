from pytube import YouTube
from pytube.exceptions import *

try:
    # crea una instancia de la clase YouTube
    video = YouTube('https://www.youtube.com/watch?v=xxxxxxxxxxx')
    
    # obtén la corriente de mayor resolución disponible
    stream = video.streams.get_highest_resolution()
    
    # descarga el video
    stream.download(output_path='/ruta/de/la/carpeta/de/destino')
    # stream.download(output_path='output')
    
    print('Descarga completa')
    
except (RegexMatchError, VideoUnavailable, PytubeError) as e:
    print(e)