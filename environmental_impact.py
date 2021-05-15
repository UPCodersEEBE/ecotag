

def get_grade(impact,weight):
    total_impact = sum(impact.values())*weight/1000
    if total_impact==0:
        grade ="no_info"
    elif total_impact < 5:
        grade = 'a'
    elif total_impact < 15:
        grade= 'b'
    elif total_impact < 40:
        grade= 'c'
    elif total_impact < 70:
        grade= 'd'
    elif total_impact < 100:
        grade= 'e'
    elif total_impact > 100:
        grade= 'f'

    
    return grade