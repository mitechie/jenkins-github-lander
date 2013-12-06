from pyramid.config import Configurator
from pyramid.response import Response

from jenkinsgithublander.jobs import kick_mergeable_pull_requests
from jenkinsgithublander.utils import build_config
from jenkinsgithublander import views



def main(global_config, **settings):
    settings['mako.directories'] = 'jenkinsgithublander:templates'

    # Add the github request info to the settings.
    settings = build_config(settings)
    config = Configurator(settings=settings)
    config.include('pyramid_mako')

    config.add_route('home', '/')
    config.add_route('check_pulls', '/check_pulls')
    config.add_route('new_comment', '/new_comment')

    # Load up all of the views.
    config.scan('jenkinsgithublander.views')
    return config.make_wsgi_app()
