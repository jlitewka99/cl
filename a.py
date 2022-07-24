from PIL import Image

im = Image.open('out.png') # Can be many different formats.
pix = im.load()
rgb_im = im.convert('RGB')

width, height = im.size
print(width, height)



def getHeight(px):
	px2 = px
	bp = 20
	rgb = 191
	while True:
		ra, ga, ba = rgb_im.getpixel((700, px2))
		if (ra >= rgb - bp and ra <= rgb + bp) and (ga >= rgb - bp and ga <= rgb + bp) and (ba >= rgb - bp and ba <= rgb + bp):
			px2 += 1
		else:
			break
	return px2 - px

def crop(top, bottom, nopict):
	if nopict != 0:
		im1 = im.crop((0, top, width-1, bottom))
		name = str(nopict)+".png"
		im1 = im1.save(name)


i = 0
no = 0
last = 0
while i<height:
	if getHeight(i) == 40 and getHeight(i-1) <= 40:
		print(i)
		crop(last, i-1, no)
		last = i
		no += 1
	elif getHeight(i) == 39 and getHeight(i-1) != 40:
		print(i)
		crop(last, i-1, no)
		last = i
		no += 1
	elif getHeight(i) == 38 and getHeight(i-2) != 40 and getHeight(i-1) != 39:
		print(i)
		crop(last, i-1, no)
		last = i
		no += 1
	elif getHeight(i) == 37 and getHeight(i-3) != 40 and getHeight(i-2) != 39 and getHeight(i-1) != 38:
		print(i)
		crop(last, i-1, no)
		last = i
		no += 1
	elif getHeight(i) == 36 and getHeight(i-4) != 40 and getHeight(i-3) != 39 and getHeight(i-2) != 38 and getHeight(i-1) != 37:
		print(i)
		crop(last, i-1, no)
		last = i
		no += 1
	elif getHeight(i) == 35 and getHeight(i-5) != 40 and getHeight(i-4) != 39 and getHeight(i-3) != 38 and getHeight(i-2) != 37 and getHeight(i-1) != 36:
		print(i)
		crop(last, i-1, no)
		last = i
		no += 1
	elif getHeight(i) == 34 and getHeight(i-6) != 40 and getHeight(i-5) != 39 and getHeight(i-4) != 38 and getHeight(i-3) != 37 and getHeight(i-2) != 36 and getHeight(i-1) != 35:
		print(i)
		crop(last, i-1, no)
		last = i
		no += 1
	i+=1

crop(last, height-1, no)
print(no)