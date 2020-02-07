import os
from PIL import Image

entries = os.listdir('./validation')
for entry in entries:
	file = './validation/' + entry
	out = './out/' + entry
	img = Image.open(file)
	img = img.resize((256, 256), Image.ANTIALIAS)
	img.save(out)
