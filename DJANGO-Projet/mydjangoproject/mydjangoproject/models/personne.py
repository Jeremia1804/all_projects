class Personne:
    def __init__(self):
        self.name = 'jeremia'
        self.age = 18

    def __str__(self):
        return self.name

    def getElect(self):
        return self.name + 'gentille'