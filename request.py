from typing import  TypeVar, Generic
import asyncio
import datetime

T = TypeVar('T')
class Request(Generic[T]):
    def __init__(self, id: int, method='', params=None, on_cancel=None) -> None:
        self.result: asyncio.Future[T] = asyncio.Future()
        self.id: int = id
        self.method = method
        self.params = params
        self.request_start_time = datetime.datetime.now()
        self.request_end_time: datetime.datetime | None = None
        self.on_cancel = on_cancel or (lambda: ...)

    def set_result(self, data: T) -> None:
        self.request_end_time = datetime.datetime.now()
        self.result.set_result(data)

    def set_exception(self, exception: Exception) -> None:
        self.request_end_time = datetime.datetime.now()
        self.result.set_exception(exception)

    def cancel(self) -> None:
        if self.request_end_time is not None:
            # ignore canceling finished requests
            return
        self.on_cancel()
        self.result.cancel()

    @property
    def duration(self):
        if self.request_end_time is None:
            return None
        return round((self.request_end_time-self.request_start_time).total_seconds(), 2)



