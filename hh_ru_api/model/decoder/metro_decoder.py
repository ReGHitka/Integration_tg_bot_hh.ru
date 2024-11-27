from typing import List
from typing import Any
from dataclasses import dataclass


@dataclass
class Line2:
    id: str
    hex_color: str
    name: str

    @staticmethod
    def from_dict(obj: Any) -> 'Line2':
        _id = str(obj.get("id"))
        _hex_color = str(obj.get("hex_color"))
        _name = str(obj.get("name"))
        return Line2(_id, _hex_color, _name)

@dataclass
class Station:
    id: str
    name: str
    lat: float
    lng: float
    order: int
    line: Line2

    @staticmethod
    def from_dict(obj: Any) -> 'Station':
        _id = str(obj.get("id"))
        _name = str(obj.get("name"))
        _lat = float(obj.get("lat"))
        _lng = float(obj.get("lng"))
        _order = int(obj.get("order"))
        _line2 = Line2.from_dict(obj.get("line"))
        return Station(_id, _name, _lat, _lng, _order, _line2)

@dataclass
class Line:
    id: str
    hex_color: str
    name: str
    stations: List[Station]

    @staticmethod
    def from_dict(obj: Any) -> 'Line':
        _id = str(obj.get("id"))
        _hex_color = str(obj.get("hex_color"))
        _name = str(obj.get("name"))
        _stations = [Station.from_dict(y) for y in obj.get("stations")]
        return Line(_id, _hex_color, _name, _stations)

@dataclass
class Metro:
    id: str
    name: str
    url: str
    lines: List[Line]

    @staticmethod
    def from_dict(obj: Any) -> 'Metro':
        _id = str(obj.get("id"))
        _name = str(obj.get("name"))
        _url = str(obj.get("url"))
        _lines = [Line.from_dict(y) for y in obj.get("lines")]
        return Metro(_id, _name, _url, _lines)

@dataclass
class AllMetro:
    allMetro: List[Metro]

    @staticmethod
    def from_dict(obj: Any) -> 'AllMetro':
        _allMetro = []

        for i in range(0, len(obj)):
            _allMetro.append(Metro.from_dict(obj[i]))

        return AllMetro(_allMetro)