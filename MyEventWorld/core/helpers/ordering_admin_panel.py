ADMIN_ORDERING = [
    "auth",
    "accounts",
    "events",
    "common_stuff",
    "admin_interface",
]


def get_app_list(self, request):
    """
        This will override django build in get_app_list method, so we can order apps in admin panel in a way we want
    """
    app_dict = self._build_app_dict(request)
    for app_name in ADMIN_ORDERING:
        app = app_dict[app_name]
        app['models'].sort(key=lambda x: (x['object_name']))
        yield app
