from datetime import datetime, timedelta
import time
import requests


class MangoOffice:
    _URL_AUTH = 'https://auth.mango-office.ru/auth/vpbx/'
    _URL_LK = 'https://lk.mango-office.ru'
    _HEADERS = {
        'Accept': 'text/html,application/xhtml+xml,application/xml,application/json,text/plain,*/*;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'
    }

    def __init__(self):
        self.data = {'app': 'ics'}
        self.profile = {}
        self.request_data = {}
        self.session = requests.sessions.Session()
        self.session.headers = self._HEADERS
        self.reset_request_data()

    def __del__(self):
        self.session.close()

    def reset_request_data(self):
        date = datetime.now().strftime("%d.%m.%Y")
        self.request_data = {
            'perpage': 1000000,  # количество записей
            'type': 'calls',  # тип данных
            'period': 'arbitrary',  # имя периода arbitrary-произвольный
            'startDate': date,  # с даты
            'endDate': date,  # по дату
            'whoCalledType': 'client',  # кто звонил сотрудник(member), клиент(client), или (client_or_member)
            'whoCalled': 'any',  # кто звонил конкретно из сотрудников m:{id сотрудника}
            'clientNumber': '',  # номер клиента
            'line': 'any',  # номер на который звонили: любой (any) или пишем номер (71234567890)
            'groups': [],  # группа
            'phones': [],  # номера
            'offset': 0,  #
            'sorting': '',  #
            'fromLine': '',  #
            'members': [],  #
            'callStatus': 'all',  # статус звонка: все, пропущенные, удачные
            'filterParty': 'listall',  #
            'trunks': [],  #
            'export': 'csv',  # формат экспорта
        }

    def connect(self, username, password):
        self.data.update({'username':  username, 'password': password})
        # авторизуемся
        try:
            response = self.session.post(self._URL_AUTH, data=self.data).json()
            if response['result'] != 1000:
                raise ValueError('Не удалось подключиться. Возможно логин или пароль неверны')
            self.data['auth_token'] = response['auth_token']
            self.data['refresh_token'] = response['refresh_token']
            # создаем сессию
            self.session.post(f'{self._URL_LK}/auth/create-session/', data=self.data)
        except ValueError as err:
            return False, err.args[0]
        except Exception as err:
            return False, err.args[0]
        else:
            return True, 'Подключено'

    def upload_profile_data(self):
        # получаем account  и product id для формирования урл для запроса
        response = self.session.get(self._URL_LK).url.split('/')
        account_id = response[-2]
        prod_id = response[-1]
        self.profile['account'] = account_id

        # полчаем список продуктов(виртуальные АТС)
        response = self.session.get(f'{self._URL_LK}/profile/{account_id}/{prod_id}/api/products').json()
        self.profile['products'] = {}
        for product in response:
            if product['brand'] == 'vpbx':
                self.profile['products'].update({product['name']: {'id': product['id'], 'users': ''}})

    def get_sip_users(self, product_name):
        # получаем список пользователей переданной АТС
        prod_id = self.profile['products'][product_name]['id']
        account_id = self.profile['account']
        response = self.session.get(f'{self._URL_LK}/profile/{account_id}/{prod_id}/api/members').json()
        users = {}
        for user in response:
            if user['active'] == '1':
                users[user['abonent']['name']] = user['id']
        self.profile['products'][product_name]['users'] = users

    def get_call_statics(self, product_name):
        # История звонков
        prod_id = self.profile['products'][product_name]['id']
        account_id = self.profile['account']
        response = self.session.post(f'{self._URL_LK}/{account_id}/{prod_id}/stats/calls', self.request_data)
        h = response.json()["hash"]
        while response.json()['status'] != 'export':
            time.sleep(2)
            response = self.session.post(f'{self._URL_LK}/{account_id}/{prod_id}/stats/response-stats', {'hash': h})
        response = self.session.request(method='get',
                                        url=f'{self._URL_LK}/{account_id}/{prod_id}/stats/export-history',
                                        params={'export': 'csv', 'hash': h},)
        with open('static.csv', 'wb') as f:  # TODO передача пути для сохранение файла и возврат его из функции
            f.write(response.content)

    def set_who_called_type(self, wc_type):
        who_called_type_choise = {'Сотрудник': 'member', 'Клиент': 'client', 'Клиент или сотрудник': 'client_or_member'}
        self.request_data['whoCalledType'] = who_called_type_choise[wc_type]

    def set_who_called(self, product_name, who_called):
        if who_called == '':
            self.request_data['whoCalled'] = 'any'
        else:
            self.request_data['whoCalled'] = f"m:{self.profile['products'][product_name]['users'][who_called]}"

    def set_client_number(self, number):
        self.request_data['clientNumber'] = number

    def set_star_stop_date(self, start: datetime.date, stop: datetime.date):
        self.request_data['startDate'] = start.strftime("%d.%m.%Y")
        self.request_data['endDate'] = stop.strftime("%d.%m.%Y")


if __name__ == '__main__':
    mango = MangoOffice()

    mango.connect('', '')

    mango.upload_profile_data()

    mango.request_data['whoCalledType'] = 'client'
    mango.request_data['startDate'] = datetime.strftime(datetime.now() - timedelta(days=5), "%d.%m.%Y")

    mango.get_call_statics('')




