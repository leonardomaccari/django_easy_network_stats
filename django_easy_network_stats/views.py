from django.shortcuts import render, render_to_response, get_object_or_404
from django_netjsongraph.models import Topology, Link, Node, Update
from graphos.sources.simple import SimpleDataSource
from graphos.renderers.flot import LineChart
from collections import defaultdict
import networkx as nx


def index(request):
    context = {}
    return render(request, 'stats/index.html', context)


def topology_list(request):
    topologies = Topology.objects.all()
    return render_to_response('netjsongraph/list.html',
                              {'topologies': topologies})


def topology_detail(request, pk):
    # FIXME put all the nx code somewhere esle
    topology = get_object_or_404(Topology, pk=pk)
    link_get = request.GET.get('link_stats')
    link_data = defaultdict(list)
    links = Link.objects.all().filter(topology=pk)
    nodes = set([str(n) for n in Node.objects.filter(topology=pk)])
    for l in links:
        link_data[str(l)].append([l.update_id, l.cost])
    params = {'topology': topology, 'links': link_data.keys(),
              'nodes': sorted([str(n) for n in nodes])}
    if link_get:
        axes = [["sample", "ETX"]]
        for (i, cost) in link_data[link_get]:
            axes.append([i, cost])
        chart = LineChart(SimpleDataSource(data=axes))
        chart.height = "150"
        chart.width = "500"
        params['chart'] = chart

    path_stats_source = request.GET.get('path_stats_source')
    path_stats_target = request.GET.get('path_stats_target')
    if path_stats_source and path_stats_target:
        axes = [["sample", "ETX"]]
        update_list = Update.objects.all()
        for u in update_list:
            g = nx.Graph()
            for l in links:
                if l.update == u:
                    g.add_edge(str(l.source), str(l.target),
                               {'cost': float(l.cost)})
            cost = nx.dijkstra_path_length(g, str(path_stats_source),
                                           str(path_stats_target),
                                           weight='cost')
            axes.append([u.id, cost])
        chart = LineChart(SimpleDataSource(data=axes))
        chart.height = "150"
        chart.width = "500"
        params['chart'] = chart

    return render_to_response('stats/detail.html', params)
