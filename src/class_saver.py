from abc import ABC, abstractmethod


class Saver(ABC):
    pass


class JSON_Saver(Saver):
    pass


class SCV_Saver(Saver):
    pass


class XLSX_Saver(Saver):
    pass