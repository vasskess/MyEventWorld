from enum import Enum

from MyEventWorld.core.mixins.choises_len_mixin import ChoicesLengthMixin
from MyEventWorld.core.mixins.choises_mixin import ChoicesMixin


class Events(ChoicesLengthMixin, ChoicesMixin, Enum):
    Sport = "Sport"
    Culture = "Culture"
    Entertainment = "Entertainment"
    Nature = "Nature"
    Other = "Other"
