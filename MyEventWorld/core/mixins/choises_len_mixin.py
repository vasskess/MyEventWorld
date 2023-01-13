class ChoicesLengthMixin:
    @classmethod
    def max_length(cls):
        return max(len(name) for name, _ in cls.choices())
