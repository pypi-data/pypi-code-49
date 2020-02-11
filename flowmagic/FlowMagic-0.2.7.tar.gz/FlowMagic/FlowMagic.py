import functools
import json, traceback, os, glob, logging as log
import pathlib
import zipfile
from timeit import default_timer as timer
from time import ctime

log.addLevelName(log.WARN, "\033[1;93m%s\033[1;0m" % log.getLevelName(log.WARN))
log.addLevelName(log.ERROR, "\033[1;91m%s\033[1;0m" % log.getLevelName(log.ERROR))
log.addLevelName(log.INFO, "\033[1;94m%s\033[1;0m" % log.getLevelName(log.INFO))
log.addLevelName(log.DEBUG, "\033[1;92m%s\033[1;0m" % log.getLevelName(log.DEBUG))
log.basicConfig(format='%(levelname)s - %(asctime)s - %(message)s', level=log.DEBUG)
# env = os.environ
# logging.info("All Environment Variables")
# logging.info(os.environ)
# try:
#	logging.info('Input Paths %s', json.loads(env['input_path']))
# except Exception as e:
#	logging.error("Input path not found")

FM_ALLOWED_EXTENSION = []
MAIN_FUNCTION = None
TRAIN_MAIN_FUNCTION = None
TRAIN_ENV_VAR = 'fmv1_train'


def setExtensions(*args):
    global FM_ALLOWED_EXTENSION
    for x in args:
        if x not in FM_ALLOWED_EXTENSION:
            FM_ALLOWED_EXTENSION.append(x)


def unsetExtensions(*args):
    global FM_ALLOWED_EXTENSION
    for x in args:
        FM_ALLOWED_EXTENSION.remove(x)


def allowed_file(filename):
    global FM_ALLOWED_EXTENSION
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in FM_ALLOWED_EXTENSION


def custom_input_path(path_regex):
    return glob.glob(path_regex)

'''
def base_input_path(path=None):
    try:
        return json.loads(os.environ.get('input_path'))

    except (Exception, IndexError) as e:
        if path != None:    return [path]
        return traceback.format_exc()


def base_output_path(path=None):
    try:
        output_path = json.loads(os.environ.get('output_path'))
        for x in output_path:
            os.makedirs(x, exist_ok=True)
        return output_path

    except (Exception, IndexError) as e:
        if path != None:    return [path]
        return traceback.format_exc()
'''

def getSystemValue(key=None):
    if key == None:    return os.environ
    value = os.environ.get(key)
    if value != None:    return value
    data = configJsonFile()
    for x in data['config_required']:
        # print(x)
        if str(x['name']) == key:
            return x['value']
    return None


def input_tree_path(obj, prevPath, k):
    if obj['type'] == 'dir':
        for x in obj['children']:
            # print(  os.path.join(prevPath,x['name']) )
            input_tree_path(x, os.path.join(prevPath, x['name']), k)
    elif obj['type'] == 'file':
        # print(  prevPath+ "."+obj['endsWith'] )
        k.append(prevPath + "." + obj['endsWith'])


def configJsonFile():
    configFileData = {}
    with open('config.json') as json_file:
        configFileData = json.load(json_file)
    return configFileData


def get_config_required(**kwargs):
    data = configJsonFile()
    for x in data['config_required']:
        if x['name'] == kwargs['name']:
            return x


def input_path(key=None):
    try:
        data = json.loads(os.environ.get('fmv1_inputs'))
        if key:
            os.makedirs(data[key], exist_ok=True)
            return data[key]
        else:
            for k in data:
                os.makedirs(data[k], exist_ok=True)

            return data

    except (Exception, IndexError) as e:
        print(e)
        if key != None:    return key
        return traceback.format_exc()


def output_path(key=None):
    try:
        data = json.loads(os.environ.get('fmv1_outputs'))
        if key:
            os.makedirs(data[key], exist_ok=True)
            return data[key]
        else:
            for k in data:
                os.makedirs(data[k], exist_ok=True)

            return data

    except (Exception, IndexError) as e:
        if key != None:    return key
        return traceback.format_exc()


def main(func):
    """
    Used as decorator; Annotates the function as main function that will be called when app starts
    :param func: the main function
    :return: func
    Example:
    .. code-block::
       @main
       def execute_app():
           pass
       FlowMagic.start()
    """
    global MAIN_FUNCTION
    assert MAIN_FUNCTION is None, 'More than one function is annotated as Main function'
    MAIN_FUNCTION = func
    return func


def start(*params,timeit=True):
    """
    Starts executing the function denoted as main function with :func:`MAIN_FUNCTION`
    :param timeit: Denotes whether the call should be timed or not
    :type timeit: bool

    Example:
    .. code-block::
       @main
       def execute_app():
           pass
       FlowMagic.start()
    """
    global MAIN_FUNCTION
    if timeit:
        log.info('Execution started at {}'.format(ctime()))
        start_time = timer()
    if callable(MAIN_FUNCTION) and (MAIN_FUNCTION is not None):
        MAIN_FUNCTION(*params)
    else:
        raise AssertionError('Main function is not callable or not set.')

    if timeit:
        end_time = timer()
        log.info('Execution finished at {}'.format(ctime()))
        log.info('Took {} seconds'.format(end_time-start_time))

def get_path_list(key):
    try:
        data = json.loads(os.environ.get('fmv1_inputs'))
        if type(data[key])==list:
            return data[key]
        else:
            log.error("Use input_path( "+key+" ) , found get_path_list("+key+")")
            return []
    except:
            return traceback.format_exc()


def get_training_config():
    training_env = os.getenv(TRAIN_ENV_VAR)
    try:
        parsed_training_env = json.loads(training_env)
        return parsed_training_env
    except TypeError as e:
        raise TypeError("Unable to load training configuration data") from e


def train_mode(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        training_env = os.getenv(TRAIN_ENV_VAR)
        if training_env is None:
            raise TypeError('This function can only be called inside training mode')
        try:
            parsed_training_env = get_training_config()
        except TypeError as e:
            raise TypeError("Unable to load training configuration data") from e
        return func(*args, **kwargs)
    return wrapper


def train_main(func):
    """
    Used as decorator; Annotates the function as main function that will be called when training starts
    :param func: the training main function
    :return: func
    Example:
    .. code-block::
       @main
       def execute_app():
           pass
       FlowMagic.start()
    """
    global TRAIN_MAIN_FUNCTION
    assert TRAIN_MAIN_FUNCTION is None, 'More than one function is annotated as Main function'
    TRAIN_MAIN_FUNCTION = func
    return func


def train(*params, timeit=True):
    """
    Starts executing the function denoted as train_main function with :func:`MAIN_FUNCTION`
    :param timeit: Denotes whether the call should be timed or not
    :type timeit: bool

    Example:
    .. code-block::
       @main
       def execute_app():
           pass
       FlowMagic.start()
    """
    global TRAIN_MAIN_FUNCTION
    if timeit:
        log.info('Training started at {}'.format(ctime()))
        start_time = timer()
    if callable(TRAIN_MAIN_FUNCTION) and (TRAIN_MAIN_FUNCTION is not None):
        TRAIN_MAIN_FUNCTION(*params)
    else:
        raise AssertionError('Training main function is not callable or not set.')

    if timeit:
        end_time = timer()
        log.info('Training finished at {}'.format(ctime()))
        log.info('Took {} seconds'.format(end_time-start_time))


if os.getenv(TRAIN_ENV_VAR):
    ## Training env setup
    training_conf = get_training_config()

    ## Setup train data
    log.info("Preparing training data")
    for train_data_path in training_conf.get('train_data', []):
        train_data_path = pathlib.Path(train_data_path)
        train_data_dir = os.path.dirname(train_data_path)
        if not train_data_path.exists():
            log.error('Training data zip {} does not exist, skipping...'.format(train_data_path))
            continue
        log.info('Extracting zip: {}'.format(train_data_path))
        with zipfile.ZipFile(train_data_path) as zip_file:
            if zip_file.testzip():
                log.error('Invalid zip file {}, skipping'.format(train_data_path))
                log.error('Bad files: {}'.format(zip_file.testzip()))
                continue
            zip_file.extractall(train_data_dir)
        log.info('Extraction complete.')
        # log.info('Removing zip {}'.format(train_data_path))
        # train_data_path.unlink()

    ## Setup test data
    log.info("Preparing test data")
    for test_data_path in training_conf.get('test_data', []):
        test_data_path = pathlib.Path(test_data_path)
        test_data_dir = os.path.dirname(test_data_path)
        if not test_data_path.exists():
            log.error('Test data zip {} does not exist, skipping...'.format(test_data_path))
            continue
        log.info('Extracting zip: {}'.format(test_data_path))
        with zipfile.ZipFile(test_data_path) as zip_file:
            if not zip_file.testzip():
                log.error('Invalid zip file {}, skipping'.format(test_data_path))
                continue
            zip_file.extractall(test_data_dir)
        log.info('Extraction complete.')
        # log.info('Removing zip {}'.format(test_data_path))
        # test_data_path.unlink()
else:
    log.info('Not in training mode')


@train_mode
def get_train_dirs():
    """Get dirs of training data"""
    train_config = get_training_config()
    return [pathlib.Path(os.path.dirname(path)) for path in train_config.get('train_data', [])]


@train_mode
def get_test_dirs():
    """Get dirs of testing data"""
    train_config = get_training_config()
    return [pathlib.Path(os.path.dirname(path)) for path in train_config.get('test_data', [])]


@train_mode
def write_metrics(metrics):
    """Write performance metrics of the new model"""
    if not isinstance(metrics, dict):
        raise ValueError('metrics must be a dictionary')
    train_config = get_training_config()
    metrics_file = train_config['metrics']

    with open(metrics_file, 'w') as f:
        f.write(json.dumps(metrics))


@train_mode
def get_previous_model():
    """Get path of the previous model on which to train on"""
    train_config = get_training_config()
    latest_model_path = train_config.get('latest_model', '')
    return pathlib.Path(latest_model_path)


@train_mode
def get_model_destination():
    """Get newly trained model destination"""
    train_config = get_training_config()
    model_destination = train_config.get('new_model', '/tmp/model')
    return pathlib.Path(model_destination)




