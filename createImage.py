import pymongo
from PIL import Image, ImageFont, ImageDraw, ImageEnhance

client = pymongo.MongoClient("mongodb+srv://tampier:tampier@cluster0.wybmf.mongodb.net/ecotag?retryWrites=true&w=majority")

db = client.ecotag

objects = db.objects

obj_to_draw = objects.find_one({ "id": 10 })

clean_obj =  {
    "h2o": obj_to_draw.get('h2o'),
    "c02": obj_to_draw.get('co2')
}


img = Image.new('RGB', (1500, 900), color = (230, 80, 137))

fnt = ImageFont.truetype('arial.ttf', 60)

d = ImageDraw.Draw(img)
d.text((10,10), "Hello World", fill=(255,255,255))
 
img.save('pil_tt.png')

print(obj_to_draw)
print(clean_obj)



