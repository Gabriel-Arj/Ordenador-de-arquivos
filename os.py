import os
import shutil
import time

origem = '/home/gabriel/Downloads'

def organize_downloads(file):
    return os.path.join(origem, file)

os.chdir('/home/gabriel/Downloads')

while True:
    for file in os.listdir():
        if os.path.isfile(file):
            if file.endswith('.zip'):
                shutil.move(organize_downloads(file), '/home/gabriel/Downloads/Zips')
            elif file.endswith('.pdf'):
                shutil.move(organize_downloads(file), '/home/gabriel/Downloads/PDFs')
            elif file.endswith(('.jpg', '.jpeg', '.png')):
                shutil.move(organize_downloads(file), '/home/gabriel/Downloads/Imagens')
            else:
                shutil.move(organize_downloads(file), '/home/gabriel/Downloads/Outros')
    time.sleep(5)