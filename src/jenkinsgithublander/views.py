from pyramid.response import Response
from pyramid.view import view_config

from jenkinsgithublander.jobs import kick_mergeable_pull_requests


@view_config(route_name='home', renderer='home.mako')
def home(request):
    settings = request.registry.settings
    return {
        'projects': settings['projects'],
        'owner': settings['github.owner'],
    }


@view_config(route_name='check_pulls')
def trigger_mergable_commits(request):
    config = request.registry.settings
    kicked = kick_mergeable_pull_requests(config)
    if kicked:
        ret = "\n".join(kicked)
    else:
        ret = "No pull requests to merge."

    return Response(ret)


@view_config(route_name='new_comment')
def github_new_comment_hook(request):


