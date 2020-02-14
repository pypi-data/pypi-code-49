# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyppl_report', 'pyppl_report.filters']

package_data = \
{'': ['*'],
 'pyppl_report': ['templates/bootstrap/*',
                  'templates/bootstrap/static/*',
                  'templates/layui/*',
                  'templates/layui/static/*',
                  'templates/layui/static/css/*',
                  'templates/layui/static/css/modules/*',
                  'templates/layui/static/css/modules/laydate/default/*',
                  'templates/layui/static/css/modules/layer/default/*',
                  'templates/layui/static/font/*',
                  'templates/layui/static/images/face/*',
                  'templates/layui/static/lay/*',
                  'templates/layui/static/lay/modules/*',
                  'templates/layui/static/lay/modules/mobile/*',
                  'templates/semantic/*',
                  'templates/semantic/static/*',
                  'templates/semantic/static/themes/default/assets/fonts/*',
                  'templates/semantic/static/themes/default/assets/images/*']}

install_requires = \
['cmdy', 'liquidpy', 'panflute>=1.11.0,<1.12.0', 'pyppl', 'toml>=0.10,<0.11']

entry_points = \
{'pyppl': ['pyppl_report = pyppl_report']}

setup_kwargs = {
    'name': 'pyppl-report',
    'version': '0.6.0',
    'description': 'A report generating system for PyPPL',
    'long_description': '# pyppl_report\n\n[![Pypi][3]][4] [![Github][5]][6] [![PyPPL][7]][1] [![PythonVers][8]][4] [![Travis building][10]][11] [![Codacy][12]][13] [![Codacy coverage][14]][13]\n\nA report generating system for [PyPPL][1]\n\n## Installation\nRequires pandoc 2.7+ (and wkhtmltopdf 0.12.4+ when creating PDF reports)\n\n`pyppl_report` requires `pandoc/wkhtmltopdf` to be installed in `$PATH`\n\n```shell\npip install pyppl_report\n```\n\n## Usage\n### Specifiation of template\n\n````python\npPyClone.config.report_template = """\n# {{report.title}}\n\nPyClone[1] is a tool using Probabilistic model for inferring clonal population\nstructure from deep NGS sequencing.\n\n![Similarity matrix]({{path.join(job.o.outdir, "plots/loci/similarity_matrix.svg")}})\n\n```table\ncaption: Clusters\nfile: "{{path.join(job.o.outdir, "tables/cluster.tsv")}}"\nrows: 10\n```\n\n[1]: Roth, Andrew, et al. "PyClone: statistical inference of clonal population structure in cancer."\nNature methods 11.4 (2014): 396.\n"""\n\n# or use a template file\n\npPyClone.config.report_template = "file:/path/to/template.md"\n````\n\n### Generating report\n```python\nPyPPL().start(pPyClone).run().report(\n\t\'/path/to/report\',\n\ttitle=\'Clonality analysis using PyClone\',\n\ttemplate=\'bootstrap\'\n)\n\n# or save report in a directory\nPyPPL(name=\'Awesome-pipeline\').start(pPyClone).run().report(\'/path/to/\')\n# report generated at ./Awesome-pipeline.report.html\n```\n\nCommand line tool:\n```shell\n> pyppl report\nDescription:\n  Convert a Markdown file to report.\n\nUsage:\n  pyppl report --in <LIST> [OPTIONS]\n\nRequired options:\n  -i, --in <LIST>           - The input file.\n\nOptional options:\n  -o, --out <AUTO>          - The output file. Default: <in>.html\n  -n, --nonstand [BOOL]     - Non-standalone mode. Save static files in  <filename of --out>.files  separately. \\\n                              Default: False\n      --filter <LIST>       - The filters for pandoc Default: []\n      --toc <INT>           - The depth of heading levels to put in TOC. 0 to disable. Default: 3\n      --title <STR>         - The title of the document.\n                              If the first element of the document is H1 (#), this will be ignored \\\n                              and the text of H1 will be used as title.\n                              If the title is specified as "# Title", then a title will be added \\\n                              anyway. Default: Untitled document\n      --template <STR>      - The template to use. Either standard template name or full path to \\\n                              template file. Default: bootstrap\n  -h, -H, --help            - Show help message and exit.\n```\n\n\n### Extra data for rendering\nYou can generate a `toml` file named `job.report.data.toml` under `<job.outdir>` with extra data to render the report template. Beyond that, `proc` attributes and `args` can also be used.\n\nFor example:\n`job.report.data.toml`:\n```toml\ndescription = \'A awesome report for job 1\'\n```\nThen in your template, you can use it:\n```markdown\n## {{jobs[0].description}}\n```\n\n## Built-in templates\n\nCheck them to see features those templates support:\n\n- [Layui](https://pwwang.github.io/pyppl_report/layui.html)\n- [Bootstrip](https://pwwang.github.io/pyppl_report/bootstrap.html)\n- [Semantic](https://pwwang.github.io/pyppl_report/semantic.html)\n\n\n## How does it work?\n\nFollowing figure demonstrates how the plugin works:\n\n![How it works](./docs/howitworks.png)\n\nEach process that you want to report, will need to have a template assigned with `pXXX.config.report_template`. Like scripts, you may prefice it with `file:`, and then followed by an absolute path to the template or a relative one to where it\'s assigned. You may even assign a template using a direct string. A process with no template assign will be hidden from the report.\n\nYou can use the data from the jobs or the process to render the template.\n\nThe report for each process will then be assembled by the plugin, and converted using pandoc with a default template and some built-in filters. Finally, your report will be a standalone html file.\n\nFor larget reports, `non-standaone` reports are recommended: `.report(standalone=False, ...)`\n\n## Environments\n\nYou may pass values to process envs to control report content:\n```python\npXXX.config.report_envs.foo = "bar"\n```\nThen in you can use it in the report template:\n```python\npXXX.config.report_template = """\nThe value of foo is "{{foo}}".\n"""\n```\n\n### Preserved envs variables\n\nWe have 4 preserved variables under `pXXX.envs`:\n```python\n# Control the level of headings in the\npXXX.config.report_envs.level = 1\n# Content to add before the template\npXXX.config.report_envs.pre = \'\'\n# Content to add after the template\npXXX.config.report_envs.post = \'\'\n# The title of the process report\npXXX.config.report_envs.title = None\n```\n\n#### Process report levels\n\nNo matter at which level you want to put this process report in the entire report, you need to each heading from level 1, then according to `pXXX.config.report_envs.level`, the headings will be shifted to corresponding level. For example, with `pXXX.config.report_envs.level = 2`, following template\n\n```markdown\n# Section\n## Subsection\ncontent\n```\n\nwill be rendered into:\n```markdown\n## Section\n### Subsection\ncontent\n```\n\nIt will not affect comments in code blocks such as:\n````\n```\n## some comments\n```\n````\n\n#### Adding extra contents to process report\n\nYou may add extra contents to the process report. For example, if you put the process report at level 2, then you probably need a level-1 heading. For previous example, if you have `pXXX.config.report_envs.level = 2`, without a level-2 heading, the entire report will look like:\n\n```markdown\n## Section\n### Subsection\ncontent\n```\n\nThen you missed a level-1 heading, which will make your report look wired. Here you can specify a level-1 heading with `pXXX.config.report_envs.pre = \'# I am H1\'`:\n\n```markdown\n# I am H2\n## Section\n### Subsection\ncontent\n```\n\nYou may also append something to the process report with `pXXX.config.report_envs.post`\n\nHeadings added by `pre` and `post` will **NOT** be adjusted by `pXXX.config.report_envs.level`\n\n#### Title of the process report\n\nBy default, if not assigned or assigned with `None`, the process description will be used as the title of the process report. Of course you can overwrite it with `pXXX.config.report_envs.title`.\n\n```python\n# by default\npXXX = Proc(desc = \'Some analysis\')\n# ... other necessary settings\npXXX.report = \'# {{report.title}}\'\n```\n\nwill be rendered as:\n```markdown\n# Some analysis\n```\n\nwith `pXXX.config.report_envs.title = \'An amazing analysis\'`, we will have:\n\n```markdown\n# An amazing analysis\n```\n\n### Making your report flexiable\n\nYou can interpolate some variables in the templates to make your report flexiable. For example, you may want to hide an image in some cases:\n\n```markdown\n# {{report title}}\n\nI have enough details.\n\n{% if report.get(\'showimage\') %}\n![Image](./path/to/image)\n{% endif %}\n```\n\nThen you can show that image in the report only when you have `pXXX.config.report_envs.showimage = True`.\n\n## Change log\n\n[Change log](./docs/CHANGELOG.md)\n\n[1]: https://github.com/pwwang/PyPPL\n[2]: https://pyppl_report.readthedocs.io/en/latest/\n[3]: https://img.shields.io/pypi/v/pyppl_report?style=flat-square\n[4]: https://pypi.org/project/pyppl_report/\n[5]: https://img.shields.io/github/tag/pwwang/pyppl_report?style=flat-square\n[6]: https://github.com/pwwang/pyppl_report\n[7]: https://img.shields.io/github/tag/pwwang/pyppl?label=PyPPL&style=flat-square\n[8]: https://img.shields.io/pypi/pyversions/pyppl_report?style=flat-square\n[9]: https://img.shields.io/readthedocs/pyppl_report.svg?style=flat-square\n[10]: https://img.shields.io/travis/pwwang/pyppl_report?style=flat-square\n[11]: https://travis-ci.org/pwwang/pyppl_report\n[12]: https://img.shields.io/codacy/grade/2b7914a18f794248a62d7b36eb2408a3?style=flat-square\n[13]: https://app.codacy.com/manual/pwwang/pyppl_report/dashboard\n[14]: https://img.shields.io/codacy/coverage/2b7914a18f794248a62d7b36eb2408a3?style=flat-square\n',
    'author': 'pwwang',
    'author_email': 'pwwang@pwwang.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pwwang/pyppl_report',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
