
import segno

def normal_qr(id):
    qr = segno.make(id, micro=False)
    qr.save("normal_qr.jpg")
    return qr
