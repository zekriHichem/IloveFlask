from .Attribut import Attribut

class Function:
    typee = ""
    desc = ""
    url = ""
    attributs = []
    returnn = ""
    def __init__(self, typee, url):
        self.typee = typee
        self.url = url
        self.attributs = []
    def get_att(self):
        att = ""
        for i in self.attributs:
            att += i.name + ": " + i.desc + "\n"
        return att[:-2]