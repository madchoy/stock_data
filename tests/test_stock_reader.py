import datetime
from decimal import Decimal

import pkg_resources

from stock_data.stock_reader import StockReader


def load_file(self, filename):
    return pkg_resources.resource_stream(__name__, "/test_data/" + filename)

class TestStockReader(object):
    def test_read_stock(self):
        start = datetime.datetime(2017,1,1)
        end = datetime.datetime(2017,1,31)
        stock_reader = StockReader('yahoo')
        data_frame = stock_reader.read_stock('TSLA',start, end)
        index = data_frame.ix[0]
        assert Decimal('220.33') == Decimal(index.High).quantize(Decimal('1.00'))

    def test_to_csv(self):
        start = datetime.datetime(2017, 1, 1)
        end = datetime.datetime(2017, 1, 31)
        stock_reader = StockReader('yahoo')
        path = stock_reader.to_csv('TSLA', start, end)
        with open(path,'rb') as file:
            doc = file.readlines()

        assert b'2017-01-03,214.86000099999998,220.330002,210.960007,216.99000499999997,5923300,216.99000499999997\n' == doc[1]

    def test_read_csv(self):
        # start = datetime.datetime(2017, 1, 1)
        # end = datetime.datetime(2017, 1, 31)
        # stock_reader = StockReader('yahoo')
        # path = stock_reader.to_csv('TSLA', start, end)
        tsla = load_file('TSLA.csv')
        data_frame = stock_reader.read_csv(tsla)

        assert ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close'] == data_frame.head
        assert b'2017-01-03,214.86000099999998,220.330002,210.960007,216.99000499999997,5923300,216.99000499999997\n' == data_frame[0]