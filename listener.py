import threading

from builder.extractor import extract
from builder.loader import load
from builder.transformer import transform
from builder.utils import get_w3


class Listener:
    def __init__(self, *args, **kwargs):
        self.extraction_data = []
        self.transformation_data = []
        self.loaded_data = []

        self.w3 = get_w3()

    def run(self):
        while True:
            self.extraction_data += extract(self.w3)

            if self.extraction_data:
                data = self.extraction_data[:100]

                self.extraction_data = self.extraction_data[100:]

                self.transformation_data += transform(data)

            if self.transformation_data:
                data = self.transformation_data[:100]

                self.transformation_data = self.transformation_data[100:]

                load(data)

    def run_threads(self):
        e = threading.Thread(target=self.extraction)
        e.start()

        t = threading.Thread(target=self.transformation)
        t.start()

        l = threading.Thread(target=self.loading)
        l.start()

        threads = [e,t,l]

        for thread in threads:
            thread.join()

    def extraction(self):
        while True:
            self.extraction_data += extract(self.w3)

    def transformation(self):
        while True:
            if self.extraction_data:
                data = self.extraction_data[:100]

                self.extraction_data = self.extraction_data[100:]

                self.transformation_data += transform(data)

    def loading(self):
        while True:
            if self.transformation_data:
                data = self.transformation_data[:100]

                self.transformation_data = self.transformation_data[100:]

                load(data)

if __name__ == "__main__":
    listener = Listener()
    listener.run_threads()

    