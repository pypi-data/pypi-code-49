from rest_framework import routers, viewsets, serializers
from actions.mixins import ActionMixin
from actions.actions.action_registry import ACTIONS
from actions.models import ActionEvent


class ActionEventSerializer(serializers.Serializer):
    class Meta:
        model = ActionEvent
        fields = '__all__'


class ActionEventViewSet(ActionMixin, viewsets.ModelViewSet):
    queryset = ActionEvent.objects.all()
    serializer_class = ActionEventSerializer
    action_registry = ACTIONS


router = routers.DefaultRouter()
router.register(r'actionevents', ActionEventViewSet)
