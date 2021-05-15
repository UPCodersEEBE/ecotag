
import segno


def normal_qr(id):
    qr = segno.make(id, micro=False)

    qr.save(f"static/{id}.png",scale = 10)
    return qr
