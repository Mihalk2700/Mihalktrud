from PIL import Image, ImageDraw,ImageFont
def m (s,i):
    #im= Image.new('RGB',(2000,2000), color=('#FAACAC'))
    im=Image.open('2panda.jpg')
    font=ImageFont.truetype('timesnewromanpsmt.ttf',size=100)
    draw_text=ImageDraw.Draw(im)
    draw_text.text(
        (200,200),
        s,
        font=font,
        fill='#1C0606')
#    im.show()
    im.save(str(i)+"new_pic.jpg")
s=['абоба',"Павел Николаевич Лучший!!","амогус"]
for i in range(3):
    m(s[i],i)
