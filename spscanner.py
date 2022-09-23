from PIL import ImageGrab
import time

sp = False
second_sp = False
imagepath = ""

def save(image):
    image.crop((170,50,400,150)).save(imagepath, "PNG")

def check():
    global sp
    global second_sp
    print("checking")
    image_rgb = ImageGrab.grab()  
    
    minheight = 50
    maxheight = 150
    
    minwidth = 170
    maxwidth = 400
    sp_found = False
    second_sp_found = False
    
    for col in range(minheight, maxheight):
        for row in range (minwidth, maxwidth):
            color = image_rgb.getpixel((row,col))
            if color == (228, 0, 0):
                sp_found = True
                if row > 350:
                    second_sp_found = True
                if not sp:
                    save(image_rgb)
                    sp = True
                    return
                elif row > 350 and not second_sp:
                    save(image_rgb)
                    sp = True
                    second_sp = True
                    return               
    
    sp = sp_found
    second_sp = second_sp_found
                
while True:
    time.sleep(60)
    check()
    
