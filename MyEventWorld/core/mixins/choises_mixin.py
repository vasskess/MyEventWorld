class ChoicesMixin:
    @classmethod
    def choices(cls):
        return [(pick.name, pick.value) for pick in cls]
