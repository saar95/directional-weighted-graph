class Node_data:

    def __init__(self, key, tag, info, pos):
        self.key = key
        self.tag = tag
        self.info = info
        self.pos = pos
        self.map = {}

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
