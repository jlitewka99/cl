# Import required packages
import cv2
import pytesseract


from PIL import Image

im = Image.open('out.png') # Can be many different formats.
pix = im.load()
rgb_im = im.convert('RGB')

width, height = im.size
print(width, height)

# Mention the installed location of Tesseract-OCR in your system


# Read image from which text needs to be extracted
img = cv2.imread("out.png")

# Preprocessing the image starts

# Convert the image to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Performing OTSU threshold
ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

# Specify structure shape and kernel size.
# Kernel size increases or decreases the area
# of the rectangle to be detected.
# A smaller value like (10, 10) will detect
# each word instead of a sentence.
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

# Applying dilation on the threshold image
dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)

# Finding contours
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Creating a copy of image
im2 = img.copy()

def crop(top, bottom, nopict):
      if nopict != 0:
            namenum =''
            if nopict < 10:
                  namenum = '0' + str(nopict)
            else:
                  namenum = str(nopict)
            im1 = im.crop((0, top, width-1, bottom))
            name = namenum+".png"
            im1 = im1.save(name)

last = 0
i = 0
end = height
# Looping through the identified contours
# Then rectangular part is cropped and passed on
# to pytesseract for extracting text from it
# Extracted text is then written into the text file
for cnt in reversed(contours):

      x, y, w, h = cv2.boundingRect(cnt)
      
      # Drawing a rectangle on copied image
      rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
      
      # Cropping the text block for giving input to OCR
      cropped = im2[y:y + h, x:x + w]
      
      # Open the file in append mode
      
      
      # Apply OCR on the cropped image
      text = pytesseract.image_to_string(cropped)
      
      # Appending the text into file
      if "Zadanie" in text:
            print("znalazlem")
            print(text)

            if i != 0:
                  crop(last, y, i)


            last = y
            i += 1
      elif "Brudnopis" in text:
            end = y

crop(last, end, i+1)

 
