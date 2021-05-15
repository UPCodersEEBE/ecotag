
import segno


def normal_qr(id):
    qr = segno.make(id, micro=False)

    qr.save("normal_qr.png",scale = 10)
    return qr
