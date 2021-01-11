class Node_data:
    """
    This class represents vertex in graph using node data structure.
    Node has some useful data as key,tag,weight,info,pos and map for all his neighbours
    each node has unique key.
    """
    def __init__(self, key, pos):
        self.key = key
        self.tag = 0
        self.weight = 999999
        self.info = ""
        self.map = {}
        if pos is None:
            self.pos = Geo_location(0, 0, 0)
        else:
            self.pos = pos

    def get_key(self) -> int:
        return self.key

    def get_tag(self):
        return self.tag

    def get_info(self):
        return self.info

    def get_pos(self):
        return self.pos

    def set_tag(self, tag):
        self.tag = tag

    def set_info(self, info):
        self.info = info

    def set_pos(self, pos):
        self.pos = pos

    def set_weight(self, weight):
        self.weight = weight

    def get_weight(self):
        return self.weight

    def connect(self, key, weight):
        self.map[key] = weight

    def get_map(self):
        return self.map

    def __lt__(self, other):
        return self.weight<other.weight


class Geo_location:
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z
