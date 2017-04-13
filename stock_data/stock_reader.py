import  pandas_datareader.data as web
import pandas

class StockReader(object):
    def __init__(self, source):
        self.__source = source

    def read_stock(self, symbol, start, end):
        dataframe = web.DataReader(symbol,
                                   data_source = self.__source,
                                   start = start,
                                   end = end)
        return dataframe

    def to_csv(self, symbol, start, end):
        dataframe = self.read_stock(symbol, start, end)
        file_path = f'{symbol}.csv'
        dataframe.to_csv(file_path)
        return file_path

    def read_csv(self, file_path):
        return DataFrame(file_path)

class DataFrame(object):
    def __init__(self, file_path):
        self.__file_path = file_path
        self.__data_frame = pandas.read_csv(file_path)

    @property
    def head(self):
        head = self.__data_frame.head()
        return head


