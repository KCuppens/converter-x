from apps.action.tests.factories import ActionFactory
from apps.base.utils import CustomGraphQLTestCase


class ActionModelsTestCase(CustomGraphQLTestCase):
    def test_action_str_id(self):
        action_obj = ActionFactory()
        assert action_obj.__str__() == str(action_obj.id)
