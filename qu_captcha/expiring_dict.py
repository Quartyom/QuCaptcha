import threading


# Stores key-values for a limited amount of time. Built atop standard python dict()
class ExpiringDict:
    def __init__(self, expiration_time_seconds=120):
        self.store = {}
        self.expiration_time = expiration_time_seconds
        self.lock = threading.Lock()

    def set(self, key, value):
        with self.lock:
            self.store[key] = value
            timer = threading.Timer(self.expiration_time, self.remove, args=(key,))
            timer.start()

    def get(self, key, default):
        with self.lock:
            return self.store.get(key, default)

    def remove(self, key):
        with self.lock:
            if key in self.store:
                self.store.pop(key)

    def clear(self):
        with self.lock:
            self.store.clear()
