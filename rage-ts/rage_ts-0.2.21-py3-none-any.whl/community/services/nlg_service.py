import itertools
import json
import logging
import time
from typing import Text, List, Dict, Any, Optional, Tuple, Set

from sqlalchemy import or_, and_, true, false

from ragex.community import config
from ragex.community.database.data import Template
from ragex.community.database.service import DbService
from ragex.community.utils import (
    get_columns_from_fields,
    get_query_selectors,
    query_result_to_dict,
    QueryResult,
)

logger = logging.getLogger(__name__)


class NlgService(DbService):
    def save_template(
        self,
        template: Dict[Text, Any],
        username: Optional[Text] = None,
        domain_id: Optional[Text] = None,
        project_id: Text = config.project_name,
    ) -> Dict[Text, Any]:

        if domain_id is None:
            logger.warning("Template could not be saved since domain id is None.")
            return {}

        if not username:
            username = config.default_username

        new_template = Template(
            template=template["template"],
            text=template.get("text"),
            content=json.dumps(template),
            annotated_at=time.time(),
            annotator_id=username,
            project_id=project_id,
        )

        if domain_id:
            new_template.domain_id = domain_id

        self.add(new_template)

        self._add_actions_to_domain([template["template"]], project_id=project_id)
        return new_template.as_dict()

    def fetch_templates(
        self,
        text_query: Optional[Text] = None,
        template_query: Optional[Text] = None,
        fields_query: List[Tuple[Text, bool]] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        sort_by_template_name: bool = False,
        intersect_filters: bool = False,
    ) -> QueryResult:
        """Returns a list of responses. Each response includes its template name
        as a property under "template".

        An example of a response item could be:
        ```
        {
            "text": "Hey! How are you?",
            "template": "utter_greet",
            "id": 6,
            "annotator_id": "me",
            "annotated_at": 1567780833.8198001,
            "project_id": "default",
            "edited_since_last_training": false
        }
        ```

        Args:
            text_query: Filter results by response text (case insensitive).
            template_query: Filter results by template name.
            fields_query: Fields to include per item returned.
            limit: Maximum number of responses to be retrieved.
            offset: Excludes the first ``offset`` responses from the result.
            sort_by_template_name: If ``True``, sort responses by their
                "template" property.
            intersect_filters: If ``True``, join ``text_query`` and
                ``template_query`` conditions with an AND instead of an OR.

        Returns:
            List of responses with total number of responses found.
        """

        templates_to_query = template_query.split(",") if template_query else []
        columns = get_columns_from_fields(fields_query)

        if not templates_to_query and not text_query:
            # Case 1: No conditions were specified - base query is TRUE (all results)
            query = true()
        else:
            if intersect_filters:
                # Case 2: One or both conditions were specified, and caller wants to join
                #         them with AND
                query = true()
            else:
                # Case 3: One or both conditions were specified, and caller wants to join
                #         them with OR.
                query = false()

        query_joiner = and_ if intersect_filters else or_

        if text_query:
            query = query_joiner(query, Template.text.ilike(f"%{text_query}%"))

        if template_query:
            query = query_joiner(query, Template.template.in_(templates_to_query))

        templates = self.query(*get_query_selectors(Template, columns)).filter(query)

        if sort_by_template_name:
            templates = templates.order_by(Template.template.asc())

        total_number_of_results = templates.count()

        templates = templates.offset(offset).limit(limit).all()

        if columns:
            results = [query_result_to_dict(r, fields_query) for r in templates]
        else:
            results = [t.as_dict() for t in templates]

        return QueryResult(results, total_number_of_results)

    def get_grouped_responses(
        self, text_query: Optional[Text] = None, template_query: Optional[Text] = None
    ) -> QueryResult:
        """Returns responses grouped by their template name.

        Args:
            text_query: Filter responses by response text (case insensitive).
            template_query: Filter template groups by template name.

        Returns:
            `QueryResult` containing grouped responses and total number of responses
            across all groups.
        """

        # Sort since `groupby` only groups consecutive entries
        templates = self.fetch_templates(
            text_query=text_query,
            template_query=template_query,
            sort_by_template_name=True,
            intersect_filters=True,
        ).result

        grouped_templates = itertools.groupby(
            templates, key=lambda each: each["template"]
        )

        result = [{"template": k, "responses": list(g)} for k, g in grouped_templates]
        count = sum(len(item["responses"]) for item in result)

        return QueryResult(result, count)

    def fetch_all_template_names(self) -> Set[Text]:
        """Fetch a list of all template names in db."""

        return {t["template"] for t in self.fetch_templates()[0]}

    def delete_template(self, _id: Text) -> bool:
        delete_result = self.query(Template).filter(Template.id == _id).delete()

        return delete_result

    def delete_all_templates(self) -> None:
        self.query(Template).delete()

    def update_template(
        self, _id: Text, template: Dict[Text, Any], user: Dict[Text, Any]
    ) -> Optional[Dict[Text, Any]]:
        old_template = self.query(Template).filter(Template.id == _id).first()

        if old_template:
            old_template.text = template["text"]
            old_template.template = template["template"]
            old_template.annotated_at = time.time()
            old_template.content = json.dumps(template)
            old_template.annotator_id = user["username"]
            old_template.edited_since_last_training = True

            self._add_actions_to_domain([template["template"]])

            return old_template.as_dict()

        return None

    def replace_templates(
        self,
        new_templates: List[Dict[Text, Any]],
        username: Optional[Text] = None,
        domain_id: Optional[Text] = None,
    ) -> int:
        """Deletes all responses and adds responses from template_list.

        Returns the number of inserted templates.
        """

        self.delete_all_templates()
        insertions = 0
        for template in new_templates:
            inserted = self.save_template(template, username, domain_id=domain_id)
            if inserted:
                insertions += 1

        return insertions

    def _add_actions_to_domain(
        self, actions: List[Text], project_id: Text = config.project_name
    ) -> None:
        from ragex.community.services.domain_service import DomainService

        DomainService(self.session).add_items_to_domain(
            actions=actions, project_id=project_id, origin="responses"
        )

    def mark_templates_as_used(
        self, training_start_time: float, project_id: Text = config.project_name
    ) -> None:
        """Unsets the `edited_since_last_training_flag` for templates which were included
           in the last training.

        Args:
            training_start_time: annotation time until templates should be marked as
                used in training.
            project_id: Project which was trained.

        """

        templates_which_were_used_in_training = (
            self.query(Template)
            .filter(
                and_(
                    Template.annotated_at <= training_start_time,
                    Template.edited_since_last_training,
                    Template.project_id == project_id,
                )
            )
            .all()
        )
        for template in templates_which_were_used_in_training:
            template.edited_since_last_training = False

    def rename_templates(
        self, old_template_name: Text, template: Dict[Text, Text], annotator: Text
    ) -> None:
        """
        Bulk renames a template name.

        Args:
            old_template_name: The name of the template which should be renamed.
            template: The object containing the new template values.
            annotator: The name of the user who is doing the rename.
        """

        templates = (
            self.query(Template).filter(Template.template == old_template_name).all()
        )
        new_template_name = template["name"]
        for template in templates:
            template.template = new_template_name
            template.annotated_at = time.time()
            template.annotator_id = annotator
