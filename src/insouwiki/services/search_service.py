class SearchService(ABC):

    @abstractmethod
    def search(
        self,
        query: str,
    ):
        ...