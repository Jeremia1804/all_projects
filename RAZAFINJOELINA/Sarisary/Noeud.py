import base64
import io

class Noeud:
    def __init__(self,image,x,y,numero):
        self.photo = image;
        self.x = x;
        self.y = y;
        self.numero = numero;
        self.toBase64()

    def toBase64(self):
        buffered = io.BytesIO()
        self.photo.save(buffered, format="JPEG")
        self.base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')

    
    def toJson(self):
        info = {
            "x" : self.x,
            "y" : self.y,
            "numero":self.numero,
            "image":self.base64
        }
        return info

        