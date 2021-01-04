class Node_data:

    def __init__(self, key, tag, info, pos):
        self.key = key
        self.tag = tag
        self.info = info
        self.map = {}
        if pos == None:
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

    def connect(self, key, weight):
        self.map[key] = weight


class Geo_location:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z
