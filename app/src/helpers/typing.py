import requests

from typing import Union

StrOrNone = Union[str, None]
IntOrNone = Union[int, None]
ListOrNone = Union[list, None]
DictOrNone = Union[dict, None]
DictOrList = Union[dict, list]
Response = requests.models.Response
ResponseOrNone = Union[Response, None]
ResponseOrList = Union[Response, list]
