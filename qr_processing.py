
import segno


def normal_qr(id):
    qr = segno.make(id, micro=False)
    qr.save(f"static/{id}.png",scale = 10)
    return qr

def qr_colors(id,grade):
    #qr = segno.make(id, micro=False)
    qr = segno.make(f"ecotag.herokuapp.com/oi/{id}", error='h')
    qr.to_artistic(background=f'static/base/{grade}.png', target=f"static/{id}.png", scale=10)
    #qr.save(f"static/{id}.png",scale = 10)
    return qr
