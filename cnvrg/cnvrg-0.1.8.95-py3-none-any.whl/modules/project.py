from cnvrg.helpers.apis_helper import post as apis_post, get as apis_get, credentials
from cnvrg.modules.cnvrg_files import CnvrgFiles
from cnvrg.modules.errors import CnvrgError
import cnvrg.helpers.config_helper as config_helper
import cnvrg.helpers.env_helper as env_helper
import cnvrg.helpers.args_helper as args_helper
import cnvrg.helpers.param_build_helper as param_build_helper
from cnvrg.helpers.url_builder_helper import url_join
import cnvrg.helpers.spawn_helper as spawn_helper
import json
class Project(CnvrgFiles):
    def __init__(self, project=None, project_url=None, working_dir=None):
        if project_url:
            owner_slug, project_slug = Project.get_owner_and_project_from_url(project_url)
        else:
            owner_slug, project_slug = param_build_helper.parse_params(project, param_build_helper.PROJECT, working_dir=working_dir)
        self.__owner = owner_slug or credentials.owner
        self.__project = project_slug

        in_dir = config_helper.is_in_dir(config_helper.CONFIG_TYPE_PROJECT, project_slug, working_dir)
        super(Project, self).__init__(in_dir=in_dir)
        if in_dir:
            self._set_working_dir(config_helper.find_config_dir(path=working_dir))
            self.in_dir = True
        elif not self.__project or not self.__owner:
            raise CnvrgError("Cant init project without params and outside project directory")

    def __fetch_config(self):
        resp = apis_get(self.get_base_url())
        return {"slug": self.slug, "owner": self.owner, **resp.get("result")}

    def is_git(self):
        resp = apis_get(url_join(self.get_base_url(), 'get_project'))
        if not resp.get("result"):
            return False
        result = json.loads(resp.get("result"))
        return result.get("git")


    @property
    def owner(self):
        return self.__owner

    @property
    def slug(self):
        return self.__project

    @property
    def git(self):
        config = self.get_config()
        if config:
            return config.get(":git") or False
        return self.__fetch_config().get("git")


    def get_git_commit(self):
        return spawn_helper.run_and_get_output("git rev-parse --verify HEAD")

    def get_git_branch(self):
        return spawn_helper.run_and_get_output("git rev-parse --abbrev-ref HEAD")

    def get_base_url(self):
        return "users/{owner}/projects/{project}".format(owner=self.__owner, project=self.__project)

    def _default_config(self):
        return {
            "project": self.__project,
            "owner": self.__owner,
            "commit": None
        }

    def web_url(self):
        return url_join(credentials.web_url(), self.__owner, 'projects', self.__project)

    def get_project_name(self):
        return self.__project

    def get_output_dir(self):
        return self.get_working_dir()

    def run_task(self, cmd, **kwargs):
        #if "grid" in kwargs: kwargs["grid"] = hyper_search_helper.load_hyper_search(kwargs["grid"])
        kwargs = {**env_helper.get_origin_job(), **kwargs}
        resp = apis_post(url_join(self.get_base_url(), "experiments"), data={"cmd": cmd, **kwargs})
        hyper_search = resp.get("hyper_search")
        if not hyper_search:
            error_msg = resp.get("error") or "Can't run experiment"
            raise CnvrgError(error_msg)
        return hyper_search


    def sync(self, **options):
        command = "cnvrg sync {args}".format(args=args_helper.args_to_string(options))
        spawn_helper.run_sync(command, print_output=True)