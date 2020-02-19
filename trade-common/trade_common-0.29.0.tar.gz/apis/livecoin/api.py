import hashlib
import hmac
import urllib.parse
from collections import OrderedDict

from trade_common.apis.api import ApiClient
from trade_common.utils.decorators import trace_result


class OpenClosed:
    """
    Возможные варианты:
        ALL - (default) Все ордера
        OPEN - Открытые ордера
        CLOSED - Закрытые (исполненные и отмененые) ордера
        CANCELLED - Отмененные ордера
        NOT_CANCELLED - Все ордера, кроме отмененых
        PARTIALLY - Частично исполненные ордера
    """

    ALL = "ALL"
    OPEN = "OPEN"
    CLOSED = "CLOSED"
    CANCELLED = "CANCELLED"
    PARTIALLY = "PARTIALLY"


class BalanceType:
    """
    Возможные виды балансов:
        total: общий,
        available: доступные для торговли средства,
        trade: средства в открытых ордерах,
        available_withdrawal: доступный для вывода
    """

    total = "total"
    available = "available"
    trade = "trade"
    available_withdrawal = "available_withdrawal"


class TransactionType:
    """
    Возможные типы транзакций:
        BUY - покупка
        SELL - продажа
        DEPOSIT - пополнение
        WITHDRAWAL - вывод
    """

    BUY = "BUY"
    SELL = "SELL"
    DEPOSIT = "DEPOSIT"
    WITHDRAWAL = "WITHDRAWAL"


class OperationType:
    """
    Возможные значения:
        ALL - все
        BUY - покупка
        SELL - продажа
    """

    ALL = "ALL"
    BUY = "BUY"
    SELL = "SELL"


class OrderAction:
    """
    Возможные варианты:
        buy - заявка на покупку лимитный/рыночный ордер
        sell - заявка на продажу лимитный/рыночный ордер
    """

    buy = "buy"
    sell = "sell"


class LivecoinApi(ApiClient):
    def __request(self, http_method, headers, api_method="", params=b"", data=None) -> dict:
        """Constructs and sends :class:`Request`

        :param RequestType http_method: The http method
        :param dict headers: includes api_key, api_secret and encoded data
        :param str api_method: Part of api url with called method
        :param params: additional url parameters encoded into bytes
        :param dict data: request data
        :returns dict
        """

        try:
            response = self.__session.request(
                http_method, url=f"{self.base_url}{api_method}", data=data, params=params, headers=headers
            )
            data = response.json()
            return data

        except Exception as e:
            raise e

    def __sign_n_encode(self, data, flatten=True) -> tuple:
        """Encode :data, generate signature and request headers

        :param list data: url parameters
        :param bool flatten: Флаг определяющий в каком формате возвращать data
        """

        # поскольку data может соделжать в себе пустые tuples их необходимо
        # отфильтровать, а затем отсортировать в алфавитном порядке

        ordered_data = OrderedDict(sorted(filter(bool, data)))
        flatten_data = urllib.parse.urlencode(ordered_data)

        sign = (
            hmac.new(self.api_secret.encode("utf-8"), msg=flatten_data.encode("utf-8"), digestmod=hashlib.sha256)
            .hexdigest()
            .upper()
        )
        headers = {"Api-key": self.api_key, "Sign": sign}
        return flatten_data if flatten else ordered_data, headers

    # ----------------------
    # PRIVATE client data
    # ----------------------

    @trace_result
    def client_orders(
        self,
        currency_pair,
        open_closed=OpenClosed.ALL,
        issued_from=None,
        issued_to=None,
        start_row=0,
        end_row=2_147_483_646,
    ):
        """По конкретному клиенту и по конкретной паре валют получить полную информацию о его ордерах, информация может
        быть ограничена либо только открытые либо только закрытые ордера.

        :param str currency_pair: (optional) Идентификатор пары валют. Если не указано - будет возвращено по всем парам.
        :param OpenClosed open_closed: (optional) Тип ордера (открытые, закрытые, все)
        :param int issued_from: (optional) Начальная дата выборки (в формате UNIX Time в миллисекундах)
        :param int issued_to: (optional) Конечная дата выборки (в формате UNIX Time в миллисекундах)
        :param int start_row: (optional) Порядковый номер первой записи
        :param int end_row: (optional) Порядковый номер последней записи по умолчанию 2_147_483_646
        """
        params, headers = self.__sign_n_encode(
            [
                ("currencyPair", currency_pair) if currency_pair else (),
                ("openClosed", open_closed),
                ("issuedFrom", issued_from) if issued_from else (),
                ("issuedTo", issued_to) if issued_to else (),
                ("startRow", start_row),
                ("endRow", end_row),
            ]
        )

        rsp = self.get(headers, params=params, api_method=f"/exchange/client_orders")
        return rsp.get("data")

    @trace_result
    def client_order(self, order_id):
        """Получить информацию об ордере по его ID

        :param int order_id - ID ордера
        """
        params, headers = self.__sign_n_encode([("orderId", order_id)])
        rsp = self.get(headers, api_method=f"/exchange/order", params=params)
        return rsp

    @trace_result
    def payment_balances(self, currencies, balance_type=BalanceType.available):
        """

        :param str currencies: Валюты, описанные через запятую
        :param BalanceType balance_type: Вид баланса
        :return:
        """
        my_balances = self.__payment_balances(currencies)
        return {b["currency"]: b["value"] for b in my_balances if b["type"] == balance_type}

    def __payment_balances(self, currencies):
        """Возвращает массив с балансами пользователя.

        :param str currencies: (optional) Валюта (валюты), описанные через запятую.
        """
        params, headers = self.__sign_n_encode([("currency", currencies) if currencies else ()])
        rsp = self.get(headers, params=params, api_method="/payment/balances")
        return rsp

    @trace_result
    def payment_balance(self, currency):
        """Возвращает доступный баланс для выбранной валюты

        :param currency: Валюта
        """
        params, headers = self.__sign_n_encode([("currency", currency)])
        rsp = self.get(headers, params=params, api_method=f"/payment/balance")
        return rsp

    @trace_result
    def history_transactions(self, start, end, types, limit=100, offset=0):
        """Возвращает список транзакций пользователя

        :param int start: Дата начала выборки (в формате UNIX Time в миллисекундах)
        :param int end: Дата конца выборки (в формате UNIX Time в миллисекундах)
        :param TransactionType types: (optional) Типы транзакций (через запятую)
        :param int limit: (optional) Максимальное количество результатов (default=100)
        :param int offset: (optional) Первый индекс записи
        """
        params, headers = self.__sign_n_encode(
            [("start", start), ("end", end), ("types", types), ("limit", limit), ("offset", offset)]
        )
        rsp = self.get(headers, params=params, api_method="/payment/history/transactions")
        return rsp

    @trace_result
    def history_size(self, start, end, types):
        """Возвращает количество транзакций пользователя с заданными параметрами

        :param int start: Дата начала выборки (в формате UNIX Time в миллисекундах)
        :param int end: Дата конца выборки (в формате UNIX Time в миллисекундах)
        :param TransactionType types: (optional) Типы транзакций (через запятую)
        """
        params, headers = self.__sign_n_encode([("start", start), ("end", end), ("types", types)])
        rsp = self.get(headers, params=params, api_method="/payment/history/size")
        return rsp

    @trace_result
    def commission_current(self):
        """Возвращает текущую комиссию пользователя"""

        _, headers = self.__sign_n_encode([])
        rsp = self.get(headers, api_method="/exchange/commission")
        return float(rsp["fee"])

    @trace_result
    def commission_common(self):
        """Возвращает текущую комиссию пользователя и объем торгов в USD за последние 30 дней
        """
        _, headers = self.__sign_n_encode([])
        rsp = self.get(headers=headers, api_method="/exchange/commissionCommonInfo")
        return rsp

    # ----------------------
    # PUBLIC client data
    # ----------------------
    @trace_result
    def ticker(self, currency_pair):
        """Получить информацию за последние 24 часа по конкретной паре валют

        :param currency_pair: (optional) Идентификатор пары валют.
        """
        params, headers = self.__sign_n_encode([("currencyPair", currency_pair)])
        rsp = self.get(headers, params=params, api_method="/exchange/ticker")
        return rsp

    @trace_result
    def last_trades(self, currency_pair: str, minutes_or_hour=True, operation_type=OperationType.ALL):
        """Получить информацию о последних сделках (транзакциях) по заданной паре валют.
        Информацию можно получить либо за последний час либо за последнюю минуту.

        :param currency_pair: Идентификатор пары валют.
        :param minutes_or_hour: Если true, то информация возвращается за последнюю минуту, в провном случае час
        :param operation_type: Тип операции
        """
        params, headers = self.__sign_n_encode(
            [("currencyPair", currency_pair), ("minutesOrHour", minutes_or_hour), ("type", operation_type)]
        )
        rsp = self.get(headers, params=params, api_method="/exchange/last_trades")
        return rsp

    @trace_result
    def order_book(self, currency_pair: str, group_by_price=True, depth=10):
        """Получить ордера по выбранной паре (можно установить признак группировки ордеров по ценам)

        :param currency_pair: - Идентификатор пары валют.
        :param group_by_price: - (optional) Если true, то ордера будут сгруппированы по ценам. Default = False
        :param depth: - (optional) Максимальное количество бидов(асков) в ответе.
        """
        params, headers = self.__sign_n_encode(
            [("currencyPair", currency_pair), ("groupByPrice", group_by_price), ("depth", depth)]
        )
        rsp = self.get(headers, params=params, api_method="/exchange/order_book")
        return rsp

    @trace_result
    def full_order_book(self, group_by_price=False, depth=10):
        """Возвращает ордербук по каждой валютной паре

        :param bool group_by_price: - (optional) Если true, то ордера будут сгруппированы по ценам. Default = False
        :param int depth: - (optional) Максимальное количество бидов(асков) в ответе.
        """
        params, headers = self.__sign_n_encode([("groupByPrice", group_by_price), ("depth", depth)])
        rsp = self.get(headers, params=params, api_method=f"/exchange/all/order_book")
        return rsp

    @trace_result
    def maxbid_minask(self, currency_pair) -> tuple:
        """Возвращает максимальный бид и минимальный аск в текущем стакане

        :param str currency_pair:
        :return: tuple из max_bid, min_ask
        """
        params, headers = self.__sign_n_encode([("currencyPair", currency_pair)])
        rsp = self.get(headers, params=params, api_method="/exchange/maxbid_minask")

        if "errorMessage" in rsp:
            raise Exception(rsp["errorMessage"])
        else:
            m = rsp[0]
            return float(m["maxBid"]), float(m["minAsk"])

    @trace_result
    def restrictions(self):
        """Возвращает ограничения по каждой паре
            мининимальный размер ордера
            максимальному количесво знаков после запятой в цене.
        """
        _, headers = self.__sign_n_encode([])
        rsp = self.get(headers, api_method="/exchange/restrictions")
        return rsp

    @trace_result
    def coin_info(self):
        """Возвращает общую информацию по критовалютам:
            name - название
            symbol - символ
            walletStatus - статус кошелька
            normal - Кошелек работает нормально
            delayed - Кошелек задерживается (нет нового блока 1-2 часа)
            blocked - Кошелек не синхронизирован (нет нового блока минимум 2 часа)
            blocked_long - Последний блок получен более 24 ч. назад
            down - Кошелек временно выключен
            delisted - Монета будет удалена с биржи, заберите свои средства
            closed_cashin - Разрешен только вывод
            closed_cashout - Разрешен только ввод
            withdrawFee - комиссия вывод
            minDepositAmount - мин. сумма пополнения
            minWithdrawAmount - мин. сумма вывода
        """
        _, headers = self.__sign_n_encode([])
        rsp = self.get(headers, api_method="/info/coinInfo")
        return rsp

    # ----------------------
    # OPERATIONS with order
    # ----------------------

    @trace_result
    def limit_order_operations(self, action, currency_pair, price, quantity):
        """Совершить операцию покупки или продажи лимитного ордера.

        :param str action: Вид операции
        :param str currency_pair: Идентификатор пары валют.
        :param float price: Цена
        :param float quantity: Количество
        """
        data, headers = self.__sign_n_encode(
            [("currencyPair", currency_pair), ("price", price), ("quantity", quantity)], flatten=False
        )
        rsp = self.post(headers, data=data, api_method=f"/exchange/{action}limit")
        return rsp

    @trace_result
    def market_order_operations(self, action: str, currency_pair, quantity):
        """Совершить операцию покупки или продажи рыночного ордера.

        :param str action: Вид операции
        :param str currency_pair: Идентификатор пары валют.
        :param float quantity: Количество
        """
        data, headers = self.__sign_n_encode([("currencyPair", currency_pair), ("quantity", quantity)], flatten=False)
        rsp = self.post(headers, data=data, api_method=f"/exchange/{action}market")
        return rsp

    @trace_result
    def api_limit_order_cancel(self, currency_pair, order_id):
        """Отменить ордер (лимитный).

        :param str currency_pair: Идентификатор пары валют.
        :param int order_id: ID ордера
        """
        data, headers = self.__sign_n_encode([("currencyPair", currency_pair), ("orderId", order_id)], flatten=False)

        rsp = self.post(headers, data=data, api_method="/exchange/cancellimit")
        return rsp
