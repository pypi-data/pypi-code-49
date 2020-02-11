from enum import Enum
from spectre.generation import utils
from spectre.generation import serializer
from spectre.model import Entity, SpectreType, Field, UnknownTypeException
from spectre.config import Config

BASE_IMPORTS = [ 'java.util.Optional', 'java.util.List' ]

class ClassType(Enum):
    ENTITY = 1,
    REPOSITORY = 2
    MANAGER = 3
    REST_CONTROLLER = 4

    def get_name(self, entity_name: str):
        name = utils.to_pascal(entity_name)
        if self is ClassType.ENTITY:
            return name
        if self is ClassType.REPOSITORY:
            return f'{name}Repository'
        if self is ClassType.MANAGER:
            return f'{name}Manager'
        if self is ClassType.REST_CONTROLLER:
            return f'{name}Controller'
        raise UnknownTypeException(f'Unknown Java class type (Naming not yet implemented): {self}')
        
def get_out_path(entity: Entity, config: Config, t: ClassType):
    path = ['src/main/java']
    package = get_package(entity, config, t)
    path.append(package.replace('.', '/'))
    path.append(f'{t.get_name(entity.name)}.java')
    return '/'.join(path)

def get_package(entity: Entity, config: Config, t: ClassType):
    package = [config.namespace]
    if t is ClassType.ENTITY:
        package.append(f'model')
    if t is ClassType.REPOSITORY:
        package.append(f'dao')
    if t is ClassType.MANAGER:
        package.append(f'manager')
    if t is ClassType.REST_CONTROLLER:
        package.append(f'rest')
    return '.'.join(package).lower()

def get_type(t: SpectreType, name = None):
    '''
    Convert from a generic Spectre type to a specific Java type. Name of field is used if type is an enum, not needed otherwise
    '''
    if t is SpectreType.INT:
        return 'int'
    if t is SpectreType.STRING:
        return 'String'
    if t is SpectreType.DATETIME:
        return 'Instant'
    if t is SpectreType.BOOL:
        return 'boolean'
    if t is SpectreType.FLOAT:
        return 'double'
    if t is SpectreType.ENUM:
        return name
    if t is SpectreType.UUID:
        return 'String'
    raise UnknownTypeException(f'Unknown Spectre type (Java mapping not yet implemented): {t.name}')

def generate(config: Config, path):
    entities = utils.read_entities(path)
    written = []
    for ent in entities:
        written.extend(write_classes(ent, config))
    return written

def get_class_stub(entity: Entity, imports, config: Config, class_type: ClassType):

    should_have_logger = class_type in [ClassType.MANAGER, ClassType.REST_CONTROLLER]

    output = [f'package {get_package(entity, config, class_type)};', '']
    entity_name = utils.to_pascal(ClassType.ENTITY.get_name(entity.name))

    if should_have_logger:
        imports.extend([ 'org.slf4j.Logger', 'org.slf4j.LoggerFactory' ])

    if imports:
        output.extend([ get_import(i) for i in imports ])
        output.append('')

    class_name = class_type.get_name(entity.name)
    if class_type is ClassType.ENTITY:
        if config.java_options.get('spring_data', False):
            output.append('@Entity')
        output.append(f'public class {class_name} implements Serializable {{')
    if class_type is ClassType.MANAGER:
        output.append('@Service')
        output.append(f'public class {class_name} {{')
    if class_type is ClassType.REPOSITORY:
        output.append('@Repository')
        output.append(f'public interface {class_name} extends JpaRepository<{entity_name}, {get_type(SpectreType.UUID)}> {{')
    if class_type is ClassType.REST_CONTROLLER:
        output.append('@RestController')
        output.append('@RequestMapping("' + f'/api/{entity_name}")'.lower())
        output.append(f'public class {class_name} {{')

    output.append('')
    if should_have_logger:
        output.append(f'\tprivate final Logger log = LoggerFactory.getLogger({class_name}.class);')
        output.append('')
    return output

def get_imports(fields):
    output = set()
    def imprt(t):
        output.add(f'import {t};')
    for field in fields:
        if field.type is SpectreType.DATETIME:
            imprt('java.time.Instant')
    return list(output)

def get_import(name):
    return f'import {name};'

def get_entity_imports():
    output = []
    for c in [ 'Entity', 'GeneratedValue', 'GenerationType', 'Id' ]:
        output.append(f'javax.persistence.{c}')
    return output

def get_field(field: Field, config: Config, t: ClassType):
    output = []
    if t is ClassType.ENTITY:
        if config.java_options.get('spring_data', False) and field.type is SpectreType.UUID:
            output.extend(['\t@Id', '\t@GeneratedValue(strategy=GenerationType.AUTO)'])
    output.append(f'\tprivate {get_type(field.type, field.name)} {utils.to_camel(utils.to_pascal(field.name))};\n')
    return output

def create_constructor(name, arguments):
    signature = f'{create_signature(name=name, arguments=arguments)} {{'
    output = [ signature ]
    for arg_tuple in arguments:
        arg_name = utils.to_camel(arg_tuple[0])
        output.append(f'\t\tthis.{arg_name} = {arg_name};')
    output.extend([ '\t}', '' ] )
    return output

def create_signature(name, arguments=[], visibility='public', return_type=None):
    signature = [f'\t{visibility} ']
    if return_type:
        signature.append(f'{return_type} ')
    signature.append(f'{name}(')
    for index, val in enumerate(arguments):
        (t, var) = val
        signature.append(f'{t} {var}')
        if len(arguments) > index + 2:
            signature.append(',')
    signature.append(')')
    return ''.join(signature)

def create_function(visibility, return_type, name, arguments, body=None, annotation=None):
    output = []
    if annotation:
        output.append(f'\t{annotation}')
    signature = create_signature(visibility=visibility, return_type=return_type, arguments=arguments, name=name)
    if body:
        signature = "".join(signature) + ' {'
        output.append(signature) 
        [ output.append(f'\t\t{line}') for line in body ]
        output.append('\t}')
        return output
    else:
        signature += ';'
        output.append("".join(signature))
        return output

def get_getter_parameters(entity: Entity):
    """Get argument type and variable name for an entity using ID. For use in function signatures
    
    Arguments:
        entity {Entity} -- The entity for which to generate the getter arguments
    
    Returns:
        [tuple] -- Tuple holding the Type [0] and Variable Name [1]
    """
    return ( get_type(SpectreType.UUID), get_id_name(entity.name) )

def get_id_name(entity_name):
    return f'{utils.to_camel(entity_name)}Id'

def generate_model(entity: Entity, config: Config):
    imports = get_imports(entity.fields)
    imports.extend( [ 'java.io.Serializable' ] )
    if config.java_options.get('spring_data', False):
        for imprt in get_entity_imports():
            imports.append(imprt)
    output = get_class_stub(entity, imports, config, ClassType.ENTITY)
    for field in entity.fields:
        output.extend(get_field(field, config, ClassType.ENTITY))
    for field in entity.fields:
        output.extend(create_function(visibility='public', return_type=get_type(field.type), name=f'get{utils.to_pascal(field.name)}', arguments=[], body=[
            f'return this.{utils.to_camel_from_snake(field.name)};'
        ]))
    output.extend(
        create_function(
            visibility='public', return_type='String', name='toString', arguments=[],
            body=[
                'return "";'
            ]
        )
    )
    output.append('}')
    return output

def write_model(entity: Entity, config: Config):
    output = "\n".join(generate_model(entity, config))
    path = get_out_path(entity, config, ClassType.ENTITY)
    return utils.write_to_file(output, path, config)

def generate_method(method_name, method_map):
    try:
        return create_function(
            visibility=method_map.get('visibility', 'public'), 
            return_type=method_map['return_type'],
            name=method_map['name'], 
            arguments=method_map.get('arguments', []),
            body=method_map.get('body', None),
            annotation=method_map.get('annotation', None)
        )
    except KeyError as e:
        raise Exception(f'Java generator does not implement method {method_name}')

def generate_repository(entity: Entity, config: Config):
    entity_name = ClassType.ENTITY.get_name(entity.name)

    method_map = {
        'list': {
            'name': 'findAll',
            'return_type': f'List<{entity_name}>'
        },
        'get': {
            'name': 'findById',
            'return_type': f'Optional<{entity_name}>',
            'arguments': [ (get_type(SpectreType.UUID), get_id_name(entity_name)) ]
        },
        'create': {
            'name': 'save',
            'return_type': entity_name,
            'arguments': [ (entity_name, utils.to_camel(entity_name)) ]
        },
        'delete': {
            'name': 'delete',
            'return_type': 'void',
            'arguments': [ (entity_name, utils.to_camel(entity_name)) ]
        },
        'delete_by_id': {
            'name': 'deleteById',
            'return_type': 'void',
            'arguments': [ (get_type(SpectreType.UUID), get_id_name(entity_name)) ]
        },
    }
        
    imports = [f'{get_package(entity, config, ClassType.ENTITY)}.{entity_name}']
    imports.extend(BASE_IMPORTS)
    imports.extend([f'org.springframework.{c}' for c in ['data.jpa.repository.JpaRepository', 'stereotype.Repository']])
    output = get_class_stub(entity, imports, config, ClassType.REPOSITORY)
    for method in config.methods:
        if method is not 'update':
            output.extend(generate_method(method, method_map[method]))
    if 'delete' in config.methods:
        output.extend(generate_method('delete_by_id', method_map['delete_by_id']))
    output.append('}')
    return output

def write_repository(entity: Entity, config: Config):
    path = get_out_path(entity, config, ClassType.REPOSITORY)
    return utils.write_to_file('\n'.join(generate_repository(entity, config)), path, config)

#TODO: Finish method generation, add some kind of httpresponses etc to imports
def generate_controller(entity: Entity, config: Config):

    entity_type = ClassType.ENTITY.get_name(entity.name)
    entity_var = utils.to_camel(entity.name)
    manager_type = ClassType.MANAGER.get_name(entity.name)
    manager_var = utils.to_camel(ClassType.MANAGER.get_name(entity.name))
    id_parameters = get_getter_parameters(entity)

    #TODO: Add bodies
    method_map = {
        'list': {
            'name': 'list',
            'return_type': f'List<{entity_type}>',
            'body': [
                f'log.info("Request to retrieve all {entity_type}");',
                f'return {manager_var}.getAll();',
            ],
            'annotation': f'@GetMapping("")'
        },
        'get': {
            'name': 'get',
            'return_type': f'Optional<{entity_type}>',
            'arguments': [ (f'@PathVariable {id_parameters[0]}', id_parameters[1]) ],
            'body': [
                f'log.info("Request to retrieve {entity_type}: {{}}", {id_parameters[1]});',
                f'return {manager_var}.get({get_id_name(entity_type)});'
            ],
            'annotation': f'@GetMapping("/{{{id_parameters[1]}}}")'
        },
        'create': {
            'name': 'create',
            'return_type': entity_type,
            'arguments': [ (f'@RequestBody {entity_type}', entity_var) ],
            'body': [
                f'log.info("Request to create {entity_type}: {{}}", {entity_var}.toString());',
                f'return {manager_var}.save({entity_var});'
            ],
            'annotation': '@PostMapping'
        },
        'update': {
            'name': 'update',
            'return_type': entity_type,
            'arguments': [ (f'@RequestBody {entity_type}', entity_var) ],
            'body': [
                f'log.info("Request to update {entity_type}: {{}}", {entity_var}.toString());',
                f'return {manager_var}.save({entity_var});'
            ],
            'annotation': '@PutMapping'
        },
        'delete': {
            'name': 'delete',
            'return_type': 'void',
            'arguments': [ (f'@PathVariable {id_parameters[0]}', id_parameters[1]) ],
            'body': [ 
                f'log.info("Request to delete {entity_type} with ID {{}}", {id_parameters[1]});',
                f'{manager_var}.deleteById({get_id_name(entity_type)});',
            ],
            'annotation': f'@DeleteMapping("/{{{id_parameters[1]}}}")'
        }
    }

    imports = [f'{get_package(entity, config, ClassType.ENTITY)}.{ClassType.ENTITY.get_name(entity.name)}']
    imports.extend(BASE_IMPORTS)
    imports.append(f'{get_package(entity, config, ClassType.MANAGER)}.{ClassType.MANAGER.get_name(entity.name)}')
    imports.extend(
        [ 
            f'org.springframework.web.bind.annotation.{c}' for c in 
                [
                    'GetMapping',
                    'PathVariable',
                    'RequestBody',
                    'RequestMapping',
                    'RequestParam',
                    'RestController',
                    'PostMapping',
                    'PutMapping',
                    'DeleteMapping',
                ]
        ]
    )
    output = get_class_stub(entity, imports, config, ClassType.REST_CONTROLLER)
    output.append(f'\tprivate {manager_type} {manager_var};\n')
    output.extend(create_constructor(ClassType.REST_CONTROLLER.get_name(entity.name), [ (manager_type, manager_var) ] ))

    for method in config.methods:
        output.extend(generate_method(method, method_map[method]))
        output.append('')

    output.append('}')
    return output

def write_controller(entity: Entity, config: Config):
    path = get_out_path(entity, config, ClassType.REST_CONTROLLER)
    return utils.write_to_file('\n'.join(generate_controller(entity, config)), path, config)

def generate_manager(entity: Entity, config: Config):
    entity_name = ClassType.ENTITY.get_name(entity.name)
    imports = [f'{get_package(entity, config, ClassType.ENTITY)}.{entity_name}']
    imports.append('org.springframework.stereotype.Service')
    imports.extend(BASE_IMPORTS)
    imports.append(f'{get_package(entity, config, ClassType.REPOSITORY)}.{ClassType.REPOSITORY.get_name(entity.name)}')
    output = get_class_stub(entity, imports, config, ClassType.MANAGER)
    if config.java_options.get('spring_data', False):
        repo_pascal = ClassType.REPOSITORY.get_name(entity_name)
        repo_camel = utils.to_camel(repo_pascal)
        method_map = {
            'list': {
                'name': 'getAll',
                'return_type': f'List<{entity_name}>',
                'body': [f'return {repo_camel}.findAll();',],
            },
            'get': {
                'name': f'get',
                'return_type': f'Optional<{entity_name}>',
                'arguments': [get_getter_parameters(entity)],
                'body': [f'return {repo_camel}.findById({get_id_name(entity.name)});'],
            },
            'create': {
                'name': 'save',
                'return_type': entity_name,
                'arguments': [ (entity_name, utils.to_camel(entity_name)) ],
                'body': [f'return {repo_camel}.save({utils.to_camel(entity.name)});'],
            },
            'delete': {
                'name': 'delete',
                'return_type': 'void',
                'arguments': [ (entity_name, utils.to_camel(entity_name)) ],
                'body': [f'{repo_camel}.delete({utils.to_camel(entity.name)});'],
            },
            'delete_by_id': {
                'name': 'deleteById',
                'return_type': 'void',
                'arguments': [ (get_type(SpectreType.UUID), get_id_name(entity_name)) ],
                'body': [f'{repo_camel}.deleteById({get_id_name(entity_name)});'],
            },
        }
        output.append(f'\tprivate {repo_pascal} {repo_camel};\n')
        output.extend(create_constructor(ClassType.MANAGER.get_name(entity.name), [ (repo_pascal, repo_camel) ] ))

        for method in config.methods:
            #update and create is currently the same. dont want to generate twice. If different impl is needed, add update to method map and remove check
            if method is not 'update':
                output.extend(generate_method(method, method_map[method]))
                output.append('')
        if 'delete' in config.methods:
            output.extend(generate_method('delete_by_id', method_map['delete_by_id']))
    output.append('}')
    return output

def write_manager(entity: Entity, config: Config):
    path = get_out_path(entity, config, ClassType.MANAGER)
    return utils.write_to_file('\n'.join(generate_manager(entity, config)), path, config)

def write_classes(entity: Entity, config: Config):
    output = []
    output.append(write_model(entity, config))
    output.append(write_manager(entity, config))
    if config.java_options.get('spring_data', False):
        output.append(write_repository(entity, config))
    if config.java_options.get('spring_web', False):
        output.append(write_controller(entity, config))
    return output
