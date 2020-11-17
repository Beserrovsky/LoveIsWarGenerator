from PIL import Image
import easygui as gui
from datetime import datetime
IsRunning=True
while(IsRunning):
    size=(0,0)
    position=(0,0)
    i = True
    while(i):
        choice = str(input("Fujiwara ou Ishigami? F/I ")).lower()
        if(choice=="f"):
            Im = Image.open("elenco/fuji.jpg")
            Mask = Image.open("elenco/wara.jpg").convert('L')
            size=(167,400)
            position=(54,107)
            i=False
        elif(choice=="i"):
            Im = Image.open("elenco/ishi.jpg")
            Mask = Image.open("elenco/gami.jpg").convert('L')
            size=(65,98)
            position=(710,288)
            i=False
        else:
            print("Não entendi, tente novamente!")
    Img = Image.open(str(gui.fileopenbox()))

    if Img.mode == 'RGBA':
        Img = Image.alpha_composite(Image.new('RGBA',Img.size,(255,255,255)),Img)

    Img = Img.resize(size)

    Img = Img.convert('RGB')

    Imback = Image.new('RGB',Im.size,(255))

    Imback.paste(Img,position)
    
    Im = Image.composite(Im,Imback,Mask)

    name = datetime.now()
    name = "GenAt"+str(name.strftime("%d%m%Y%H%M%S"+".jpg"))
    Im.save(name)
    final = Image.open(name)
    final.show()
    IsRunning = False
