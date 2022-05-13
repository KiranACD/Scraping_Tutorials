from config import storage_path
import os

class Tickers:
    def __init__(self, index):
        self.index = index
    
    def load_file_path(self):
        file_name = f'{self.index}_tickers.txt'
        self.file_path = os.path.join(storage_path, file_name)
    
    def __iter__(self):
        return self.get_tickers()
    
    def get_tickers(self):
        self.load_file_path()
        with open(self.file_path) as f:
            for line in f.readlines():
                yield line.split(' - ')[0].strip()

if __name__ == '__main__':
    t = Tickers('s&p500')
    for name in t:
        print(name)