import argparse


class UniquePathAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if getattr(self, "seen", False):
            raise argparse.ArgumentError(
                self, f"{self.dest} can only be specified once"
            )
        setattr(self, "seen", True)
        setattr(namespace, self.dest, values)


class UniqueVersionAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if getattr(self, "version_seen", False):
            raise argparse.ArgumentError(self, f"version can only be specified once")
        setattr(self, "version_seen", True)
        setattr(namespace, self.dest, values)


class UniqueKeyAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if getattr(self, "key_seen", False):
            raise argparse.ArgumentError(self, "key can only be specified once")
        setattr(self, "key_seen", True)
        setattr(namespace, self.dest, values)


class UniqueServiceNameAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if getattr(self, "service_name_seen", False):
            raise argparse.ArgumentError(
                self, "service name can only be specified once"
            )
        setattr(self, "service_name_seen", True)
        setattr(namespace, self.dest, values)
