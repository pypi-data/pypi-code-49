import factory
from devops_microsoft_sspo_etl.scrum_project import ScrumProject
from devops_microsoft_sspo_etl.scrum_project_team import ScrumProjectTeam
from devops_microsoft_sspo_etl.team_member import TeamMember
from devops_microsoft_sspo_etl.sprint import Sprint
from devops_microsoft_sspo_etl.user_story import UserStory
from devops_microsoft_sspo_etl.scrum_development_task import ScrumDevelopmentTask
from devops_microsoft_sspo_etl.product_backlog import ProductBacklog
import factory

class ScrumProjectFactory(factory.Factory):
    class Meta:
        model = ScrumProject

class ScrumProjectTeamFactory(factory.Factory):
    class Meta:
        model = ScrumProjectTeam

class TeamMemberFactory(factory.Factory):
    class Meta:
        model = TeamMember

class SprintFactory(factory.Factory):
    class Meta:
        model = Sprint

class UserStoryFactory(factory.Factory):
    class Meta:
        model = UserStory

class ScrumDevelopmentTaskFactory(factory.Factory):
    class Meta:
        model = ScrumDevelopmentTask

class ProductBacklogFactory(factory.Factory):
    class Meta:
        model = ProductBacklog