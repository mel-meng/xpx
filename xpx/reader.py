import shlex
import logging


class reader:
    def __init__(self, f):
        self.dom = {}



def parse_xpx(f):
    dom = {}
    nodes = {}
    links = {}
    multi_links = {}
    with open(f) as inp:
        for l in inp:
            line = shlex.split(l)
            obj = process_line(line)
            if obj['command'] == 'NODE':
                nodes.setdefault(obj['name'], {})
                for fld in obj.keys():
                    nodes[obj['name']][fld] = obj[fld]
            elif obj['command'] == 'LINK':
                links.setdefault(obj['name'], {})
                for fld in obj.keys():
                    links[obj['name']][fld] = obj[fld]

    return {'nodes': nodes, 'links': links}


def process_line(line):
    t0 = line[0]
    if t0 == 'NODE':
        return {'command': 'NODE', 'name': line[2], 'type': line[1], 'x': line[3], 'y': line[4]}
    elif t0 == 'LINK':
        return {'command': 'LINK', 'name': line[2], 'type': line[1], 'from': line[3], 'to': line[4]}
    else:
        logging.info('command not implemented: %s' % t0)
        return {'command': t0}

