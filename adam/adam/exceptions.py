from adam.config.constants import AdamExceptions


class ServiceNotFound(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class ServiceKeyInvalid(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
