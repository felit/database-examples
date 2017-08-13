class LeveldbDemo():
    pass


class Leveldb():
    def __init__(self, filename="db"):
        self.db = {}
        self.filename = filename

    def open(self):
        self.file = open(self.filename, 'w+')
        print self.file
        se = self.file.read()
        print se
        while len(se) > 0:
            kv = se.split("=")
            self.db[kv[0]] = kv[1]
            se = self.file.readline()


    def Put(self, key, value):
        self.db[key] = value
        self.flush()

    def get(self, key):
        if self.db.has_key(key):
            return self.db[key]
        else:
            return None

    def delete(self, key):
        if self.db.has_key(key):
            del self.db[key]
        self.flush()

    def flush(self):
        for key, value in self.db.items():
            self.file.write("{key}={value}\n".format(key=key, value=value))
        self.file.flush()

    def close(self):
        self.file.close()


if __name__ == '__main__':
    db = Leveldb()
    db.open()
    db.Put("hello", "world")
    print db.db
    print db.get("hello")
    # db.delete("hello")
    # print db.get("hello")