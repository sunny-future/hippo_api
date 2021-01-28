import xadmin
from . import models


class HostXadmin(object):
    pass


xadmin.site.register(models.Hosts, HostXadmin)
