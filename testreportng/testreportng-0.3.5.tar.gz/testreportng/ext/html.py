"""
this is a offline html report builder, with no third-party js package requirement.
"""
from jinja2 import Template
import typing
from collections import OrderedDict

from testreportng.result import NGResult, NGResultOperator
from testreportng.constants import Label

COLOR_DICT = {
    Label.LABEL_STATUS_PASS: "#dff0d8",
    Label.LABEL_STATUS_FAIL: "#fcf8e3",
    Label.LABEL_STATUS_ERROR: "#f2dede",
    Label.LABEL_STATUS_SKIP: "#ffffff",
    Label.LABEL_STATUS_INIT: "#ffffff",
}

TEMPLATE = r"""
<!DOCTYPE html>
<html>
   <head>
      <title>{{ test_name }}</title>
      <style>
         table, th, td {
         border: 1px solid black;
         border-collapse: collapse;
         }
         th, td {
         padding: 5px;
         }
         th {
         text-align: left;
         }
      </style>
   </head>
   <body>
      <h1>{{ test_name }}</h1>
      <h2>Summary</h2>
      <table style="width:90%">
         <tr>
            {% for title, count in summary.items() %}
            <th>{{ title }}</th>
            {% endfor %}
         </tr>
         <tr>
         {% for title, count in summary.items() %}
         <td>{{ count }}</td>
         {% endfor %}
         </tr>
      </table>
      <h2>Result</h2>
      <div id="users">
         {% if not offline %}
         <button class="sort" data-sort="status">
         sorted by status!
         </button>
         {% endif %}
         <table style="width:90%">
            <tr>
               <th>suite</th>
               <th>case</th>
               <th>status</th>
               <th>error</th>
               <th>traceback</th>
            </tr>
            <tbody class="list">
               {% for suite_name, each in test_result.items() %}
               {% for each_case_name, each_case in each.items() %}
               <tr style="background-color: {{ color_dict[each_case.status] }}">
                  <td class="suite">{{ suite_name }}</td>
                  <td class="name">{{ each_case_name }}</td>
                  <td class="status">{{ each_case.status }}</td>
                  <td class="status">{{ each_case.error }}</td>
                  <td>{{ each_case.traceback }}</td>
               </tr>
               {% endfor %}
               {% endfor %}
            </tbody>
         </table>
      </div>
      {% if not offline %}
      <script src="http://cdnjs.cloudflare.com/ajax/libs/list.js/1.5.0/list.min.js"></script>
      <script>
         var options = {
           valueNames: [ 'suite', 'case', 'status' ],
         };
         var userList = new List('users', options);
      </script>
      {% endif %}
   </body>
</html>
"""


class HtmlReporter(object):
    _template = TEMPLATE
    _default_test_name = "default"

    @classmethod
    def render(
        cls,
        test_name: str,
        result: typing.Union[typing.Dict[str, NGResult], NGResult],
        offline: bool = True,
        with_template: bool = None,
    ) -> str:
        # custom template
        if with_template:
            html_template = Template(with_template)
        else:
            html_template = Template(TEMPLATE)
        # re-format
        if isinstance(result, NGResult):
            result = {result.kls_name: result}

        result_operator = NGResultOperator()
        result_operator.load(result)
        summary = result_operator.summary()

        # wrap to dict
        new_result = dict()
        for k, v in result.items():
            new_result[k] = v.to_dict(safe_repr=True)
        result = new_result

        return html_template.render(
            test_name=test_name,
            summary=summary,
            test_result=result,
            color_dict=COLOR_DICT,
            offline=offline,
        )
