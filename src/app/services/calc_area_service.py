import math

def calc_area_available(area, figure, street_size, space_between_streets):
    if figure == 'retangulo':
        total_street_size = street_size + space_between_streets
        street_qdt = math.floor(area / total_street_size)
        area_occupied_by_streets = street_qdt * street_size
        area_available = area - area_occupied_by_streets
        return {'plantingArea': area_available, 'numberOfStreets': street_qdt}

    if figure == 'triangulo':
        base = math.sqrt(2 * area)
        height = base / 2
        total_area = (base * height) / 2
        total_street_size = street_size + space_between_streets
        streets_qtd = math.floor(height / total_street_size)
        area_available = total_area - (streets_qtd * street_size * base / total_area)
        return {'plantingArea': area_available, 'numberOfStreets': streets_qtd}

    return {'error': True}