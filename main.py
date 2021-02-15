import sys
import pandas as pd
from PySide2 import QtCore, QtWidgets
from natsort import index_natsorted, order_by_index
from mainwindow_ui import Ui_MainWindow
from mangoconnect import MangoOffice
from pdframe import PandasDataFrame


class DataFrameModel(QtCore.QAbstractTableModel):
    DtypeRole = QtCore.Qt.UserRole + 1000
    ValueRole = QtCore.Qt.UserRole + 1001

    def __init__(self, df=pd.DataFrame(), parent=None):
        super(DataFrameModel, self).__init__(parent)
        self._dataframe = df

    def setDataFrame(self, dataframe):
        self.beginResetModel()
        self._dataframe = dataframe.copy()
        self.endResetModel()

    def dataFrame(self):
        return self._dataframe

    dataFrame = QtCore.Property(pd.DataFrame, fget=dataFrame, fset=setDataFrame)

    @QtCore.Slot(int, QtCore.Qt.Orientation, result=str)
    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: int = QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self._dataframe.columns[section]
            else:
                return str(self._dataframe.index[section])
        return None

    def rowCount(self, parent=QtCore.QModelIndex()):
        if parent.isValid():
            return 0
        return len(self._dataframe.index)

    def columnCount(self, parent=QtCore.QModelIndex()):
        if parent.isValid():
            return 0
        return self._dataframe.columns.size

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if not index.isValid() or not (0 <= index.row() < self.rowCount() and 0 <= index.column() < self.columnCount()):
            return None
        row = self._dataframe.index[index.row()]
        col = self._dataframe.columns[index.column()]
        dt = self._dataframe[col].dtype

        val = self._dataframe.loc[row][col]
        if role == QtCore.Qt.DisplayRole:
            return str(val)
        elif role == DataFrameModel.ValueRole:
            return val
        if role == DataFrameModel.DtypeRole:
            return dt
        return None

    def roleNames(self):
        roles = {
            QtCore.Qt.DisplayRole: b'display',
            DataFrameModel.DtypeRole: b'dtype',
            DataFrameModel.ValueRole: b'value'
        }
        return roles

    def sort(self, column, order):
        self.layoutAboutToBeChanged.emit()
        if order == 0:
            self._dataframe = self._dataframe.reindex(index=order_by_index(self._dataframe.index, index_natsorted(
                eval('self._dataframe["%s"]' % (list(self._dataframe.columns)[column])))))
        else:
            self._dataframe = self._dataframe.reindex(index=order_by_index(self._dataframe.index, reversed(
                index_natsorted(eval('self._dataframe["%s"]' % (list(self._dataframe.columns)[column]))))))

        self._dataframe.reset_index(inplace=True, drop=True)
        self.setDataFrame(self._dataframe)
        self.layoutChanged.emit()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.de_start.setDate(QtCore.QDate().currentDate())
        self.ui.de_stop.setDate(QtCore.QDate().currentDate())
        self.ui.cb_whocalled.setVisible(False)
        self.ui.btn_report.setVisible(False)
        self.ui.tab_2.setEnabled(False)
        self.mango = MangoOffice()
        self.dframe = PandasDataFrame()

        # connections
        self.ui.btn_connection.clicked.connect(self.connection)
        self.ui.btn_download.clicked.connect(self.feel_table)
        self.ui.cb_whocalledtype.currentIndexChanged.connect(self.who_called_type_change)
        self.ui.cb_ats.currentIndexChanged.connect(self.who_called_type_change)
        self.ui.btn_clear.clicked.connect(self.btn_clear_click)
        self.ui.de_start.dateChanged.connect(self.de_start_date_change)
        self.ui.de_stop.dateChanged.connect(self.de_stop_date_change)
        self.ui.btn_report.clicked.connect(self.export_to_xls)

    def connection(self):
        """
        подключение к сервису MangoOffice, загрузка дополнительной информации
        :return:
        """
        # подключаемся к сервису MangoOffice
        self.ui.statusbar.showMessage('Подключение')
        connected, info = self.mango.connect(self.ui.edt_login.text(), self.ui.edt_pass.text())
        # выводим в статус бар информацию о подключении
        self.ui.statusbar.showMessage(info)
        if not connected:
            return None
        # обновляем информацию о профиле
        self.mango.upload_profile_data()
        self.ui.cb_ats.clear()
        # подгружаем названия продуктов и список пользователей в этих продуктах
        for product in self.mango.profile['products']:
            self.ui.cb_ats.addItem(product)
            self.mango.get_sip_users(product)
        # переключаемся на вкладку с настройками
        self.ui.tab_2.setEnabled(True)
        self.ui.tabWidget.setCurrentIndex(1)

    def feel_table(self):
        """
        Загрузка истории звонков с использованием выбранных польхователем параметров и отображении данных в таблице
        :return:
        """
        # TODO self.ui.statusbar.showMessage('Загружаем данные..') не работает
        # устанвливаем тип звонящего
        self.mango.set_who_called_type(self.ui.cb_whocalledtype.currentText())

        # Видимость кнопки Отчет в XLS
        if self.ui.cb_whocalledtype.currentText() == 'Сотрудник':
            self.ui.btn_report.setVisible(True)
        else:
            self.ui.btn_report.setVisible(False)

        # уточняем кто звонил
        if self.ui.cb_whocalled.isVisible():
            self.mango.set_who_called(self.ui.cb_ats.currentText(), self.ui.cb_whocalled.currentText())
        if self.ui.ed_clientnumber.isVisible():
            self.mango.set_client_number(self.ui.ed_clientnumber.text())

        # устанавливаем период
        self.mango.set_star_stop_date(self.ui.de_start.date().toPython(), self.ui.de_stop.date().toPython())

        # получаем статистику
        self.mango.get_call_statics(self.ui.cb_ats.currentText())

        # загружаем данные
        self.dframe.load_data('static.csv')
        dframe = self.dframe.data
        # формируем модель
        model = DataFrameModel(dframe)
        # передаем модель на отображениие в интерфейсе таблицы
        self.ui.tbl_view_pandas.setModel(model)
        self.ui.tbl_view_pandas.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
        self.ui.tbl_view_pandas.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Fixed)
        self.ui.tbl_view_pandas.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Fixed)
        self.ui.tbl_view_pandas.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.ui.tbl_view_pandas.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        self.ui.tbl_view_pandas.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        self.ui.tbl_view_pandas.horizontalHeader().setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        self.ui.statusbar.showMessage(f'Всего {self.ui.tbl_view_pandas.model().rowCount()} записей')

    def who_called_type_change(self):
        # при выборе типа звоняшего
        caller_type = self.ui.cb_whocalledtype.currentText()
        self.ui.ed_clientnumber.setVisible(True)
        self.ui.ed_clientnumber.setEnabled(False)
        self.ui.cb_whocalled.setVisible(False)
        if caller_type == 'Сотрудник':
            self.ui.ed_clientnumber.setVisible(False)
            self.ui.cb_whocalled.setVisible(True)
            self.ui.cb_whocalled.clear()
            self.ui.cb_whocalled.addItem('')
            for user in self.mango.profile['products'][self.ui.cb_ats.currentText()]['users']:
                self.ui.cb_whocalled.addItem(user)
        if caller_type == 'Клиент':
            self.ui.ed_clientnumber.setEnabled(True)

    def btn_clear_click(self):
        # действие на кнопку Очистить
        date = QtCore.QDate().currentDate()
        self.ui.de_start.setDate(date)
        self.ui.de_stop.setDate(date)
        self.ui.ed_clientnumber.clear()
        self.ui.cb_whocalledtype.setCurrentIndex(0)

    def de_start_date_change(self):
        date = self.ui.de_start.date()
        if date > self.ui.de_stop.date():
            self.ui.de_stop.setDate(date)

    def de_stop_date_change(self):
        date = self.ui.de_stop.date()
        if date < self.ui.de_start.date():
            self.ui.de_start.setDate(date)

    def export_to_xls(self):
        dframe = self.dframe.call_stat_by_day()
        dframe.to_excel('report.xls')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')

    window = MainWindow()
    window.resize(800, 600)
    window.show()

    sys.exit(app.exec_())

