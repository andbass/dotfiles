
class Module:
    default_dest = "~/"
    overriden_dests = {}

    def install(self):
        """This method is called before the files within a module are copied over
        It should "yield" progress messsages
        """
        return []

    def post_install(self):
        """This is called after the "install" method is called and files are copied over
        Like "install", it should "yield" some messages about its installation progress
        """
        return []
