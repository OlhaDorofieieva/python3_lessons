# Proxy
# read-writer

import os

class Reader:

    def __init__(self, file_path):
        self.__file_path = file_path
        self.data = None

    def read_file(self):
        print("Reading from file...", self.__file_path)
        with open(self.__file_path, 'r') as f:  # 'r' -  мод читання
            self.data = f.read()


class Writer:  # write realisation
    def __init__(self, file_path):
        self.__file_path = file_path
        self.data = None

    def write(self, data):
        print("Writing to file...", self.__file_path)
        with open(self.__file_path, mode='a') as f:
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
        if not self.data or self.is_modified():  # It will be true, if file had already read and it didn't modified.
            self.reader.read_file()
            self.data = self.reader.data

    def write(self, row):  # write realisation
        """
        2) Він повинен записувати інформацію в кінець файлу(не переписуе, а доповлюе, дивись mode = 'a')
        3) Якщо інформація на запис надсилаеться повторно, то не записувати другий раз поспіль одне і те саме
        Важливо. Для перевірки чи МИНУЛИЙ раз ми записували цю ж строку що і зараз в файл читати не треба
        :return: None
        """
        self._last_modified = os.path.getmtime(self.file_path)
        if row != self._last_written:
            self.writer.write(row)
            self._last_written = row


proxy_rw = ProxyReaderWriter(file_path='tst_file.txt')
proxy_rw2 = ProxyReaderWriter(file_path='tst_file2.txt')

proxy_rw.read()

print('STEP1')
proxy_rw2.read()
print('STEP2')
proxy_rw2.read() # не буде читати
print('STEP3')
proxy_rw2.write('asd1\n')  # буде запис
print('STEP4')
proxy_rw2.read() # буде читати
print('STEP5')
proxy_rw2.write('asd1\n')  # не буде запис
print('STEP6')
proxy_rw2.read() # не буде читати
print('STEP7')
proxy_rw2.write('asd2\n')  # буде запис
print('STEP8')
proxy_rw2.read() # буде читати
print('STEP9')
proxy_rw2.write('asd2\n')  # не буде запис
print('STEP10')
proxy_rw2.read() # не буде читати
print('STEP11')
proxy_rw2.write('asd3\n')  # буде запис


print(proxy_rw.data)

