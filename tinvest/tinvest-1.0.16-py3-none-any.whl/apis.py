from typing import Any, Optional

from .shemas import (
    CandleResolution,
    CandlesResponse,
    Empty,
    LimitOrderRequest,
    LimitOrderResponse,
    MarketInstrumentListResponse,
    MarketOrderRequest,
    MarketOrderResponse,
    OperationsResponse,
    OrderbookResponse,
    OrdersResponse,
    PortfolioCurrenciesResponse,
    PortfolioResponse,
    SandboxRegisterRequest,
    SandboxRegisterResponse,
    SandboxSetCurrencyBalanceRequest,
    SandboxSetPositionBalanceRequest,
    SearchMarketInstrumentResponse,
    UserAccountsResponse,
)


class BaseApi:
    def __init__(self, client: Any) -> None:
        self._client = client

    @property
    def client(self) -> Any:
        return self._client


class SandboxApi(BaseApi):
    """Операция в sandbox"""

    def sandbox_register_post(self, body: SandboxRegisterRequest, **kwargs: Any) -> Any:
        """POST /sandbox/register Регистрация клиента в sandbox"""
        kwargs.setdefault('data', body.json(by_alias=True))
        return self.client.request(
            'POST',
            '/sandbox/register',
            response_model=SandboxRegisterResponse,
            **kwargs,
        )

    def sandbox_currencies_balance_post(
        self,
        body: SandboxSetCurrencyBalanceRequest,
        broker_account_id: Optional[str] = None,
        **kwargs: Any
    ) -> Any:
        """POST /sandbox/currencies/balance
        Выставление баланса по валютным позициям"""
        kwargs.setdefault('params', {})
        params = kwargs['params']
        if broker_account_id:
            params.setdefault('brokerAccountId', broker_account_id)
        kwargs.setdefault('data', body.json(by_alias=True))
        return self.client.request(
            'POST', '/sandbox/currencies/balance', response_model=Empty, **kwargs,
        )

    def sandbox_positions_balance_post(
        self,
        body: SandboxSetPositionBalanceRequest,
        broker_account_id: Optional[str] = None,
        **kwargs: Any
    ) -> Any:
        """POST /sandbox/positions/balance
        Выставление баланса по инструментным позициям"""
        kwargs.setdefault('params', {})
        params = kwargs['params']
        if broker_account_id:
            params.setdefault('brokerAccountId', broker_account_id)
        kwargs.setdefault('data', body.json(by_alias=True))
        return self.client.request(
            'POST', '/sandbox/positions/balance', response_model=Empty, **kwargs
        )

    def sandbox_remove_post(
        self, broker_account_id: Optional[str] = None, **kwargs: Any
    ) -> Any:
        """POST /sandbox/remove Удаление счета клиента"""
        kwargs.setdefault('params', {})
        params = kwargs['params']
        if broker_account_id:
            params.setdefault('brokerAccountId', broker_account_id)
        return self.client.request(
            'POST', '/sandbox/remove', response_model=Empty, **kwargs
        )

    def sandbox_clear_post(
        self, broker_account_id: Optional[str] = None, **kwargs: Any
    ) -> Any:
        """POST /sandbox/clear Удаление всех позиций"""
        kwargs.setdefault('params', {})
        params = kwargs['params']
        if broker_account_id:
            params.setdefault('brokerAccountId', broker_account_id)
        return self.client.request(
            'POST', '/sandbox/clear', response_model=Empty, **kwargs
        )


class OrdersApi(BaseApi):
    """Операции заявок"""

    def orders_get(self, broker_account_id: Optional[str] = None, **kwargs: Any) -> Any:
        """GET /orders Получение списка активных заявок"""
        kwargs.setdefault('params', {})
        params = kwargs['params']
        if broker_account_id:
            params.setdefault('brokerAccountId', broker_account_id)
        return self.client.request(
            'GET', '/orders', response_model=OrdersResponse, **kwargs
        )

    def orders_limit_order_post(
        self,
        figi: str,
        body: LimitOrderRequest,
        broker_account_id: Optional[str] = None,
        **kwargs: Any
    ) -> Any:
        """POST /orders/limit-order Создание лимитной заявки"""
        kwargs.setdefault('params', {})
        params = kwargs['params']
        params.setdefault('figi', figi)
        if broker_account_id:
            params.setdefault('brokerAccountId', broker_account_id)
        kwargs.setdefault('data', body.json(by_alias=True))
        return self.client.request(
            'POST', '/orders/limit-order', response_model=LimitOrderResponse, **kwargs,
        )

    def orders_market_order(
        self,
        figi: str,
        body: MarketOrderRequest,
        broker_account_id: Optional[str] = None,
        **kwargs: Any
    ) -> Any:
        """POST /orders/market-order Создание рыночной заявки"""
        kwargs.setdefault('params', {})
        params = kwargs['params']
        params.setdefault('figi', figi)
        if broker_account_id:
            params.setdefault('brokerAccountId', broker_account_id)
        kwargs.setdefault('data', body.json(by_alias=True))
        return self.client.request(
            'POST', '/orders/market-order', response_model=MarketOrderResponse, **kwargs
        )

    def orders_cancel_post(
        self, order_id: str, broker_account_id: Optional[str] = None, **kwargs: Any
    ) -> Any:
        """POST /orders/cancel Отмена заявки"""
        kwargs.setdefault('params', {})
        params = kwargs['params']
        params.setdefault('orderId', order_id)
        if broker_account_id:
            params.setdefault('brokerAccountId', broker_account_id)
        return self.client.request(
            'POST', '/orders/cancel', response_model=Empty, **kwargs
        )


class PortfolioApi(BaseApi):
    """Операции с портфелем пользователя"""

    def portfolio_get(
        self, broker_account_id: Optional[str] = None, **kwargs: Any
    ) -> Any:
        """GET /portfolio Получение портфеля клиента"""
        kwargs.setdefault('params', {})
        params = kwargs['params']
        if broker_account_id:
            params.setdefault('brokerAccountId', broker_account_id)
        return self.client.request(
            'GET', '/portfolio', response_model=PortfolioResponse, **kwargs
        )

    def portfolio_currencies_get(
        self, broker_account_id: Optional[str] = None, **kwargs: Any
    ) -> Any:
        """GET /portfolio/currencies Получение валютных активов клиента"""
        kwargs.setdefault('params', {})
        params = kwargs['params']
        if broker_account_id:
            params.setdefault('brokerAccountId', broker_account_id)
        return self.client.request(
            'GET',
            '/portfolio/currencies',
            response_model=PortfolioCurrenciesResponse,
            **kwargs,
        )


class MarketApi(BaseApi):
    """Получении информации по бумагам"""

    def market_stocks_get(self, **kwargs: Any) -> Any:
        """GET /market/stocks Получение списка акций"""
        return self.client.request(
            'GET',
            '/market/stocks',
            response_model=MarketInstrumentListResponse,
            **kwargs,
        )

    def market_bonds_get(self, **kwargs: Any) -> Any:
        """GET /market/bonds Получение списка облигаций"""
        return self.client.request(
            'GET',
            '/market/bonds',
            response_model=MarketInstrumentListResponse,
            **kwargs,
        )

    def market_etfs_get(self, **kwargs: Any) -> Any:
        """GET /market/etfs Получение списка ETF"""
        return self.client.request(
            'GET',
            '/market/etfs',
            response_model=MarketInstrumentListResponse,
            **kwargs,
        )

    def market_currencies_get(self, **kwargs: Any) -> Any:
        """GET /market/currencies Получение списка валютных пар"""
        return self.client.request(
            'GET',
            '/market/currencies',
            response_model=MarketInstrumentListResponse,
            **kwargs,
        )

    def market_orderbook_get(self, figi: str, depth: int, **kwargs: Any) -> Any:
        """GET /market/orderbook Получение стакана"""
        kwargs.setdefault('params', {})
        params = kwargs['params']
        params.setdefault('figi', figi)
        params.setdefault('depth', depth)
        return self.client.request(
            'GET', '/market/orderbook', response_model=OrderbookResponse, **kwargs,
        )

    def market_candles_get(
        self, figi: str, from_: str, to: str, interval: CandleResolution, **kwargs: Any
    ) -> Any:
        """GET /market/candles Получение исторических свечей по FIGI"""
        kwargs.setdefault('params', {})
        params = kwargs['params']
        params.setdefault('figi', figi)
        params.setdefault('from', from_)
        params.setdefault('to', to)
        params.setdefault('interval', interval)
        return self.client.request(
            'GET', '/market/candles', response_model=CandlesResponse, **kwargs
        )

    def market_search_by_figi_get(self, figi: str, **kwargs: Any) -> Any:
        """GET /market/search/by-figi Получение инструмента по FIGI"""
        kwargs.setdefault('params', {})
        params = kwargs['params']
        params.setdefault('figi', figi)
        return self.client.request(
            'GET',
            '/market/search/by-figi',
            response_model=SearchMarketInstrumentResponse,
            **kwargs,
        )

    def market_search_by_ticker_get(self, ticker: str, **kwargs: Any) -> Any:
        """GET /market/search/by-ticker Получение инструмента по тикеру"""
        kwargs.setdefault('params', {})
        params = kwargs['params']
        params.setdefault('ticker', ticker)
        return self.client.request(
            'GET',
            '/market/search/by-ticker',
            response_model=MarketInstrumentListResponse,
            **kwargs,
        )


class OperationsApi(BaseApi):
    """Получении информации по операциям"""

    def operations_get(
        self, from_: str, to: str, figi: Optional[str] = None, **kwargs: Any
    ) -> Any:
        """GET /operations Получение списка операций"""
        kwargs.setdefault('params', {})
        params = kwargs['params']
        params.setdefault('from', from_)
        params.setdefault('to', to)
        if figi:
            params.setdefault('figi', figi)
        return self.client.request(
            'GET', '/operations', response_model=OperationsResponse, **kwargs
        )


class UserApi(BaseApi):
    """Получении информации по брокерским счетам"""

    def accounts_get(self, **kwargs):
        """GET /user/accounts Получение брокерских счетов клиента"""
        return self.client.request(
            'GET', '/user/accounts', response_model=UserAccountsResponse, **kwargs
        )


__all__ = (
    'MarketApi',
    'OperationsApi',
    'OrdersApi',
    'PortfolioApi',
    'SandboxApi',
    'UserApi',
)
