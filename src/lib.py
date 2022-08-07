from datetime import datetime
from abc import ABC, abstractmethod, abstractclassmethod, abstractstaticmethod, abstractproperty
from typing import Type


class Universe:
    def __init__(self, dt_start, dt_end):
        self.dt_start = dt_start
        self.dt_end = dt_end

    @classmethod
    def starts_now(cls):
        return cls(datetime.now(), None)


class ResourceSettings(ABC):
    @abstractmethod
    def validate_settings(self):
        pass


class Capability(ABC):
    pass


class Handler(ABC):
    capabilities = list()

    def is_capable(self, cap: Type[Capability]):
        if cap in self.capabilities:
            return True


class SourceHandler(Handler):
    def __init__(self, settings: ResourceSettings):
        self.settings = settings


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
    def __init__(self, source_handler: SourceHandler, processing_handler: ProcessingHandler,
                 output_handler: OutputHandler, universe: Universe):
        self.source_handler = source_handler
        self.processing_handler = processing_handler
        self.output_handler = output_handler
        self.universe = universe
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
