import os
def generate_image_list(key_word):
    image_name_list = []
    path = 'C:/Users/andre/OneDrive/Desktop/veb-site/urfu_project/generator/static/generator/images'
    files = os.listdir(path=path)
    for i in range(len(files)):
        full_path = os.path.join(path, files[i])
        image_name_list.append(full_path)
    return image_name_list