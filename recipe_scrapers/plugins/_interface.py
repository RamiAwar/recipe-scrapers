class PluginInterface:
    """
    TODO: write docstring
    """

    run_on_hosts = ("*",)
    run_on_methods = ("title",)

    @classmethod
    def run(cls, decorated):
        pass

    @classmethod
    def should_run(cls, host, method):
        return cls._should_run_host_check(host) and cls._should_run_method_check(method)

    @classmethod
    def _should_run_host_check(cls, host):
        return "*" in cls.run_on_hosts or host in cls.run_on_hosts

    @classmethod
    def _should_run_method_check(cls, method):
        return method in cls.run_on_methods
