
import pytest
from spectre import creator
from spectre.model import SpectreType
from spectre.config import Config
import click
from click.testing import CliRunner

@pytest.fixture
def input_str():
    #Put these in the order of the prompts in the wizard
    enter = '\n'
    name = 'test_entity'
    description = 'Im describing my test entity'
    id_confirm = 'Y'
    field_name = 'foo'
    field_type = '1'
    field_desc = 'foo description'
    field_required = 'N'
    another_field = 'N'
    output = []

    for prompt in [name, description, id_confirm, field_name, field_type, field_desc, field_required, another_field ]: 
        output.append(prompt)
    #Enter after each input
    return enter.join(output)
    #return 'test_entity\nim describing my test entity\nY\nfoo_field\n1\nfield description\nN\nN\n'

@pytest.fixture
def config():
    output = Config()
    output.namespace = 'spectre.creator.entity'
    output.debug = True
    return output

def test_boolean_prompt():
    @click.command()
    def expect_true():
        result = creator.prompt_boolean('')
        if result:
            click.echo('SUCCESS')

    @click.command()
    def expect_false():
        result = creator.prompt_boolean('')
        if not result:
            click.echo('SUCCESS')

    runner = CliRunner()

    for response in [ 'Y', 'y' ]:
        result = runner.invoke(expect_true, input=response)
        assert 'SUCCESS' in result.stdout
        
    for response in [ 'N', 'n' ]:
        result = runner.invoke(expect_false, input=response)
        assert 'SUCCESS' in result.stdout

def test_type_prompt():
    @click.command()
    def prompt_type():
        t = creator.prompt_type()

    runner = CliRunner()
    result = runner.invoke(prompt_type, input='1')
    #Iterate over all enumeration values and assert they are prompted or not
    for t in SpectreType:
        if t is SpectreType.UNDEFINED:
            #UNDEFINED should not be a choice in the prompt, only used to indicate an error in conversions or imports
            assert not t.name in result.stdout
        else:
            #Make sure type is printed
            assert t.name in result.stdout

def test_wizard(input_str, config):
    @click.command()
    def create_entity():
        from spectre import creator
        result = creator.create_entity()
        assert len(result.fields) == 2
        assert result.name == 'test_entity'
        assert result.description == 'Im describing my test entity'
        assert result.fields[0].type is SpectreType.UUID 
        assert result.fields[0].name == 'id'
        assert result.fields[1].name == 'foo'
        assert result.fields[1].description == 'foo description'

    runner = CliRunner()
    result = runner.invoke(create_entity, input=input_str)
    #If one of asserts in create_entity() fails result will have an error
    assert result.exception == None