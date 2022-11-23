from PIL import Image, ImageDraw,ImageFont
from moviepy.editor import *
import os
def video():
	di='C:/Users/student/Documents/132Б/Пустовалов Михаил/pictore maker'
	fis=os.listdir(di)
	ims=list(filter(lambda x: x.endswith('.jpg'),fis))
	clips=[ImageClip(m).set_duration(2) for m in ims]
	final_clip=concatenate_videoclips(clips, method='compose')
	final_clip.write_videofile('cool.webm',fps=24)
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
print('Шо тебе надо?\n 1)Видео\n 2)Картиночки')
a=input()
if a==1:
	video()
elif a==2:
	for i in range(3):
        m(s[i],i)
else:
	print('Иди н')


