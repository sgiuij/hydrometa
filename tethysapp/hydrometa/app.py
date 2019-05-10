from tethys_sdk.base import TethysAppBase, url_map_maker


class Hydrometa(TethysAppBase):
    """
    Tethys app class for Hydrometa.
    """

    name = 'Hydrometa'
    index = 'hydrometa:home'
    icon = 'hydrometa/images/icon.gif'
    package = 'hydrometa'
    root_url = 'hydrometa'
    color = '#c0392b'
    description = 'Place a brief description of your app here.'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='hydrometa',
                controller='hydrometa.controllers.home'
            ),
            UrlMap(
                name='hydroshare',
                url='hydrometa/hydroshare',
                controller='hydrometa.controllers.hydroshare'
            ),
            UrlMap(
                name='proj_search',
                url='hydrometa/proj_search',
                controller='hydrometa.controllers.proj_search'
            ),
        )

        return url_maps
