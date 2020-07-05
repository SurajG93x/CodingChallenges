class Car(object):
    def __init__(self, color, size, years, clearance):
        self.color = color
        self.size = size
        self.years = years
        self.clearance = clearance


carlist = []

carlist.append(Car("red", "mid", 7, 2))
carlist.append(Car("white", "large", 8, 4))
carlist.append(Car("white", "large", 5, 3))


def is_match(vehicles):
    match = False
    if vehicles and len(vehicles) == 3:
        if vehicles[0].clearance == vehicles[1].clearance == vehicles[2].clearance and vehicles[0].color == vehicles[
            1].color == vehicles[2].color and vehicles[0].size == vehicles[1].size == vehicles[2].size and vehicles[
            0].years == vehicles[1].years == vehicles[2].years:
            match = True
        elif vehicles[0].clearance != vehicles[1].clearance and vehicles[1].clearance != vehicles[2].clearance and vehicles[
            0].clearance != vehicles[2].clearance:
            if vehicles[0].years != vehicles[1].years and vehicles[1].years != vehicles[2].years and vehicles[
                0].years != vehicles[2].years:
                    match = True
    return match


print(is_match(carlist))
