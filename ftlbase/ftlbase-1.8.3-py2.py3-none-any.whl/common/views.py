# -*- coding: utf-8 -*-

import itertools
import json
import re

from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import Submit, Button
from django import forms
from django.contrib import messages
from django.contrib.auth import logout, REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.template import Context, RequestContext
from django.urls import path, reverse, resolve
from django.utils.crypto import get_random_string
from django.utils.safestring import mark_safe
from render_block import render_block_to_string
from reversion.models import Version
from reversion_compare.mixins import CompareMixin

from common import empresa as emp
from common.logger import Log
from common.utils import has_permission, get_goto_url, ACAO_ADD, ACAO_EDIT, ACAO_DELETE, ACAO_VIEW, ACAO_REPORT, \
    ACAO_REPORT_EXPORT, ACAO_WORKFLOW_START, ACAO_WORKFLOW_TO_APPROVE, ACAO_WORKFLOW_APPROVE, ACAO_WORKFLOW_RATIFY, \
    ACAO_WORKFLOW_READONLY, ACAO_EMAIL, ACAO_EXEC
from goflow.apptools.forms import ProcessesInstanceTable
from goflow.runtime.models import InvalidWorkflowStatus, ProcessInstance, WorkItem, WorkItemManager
from goflow.workflow.models import Process
from .form import PeriodoForm
from .reports import montaURLjasperReport

log = Log('commom.views')


# Create your views here.


class InvalidFormConfiguration(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


def get_form(form):
    if form and isinstance(form, str):
        # Se form_class existe então deve ser no formado <módulo>.<arquivo>.FormClass
        #   e faz seu carregamento manualmente abaixo
        p = form.split('.')
        if len(p) == 3:
            the_module = __import__(p[0] + '.' + p[1])
            the_class = getattr(the_module, p[1])
            the_form = getattr(the_class, p[2])
            return the_form
        else:
            raise InvalidFormConfiguration('InvalidFormConfiguration: form=' + form)
    return form


def configuraButtonsNoForm(form, acao, goto, *args, **kwargs):
    """
    Configura botões padrões de save ou delete e cancel no final do form
    """
    url = get_goto_url(form.instance, goto)
    linkCancel = "window.location.href='#%s'" % url
    linkWorkflow = "ftltabs.trigger('closeTab', 'Workflow', '#%s');" % url
    css_class = 'col-md-11 text-right buttons-do-form'
    if acao in (ACAO_WORKFLOW_START, ACAO_WORKFLOW_TO_APPROVE, ACAO_WORKFLOW_APPROVE,
                ACAO_WORKFLOW_RATIFY, ACAO_WORKFLOW_READONLY):
        cancel = Button('cancel', 'Cancelar', css_class="btn-cancel btn-sm", onclick=linkWorkflow)
    else:
        cancel = Button('cancel', 'Cancelar', css_class="btn-cancel btn-sm", onclick=linkCancel)

    workitem = kwargs.get('workitem', None)
    onclick = kwargs.get('onclick', None)

    # onde = mark_safe("<i class='fa fa-map-marker' style='font-size:18px;color:#09568d;' data-toggle='tooltip' " +
    #                  "title='Onde estou?'>Onde estou?</i>")

    # form.helper['save'].update_attributes(css_class="hello")
    if acao in (ACAO_ADD, ACAO_EDIT, ACAO_WORKFLOW_START, ACAO_EXEC):
        form.helper.layout.extend([
            FormActions(
                Submit('save', 'Salvar', css_class="btn-primary btn-sm", onclick=onclick),
                cancel,
                css_class=css_class)
        ])
    elif acao == ACAO_DELETE:
        form.helper.layout.extend([
            FormActions(
                Submit('DELETE', 'Confirmar exclusão do registro', css_class="btn-danger btn-sm", aria_hidden="true"),
                cancel,
                css_class=css_class)
        ])
    elif acao == ACAO_REPORT:
        form.helper.layout.extend([
            FormActions(
                Submit('save', 'Consultar', css_class="btn-primary btn-sm"),
                Button('cancel', 'Cancelar', css_class="btn-cancel btn-sm", onclick=linkCancel),
                css_class='col-md-11 text-right')
        ])
    elif acao == ACAO_REPORT_EXPORT:
        form.helper.layout.extend([
            FormActions(
                Submit('save', 'Consultar', css_class="btn-primary btn-sm"),
                Submit('save', 'Exportar', css_class="btn-success btn-sm"),
                cancel,
                css_class=css_class)
        ])
    elif acao == ACAO_WORKFLOW_TO_APPROVE:
        fields = [Submit('save', i.condition, css_class="btn-danger btn-sm") for i in
                  workitem.activity.transition_inputs.all()]
        form.helper.layout.extend([
            FormActions(
                Submit('save', 'Salvar', css_class="btn-primary btn-sm"),
                # Submit('save', 'Salvar e Continuar Editando', css_class="btn-primary btn-sm"),
                *fields,
                cancel,
                css_class=css_class)
        ])
    elif acao == ACAO_WORKFLOW_APPROVE:
        form.helper.layout.extend([
            FormActions(
                Submit('save', 'Aprovar', css_class="btn-primary btn-sm"),
                Submit('save', 'Rejeitar', css_class="btn-danger btn-sm"),
                cancel,
                css_class=css_class)
        ])
    elif acao == ACAO_WORKFLOW_RATIFY:
        form.helper.layout.extend([
            FormActions(
                Submit('save', 'Salvar e Continuar Editando', css_class="btn-primary btn-sm"),
                Submit('save', 'Homologar e Concluir', css_class="btn-danger btn-sm"),
                cancel,
                css_class=css_class)
        ])
    else:
        form.helper.layout.extend([FormActions(cancel, css_class='col-md-11 text-right')])
    return form


def commonRender(request, template_name, dictionary):
    """
    Executa o render do template normal para html ou se a requisição é Ajax, então executa separadamente cada parte para JSON
    """
    dic = dictionary.copy()
    goto = dic.get('goto', 'index')
    form = dic.get('form', None)
    try:
        url = get_goto_url(form.instance if form else None, goto)
        dic.update({'goto': url})
        linkCancel = "window.location.href='#%s'" % url
    except Exception as e:  # NOQA
        linkCancel = "window.location.href='#%s'" % goto

    # try:
    #     url = reverse(goto)
    #     dic.update({'goto': url})
    #     linkCancel = "window.location.href='#%s'" % url
    # except Exception as e:  # NOQA
    #     linkCancel = "window.location.href='#%s'" % goto

    ctx = None

    if request is not None:
        ctx = RequestContext(request, dic)
        ctx.update({'ajax': request.is_ajax()})
    else:
        ctx = Context(dic)

    ctx.update({'linkCancel': linkCancel})
    # ctx = {k: v for d in ctx for k, v in d.items() if d}
    ctx = ctx.flatten()

    if dic.get('acao', ACAO_VIEW) == ACAO_EMAIL:
        html = render_block_to_string(template_name, "content", context=ctx)
        return HttpResponse(html)

    if request.is_ajax():
        title = render_block_to_string(template_name, "title_html", context=ctx)
        html = render_block_to_string(template_name, "content", context=ctx)
        html = re.sub('<link(.*?)/>', '', html)
        html = re.sub('<script type="text/javascript" src=(.*?)</script>', '', html)

        script = render_block_to_string(template_name, "extrajavascript", context=ctx)

        return HttpResponse(
            json.dumps({'title': title, 'html': html, 'extrajavascript': script, 'goto': goto,
                        'form_errors': dic.get('form_errors'),
                        'formset_errors': dic.get('formset_errors')}),
            content_type='application/json'
        )

    return render(request, template_name, ctx)


def commonProcess(form, formset, request, acao, goto, process_name=None, instance_label=None, workitem=None,
                  extrajavascript=''):
    # print('commonProcess')
    regs = 10
    if acao in (ACAO_ADD, ACAO_EDIT, ACAO_WORKFLOW_START, ACAO_WORKFLOW_TO_APPROVE,
                ACAO_WORKFLOW_APPROVE, ACAO_WORKFLOW_RATIFY):
        # from django.db import transaction
        obj = None
        # Não faz o try pois as exceptions serão tratadas na view, para que os erros sejam mostrados
        with transaction.atomic():
            obj = form.save()
            if formset:
                if isinstance(formset, forms.formsets.BaseFormSet):
                    formset.save()
                else:
                    # Senão, é list de formsets
                    for d in formset:
                        if d['formset']:
                            d['formset'].save()
            # Ainda dentro da transaction.atomic, faz o tratamento do start do processo e
            if acao in (ACAO_WORKFLOW_START) and obj:
                # Start Workflow
                # Prioridade é tratada no start
                workitem = ProcessInstance.objects.start(process_name, request, obj, instance_label)
            elif workitem:
                workitem.process(request)

    elif acao == ACAO_DELETE:
        try:
            form.instance.delete()
        except Exception as e:
            if hasattr(e, 'protected_objects') and e.protected_objects:
                itens = []
                for item in e.protected_objects[:regs]:
                    itens.append({'msg': '{}: {}'.format(item._meta.model._meta.verbose_name.title(), item.__str__())})
                return JsonResponse({'msg': [{'type': 'danger',
                                              'msg': 'Desculpe, mas há {} registro(s) dependente(s) desse {}:'.format(
                                                  len(e.protected_objects),
                                                  form._meta.model._meta.verbose_name.title()),
                                              'itens': itens,
                                              'total': len(e.protected_objects) - regs}, ],
                                     'goto': request.get_full_path()})
            else:
                return JsonResponse({'msg': [{'type': 'danger',
                                              'msg': 'Desculpe, mas houve erro na exclusão {}:'.format(e)}],
                                     'goto': request.get_full_path()})

    return JsonResponse({'goto': goto,
                         'extrajavascript': extrajavascript if request.POST else None}) if request.is_ajax() else redirect(
        goto)


def commom_detail_handler(clsMaster, formInlineDetail, can_delete=True, isTree=False):
    # fs = []
    detail = []

    if formInlineDetail:
        if isinstance(formInlineDetail, list):
            for f in formInlineDetail:
                detail.append({'prefix': formInlineDetail.index(f), 'clsDetail': f._meta.model, 'formInlineDetail': f})
        else:
            if hasattr(formInlineDetail, '_meta'):
                clsDetail = formInlineDetail._meta.model
            elif hasattr(formInlineDetail, 'Meta'):
                clsDetail = formInlineDetail.Meta.model
            else:
                clsDetail = formInlineDetail.form.Meta.model
            detail = [{'prefix': '', 'clsDetail': clsDetail, 'formInlineDetail': formInlineDetail}]

        if isinstance(isTree, list):
            for i, d in enumerate(detail):
                d['isTree'] = isTree[i]
        else:
            detail[0]['isTree'] = isTree

        for d in detail:
            d['tituloDetail'] = d['clsDetail']._meta.verbose_name.title()
            # forms = django.forms
            d['Detail'] = (
                d['clsDetail'] if d['isTree'] else forms.inlineformset_factory(parent_model=clsMaster,
                                                                               model=d['clsDetail'],
                                                                               form=d['formInlineDetail'],
                                                                               extra=0, min_num=0,
                                                                               can_delete=can_delete)) if issubclass(
                d['formInlineDetail'], forms.BaseModelForm) else d['formInlineDetail']
    # return fs, detail
    return detail


@login_required
def commonCadastro(request, acao=ACAO_VIEW, formModel=None, **kwargs):
    """
    Cadastro genérico.
        Parâmetros são:
            pk: chave principal
            acao: common_forms.ACAO_ADD, common_forms.ACAO_EDIT ou common_forms.ACAO_DELETE
            formModel: form de cadastro do Model
            goto: nome da url para onde será redirecionado após submmit
            template_name: nome do template a ser usado, default o template padrão
    """
    goto = kwargs.get('goto', 'index')
    formInlineDetail = get_form(kwargs.get('formInlineDetail', None))
    pk = kwargs.get('pk', None)
    template_name = kwargs.get('template_name', 'cadastroPadrao.html')
    # can_add = kwargs.get('can_add', True)
    can_edit = kwargs.get('can_edit', True)
    if not can_edit and acao == ACAO_EDIT:
        acao = ACAO_VIEW
    can_delete = kwargs.get('can_delete', True)
    configuraButtons = kwargs.get('configuraButtons', True)
    extrajavascript = kwargs.get('extrajavascript', '')
    permissions = kwargs.get('permissions', None)
    isTree = kwargs.get('isTree', False)
    idTree = kwargs.get('idTree', 'masterTreeManager')
    acaoURL = kwargs.get('acaoURL', None)
    dataUrl = kwargs.get('dataUrl', None)
    updateParent = kwargs.get('updateParent', None)
    dictionary = kwargs.get('dictionary', {})
    workitem = kwargs.get('workitem', None)
    instance_label = kwargs.get('instance_label', None)
    disableMe = dictionary.get('disableMe', False)

    formM = get_form(formModel)

    clsModel = formM._meta.model
    titulo = clsModel._meta.verbose_name.title()

    has_permission(request=request, model=clsModel, acao=acao, permissions=permissions)
    # commonPermission(request=request, clsModel=clsModel, acao=acao, permissions=permissions)

    if pk and acao not in (ACAO_ADD, ACAO_REPORT, ACAO_WORKFLOW_START):
        mymodel = get_object_or_404(clsModel, pk=pk)
        titulo = '{0} - {1}'.format(titulo, mymodel.__str__())
    else:
        mymodel = clsModel()

    form_errors = None
    formset_errors = None

    pref = 'nested-' + clsModel._meta.label_lower.replace('.', '-')

    dataTreeURL = dataUrl % pk if dataUrl and pk else ""

    detail = commom_detail_handler(clsMaster=clsModel, formInlineDetail=formInlineDetail, can_delete=can_delete,
                                   isTree=isTree)

    script = formM.extrajavascript()
    extrajavascript = "\n".join([extrajavascript, script])

    if workitem:
        if (acao == ACAO_WORKFLOW_RATIFY) and (request.method == 'POST'):
            # Força close do Tab e ignora extrajavascript configurado
            script = 'ftltabs.trigger("closeTab", "Workflow");'
        else:
            # Javascript para buscar se há formset com classe disableMe e faz o disable (inclusão de andamento)
            script = 'configuraCampos("%s" == "True", "%s" == "True");' % (disableMe, (
                    workitem.status == WorkItem.STATUS_CONCLUDED and acao != ACAO_WORKFLOW_RATIFY))
        extrajavascript = "\n".join([extrajavascript, script])

        ok = (workitem.instance.status != ProcessInstance.STATUS_CONCLUDED)
        # # Se status é concluído então não pode inserir nem deletar
        # can_add &= ok
    else:
        # Prevenção contra adulteração:
        #   para evitar que alguém use uma tela onde não tem permissão de gravação e force um post
        ok = acao not in [ACAO_VIEW, ACAO_EMAIL, ACAO_REPORT, ACAO_REPORT_EXPORT, ]
        if acao == ACAO_VIEW:
            extrajavascript = "\n".join([extrajavascript,
                                         'configuraCampos("%s" == "True", "%s" == "True");' % (disableMe, disableMe)])

    if request.method == 'POST' and ok:
        form = formM(request.POST, request.FILES, instance=mymodel, acao=acao, prefix="main")
        for d in detail:
            d['formset'] = None if d['isTree'] else d['Detail'](request.POST, request.FILES, instance=mymodel,
                                                                prefix=pref + d['prefix'])
        # Cria campo detail no form master para posterior validação do form e dos formset em conjunto quando há dependência.
        # Exemplo, a soma dos percentuais de participação dos proprietários num contrato de adm deve ser 100%
        form.detail = detail
        # como form_tag é variável de classe, tem que forçar para ter <form na geração do html
        form.helper.form_tag = True

        if all(True if d['isTree'] else d['formset'].is_valid() for d in detail) and form.is_valid():
            if acao == ACAO_WORKFLOW_START:
                process_name = form.process_name()
                Process.objects.check_can_start(process_name=process_name, user=request.user)
                log.debug('commonCadastro: ACAO_WORKFLOW_START: instance_label:', instance_label)
            else:
                process_name = None

            return commonProcess(form=form, formset=detail, request=request, acao=acao,
                                 goto=get_goto_url(form.instance, goto),
                                 process_name=process_name, instance_label=instance_label,
                                 workitem=workitem, extrajavascript=extrajavascript)
            # return commonProcess(form=form, formset=detail, request=request, acao=acao, goto=reverse(goto),
            #                      process_name=process_name, instance_label=instance_label,
            #                      workitem=workitem, extrajavascript=extrajavascript)
        else:
            form_errors = form.errors
            errors = []

            for d in detail:
                errors.append([] if d['isTree'] else d['formset'].errors)
            # Flattening errors, transforma várias listas de erros em um única lista
            formset_errors = list(itertools.chain(*errors))
            # context['formset_errors'] = formset_errors
            messages.error(request, mark_safe('Erro no processamento'), fail_silently=True)
    else:
        form = formM(instance=mymodel, prefix="main", acao=acao)
        if acao in [ACAO_VIEW, ACAO_EXEC]:
            for i in form.fields:
                form.fields[i].disabled = True
        for d in detail:
            d['formset'] = d['formInlineDetail'] if d['isTree'] else d['Detail'](instance=mymodel,
                                                                                 prefix=pref + d['prefix'])
    if configuraButtons:
        configuraButtonsNoForm(form, acao, goto, workitem)

    # monta modal do help do workflow
    # print(idTree, pk, acao, acaoURL)
    if idTree and pk and acao and acaoURL and updateParent:
        # extrajavascriptTree = ("""ftl_form_modal = riot.mount('div#ftl-form-modal', 'ftl-form-modal', {
        #   'modal': {isvisible: false, contextmenu: false, idtree: '%s'},
        #   'data': {pk: %s, action: %s, acaoURL: '%s', updateParent: '%s', modaltitle: '%s'},
        # })
        # """ % (idTree, pk, acao, acaoURL, reverse(updateParent), mymodel.__str__()))
        extrajavascriptTree = ("""$('#{0}').attr('data-url','{1}');
        ftl_form_modal = riot.mount('div#ftl-form-modal', 'ftl-form-modal', {{
          'modal': {{isvisible: false, contextmenu: false, idtree: '{0}'}},
          'data': {{pk: {2}, action: {3}, acaoURL: '{4}', updateParent: '{5}', modaltitle: '{6}'}},
        }});
        """.format(idTree, dataTreeURL, pk, acao, acaoURL, reverse(updateParent), mymodel.__str__()))
        extrajavascript = "\n".join([extrajavascript, extrajavascriptTree])
    # else:
    #     extrajavascriptTree = None

    dictionary.update(
        {'empresa': emp, 'goto': goto, 'title': titulo, "form": form, 'form_errors': form_errors, "detail": detail,
         # "can_add": can_add, "delecao": (acao == ACAO_DELETE),
         'formset_errors': formset_errors, "idTree": idTree, "pk": pk, "isTree": True, "acaoURL": acaoURL, "acao": acao,
         "dataUrl": dataTreeURL, "updateParent": reverse(updateParent) if updateParent else None,
         "extrajavascript": extrajavascript})  # if extrajavascript else extrajavascriptTree})

    # template_name = 'cadastroMasterDetail.html'

    return commonRender(request, template_name, dictionary)


@login_required
def commonListaTable(request, model=None, queryset=None, goto='index', template_name="table.html", tableScript=None,
                     referencia=None, dictionary=None, permissions=None):
    """
    Lista padrão no formato tabela.
        Parâmetros são:
            model: form de cadastro do Model Master
            queryset: queryset para seleção dos registros a serem listados. Pode ser function para tratar request
            template_name: nome do template a ser usado, default o template padrão de tabela
            tableScript: script a ser injetado dinamicamente no html para tratamento da tabela (totalização de campos, etc.)
    """

    if queryset is not None:
        if callable(queryset):
            objetos = model(queryset(request))
        else:
            objetos = model(queryset)
    else:
        if model:
            objetos = model()
        else:
            return "z"
    # objetos = model.queryset.exclude(codtaxa__gte =10000)
    # objetos = objetos.exclude(codtaxa__gte=10000).order_by('codtaxa')
    clsTable = model.opts.model
    titulo = clsTable._meta.verbose_name.title()
    # token =  Token.objects.get(user=request.user)

    has_permission(request=request, model=clsTable, acao=ACAO_VIEW, permissions=permissions)
    # commonPermission(request=request, clsModel=clsTable, acao=ACAO_VIEW, permissions=permissions)

    dic = dictionary

    if dic is None:
        dic = {}

    extrajavascript = mark_safe(model.extrajavascript())

    dic.update({'empresa': emp, 'goto': goto, 'objetos': objetos, 'title': titulo, 'tableScript': tableScript,
                'referencia': referencia, "extrajavascript": extrajavascript})

    # update id of datatables to random name
    model.opts.id = get_random_string(length=10)

    return commonRender(request, template_name, dic)


def commonRelatorioTable(model=None, queryset=None, template_name="table.html", tableScript=None, extrajavascript='',
                         dictionary=None):
    """
    Lista padrão no formato tabela.
        Parâmetros são:
            model: form de cadastro do Model Master
            queryset: queryset para seleção dos registros a serem listados
            template_name: nome do template a ser usado, default o template padrão de tabela
            tableScript: script a ser injetado dinamicamente no html para tratamento da tabela (totalização de campos, etc.)
    """
    if queryset:
        objetos = model(queryset)
    else:
        if model:
            objetos = model()
        else:
            return "z"

    clsTable = model.opts.model
    titulo = clsTable._meta.verbose_name.title()

    dic = dictionary

    if dic is None:
        dic = {}

    dic.update({'empresa': emp, 'objetos': objetos, 'title': titulo, 'tableScript': tableScript,
                'extrajavascript': extrajavascript})

    return commonRender(request=None, template_name=template_name, dictionary=dic)


@login_required
def common_workflow_table_process(request, table=ProcessesInstanceTable, goto='index', my_work=False, news=False,
                                  pending=False, subject=None, add=True, disableMe=False):
    query = ProcessInstance.objects.all_safe(user=request.user, my_work=my_work, news=news, pending=pending,
                                             subject=subject)
    # if request.resolver_match.url_name != 'workflow':
    #     href = request.resolver_match.url_name.split('_all')[0]
    #
    # else:
    #     href = request.resolver_match.url_name
    # href = href+'/add'
    # href = 'add/'
    # self.std_button_create_href = getattr(options, 'std_button_create_href', 'add/')
    if add:
        table.opts.std_button_create = {'text': 'Incluir novo registro', 'icon': 'fa fa-plus-square fa-fw',
                                        'href': table.opts.std_button_create_href,
                                        "className": 'btn btn-primary btn-sm', }
    else:
        table.opts.std_button_create = False
    # ProcessesInstanceTable.opts.std_button_create = {'text': 'Incluir novo atendimento', 'icon': 'fa fa-plus-square fa-fw',
    #                                               'href': href, "className": 'btn btn-primary btn-sm', }

    if subject and table == ProcessesInstanceTable:
        table.base_columns[0].visible = False  # Column pk is hidden if filtering by subject
        table.base_columns[1].visible = False  # Column Processo is hidden if filtering by subject
    else:
        table.base_columns[0].visible = True
        table.base_columns[1].visible = True

    # Tratamento para workflow ou itens onde tem formset que pode ser adicionado, mas os anteriores ficam desabilitado
    # para não ter alteração.
    dictionary = {'disableMe': disableMe}

    return commonListaTable(request, model=table, queryset=query, goto=goto, dictionary=dictionary)


@login_required
def common_history_workitems_table(request, pk, model=None, queryset=None, goto='index', template_name="table.html",
                                   tableScript=None, referencia=None, extrajavascript='', dictionary=None,
                                   permissions=None):
    workitems = WorkItemManager.get_process_workitems(pk, user=request.user)
    return commonListaTable(request, model=model, queryset=workitems, goto=goto, template_name=template_name,
                            tableScript=tableScript, referencia=referencia, dictionary=dictionary,
                            permissions=permissions)
    # extrajavascript=extrajavascript, dictionary=dictionary, permissions=permissions)


@login_required
def common_workflow(request, id=None, goto='workflow_pending', dictionary=None):
    """
    activates and redirect to the application.

    :param request:
    :param id: workitem id
    :param goto: 'workflow_pending' ou 'workflows_all' se workflow concluído
    :param dictionary: parâmetros extras, ex.: {'disableMe': True}
    :return: rendered html
    """

    def _app_response(request, workitem, goto, dictionary):
        """
        Verifica se há subworkflow e executa, senão faz o redirect para a configuração do WF

        :param workitem:
        :return:
        """

        # id = workitem.id
        def _execute_activity(workitem, activity, dictionary):
            # standard activity
            url = activity.application.get_app_url(workitem)
            func, args, kwargs = resolve(url)
            # params has to be an dict ex.: { 'form_class': 'imovel.form.ContratoLocForm', 'goto': 'contratoLoc'}
            params = activity.app_param
            # params values defined in activity override those defined in urls.py
            if params:
                try:
                    params = eval('{' + params.lstrip('{').rstrip('}') + '}')
                    # Carrega o form dos parâmetros form_class e formInlineDetail dinamicamente e faz a substituição
                    forms = ['form_class', 'formInlineDetail']
                    for f in forms:
                        if f in params:
                            # Se form_class existe então deve ser no formado <módulo>.<arquivo>.FormClass
                            #   e faz seu carregamento manualmente abaixo
                            p = params.get(f, None)
                            try:
                                params.update({f: get_form(form=p)})
                            except:
                                pass
                except Exception as v:
                    pass
                kwargs.update({'dictionary': dictionary})
                kwargs.update(params)

            # Marretada para evitar que o param acao seja injected em kwargs e dê problema no sendmail
            # Opção seria incluir acao no sendmail
            if activity.application.url not in ['apptools/sendmail', ]:
                kwargs.update({'workitem': workitem,
                               'acao': ACAO_WORKFLOW_READONLY if workitem.instance.status == ProcessInstance.STATUS_CONCLUDED
                               else ACAO_WORKFLOW_APPROVE if activity.approve
                               else ACAO_WORKFLOW_RATIFY if activity.ratify
                               else dictionary.get('acao', ACAO_EDIT)})
            ret = func(request, **kwargs)
            return ret

        dic = dictionary.copy()

        if dic is None:
            dic = {}

        dic.update({'empresa': emp})

        activity = workitem.activity

        if workitem.instance.status != ProcessInstance.STATUS_CONCLUDED:
            if request.method == 'POST':
                workitem.activate(request)

            if not activity.process.enabled:
                extrajavascript = 'riot.mount("ftl-error-message", {messages: [{type: \'error\', msg: "Processo %s está desabilitado."}, ]});' % activity.process.title
                dic.update({'extrajavascript': extrajavascript})
                return commonRender(request, 'error.html', dic)

            if activity.kind == 'subflow':
                # subflow
                sub_workitem = workitem.start_subflow(request)
                return _app_response(request, sub_workitem, goto, dic)

        # no application: default_app
        if not activity.application:
            url = 'default_app'

            # url = '../../../default_app'
            # return HttpResponseRedirect('%s/%d/' % (url, id))
            return HttpResponseRedirect('/#' + reverse(url, args=[id]))

        if activity.kind == 'dummy':
            return _execute_activity(workitem, activity, dic)

        if activity.kind == 'standard':
            ret = _execute_activity(workitem, activity, dic)
            # Se não retornou nada (ex. sendmail(), então verifica se é autofinish para executar complete do workitem
            if ret is None and \
                    workitem.activity.autofinish and workitem.instance.status != ProcessInstance.STATUS_CONCLUDED:
                # log.debug('common_workflow autofinish: complete')
                workitem.complete(request)
                dic.update({'goto': goto})
                return commonRender(request, 'base.html', dic)
            return ret

        extrajavascript = 'riot.mount("ftl-error-message", {messages: [{type: \'error\', msg: "Erro no Workflow, não há aplicação configurada em %s."}, ]});' % activity.process.title
        dic.update({'extrajavascript': extrajavascript, 'goto': resolve(request.path).view_name})
        return commonRender(request, 'error.html', dic)
        # return HttpResponse('completion page.')

    dic = dictionary.copy()
    try:
        id = int(id)
        workitem = WorkItem.objects.get_safe(id=id, user=request.user)
    except Exception as v:
        if type(v) == InvalidWorkflowStatus:
            workitem = v.workitem
        else:
            extrajavascript = 'riot.mount("ftl-error-message", {messages: [{type: \'error\', msg: "%s"}, ]});' % str(v)
            dic.update({'extrajavascript': extrajavascript,
                        'goto': resolve(request.path).view_name})  # OR resolve(request.path).url_name ?????
            return commonRender(request, 'error.html', dic)

    return _app_response(request, workitem, goto, dic)


@login_required
def common_workflow_execute(request, **kwargs):
    """
    activates and redirect to the application.

    :param request:
    :param kwargs:
        acao: Ação a ser executada
        form_class: Form a ser usado
        formInlineDetail: Inline detail a ser usado (optional)
        goto: 'workflow_pending' ou 'workflows_all' se workflow concluído
        dictionary: parâmetros extras, ex.: {'disableMe': True}
        extrajavascript: javascript a ser anexado ao form
        workitem: workitem ativo
    :return:
    """
    workitem = kwargs.get('workitem', None)

    acao = kwargs.get('acao', ACAO_EDIT)
    formModel = kwargs.get('form_class')
    formInlineDetail = kwargs.get('formInlineDetail')
    goto = kwargs.get('goto',
                      'workflow_all' if workitem and workitem.status == WorkItem.STATUS_CONCLUDED else 'workflow_pending')
    dictionary = kwargs.get('dictionary', {})
    # submit_name é o nome do form que está sendo gravado
    dictionary.update({'submit_name': request.POST.get('save', '')})
    extrajavascript = kwargs.get('extrajavascript', '')

    pk = workitem.instance.wfobject().pk if workitem else None

    return commonCadastro(request, acao, formModel, goto=goto, formInlineDetail=formInlineDetail, pk=pk,
                          dictionary=dictionary, workitem=workitem, extrajavascript=extrajavascript)


@login_required
def common_workflow_flag_myworks(request, **kwargs):
    """
    list all my workitems

    parameters:
    template: 'Atendimento'
    """
    template_name = kwargs.get('template_name', 'workflow_myworks.html')
    workitems = WorkItemManager.list_safe(user=request.user, roles=False, withoutrole=False, noauto=False)
    dictionary = kwargs.get('dictionary', {})
    dictionary.update({'workitems': workitems})

    return commonRender(request, template_name, dictionary)


@login_required
def common_workflow_flag_news(request, **kwargs):
    """
    list all my workitems

    parameters:
    template: 'Atendimento'
    """
    template_name = kwargs.get('template_name', 'workflow_news.html')
    workitems = WorkItemManager.list_safe(user=None, roles=True, status=[WorkItem.STATUS_INACTIVE, ],
                                          withoutrole=True, noauto=False)
    dictionary = kwargs.get('dictionary', {})
    dictionary.update({'workitems': workitems})

    return commonRender(request, template_name, dictionary)


@login_required
def common_workflow_graph(request, pk, template='graph.html'):
    """Gera gráfico do workflow
    pk: process id
    template: template
    """
    instance = ProcessInstance.objects.get(pk=pk)
    mark_pending = set()
    mark_completed = set()
    mark_problem = set()
    for a in instance.workitems.all():
        if a.status in [WorkItem.STATUS_INACTIVE, WorkItem.STATUS_PENDING]:
            mark_pending.add(a.activity.pk)
        elif a.status in [WorkItem.STATUS_CONCLUDED]:
            mark_completed.add(a.activity.pk)
        else:
            mark_problem.add(a.activity.pk)
    args = {'pending': list(mark_pending), 'completed': list(mark_completed), 'problem': list(mark_problem)}
    process = instance.process
    context = {
        'process': process,
        'args': args,
    }
    return commonRender(request, template, context)


@login_required
def common_process_graph(request, title, template='graph.html'):
    """Gera gráfico do process
    pk: process id or title
    template: template
    """
    try:
        process = Process.objects.get(title=title)
    except Exception as v:
        process = Process.objects.get(id=title)
    mark_pending = set()
    mark_completed = set()
    mark_problem = set()
    args = {'pending': list(mark_pending), 'completed': list(mark_completed), 'problem': list(mark_problem)}
    context = {
        'process': process,
        'args': args,
    }
    return commonRender(request, template, context)


# Autenticação
# @csrf_protect
def loginX(request, template_name='login.html',
           redirect_field_name=REDIRECT_FIELD_NAME,
           authentication_form=AuthenticationForm,
           extra_context=None, redirect_authenticated_user=False):
    return LoginView.as_view(
        template_name=template_name,
        redirect_field_name=redirect_field_name,
        form_class=authentication_form,
        extra_context=extra_context,
        redirect_authenticated_user=redirect_authenticated_user,
    )(request)


def logoutX(request):
    logout(request)
    return HttpResponseRedirect(reverse('loginX'))


def include_CRUD(name, table=None, form=None, *args, **kwargs):
    add = kwargs.get('add', True)
    edit = kwargs.get('edit', True)

    extrajavascript = kwargs.get('extrajavascript', '')
    goto = kwargs.get('goto', name)

    configuraButtons = kwargs.get('configuraButtons', True)
    disableMe = kwargs.get('disableMe', True)

    # Table queryset
    table_queryset = kwargs.get('table_queryset', None)

    # Tree
    isTree = kwargs.get('isTree', False)
    idTree = kwargs.get('idTree', 'masterTreeManager')
    acaoURL = kwargs.get('acaoURL', None)
    dataUrl = kwargs.get('dataUrl', None)
    permissions = kwargs.get('permissions', None)
    updateParent = kwargs.get('updateParent', None)

    dic = {'formModel': form, 'goto': goto, 'extrajavascript': extrajavascript,
           'configuraButtons': configuraButtons, 'disableMe': disableMe,
           'isTree': isTree, 'idTree': idTree, 'acaoURL': acaoURL, 'dataUrl': dataUrl, 'updateParent': updateParent}

    if permissions:
        dic.update({'permissions': permissions})

    dic_add = dic.copy()
    dic_add.update({'acao': ACAO_ADD})

    urls = []

    if table:
        urls.extend([
            path('{0}/'.format(name), commonListaTable, {'model': table, 'queryset': table_queryset}, name=name)
        ])
    if add:
        urls.extend([
            path('{0}/add/'.format(name), commonCadastro,
                 # {'acao': ACAO_ADD, }.update(dic),
                 # {'acao': ACAO_ADD, 'formModel': form, 'goto': goto, },
                 dic_add,
                 name="{0}Add".format(name)),
        ])
    if edit:
        urls.extend([
            path('{0}/<pk>/<str:acao>/'.format(name), commonCadastro,
                 dic,
                 name="{0}EditDelete".format(name)),
        ])
    return urls


def include_Workflow(name, table=ProcessesInstanceTable, form=None, subject=None, pending=False, add=True,
                     disableMe=False):
    urls = []
    if table:
        urls.extend([
            path('{0}/'.format(name), common_workflow_table_process,
                 {'table': table, 'subject': subject, 'pending': pending, 'add': add, 'disableMe': disableMe},
                 name=name)
        ])
    if add:
        urls.extend([
            path('{0}/add/'.format(name), common_workflow_execute,
                 {'acao': ACAO_WORKFLOW_START, 'form_class': form, 'goto': name},
                 name="{0}Add".format(name)),
            # Não tem Update ou Delete, pois é parte de Workflow
        ])
    return urls


@login_required
def relatorio(request, *args, **kwargs):
    """
    Report genérico.
        Parâmetros são:
            formRel: form do filtro do relatório
            # model: form dos dados do relatório
            goto: nome da url para onde será redirecionado após submit
            report_name: caminho e nome do relatório no servidor Jasper (/Imobiliar/Relatorios/Razao_por_Periodo)
            fields: campos adicionais que serão passado para a view de report
            titulo: título do relatório
            template_name: nome do template a ser usado para entrada de dados do relatório, default é cadastroPadrao.html
            # template_list: nome do template a ser usado para exibição do relatório, default é table.html
            template_report: nome do template a ser usado para exibição de relatório, default é report.html
    """
    formRel = kwargs.pop('formRel', PeriodoForm)
    # model = kwargs.pop('model', None)
    goto = kwargs.pop('goto', 'index')
    report_name = kwargs.pop('report_name', None)
    fields = kwargs.pop('fields', [])
    titulo = kwargs.pop('titulo', 'Relatório')

    template_name = kwargs.pop('template_name', 'cadastroPadrao.html')
    # template_list = kwargs.pop('template_list', 'table.html')
    template_report = kwargs.pop('template_report', 'report.html')

    home = 'index'

    configuraButtons = True

    form = formRel(request.POST or None)  # , request.FILES or None) #File uploads

    # form.helper.form_tag = True # como é variável de classe, tem que forçar para ter <form na geração do html

    if request.method == 'POST':
        if form.is_valid():
            dataini = form.cleaned_data['dataini']
            datafin = form.cleaned_data['datafin']
            # dataini = datetime(dataini.year,dataini.month,dataini.day,tzinfo=utc)
            # datafin = datetime(datafin.year,datafin.month,datafin.day, 23, 59, 59,tzinfo=utc)
            params = {'year_ini': dataini.year, 'month_ini': dataini.month, 'day_ini': dataini.day,
                      'year_fin': datafin.year, 'month_fin': datafin.month, 'day_fin': datafin.day, }

            # Prepara campos adicionais
            for f in fields:
                try:
                    params.update({f: form.cleaned_data[f]})
                except:
                    params.update({f: request.session.get(f, None)})

            if request.POST['save'] == 'Consultar' and redirect:
                params.update({'acao': ACAO_REPORT})
                url = reverse(goto, kwargs=params)
                return commonRender(request, template_report,
                                    {'empresa': emp, 'title': titulo, 'goto': url})
                # url = reverse(goto, **params)
                # return HttpResponseRedirect(url)
                # return redirect(goto, **params)
            elif request.POST['save'] == 'Exportar' and report_name:
                # dataini = dataini.isoformat()
                # datafin = datafin.isoformat()
                params.update({'acao': ACAO_REPORT_EXPORT})
                relatorio = montaURLjasperReport(report_name=report_name, params=params)
                return commonRender(request, template_report,
                                    {'empresa': emp, 'title': titulo, 'goto': goto, 'form_errors': form.errors,
                                     'relatorio': relatorio})
            else:
                pass
            return redirect('periodo')
        else:
            context = RequestContext(request)
            context['form_errors'] = form.errors

    if configuraButtons:
        configuraButtonsNoForm(form, ACAO_REPORT, goto=home)
    return commonRender(request, template_name, {'empresa': emp, 'title': titulo, 'goto': home, 'form': form})


@login_required
def versionViewCompare(request, pk=None, *args, **kwargs):
    """ Tratamento especial de view de send/receive json """
    template_name = kwargs.get('template_name', 'reversion-compare/versionCompare.html')
    titulo = kwargs.get('titulo', 'Comparar Versões')
    goto = kwargs.get('goto', 'index')
    permissions = kwargs.get('permissions', None)
    name = None

    has_permission(request, model=Version, acao=ACAO_VIEW, permissions=permissions)
    # if not has_permission(request, model=Version, acao=ACAO_VIEW, permissions=permissions):
    #     return http.HttpResponseForbidden()

    compare_data = []
    has_unfollowed_fields = False

    if pk:
        v_new = Version.objects.get(pk=pk)
        obj = v_new.object
        v_old = Version.objects.get_for_object(obj).filter(revision__id__lt=v_new.revision.id).first()

        if v_old:
            # v_new.revision.version_set.all()[4]
            compare_mixin = obj.compare_version if hasattr(obj, 'compare_version') else CompareMixin
            cmp = compare_mixin()
            compare_data, has_unfollowed_fields = cmp.compare(obj, v_old, v_new)

        # titulo = v_new.object._meta.verbose_name
        try:
            titulo = str(v_new)
            name = obj._meta.verbose_name
            goto = obj.get_absolute_url()
        except Exception as e:
            pass

    # Tratamentos das FKs follweds
    compare_data_fk = []
    diff = ''
    ctx = {'empresa': emp, 'title': titulo, 'goto': goto, 'form': None, }
    fkv_all_new = v_new.revision.version_set.all().exclude(object_id=v_new.object_id,
                                                           content_type=v_new.content_type)  # Versions de FK
    if v_old:
        fkv_all_old = v_old.revision.version_set.all().exclude(object_id=v_old.object_id,
                                                               content_type=v_old.content_type)  # Versions de FK
    else:
        fkv_all_old = Version.objects.none()
    # procura pelos que existem no new
    for fkv_new in fkv_all_new:
        fkv_old = fkv_all_old.filter(content_type=fkv_new.content_type, object_id=fkv_new.object_id).first()
        # Se existe nos dois então compara
        if fkv_old:
            compare_data_fk_i, has_unfollowed_fields_fk = cmp.compare(fkv_new.object, fkv_old, fkv_new)
            # Render diff
            ctx.update({'v_new': fkv_new, 'v_old': fkv_old, 'name': name,
                        'compare_data': compare_data_fk_i, 'has_unfollowed_fields': has_unfollowed_fields_fk, })
            diff += render_block_to_string(template_name, "content", context=ctx)
            # Acumula para mostrar de uma vez todas as FKs
            compare_data_fk += [{'v_new': fkv_new, 'v_old': fkv_old,
                                 'compare_data': compare_data_fk_i,
                                 'has_unfollowed_fields': has_unfollowed_fields_fk, }]
        else:
            # É novo, então mostra que foi inserido
            pass

    # procura pelos que só existem no f_old
    # procura pelos que só existem no f_new
    # fkv_old = [i for i in fv_old if i.object != obj]  # Versions de FK
    # fkv_new = [i for i in fv_new if i.object != obj]  # Versions de FK
    a = [i.pk for i in fkv_all_old]
    b = [i.pk for i in fkv_all_new]
    f_union = fkv_all_old.union(fkv_all_new)
    f_intersection = fkv_all_old.intersection(fkv_all_new)
    f_difference = fkv_all_old.difference(fkv_all_new)
    # k_union = set(v_old).union(set(fkv_new))
    # k_intersection = set(fkv_old).intersection(set(fkv_new))
    # k_difference = set(fkv_old).difference(set(fkv_new))

    ctx.update({'v_new': v_new, 'v_old': v_old, 'name': name,
                'compare_data': compare_data, 'has_unfollowed_fields': has_unfollowed_fields,
                'compare_data_fk': compare_data_fk})
    return commonRender(request, template_name, ctx)


@login_required
def executeUseCase(request, pk=None, formModel=None, use_case=None, goto='', *args, **kwargs):
    """
    View para confirmação de execução de um use case

    :param formModel: form que irá ser mostrado, passa parâmetro com a mensagem que será mostrada na tela
    :param use_case: use case
    :param goto: pra onde vai após o post
    :param goto_error: pra onde vai após o post e há erro, default = goto
    :param permissions: list de permissões que o usuário deve ter para executar o use case
    :param msg(optional): mensagem que poderá aparecer na tela com uma observação qualquer
    """
    clsModel = formModel._meta.model
    titulo = clsModel._meta.verbose_name.title()
    acao = kwargs.get('acao', ACAO_EXEC)
    permissions = kwargs.get('permissions', None)
    has_permission(request=request, model=clsModel, acao=acao, permissions=permissions)

    msg = kwargs.get('msg', 'ERROR')
    goto_error = kwargs.get('goto_error', goto)

    mymodel = get_object_or_404(clsModel, pk=pk)
    form = formModel(request.POST or None, instance=mymodel, msg=msg)
    titulo = '{0} - {1}'.format(titulo, mymodel.__str__())

    form.helper.form_tag = True  # como é variável de classe, tem que forçar para ter <form na geração do html
    form_errors = None
    extrajavascript = kwargs.get('extrajavascript', '')
    messages = None

    if request.method == 'POST':
        if form.is_valid():
            if acao == ACAO_EXEC:
                # Publica versão do documento atual
                with transaction.atomic():
                    result = use_case.run(obj=mymodel)
                    if result.errors.has_error:
                        transaction.set_rollback(True)
                        messages.error(request, mark_safe('Erro no Caderno de Treinamento'), fail_silently=True)
                        text = result.errors.as_alert()
                        extrajavascript = 'riot.mount("ftl-error-message", {});'.format(text).replace('\n', '')
                        goto = reverse(goto_error, args=([form.instance.pk]))
                    else:
                        goto = get_goto_url(form.instance, goto)
                        # Força o fechamento do tab associado a execução do use case
                        extrajavascript += """$('[ref="#'+$f.closest("div[class^='tab-pane active']").attr('id')+'-close"]').click();"""
        else:
            form_errors = form.errors
            text = ''
            for i in form_errors:
                txt = ', '.join([str(j.message) for j in form_errors[i].data])
                text += 'Campo {}: {}'.format(i.capitalize(), txt)
                if len(form_errors) > 1:
                    text += ', '
            errors = []
            mnt = 'riot.mount("ftl-error-message", {{messages: [{{type: \'error\', msg: \'{}: {}\'}}, ]}});'
            extrajavascript = mnt.format('Erro no Caderno de Treinamento', mark_safe(text))

            messages.error(request, mark_safe('Erro no processamento'), fail_silently=True)
    else:
        for i in form.fields:
            form.fields[i].disabled = True

    template_name = 'cadastroPadrao.html'

    configuraButtonsNoForm(form, acao, goto)

    dictionary = {'goto': goto, 'title': titulo, "form": form, "pk": pk, 'form_errors': form_errors,
                  'messages': messages, 'extrajavascript': extrajavascript}

    return commonRender(request, template_name, dictionary)
