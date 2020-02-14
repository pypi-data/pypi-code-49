from __future__ import annotations

from typing import TypedDict, Mapping, Union, Sequence

TemplatePrimitive = Union[
    float,
    int,
    str,
    bool,
    Sequence['TemplatePrimitive'],
    Mapping[str, 'TemplatePrimitive']
]


class RuntimeParameter(TypedDict):
    insert_path: str
    parameter_name: str


class DynamicParameter(TypedDict):
    dynamic: bool
    dynamic_type: str
    dynamic_kwargs: TemplatePrimitive


TemplateParameter = Union[TemplatePrimitive, DynamicParameter]
TemplateParameters = Mapping[str, TemplateParameter]


class ExtractionParameters(TypedDict):
    runtime_parameters: Sequence[RuntimeParameter]
    static_parameters: TemplateParameters


class ExtractorTemplate(TypedDict):
    extractor_class: str
    runtime_parameters: Sequence[RuntimeParameter]
    static_parameters: TemplateParameters


class ProcessorTemplate(TypedDict):
    processor_class: str
    run_time_parameters: Sequence[RuntimeParameter]
    static_parameters: TemplateParameters


ParameterSet = Union[
    ExtractorTemplate,
    ProcessorTemplate,
    ExtractionParameters
]


class ExtractionTemplate(TypedDict):
    extraction_type: str
    extracted_object_type: str
    extraction: ExtractionParameters
    extractor: ExtractorTemplate
    processor: ProcessorTemplate
