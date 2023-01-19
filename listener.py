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

        self.running = True

        self.items_processed = 0

    def run(self):
        while self.running:
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

    def _format_data_bucket(self, field):
        data = field[:100]
        field = field[100:]

        return data, field

    def extraction(self):
        while self.running:
            self.extraction_data += extract(self.w3)

    def transformation(self):
        while self.running:
            if self.extraction_data:
                (data, self.extraction_data) = self._format_data_bucket(self.extraction_data)

                self.transformation_data += transform(data)

    def loading(self):
        while self.running:
            if self.transformation_data:
                (data, self.transformation_data) = self._format_data_bucket(self.transformation_data)

                load(data)

if __name__ == "__main__":
    listener = Listener()
    listener.run_threads()

    