from abc import ABCMeta, abstractmethod

class StorageInitException(BaseException):
    """Ошибка """


# абстрактный класс хранения данных
class DataStorage(metaclass=ABCMeta):

    """класс отвечает за хранение всех данных игры
        для возможности прерывания процесса,
        или в случае непредвиденного прекращения
    """

    types = {} # типы хранилища. сначала только sql

    def __init__(self, path):
        self.__path = path


    @abstractmethod
    def init_storage(self):
        """инициализирует хранилище"""


    @abstractmethod
    def write_data(self):
        """запись всех данных данных после хода"""


    @abstractmethod
    def read_data(self):
        """чтение из места хранения всех данных"""


    @abstractmethod
    def check_turn(self):
        """проверяет, чей сейчас ход"""


    @classmethod
    def get_instance(cls, ext)

        klass = cls.types.get(ext)

        if klass in None:
            raise StorageInitException(
                '{} is wrong expantion'.format(ext)
            )
        return klass

    @classmethod
    def add_type(cls, ext, klass):
        if not ext:
            raise StorageInitException(
                'Need expantion'
            )
        if not issubclass(klass, DataStorage):
            raise StorageInitException(
                'Class {} is not DataStorage'.format(klass)
            )
        cls.types[ext] = klass




