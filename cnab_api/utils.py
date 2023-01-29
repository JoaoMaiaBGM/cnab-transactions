from cnab_api.normalizers import FileNormalizer
from cnab_api.repositories import ApiRepository


class FileUtils():

    def __init__(self, repository = None):
        self.normalizer = FileNormalizer()
        self.repository = repository or ApiRepository()

    def read_file(self, file):
        file = file.decode('utf-8')
        for value in file.splitlines():
            normalizer = self.normalizer.file_normalizer(value)
            self.repository.create_transaction(normalizer)
        return file


    def filter(self, store):
        return self.repository.get_transactions(), None