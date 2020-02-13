from typing import List, Dict
from pangeamt_nlp.processor.base.processor_base import ProcessorBase
from pangeamt_nlp.processor.processor_factory import ProcessorFactory
from pangeamt_nlp.seg import Seg


class PipelineTraining:
    def __init__(self, processors: List[ProcessorBase]):
        self._processors = processors

    def process(self, seg: Seg) -> None:
        for processor in self._processors:
            processor.process_train(seg)

    # Method to create the training pipeline. Expects src_lang, tgt_lang and the
    # processors dictionary from the config.
    @staticmethod
    def create_from_dict(
        src_lang: str, tgt_lang: str, processors_config: Dict
    ) -> "PipelineTraining":
        # List that will be passed to PipelineTraining
        processors = []
        factory = ProcessorFactory
        # For each processor in the processors config dictionary
        for processor_name in processors_config:
            # Get the arguments to initialize the processor
            args = processors_config[processor_name]
            # Initialize the processor
            processor = factory.create(processor_name, src_lang, tgt_lang, *args)
            # Add the processor to the list of processors
            if isinstance(processor, ProcessorBase):
                processors.append(processor)
            else:
                raise ValueError("Non-processor object in processors list.")
        # Return the PipelineDecoding object
        return PipelineTraining(processors)
