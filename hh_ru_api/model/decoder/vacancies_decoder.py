from typing import List
from typing import Any
from dataclasses import dataclass

@dataclass
class Area:
    id: str
    name: str
    url: str

    @staticmethod
    def from_dict(obj: Any) -> 'Area':
        _id = None
        _name = None
        _url = None
        if obj is not None:
            _id = str(obj.get("id"))
            _name = str(obj.get("name"))
            _url = str(obj.get("url"))
        return Area(_id, _name, _url)

@dataclass
class Employer:
    id: str
    name: str
    url: str
    alternate_url: str
    logo_urls: str
    vacancies_url: str
    accredited_it_employer: bool
    trusted: bool

    @staticmethod
    def from_dict(obj: Any) -> 'Employer':
        _id = None
        _name = None
        _url = None
        _alternate_url = None
        _logo_urls = None
        _vacancies_url = None
        _accredited_it_employer = None
        _trusted = None

        if obj is not None:
            _id = str(obj.get("id"))
            _name = str(obj.get("name"))
            _url = str(obj.get("url"))
            _alternate_url = str(obj.get("alternate_url"))
            _logo_urls = str(obj.get("logo_urls"))
            _vacancies_url = str(obj.get("vacancies_url"))
            _accredited_it_employer = bool(obj.get("accredited_it_employer"))
            _trusted = bool(obj.get("trusted"))

        return Employer(_id, _name, _url, _alternate_url, _logo_urls, _vacancies_url, _accredited_it_employer, _trusted)

@dataclass
class Employment:
    id: str
    name: str

    @staticmethod
    def from_dict(obj: Any) -> 'Employment':
        _id = None
        _name = None

        if obj is not None:
            _id = str(obj.get("id"))
            _name = str(obj.get("name"))

        return Employment(_id, _name)

@dataclass
class Experience:
    id: str
    name: str

    @staticmethod
    def from_dict(obj: Any) -> 'Experience':
        _id = None
        _name = None

        if obj is not None:
            _id = str(obj.get("id"))
            _name = str(obj.get("name"))

        return Experience(_id, _name)

@dataclass
class ProfessionalRole:
    id: str
    name: str

    @staticmethod
    def from_dict(obj: Any) -> 'ProfessionalRole':
        _id = None
        _name = None

        if obj is not None:
            _id = str(obj.get("id"))
            _name = str(obj.get("name"))
        return ProfessionalRole(_id, _name)

@dataclass
class Schedule:
    id: str
    name: str

    @staticmethod
    def from_dict(obj: Any) -> 'Schedule':
        _id = None
        _name = None

        if obj is not None:
            _id = str(obj.get("id"))
            _name = str(obj.get("name"))

        return Schedule(_id, _name)

@dataclass
class Snippet:
    requirement: str
    responsibility: str

    @staticmethod
    def from_dict(obj: Any) -> 'Snippet':
        _requirement = None
        _responsibility = None

        if obj is not None:
            _requirement = str(obj.get("requirement"))
            _responsibility = str(obj.get("responsibility"))

        return Snippet(_requirement, _responsibility)

@dataclass
class Type:
    id: str
    name: str

    @staticmethod
    def from_dict(obj: Any) -> 'Type':
        _id = None
        _name = None

        if obj is not None:
            _id = str(obj.get("id"))
            _name = str(obj.get("name"))

        return Type(_id, _name)

@dataclass
class Metro:
    station_name: str
    line_name: str
    station_id: str
    line_id: str
    lat: float
    lng: float

    @staticmethod
    def from_dict(obj: Any) -> 'Metro':
        _station_name = None
        _line_name = None
        _station_id = None
        _line_id = None
        _lat = None
        _lng = None

        if obj is not None:
            _station_name = str(obj.get("station_name"))
            _line_name = str(obj.get("line_name"))
            _station_id = str(obj.get("station_id"))
            _line_id = str(obj.get("line_id"))
            _lat = float(obj.get("lat"))
            _lng = float(obj.get("lng"))

        return Metro(_station_name, _line_name, _station_id, _line_id, _lat, _lng)


@dataclass
class MetroStation:
    station_name: str
    line_name: str
    station_id: str
    line_id: str
    lat: float
    lng: float

    @staticmethod
    def from_dict(obj: Any) -> 'MetroStation':
        _station_name = None
        _line_name = None
        _station_id = None
        _line_id = None
        _lat = None
        _lng = None

        if obj is not None:
            _station_name = str(obj.get("station_name"))
            _line_name = str(obj.get("line_name"))
            _station_id = str(obj.get("station_id"))
            _line_id = str(obj.get("line_id"))
            _lat = float(obj.get("lat"))
            _lng = float(obj.get("lng"))

        return MetroStation(_station_name, _line_name, _station_id, _line_id, _lat, _lng)

@dataclass
class Address:
    city: str
    street: str
    building: str
    lat: float
    lng: float
    description: str
    raw: str
    metro: Metro
    metro_stations: List[MetroStation]
    id: str

    @staticmethod
    def from_dict(obj: Any) -> 'Address':
        _city = None
        _street = None
        _building = None
        _lat = None
        _lng = None
        _description = None
        _raw = None
        _metro = None
        _metro_stations = None
        _id = None

        if obj is not None:
            _city = str(obj.get("city"))
            _street = str(obj.get("street"))
            _building = str(obj.get("building"))
            _lat = str(obj.get("lat"))
            _lng = str(obj.get("lng"))
            _description = str(obj.get("description"))
            _raw = str(obj.get("raw"))
            _metro = Metro.from_dict(obj.get("metro"))
            _metro_stations = [MetroStation.from_dict(y) for y in obj.get("metro_stations")]
            _id = str(obj.get("id"))

        return Address(_city, _street, _building, _lat, _lng, _description, _raw, _metro, _metro_stations, _id)


@dataclass
class Item:
    id: str
    premium: bool
    name: str
    department: str
    has_test: bool
    response_letter_required: bool
    area: Area
    salary: str
    type: Type
    address: Address
    response_url: str
    sort_point_distance: str
    published_at: str
    created_at: str
    archived: bool
    apply_alternate_url: str
    insider_interview: str
    url: str
    alternate_url: str
    employer: Employer
    snippet: Snippet
    contacts: str
    schedule: Schedule
    accept_temporary: bool
    professional_roles: List[ProfessionalRole]
    accept_incomplete_resumes: bool
    experience: Experience
    employment: Employment
    adv_response_url: str
    is_adv_vacancy: bool
    adv_context: str

    @staticmethod
    def from_dict(obj: Any) -> 'Item':
        _id = None
        _premium = None
        _name = None
        _department = None
        _has_test = None
        _response_letter_required = None
        _area = None
        _salary = None
        _type = None
        _address = None
        _response_url = None
        _sort_point_distance = None
        _published_at = None
        _created_at = None
        _archived = None
        _apply_alternate_url = None
        _insider_interview = None
        _url = None
        _alternate_url = None
        _employer = None
        _snippet = None
        _contacts = None
        _schedule = None
        _accept_temporary = None
        _professional_roles = None
        _accept_incomplete_resumes = None
        _experience = None
        _employment = None
        _adv_response_url = None
        _is_adv_vacancy = None
        _adv_context = None

        if obj is not None:
            _id = str(obj.get("id"))
            _premium = bool(obj.get("premium"))
            _name = str(obj.get("name"))
            _department = str(obj.get("department"))
            _has_test = bool(obj.get("has_test"))
            _response_letter_required = bool(obj.get("response_letter_required"))
            _area = Area.from_dict(obj.get("area"))
            _salary = str(obj.get("salary"))
            _type = Type.from_dict(obj.get("type"))
            _address = Address.from_dict(obj.get("address"))
            _response_url = str(obj.get("response_url"))
            _sort_point_distance = str(obj.get("sort_point_distance"))
            _published_at = str(obj.get("published_at"))
            _created_at = str(obj.get("created_at"))
            _archived = bool(obj.get("archived"))
            _apply_alternate_url = str(obj.get("apply_alternate_url"))
            _insider_interview = str(obj.get("insider_interview"))
            _url = str(obj.get("url"))
            _alternate_url = str(obj.get("alternate_url"))
            _employer = Employer.from_dict(obj.get("employer"))
            _snippet = Snippet.from_dict(obj.get("snippet"))
            _contacts = str(obj.get("contacts"))
            _schedule = Schedule.from_dict(obj.get("schedule"))
            _accept_temporary = bool(obj.get("accept_temporary"))
            _professional_roles = [ProfessionalRole.from_dict(y) for y in obj.get("professional_roles")]
            _accept_incomplete_resumes = bool(obj.get("accept_incomplete_resumes"))
            _experience = Experience.from_dict(obj.get("experience"))
            _employment = Employment.from_dict(obj.get("employment"))
            _adv_response_url = str(obj.get("adv_response_url"))
            _is_adv_vacancy = bool(obj.get("is_adv_vacancy"))
            _adv_context = str(obj.get("adv_context"))

        return Item(_id, _premium, _name, _department, _has_test, _response_letter_required, _area, _salary, _type, _address, _response_url, _sort_point_distance, _published_at, _created_at, _archived, _apply_alternate_url, _insider_interview, _url, _alternate_url, _employer, _snippet, _contacts, _schedule, _accept_temporary, _professional_roles, _accept_incomplete_resumes, _experience, _employment, _adv_response_url, _is_adv_vacancy, _adv_context)

@dataclass
class Vacancies:
    items: List[Item]

    @staticmethod
    def from_dict(obj: Any) -> 'Vacancies':
        _items = None

        if obj is not None:
            _items = [Item.from_dict(y) for y in obj.get("items")]

        return Vacancies(_items)