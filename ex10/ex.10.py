# Proxy
# read-writer

import os

class Reader:

    def __init__(self, file_path):
        self.__file_path = file_path
        self.data = None

    def read_file(self):
        with open(self.__file_path, 'r') as f:  # 'r' - мод читання
            self.data = f.read()


class Writer:  # write realisation
    def __init__(self, file_path):
        self.__file_path = file_path
        self.data = None

    def write(self, data):
        with open(self.__file_path, mode='w') as f:
            return f.write(data)


class ProxyReaderWriter:

    def __init__(self, file_path):
        self.file_path = file_path
        self.reader = Reader(file_path)
        self.writer = Writer(file_path)
        self._last_modified = os.path.getmtime(file_path)
        self._last_written = None
        self.data = None

    def is_modified(self):
        current_modified = os.path.getmtime(self.file_path)
        return current_modified != self._last_modified

    def read(self):
        """
        1) Не читати файл, а просто повертати значення ЯКЩО файл не було змінено
        :return: None
        """
        # print(f'self.is_modified() = {self.is_modified()}')
        # print(f'self.data = {self.data}')
        if self.data and not self.is_modified():  # It will be true, if file had already read and it didn't modified.
            return
        self.reader.read_file()
        self.data = self.reader.data

    def write(self, row):  # write realisation
        """
        2) Він повинен записувати інформацію в кінець файлу(не переписує, а доповнює, дивись mode = 'a')
        3) Якщо інформація на запис надсилається повторно, то не записувати другий раз поспіль одне і те саме
        Важливо. Для перевірки чи МИНУЛИЙ раз ми записували цю ж строку що і зараз в файл читати не треба
        :return: None
        """
        if row != self._last_written:
            with open(self.file_path, mode='a') as f:
                self._last_written = row
                return f.write(row)


proxy_rw = ProxyReaderWriter(file_path='tst_file.txt')
proxy_rw2 = ProxyReaderWriter(file_path='tst_file2.txt')
proxy_rw.read()
proxy_rw.read()
proxy_rw.read()

proxy_rw2.read()
proxy_rw2.read()
proxy_rw2.write('asd1\n')  # буде запис
proxy_rw2.read()

proxy_rw2.write('asd1\n')  # не буде запис
proxy_rw2.write('asd2\n')  # буде запису
proxy_rw2.write('asd2\n')  # не буде запис
proxy_rw2.write('asd3\n')  # буде запис

# print(proxy_rw.is_modified())
# print(proxy_rw2.is_modified())
print(proxy_rw.data)
