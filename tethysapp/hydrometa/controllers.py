from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import Button
from hs_restclient import HydroShare, HydroShareAuthBasic
import logging


logger = logging.getLogger(__name__)
try:
    from tethys_services.backends.hs_restclient_helper import get_oauth_hs
except ImportError:
    logger.error("could not load: tethys_services.backends.hs_restclient_helper import get_oauth_hs")


@login_required
def home(request):
    context = {
    }
    return render(request, 'hydrometa/home.html', context)


@login_required
def hydroshare(request):
    if request.method == 'POST':
        get_data = request.POST
        r_title = str(get_data['resource-title'])
        r_type = str(get_data['resource-type'])
        r_fileRoute = str(get_data['resource-fileroute'])
        r_abstract = str(get_data['resource-abstract'])
        r_keywords_raw = str(get_data['resource-keywords'])
        r_keywords = r_keywords_raw.split(',')
        hs = get_oauth_hs(request)
        print(r_title, "4444444")

        # filepath = '/Users/yueshen/data.txt'

        resource_id = hs.createResource(r_type, r_title, resource_file=r_fileRoute, keywords=r_keywords, abstract=r_abstract)
        print(resource_id)

    return redirect("https://www.hydroshare.org/resource/{resource_id}".format(resource_id=resource_id))


@login_required
def proj_search(request):
    hs = get_oauth_hs(request)
    get_data = request.GET
    print(get_data)
    print("2"*50)
    # resources = hs.resources(full_text_search=get_data['search-keyword'][0])
    temp = "subject_exact:"+get_data['search-keyword'][0]
    print(temp)
    resources = hs.resources(selected_facets=temp)
    print("3"*50)
    for resource in resources:
        print(resource)
    print(resources)
    context = {
    }
    return render(request, 'hydrometa/proj_search.html', context)
