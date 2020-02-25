from .former import EntityFormer

import os
import sass
from pony.orm.core import Entity
from flask import (
    Response,
    render_template,
    redirect,
    request,
    url_for,
    abort,
    flash
)
from typing import Type


class View:
    def __init__(self, manager, endpoint: str = None):
        self.manager = manager
        self.endpoint = endpoint
        self.rules = list()
        self.registered = False

        self.is_visible = True
        self.is_manager = False

    @property
    def name(self) -> str:
        """
        Entity view name.
        """
        return self.endpoint.lower()

    def register(self):
        """
        Registration of views.
        """
        for rule in self.rules:
            self.manager.blueprint.add_url_rule(**rule)
        self.registered = True

    @staticmethod
    def is_accessible() -> bool:
        """
        Check if user can access this entity views.
        """
        return True


class UtilsView(View):
    def __init__(self, manager):
        super().__init__(manager, f'{manager.blueprint.name}.awesome_style')
        self.visible = False
        self.rules = [
            dict(
                rule='/awesome_style/<path:path>',
                endpoint='awesome_style',
                view_func=self.awesome_style
            ),
        ]

    def awesome_style(self, path: str) -> Response:
        filename = os.path.join(
            self.manager.blueprint.static_folder,
            path
        )
        if not os.path.exists(filename):
            return abort(404)
        css = sass.compile(filename=filename)
        return Response(css, mimetype='text/css')


class ManagerView(View):
    def __init__(self, manager):
        super().__init__(manager)
        self.is_manager = True
        self.endpoint = f'{self.manager.blueprint.name}.manager'
        self.rules = [
            dict(
                rule='/',
                endpoint='manager',
                view_func=self.view_protector
            ),
        ]

    @property
    def name(self) -> str:
        return 'Manager'

    def view_protector(self) -> Response:
        """
        Protection proxy for entity list view.
        """
        if self.is_accessible():
            return self.entity_list_view()
        return abort(401)

    def entity_list_view(self) -> Response:
        return render_template(
            'manager/manager.html',
            view=self
        )


class EntityView(View):
    def __init__(self, manager, entity: Type[Entity]):
        super().__init__(manager)
        self.entity = entity
        self.former = EntityFormer(self.entity)

        self.rules = [
            dict(
                rule=f'/{self.name}',
                endpoint=f'list_{self.name}',
                view_func=self.entity_list_view_protector
            ),
            dict(
                rule=f'/{self.name}/list',
                endpoint=f'list_{self.name}',
                view_func=self.entity_list_view_protector
            ),
            dict(
                rule=f'/{self.name}/edit',
                endpoint=f'edit_{self.name}',
                view_func=self.entity_edit_view_protector,
                methods=['GET', 'POST']
            ),
            dict(
                rule=f'/{self.name}/add',
                endpoint=f'add_{self.name}',
                view_func=self.entity_add_view_protector,
                methods=['GET', 'POST']
            ),
            dict(
                rule=f'/{self.name}/delete',
                endpoint=f'delete_{self.name}',
                view_func=self.entity_delete_view_protector,
                methods=['GET', 'POST']
            )
        ]

    @property
    def name(self) -> str:
        """
        Entity view name.
        """
        return self.entity.__name__

    @property
    def endpoint(self) -> str:
        """
        Endpoint for entity list view.
        """
        return self.endpoints['list_endpoint']

    @endpoint.setter
    def endpoint(self, value: str) -> None:
        """
        Quick fix.
        """
        pass

    @property
    def edit_form(self):
        """
        Get newly generated edit form.
        """
        return self.former.get_form(add_primary_keys=True)

    @property
    def add_form(self):
        """
        Get newly generated add form.
        """
        return self.former.get_form(add_primary_keys=False)

    @property
    def endpoints(self) -> dict:
        return dict(
            view=self,
            list_endpoint=f'{self.manager.blueprint.name}.list_{self.name}',
            edit_endpoint=f'{self.manager.blueprint.name}.edit_{self.name}',
            add_endpoint=f'{self.manager.blueprint.name}.add_{self.name}',
            delete_endpoint=f'{self.manager.blueprint.name}.delete_{self.name}'
        )

    def entity_list_view_protector(self) -> Response:
        """
        Protection proxy for entity list view.
        """
        if self.is_accessible():
            return self.entity_list_view()
        return abort(401)

    def entity_list_view(self) -> Response:
        page = request.args.get('page', type=int, default=1)
        max_per_page = request.args.get('per_page', type=int, default=20)
        entities = self.entity.select()
        return render_template(
            'manager/entity_list.html',
            key=self.former.primary_key(),
            columns=self.former.columns(),

            max_page=entities.count() // max_per_page,
            page=page,
            entities=entities.page(page, max_per_page),

            **self.endpoints
        )

    def entity_edit_view_protector(self) -> Response:
        """
        Protection proxy for entity edit view.
        """
        if self.is_accessible():
            return self.entity_edit_view()
        return abort(401)

    def entity_edit_view(self) -> Response:
        form = self.edit_form(**request.form)
        row = self.entity.get(**{
            request.args.get('key', default='id'): request.args.get('value', default=None)
        })

        if request.method == 'POST':
            try:
                if form.validate():
                    row = self.former.update_entity_from_form(form)
                    self.manager.db.commit()
                    flash(f'{self.entity.__name__} "{str(row)}" was successfully updated.', 'success')
                    return redirect(url_for(self.endpoints['list_endpoint']))
            except Exception as exc:
                flash(f'Error: {str(exc)}', 'danger')
        else:
            form = self.former.fill_form(self.edit_form, row)

        return render_template(
            'manager/entity.html',
            form=form,

            **self.endpoints
        )

    def entity_add_view_protector(self) -> Response:
        """
        Protection proxy for entity add view.
        """
        if self.is_accessible():
            return self.entity_add_view()
        return abort(401)

    def entity_add_view(self) -> Response:
        form = self.add_form(**request.form)

        if request.method == 'POST' and form.validate():
            try:
                row = self.former.add_entity_from_form(form)
                self.manager.db.commit()

                flash(f'{self.entity.__name__} "{str(row)}" was successfully added.', 'success')
                return redirect(url_for(self.endpoints['list_endpoint']))
            except Exception as exc:
                flash(f'Error: {str(exc)}', 'danger')

        return render_template(
            'manager/entity.html',
            form=form,

            **self.endpoints
        )

    def entity_delete_view_protector(self) -> Response:
        """
        Protection proxy for entity list view.
        """
        if self.is_accessible():
            return self.entity_delete_view()
        return abort(401)

    def entity_delete_view(self) -> Response:
        try:
            row = self.entity.get(**{
                request.args.get('key', default='id'): request.args.get('value', default=None)
            })
            row.delete()
            self.manager.db.commit()
            flash(f'{self.entity.__name__} "{str(row)}" was successfully deleted.', 'success')
        except Exception as exc:
            flash(f'Error: {str(exc)}', 'danger')
        return redirect(url_for(self.endpoints['list_endpoint']))
