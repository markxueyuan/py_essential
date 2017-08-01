class Cursor:
    def __init__(self, document):
        self.document = document
        self.position = 0

    def forward(self):
        self.position += 1

    def back(self):
        self.position -= 1

    def home(self):
        try:
            while self.document.characters[self.position - 1] != '\n':
                self.position -= 1
                if self.position <= 0:
                    break
        except:
            print("It is already at the beginning of the doc.")
            self.position = 0

    def end(self):
        while self.position < len(self.document.characters) \
                and self.document.characters[self.position] != '\n':
            self.position += 1

class Document:
    def __init__(self):
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = ''

    def insert(self, character):
        self.characters.insert(self.cursor.position, character)
        self.cursor.forward()

    def delete(self):
        self.cursor.back()
        try:
            del self.characters[self.cursor.position]
        except:
            self.cursor.forward()

    def save(self):
        with open(self.filename, 'w') as f:
            f.write(''.join(self.characters))

    @property
    def string(self):
        return "".join(self.characters)


def main():
    d = Document()
    d.insert('h')
    d.insert('e')
    d.insert('l')
    d.insert('l')
    d.insert('o')
    d.insert('\n')
    d.insert('w')
    d.insert('o')
    d.insert('r')
    d.insert('l')
    d.insert('d')
    d.cursor.home()
    d.insert('*')
    print(d.string)
