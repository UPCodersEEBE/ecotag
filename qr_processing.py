import segno

from queries_mongo import get_object_from_id, get_weight_from_id, get_impact_from_obj
from environmental_impact import get_grade


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


def qr_color_make(id):
    impact=get_impact_from_obj(id)
    weight = get_weight_from_id(id)
    grade=get_grade(impact, weight)
    qr=qr_colors(id, grade)
    return