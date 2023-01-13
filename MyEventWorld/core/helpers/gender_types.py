from enum import Enum

from MyEventWorld.core.mixins.choises_len_mixin import ChoicesLengthMixin
from MyEventWorld.core.mixins.choises_mixin import ChoicesMixin


class Genders(ChoicesLengthMixin, ChoicesMixin, Enum):
    Unpicked = "Unpicked"
    Male = "Male"
    Female = "Female"
