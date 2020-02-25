from typing import Sequence, Union, Any, Mapping, Optional
from dataclasses import dataclass

@dataclass(frozen=True)
class Discriminator:
  propertyName: str
  mapping: Optional[Mapping[str, str]] = None
  _x: Optional[Mapping[str, Any]] = None

@dataclass(frozen=True)
class ExternalDocumentation:
  url: str
  description: Optional[str] = None
  _x: Optional[Mapping[str, Any]] = None

@dataclass(frozen=True)
class XML:
  name: Optional[str] = None
  namespace: Optional[str] = None
  prefix: Optional[str] = None
  attribute: Optional[bool] = None
  wrapped: Optional[bool] = None
  _x: Optional[Mapping[str, Any]] = None

@dataclass(frozen=True)
class Reference:
  _ref: str
  _x: Optional[Mapping[str, Any]] = None

@dataclass(frozen=True)
class Schema:
  title: Optional[str] = None
  multipleOf: Optional[float] = None
  maximum: Optional[float] = None
  exclusiveMaximum: Optional[Union[bool, int]] = None
  minimum: Optional[float] = None
  exclusiveMinimum: Optional[Union[bool, int]] = None
  maxLength: Optional[int] = None
  minLength: Optional[int] = None
  pattern: Optional[str] = None
  maxItems: Optional[int] = None
  minItems: Optional[int] = None
  uniqueItems: Optional[bool] = None
  maxProperties: Optional[int] = None
  minProperties: Optional[int] = None
  required: Optional[Sequence[str]] = None
  enum: Optional[Sequence[Any]] = None
  allOf: Optional[Sequence[Union['Schema', Reference]]] = None
  oneOf: Optional[Sequence[Union['Schema', Reference]]] = None
  anyOf: Optional[Sequence[Union['Schema', Reference]]] = None
  items: Optional[Union[Sequence[Union['Schema', Reference]], 'Schema', Reference]] = None
  properties: Optional[Mapping[str, Union['Schema', Reference]]] = None
  additionalProperties: Optional[Union['Schema', Reference, bool]] = None
  description: Optional[str] = None
  default: Optional[Any] = None
  nullable: Optional[bool] = None
  discriminator: Optional[Discriminator] = None
  readOnly: Optional[bool] = None
  writeOnly: Optional[bool] = None
  example: Optional[Any] = None
  externalDocs: Optional[ExternalDocumentation] = None
  deprecated: Optional[bool] = None
  xml: Optional[XML] = None
  _format: Optional[str] = None
  _type: Optional[str] = None
  _not: Optional[Union['Schema', Reference]] = None

  _x: Optional[Mapping[str, Any]] = None

@dataclass(frozen=True)
class Contact:
  name: Optional[str] = None
  url: Optional[str] = None
  email: Optional[str] = None
  _x: Optional[Mapping[str, Any]] = None

@dataclass(frozen=True)
class License:
  name: str
  url: Optional[str] = None
  _x: Optional[Mapping[str, Any]] = None

@dataclass(frozen=True)
class Info:
  title: str
  version: str
  description: Optional[str] = None
  termsOfService: Optional[str] = None
  contact: Optional[Contact] = None
  _license: Optional[License] = None
  _x: Optional[Mapping[str, Any]] = None

@dataclass(frozen=True)
class ServerVariable:
  _default: str
  enum: Optional[Sequence[str]] = None
  description: Optional[str] = None
  _x: Optional[Mapping[str, Any]] = None

@dataclass(frozen=True)
class Server:
  url: str
  description: Optional[str] = None
  variables: Optional[Mapping[str, ServerVariable]] = None
  _x: Optional[Mapping[str, Any]] = None

@dataclass(frozen=True)
class Link:
  operationId: Optional[str] = None
  operationRef: Optional[str] = None
  parameters: Optional[Mapping[str, Any]] = None
  requestBody: Optional[Any] = None
  description: Optional[str] = None
  server: Optional[Server] = None
  _x: Optional[Mapping[str, Any]] = None

@dataclass(frozen=True)
class Example:
  summary: Optional[str] = None
  description: Optional[str] = None
  value: Optional[Any] = None
  externalValue: Optional[str] = None
  _x: Optional[Mapping[str, Any]] = None

@dataclass(frozen=True)
class Encoding:
  contentType: Optional[str] = None
  headers: Optional[Mapping[str, 'Header']] = None
  style: Optional[str] = None
  explode: Optional[bool] = None
  allowReserved: Optional[bool] = None
  _x: Optional[Mapping[str, Any]] = None

@dataclass(frozen=True)
class MediaType:
  schema: Optional[Union[Schema, Reference]] = None
  example: Optional[Any] = None
  examples: Optional[Mapping[str, Union[Example, Reference]]] = None
  encoding: Optional[Mapping[str, Encoding]] = None
  _x: Optional[Mapping[str, Any]] = None

@dataclass(frozen=True)
class Header:
  description: Optional[str] = None
  required: Optional[bool] = None
  deprecated: Optional[bool] = None
  allowEmptyValue: Optional[bool] = None
  style: Optional[str] = None
  explode: Optional[bool] = None
  allowReserved: Optional[bool] = None
  schema: Optional[Union[Schema, Reference]] = None
  content: Optional[Mapping[str, MediaType]] = None
  example: Optional[Any] = None
  examples: Optional[Mapping[str, Union[Example, Reference]]] = None
  _x: Optional[Mapping[str, Any]] = None

@dataclass(frozen=True)
class Operation:
  responses: 'Responses'
  tags: Optional[Sequence[str]] = None
  summary: Optional[str] = None
  description: Optional[str] = None
  externalDocs: Optional[ExternalDocumentation] = None
  operationId: Optional[str] = None
  parameters: Optional[Sequence[Union['Parameter', Reference]]] = None
  requestBody: Optional[Union['RequestBody', Reference]] = None
  callbacks: Optional[Mapping[str, Union['Callback', Reference]]] = None
  deprecated: Optional[bool] = None
  security: Optional[Sequence['SecurityRequirement']] = None
  servers: Optional[Sequence[Server]] = None
  _x: Optional[Mapping[str, Any]] = None

@dataclass(frozen=True)
class Response:
  description: str
  headers: Optional[Mapping[str, Union[Header, Reference]]] = None
  content: Optional[Mapping[str, MediaType]] = None
  links: Optional[Mapping[str, Union[Link, Reference]]] = None
  _x: Optional[Mapping[str, Any]] = None

@dataclass(frozen=True)
class Parameter:
  name: str
  _in: str
  description: Optional[str] = None
  required: Optional[bool] = None
  deprecated: Optional[bool] = None
  allowEmptyValue: Optional[bool] = None
  style: Optional[str] = None
  explode: Optional[bool] = None
  allowReserved: Optional[bool] = None
  schema: Optional[Union[Schema, Reference]] = None
  content: Optional[Mapping[str, MediaType]] = None
  example: Optional[Any] = None
  examples: Optional[Mapping[str, Union[Example, Reference]]] = None
  _x: Optional[Mapping[str, Any]] = None

@dataclass(frozen=True)
class RequestBody:
  content: Mapping[str, MediaType]
  description: Optional[str] = None
  required: Optional[bool] = None
  _x: Optional[Mapping[str, Any]] = None

@dataclass(frozen=True)
class APIKeySecurityScheme:
  name: str
  _type: str
  _in: str
  description: Optional[str] = None
  _x: Optional[Mapping[str, Any]] = None

@dataclass(frozen=True)
class HTTPSecurityScheme:
  _type: str
  scheme: str
  bearerFormat: Optional[str] = None
  description: Optional[str] = None
  _x: Optional[Mapping[str, Any]] = None

@dataclass(frozen=True)
class ImplicitOAuthFlow:
  authorizationUrl: str
  scopes: Mapping[str, str]
  refreshUrl: Optional[str] = None
  _x: Optional[Mapping[str, Any]] = None

@dataclass(frozen=True)
class PasswordOAuthFlow:
  tokenUrl: str
  refreshUrl: Optional[str] = None
  scopes: Optional[Mapping[str, str]] = None
  _x: Optional[Mapping[str, Any]] = None

@dataclass(frozen=True)
class ClientCredentialsFlow:
  tokenUrl: str
  refreshUrl: Optional[str] = None
  scopes: Optional[Mapping[str, str]] = None
  _x: Optional[Mapping[str, Any]] = None

@dataclass(frozen=True)
class AuthorizationCodeOAuthFlow:
  tokenUrl: str
  authorizationUrl: str
  refreshUrl: Optional[str] = None
  scopes: Optional[Mapping[str, str]] = None
  _x: Optional[Mapping[str, Any]] = None

@dataclass(frozen=True)
class OAuthFlows:
  implicit: Optional[ImplicitOAuthFlow] = None
  password: Optional[PasswordOAuthFlow] = None
  clientCredentials: Optional[ClientCredentialsFlow] = None
  authorizationCode: Optional[AuthorizationCodeOAuthFlow] = None
  _x: Optional[Mapping[str, Any]] = None

@dataclass(frozen=True)
class OAuth2SecurityScheme:
  flows: OAuthFlows
  _type: str
  description: Optional[str] = None
  _x: Optional[Mapping[str, Any]] = None

@dataclass(frozen=True)
class OpenIdConnectSecurityScheme:
  _type: str
  openIdConnectUrl: str
  description: Optional[str] = None
  _x: Optional[Mapping[str, Any]] = None

SecurityScheme = Union[APIKeySecurityScheme, HTTPSecurityScheme, OAuth2SecurityScheme, OpenIdConnectSecurityScheme, str]

Responses = Mapping[str, Union[Response, Reference]]
SecurityRequirement = Mapping[str, Sequence[str]]

@dataclass(frozen=True)
class PathItem:
  summary: Optional[str] = None
  description: Optional[str] = None
  servers: Optional[Sequence[Server]] = None
  parameters: Optional[Sequence[Union[Parameter, Reference]]] = None
  get: Optional[Operation] = None
  put: Optional[Operation] = None
  post: Optional[Operation] = None
  delete: Optional[Operation] = None
  options: Optional[Operation] = None
  head: Optional[Operation] = None
  patch: Optional[Operation] = None
  trace: Optional[Operation] = None
  _ref: Optional[str] = None
  _x: Optional[Mapping[str, Any]] = None

Callback = Mapping[str, PathItem]

@dataclass(frozen=True)
class Components:
  schemas: Optional[Mapping[str, Union[Schema, Reference]]] = None
  responses: Optional[Mapping[str, Union[Response, Reference]]] = None
  parameters: Optional[Mapping[str, Union[Parameter, Reference]]] = None
  examples: Optional[Mapping[str, Union[Example, Reference]]] = None
  requestBodies: Optional[Mapping[str, Union[RequestBody, Reference]]] = None
  headers: Optional[Mapping[str, Union[Header, Reference]]] = None
  securitySchemes: Optional[Mapping[str, Union[SecurityScheme, Reference]]] = None
  links: Optional[Mapping[str, Union[Link, Reference]]] = None
  callbacks: Optional[Mapping[str, Union[Callback, Reference]]] = None
  _x: Optional[Mapping[str, Any]] = None

Paths = Mapping[str, PathItem]

@dataclass(frozen=True)
class Tag:
  name: str
  description: Optional[str] = None
  externalDocs: Optional[ExternalDocumentation] = None
  _x: Optional[Mapping[str, Any]] = None

@dataclass(frozen=True)
class OpenAPIObject:
  openapi: str
  info: Info
  paths: Paths
  externalDocs: Optional[ExternalDocumentation] = None
  servers: Optional[Sequence[Server]] = None
  security: Optional[Sequence[SecurityRequirement]] = None
  tags: Optional[Sequence[Tag]] = None
  components: Optional[Components] = None
  _x: Optional[Mapping[str, Any]] = None
