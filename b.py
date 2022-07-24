from wand.image import Image
from wand.color import Color

file = "example.pdf"
with(Image(filename=file, resolution=300)) as source: 
      for i, image in enumerate(source.sequence):
            if i != 0:
                  image.resize(width=1654, height=2339, filter='undefined', blur=1)
                  image.crop(140, 140, 1654, 2339-158)
                  image.type = "undefined"
                  image.background_color = Color("white")
                  image.alpha_channel = 'remove'
                  if i+1<10:
                        newfilename = 'singlepages/'+ file[:-4] +'0' + str(i + 1) + '.png'
                  else:
                        newfilename = 'singlepages/'+file[:-4] + str(i + 1) + '.png'
                  Image(image).save(filename=newfilename)
                  #with Image(width=image.width, height=image.height, background=Color("white")) as bg:
                  #      bg.composite(image,0,0)
                 #       bg.save(filename=newfilename)
                #  bg.composite
                 # Image(image).save(filename=newfilename)