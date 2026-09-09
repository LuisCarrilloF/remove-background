from rembg import remove

class BackgroundRemover:
    
    # Variables de clase
    SUPPORTED_EXTENSIONS = ['.png','.jpg','.jpeg','.bmp']
    
    def __init__(self, input_folder, output_folder):
    
        # Variables de instancia
        self.input_folder = input_folder
        self.output_folder = output_folder

    def remove_background(self, input_folder, output_folder):
        with open(input_folder, 'rb') as input_file, open(output_folder, 'wb') as output_file:
            output = remove(input_file.read())
            output_file.write(output)

eliminador = BackgroundRemover('input.png','input2.png')
eliminador.remove_background('images/image.png', 'images/image_no_bg.png')

    


