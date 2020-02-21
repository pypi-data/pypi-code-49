from typing import Sequence, Union, Any, Mapping, Optional
from dataclasses import dataclass

@dataclass
class Discriminator:
  propertyName: str
  mapping: Optional[Mapping[str, str]]
  _x: Optional[Mapping[str, Any]]

@dataclass
class ExternalDocumentation:
  url: str
  description: Optional[str]
  _x: Optional[Mapping[str, Any]]

@dataclass
class XML:
  name: Optional[str]
  namespace: Optional[str]
  prefix: Optional[str]
  attribute: Optional[bool]
  wrapped: Optional[bool]
  _x: Optional[Mapping[str, Any]]

@dataclass
class Reference:
  _ref: str
  _x: Optional[Mapping[str, Any]]

@dataclass
class Schema:
  title: Optional[str]
  multipleOf: Optional[float]
  maximum: Optional[float]
  exclusiveMaximum: Optional[Union[bool, int]]
  minimum: Optional[float]
  exclusiveMinimum: Optional[Union[bool, int]]
  maxLength: Optional[int]
  minLength: Optional[int]
  pattern: Optional[str]
  maxItems: Optional[int]
  minItems: Optional[int]
  uniqueItems: Optional[bool]
  maxProperties: Optional[int]
  minProperties: Optional[int]
  required: Optional[Sequence[str]]
  enum: Optional[Sequence[Any]]
  allOf: Optional[Sequence[Union['Schema', Reference]]]  # type: Optional[ignore
  oneOf: Optional[Sequence[Union['Schema', Reference]]]  # type: Optional[ignore
  anyOf: Optional[Sequence[Union['Schema', Reference]]]  # type: Optional[ignore
  items: Optional[Union[Sequence[Union['Schema', Reference]], 'Schema', Reference]]  # type: Optional[ignore
  properties: Optional[Mapping[str, Union['Schema', Reference]]]  # type: Optional[ignore
  additionalProperties: Optional[Union['Schema', Reference, bool]]  # type: Optional[ignore
  description: Optional[str]
  default: Optional[Any]
  nullable: Optional[bool]
  discriminator: Optional[Discriminator]
  readOnly: Optional[bool]
  writeOnly: Optional[bool]
  example: Optional[Any]
  externalDocs: Optional[ExternalDocumentation]
  deprecated: Optional[bool]
  xml: Optional[XML]
  _format: Optional[str]
  _type: Optional[str]
  _not: Optional[Union['Schema', Reference]]

  _x: Optional[Mapping[str, Any]]

@dataclass
class Contact:
  name: Optional[str]
  url: Optional[str]
  email: Optional[str]
  _x: Optional[Mapping[str, Any]]

@dataclass
class License:
  name: str
  url: Optional[str]
  _x: Optional[Mapping[str, Any]]

@dataclass
class Info:
  title: str
  version: str
  description: Optional[str]
  termsOfService: Optional[str]
  contact: Optional[Contact]
  _license: Optional[License]
  _x: Optional[Mapping[str, Any]]

@dataclass
class ServerVariable:
  enum: Optional[Sequence[str]]
  description: Optional[str]
  _default: str
  _x: Optional[Mapping[str, Any]]

@dataclass
class Server:
  url: str
  description: Optional[str]
  variables: Optional[Mapping[str, ServerVariable]]
  _x: Optional[Mapping[str, Any]]

@dataclass
class Link:
  operationId: Optional[str]
  operationRef: Optional[str]
  parameters: Optional[Mapping[str, Any]]
  requestBody: Optional[Any]
  description: Optional[str]
  server: Optional[Server]
  _x: Optional[Mapping[str, Any]]

@dataclass
class Example:
  summary: Optional[str]
  description: Optional[str]
  value: Optional[Any]
  externalValue: Optional[str]
  _x: Optional[Mapping[str, Any]]

@dataclass
class Encoding:
  contentType: Optional[str]
  headers: Optional[Mapping[str, 'Header']]  # type: ignore
  style: Optional[str]
  explode: Optional[bool]
  allowReserved: Optional[bool]
  _x: Optional[Mapping[str, Any]]

@dataclass
class MediaType:
  schema: Optional[Union[Schema, Reference]]
  example: Optional[Any]
  examples: Optional[Mapping[str, Union[Example, Reference]]]
  encoding: Optional[Mapping[str, Encoding]]
  _x: Optional[Mapping[str, Any]]

@dataclass
class Header:
  description: Optional[str]
  required: Optional[bool]
  deprecated: Optional[bool]
  allowEmptyValue: Optional[bool]
  style: Optional[str]
  explode: Optional[bool]
  allowReserved: Optional[bool]
  schema: Optional[Union[Schema, Reference]]
  content: Optional[Mapping[str, MediaType]]
  example: Optional[Any]
  examples: Optional[Mapping[str, Union[Example, Reference]]]
  _x: Optional[Mapping[str, Any]]

@dataclass
class Operation:
  responses: 'Responses'  # type: ignore
  tags: Optional[Sequence[str]]
  summary: Optional[str]
  description: Optional[str]
  externalDocs: Optional[ExternalDocumentation]
  operationId: Optional[str]
  parameters: Optional[Sequence[Union['Parameter', Reference]]]  # type: ignore
  requestBody: Optional[Union['RequestBody', Reference]]  # type: ignore
  callbacks: Optional[Mapping[str, Union['Callback', Reference]]]  # type: ignore
  deprecated: Optional[bool]
  security: Optional[Sequence['SecurityRequirement']]
  servers: Optional[Sequence[Server]]
  _x: Optional[Mapping[str, Any]]

@dataclass
class Response:
  description: str
  headers: Optional[Mapping[str, Union[Header, Reference]]]
  content: Optional[Mapping[str, MediaType]]
  links: Optional[Mapping[str, Union[Link, Reference]]]
  _x: Optional[Mapping[str, Any]]

@dataclass
class Parameter:
  name: str
  description: Optional[str]
  required: Optional[bool]
  deprecated: Optional[bool]
  allowEmptyValue: Optional[bool]
  style: Optional[str]
  explode: Optional[bool]
  allowReserved: Optional[bool]
  schema: Optional[Union[Schema, Reference]]
  content: Optional[Mapping[str, MediaType]]
  example: Optional[Any]
  examples: Optional[Mapping[str, Union[Example, Reference]]]
  _in: str
  _x: Optional[Mapping[str, Any]]

@dataclass
class RequestBody:
  content: Mapping[str, MediaType]
  description: Optional[str]
  required: Optional[bool]
  _x: Optional[Mapping[str, Any]]

@dataclass
class APIKeySecurityScheme:
  description: Optional[str]
  name: str
  _type: str
  _in: str
  _x: Optional[Mapping[str, Any]]

@dataclass
class HTTPSecurityScheme:
  scheme: str
  bearerFormat: Optional[str]
  description: Optional[str]
  _type: str
  _x: Optional[Mapping[str, Any]]

@dataclass
class ImplicitOAuthFlow:
  authorizationUrl: str
  scopes: Mapping[str, str]
  refreshUrl: Optional[str]
  _x: Optional[Mapping[str, Any]]

@dataclass
class PasswordOAuthFlow:
  tokenUrl: str
  refreshUrl: Optional[str]
  scopes: Optional[Mapping[str, str]]
  _x: Optional[Mapping[str, Any]]

@dataclass
class ClientCredentialsFlow:
  tokenUrl: str
  refreshUrl: Optional[str]
  scopes: Optional[Mapping[str, str]]
  _x: Optional[Mapping[str, Any]]

@dataclass
class AuthorizationCodeOAuthFlow:
  tokenUrl: str
  authorizationUrl: str
  refreshUrl: Optional[str]
  scopes: Optional[Mapping[str, str]]
  _x: Optional[Mapping[str, Any]]

@dataclass
class OAuthFlows:
  implicit: Optional[ImplicitOAuthFlow]
  password: Optional[PasswordOAuthFlow]
  clientCredentials: Optional[ClientCredentialsFlow]
  authorizationCode: Optional[AuthorizationCodeOAuthFlow]
  _x: Optional[Mapping[str, Any]]

@dataclass
class OAuth2SecurityScheme:
  flows: OAuthFlows
  description: Optional[str]
  _type: str
  _x: Optional[Mapping[str, Any]]

@dataclass
class OpenIdConnectSecurityScheme:
  openIdConnectUrl: str
  description: Optional[str]
  _type: str
  _x: Optional[Mapping[str, Any]]

SecurityScheme = Union[APIKeySecurityScheme, HTTPSecurityScheme, OAuth2SecurityScheme, OpenIdConnectSecurityScheme, str]

Responses = Mapping[str, Union[Response, Reference]]  # type: ignore
SecurityRequirement = Mapping[str, Sequence[str]]

@dataclass
class PathItem:
  summary: Optional[str]
  description: Optional[str]
  servers: Optional[Sequence[Server]]
  parameters: Optional[Sequence[Union[Parameter, Reference]]]
  get: Optional[Operation]
  put: Optional[Operation]
  post: Optional[Operation]
  delete: Optional[Operation]
  options: Optional[Operation]
  head: Optional[Operation]
  patch: Optional[Operation]
  trace: Optional[Operation]
  _ref: Optional[str]
  _x: Optional[Mapping[str, Any]]

Callback = Mapping[str, PathItem]  # type: ignore

@dataclass
class Components:
  schemas: Optional[Mapping[str, Union[Schema, Reference]]]
  responses: Optional[Mapping[str, Union[Response, Reference]]]
  parameters: Optional[Mapping[str, Union[Parameter, Reference]]]
  examples: Optional[Mapping[str, Union[Example, Reference]]]
  requestBodies: Optional[Mapping[str, Union[RequestBody, Reference]]]
  headers: Optional[Mapping[str, Union[Header, Reference]]]
  securitySchemes: Optional[Mapping[str, Union[SecurityScheme, Reference]]]
  links: Optional[Mapping[str, Union[Link, Reference]]]
  callbacks: Optional[Mapping[str, Union[Callback, Reference]]]
  _x: Optional[Mapping[str, Any]]

Paths = Mapping[str, PathItem]  # type: ignore

@dataclass
class Tag:
  name: str
  description: Optional[str]
  externalDocs: Optional[ExternalDocumentation]
  _x: Optional[Mapping[str, Any]]

@dataclass
class OpenAPIObject:
  openapi: str
  info: Info
  paths: Paths
  externalDocs: Optional[ExternalDocumentation]
  servers: Optional[Sequence[Server]]
  security: Optional[Sequence[SecurityRequirement]]
  tags: Optional[Sequence[Tag]]
  components: Optional[Components]
  _x: Optional[Mapping[str, Any]]
