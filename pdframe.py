import pandas as pd
import matplotlib.pyplot as plt


class PandasDataFrame:
    """
    класс для работы с DataFrame из pandas
    """
    def __init__(self):
        self.data = None

    def _formatting_data(self):
        # удаляем столбец 'Стоимость, руб'
        del self.data['Стоимость, руб']

        f_time = lambda x: x.split(' ')[1]
        f_date = lambda x: x.split(' ')[0]
        # переименновываем столбец
        self.data.rename(columns={'Время': 'Дата'}, inplace=True)
        # создаем новый столбец из данных другого при помощи лямбда функции
        self.data['Время'] = self.data['Дата'].map(f_time)
        # изменяем данные столбца при помощи лямбда функции
        self.data['Дата'] = self.data['Дата'].map(f_date)

        mysubset = ['Дата', 'Время']
        self.data = self.data[sorted(self.data, key=lambda x: x not in mysubset)]

    def load_data(self, path: str):
        self.data = pd.read_csv(path, sep=';', encoding='cp1251', skiprows=1)
        self._formatting_data()

    def call_stat_by_day(self) -> pd.DataFrame:
        """
        Статистика звонков менеджеров по дням
        :return:
        """
        frm = lambda x: '{:,.2f}'.format(x)
        data = self.data.groupby([self.data['Дата'], self.data['Кто звонил']])['Длительность, сек'].\
            agg(['count', 'sum', 'mean']).\
            rename(columns={'count': 'Кол-во звонков', 'sum': 'Общая длит. звонков', 'mean': 'Сред. длит. звонков'})
        data['Сред. длит. звонков']=data['Сред. длит. звонков'].map(frm).astype(float)
        return data


if __name__ == '__main__':
    pd.set_option("display.max.columns", None)
    dframe = PandasDataFrame()
    dframe.load_data('static.csv')
    df = dframe.call_stat_by_day().reset_index()

    print(df)

    df.plot(x=['Дата', 'Кто звонил'], y="Кол-во звонков")
    plt.show()

