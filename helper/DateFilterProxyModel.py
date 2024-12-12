import sys
from PyQt5 import QtCore
from datetime import datetime

class DateFilterProxyModel(QtCore.QSortFilterProxyModel):
    def __init__(self, filter_date=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filter_date = filter_date

    def setFilterDate(self, filter_date):
        self.filter_date = filter_date
        self.invalidateFilter()

    def filterAcceptsRow(self, source_row, source_parent):
        index = self.sourceModel().index(source_row, 5, source_parent)  # Column 5 is the 'Date' column
        data = self.sourceModel().data(index)
        date = datetime.strptime(data, '%Y-%m-%d')
        if self.filter_date:
            return date == self.filter_date
        return True