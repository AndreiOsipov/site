from .image_list_generator import generate_image_list

class Image_Table():
    def __init__(self, word):
        self.rows = []
        images_names = generate_image_list(word)
        for i in range(2):
            self.colls = []
            for j in range(8):
                if j + i*8 < len(images_names):
                    self.colls.append(images_names[j + i*8])
            self.rows.append(self.colls)