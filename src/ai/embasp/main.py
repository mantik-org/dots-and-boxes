from src.ai.embasp.Edge import Edge
from src.ai.embasp.Path import Path

from lib.embasp.platforms.desktop.desktop_handler import DesktopHandler
from lib.embasp.specializations.dlv2.desktop.dlv2_desktop_service import DLV2DesktopService
from lib.embasp.languages.asp.asp_mapper import ASPMapper
from lib.embasp.languages.asp.asp_input_program import ASPInputProgram

def getEdges():
    edges = []

    edges.append(Edge(0, 1, 1))
    edges.append(Edge(0, 2, 4))
    edges.append(Edge(1, 2, 2))
    edges.append(Edge(1, 3, 4))
    edges.append(Edge(1, 4, 1))
    edges.append(Edge(2, 4, 4))
    edges.append(Edge(3, 5, 6))
    edges.append(Edge(3, 6, 1))
    edges.append(Edge(4, 3, 1))
    edges.append(Edge(6, 4, 5))
    edges.append(Edge(6, 5, 9))
    edges.append(Edge(6, 7, 1))
    edges.append(Edge(7, 5, 2))

    return edges


def join(source, path, sortedPath):
    for p in path:
        if (int(p.get_source()) == int(source)):
            sortedPath.append(p.get_destination())
            if (int(p.get_destination()) == destination):
                return
            join(p.get_destination(), path, sortedPath)
            return


def show(path, sum_):
    first = True
    print("path = ", end='')
    for n in path:
        if not first:
            print(" - ", end='')
        else:
            first = False
        print(n, end='')
    print("\nsum = " + str(sum_))


try:

    handler = DesktopHandler(DLV2DesktopService("../../../lib/executable/dlv2win"))

    ASPMapper.get_instance().register_class(Edge)
    ASPMapper.get_instance().register_class(Path)

    inputProgram = ASPInputProgram()

    source = 0  # source node
    destination = 7  # destination node

    rules = "path(X,Y,W) | notPath(X,Y,W) :- source(X), edge(X,Y,W)."
    rules += "path(X,Y,W) | notPath(X,Y,W) :- path(_,X,_), edge(X,Y,W)."
    rules += "end(X) :- destination(X), path(_,X,_)."
    rules += ":- destination(X), not end(X)."
    rules += ":~ path(X,Y,W). [W@1 ,X,Y]"

    inputProgram.add_program(rules)
    inputProgram.add_program("source(" + str(source) + "). destination(" + str(destination) + ").")

    inputProgram.add_objects_input(getEdges())

    handler.add_program(inputProgram)

    answerSets = handler.start_sync()

    for answerSet in answerSets.get_optimal_answer_sets():

        path = []  # edges in the shortest path (unsorted)
        sum_ = 0  # total weight of the path

        for obj in answerSet.get_atoms():

            if isinstance(obj, Path):
                path.append(obj)
                sum_ += int(obj.get_weight())

        sortedPath = []  # edges in the shortest path (sorted)
        sortedPath.append(source)

        join(source, path, sortedPath)  # sorts the edges
        show(sortedPath, sum_)  # shows the path

except Exception as e:
    print(str(e))
