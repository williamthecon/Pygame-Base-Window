from pygame import quit
from sys import exit

def inbetween(point, topleft=None, topright=None, bottomleft=None, bottomright=None, width=None, height=None):
    p0, p1 = point
    if topleft is not None:
        l, t = topleft
        if bottomright is not None:
            r, b = bottomright
        elif None not in [width, height]:
            r, b = l + width, t + height
        elif None not in [topright, height]:
            r, b = list(topright)[0], t + height
        elif None not in [bottomleft, width]:
            r, b = l + width, list(bottomleft)[1]
        else:
            return False

        if l < p0 < r and t < p1 < b:
            return True
    elif topright is not None:
        r, t = topleft
        if bottomleft is not None:
            l, b = bottomleft
        elif None not in [width, height]:
            l, b = r - width, t + height
        elif None not in [topleft, height]:
            l, b = list(topleft)[0], t + height
        elif None not in [bottomright, width]:
            l, b = r - width, list(bottomright)[1]
        else:
            return False

        if l < p0 < r and t < p1 < b:
            return True
    elif bottomleft is not None:
        l, b = bottomleft
        if topright is not None:
            r, t = topright
        elif None not in [width, height]:
            r, t = l + width, b - height
        elif None not in [topleft, height]:
            r, t = list(topright)[0], b - height
        elif None not in [bottomright, height]:
            r, t = list(bottomright)[0], b - height
        else:
            return False

        if l < p0 < r and t < p1 < b:
            return True
    elif bottomright is not None:
        r, b = bottomright
        if topleft is not None:
            l, t = topleft
        elif None not in [width, height]:
            l, t = r - width, b - height
        elif None not in [topright, width]:
            l, t = r - width, list(topright)[1]
        elif None not in [bottomleft, height]:
            l, t = list(bottomleft)[0], b - height
        else:
            return False

        if l < p0 < r and t < p1 < b:
            return True

    return False

def end(msg=""):
    quit()
    exit(msg)
