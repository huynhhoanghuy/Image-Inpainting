import os
from PIL import Image

entries = os.listdir('./training')
for entry in entries:
	file = './training/' + entry
	out = './out/' + entry
	img = Image.open(file)
	img = img.resize((128, 128), Image.ANTIALIAS)
	img.save(out)
