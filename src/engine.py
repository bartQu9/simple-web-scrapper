from datetime import datetime
from abc import ABC, abstractmethod, abstractclassmethod, abstractstaticmethod


class Universe:
    def __init__(self, dt_start, dt_end):
        self.dt_start = dt_start
        self.dt_end = dt_end

    @classmethod
    def starts_now(cls):
        return cls(datetime.now(), None)


class ResourceSettings(ABC):
    pass


class SourceHandler(ABC):
    pass


class OneShootSourceHandler(SourceHandler):
    pass


class ProcessingHandler(ABC):
    pass


class OneShootProcessingHandler(ProcessingHandler):
    pass


class OutputHandler(ABC):
    pass


class OneShootOutputHandler(OutputHandler):
    pass


class Orchestrator(ABC):
    def __init__(self):
        self.pre()

    @abstractmethod
    def validate_source_handler(self):
        """check if source handler has a proper type"""
        pass

    @abstractmethod
    def validate_processing_handler(self):
        """check if processing handler has a proper type"""
        pass

    @abstractmethod
    def validate_output_handler(self):
        """check if output handler has a proper type"""
        pass

    def pre(self):
        """actions before creating Orchestrator"""
        self.validate_source_handler()
        self.validate_processing_handler()
        self.validate_output_handler()


class HttpResSettings(ResourceSettings):
    def __init__(self, url: str, auth_info: tuple):
        self.url = url
        self.auth = auth_info


class StaticWebOrchestrator(Orchestrator, ABC):
    def __init__(self, source_handler, processing_handler, output_handler):
        self.source_handler = source_handler
        self.processing_handler = processing_handler
        self.output_handler = output_handler
        super().__init__()

    def validate_source_handler(self):
        if not isinstance(self.source_handler, OneShootSourceHandler):
            raise TypeError("Source Handler must be OneShootSourceHandler")
            # later on will be is HTTPCapable etc.

    def validate_processing_handler(self):
        if not isinstance(self.processing_handler, OneShootProcessingHandler):
            raise TypeError("Processing handler must be OneShootProcessingHandler")

    def validate_output_handler(self):
        if not isinstance(self.output_handler, OneShootOutputHandler):
            raise TypeError("Output handler must be OneShootOutputHandler")
