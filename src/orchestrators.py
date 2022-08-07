from abc import ABC

from lib import Orchestrator, OneShootSourceHandler, OneShootProcessingHandler, OneShootOutputHandler, Universe
from sources.web import HttpCapable, HttpsCapable


class StaticWebOrchestrator(Orchestrator):
    def __init__(self, source_handler: OneShootSourceHandler, processing_handler: OneShootProcessingHandler,
                 output_handler: OneShootOutputHandler, universe: Universe):
        super().__init__(source_handler, processing_handler, output_handler, universe)

    def validate_source_handler(self):
        if not isinstance(self.source_handler, OneShootSourceHandler):
            raise TypeError("Source Handler must be OneShootSourceHandler")
        if not (self.source_handler.is_capable(HttpCapable) or self.source_handler.is_capable(HttpsCapable)):
            raise TypeError("Source Handler must be HttpCapable or HttpsCapable")

    def validate_processing_handler(self):
        if not isinstance(self.processing_handler, OneShootProcessingHandler):
            raise TypeError("Processing handler must be OneShootProcessingHandler")

    def validate_output_handler(self):
        if not isinstance(self.output_handler, OneShootOutputHandler):
            raise TypeError("Output handler must be OneShootOutputHandler")
