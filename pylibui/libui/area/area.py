import ctypes
from .. import clibui


# ui.h L308 - L641
class uiArea(ctypes.Structure):
    pass


def uiAreaPointer(obj):
    return ctypes.cast(obj, ctypes.POINTER(uiArea))


class uiAreaHandler(ctypes.Structure):
    pass


class uiAreaMouseEvent(ctypes.Structure):
    pass


class uiAreaKeyEvent(ctypes.Structure):
    pass


# - void uiAreaSetSize(uiArea *a, int width, int height);
def uiAreaSetSize(a, width, height):
    clibui.uiAreaSetSize(a, width, height)


# - void uiAreaQueueRedrawAll(uiArea *a);
def uiAreaQueueRedrawAll(a):
    clibui.uiAreaQueueRedrawAll(a)


# - void uiAreaScrollTo(uiArea *a, double x, double y, double width, double height);
def uiAreaScrollTo(a, x, y, width, height):
    clibui.uiAreaScrollTo(a, x, y, width, height)


# - void uiAreaBeginUserWindowMove(uiArea *a);
def uiAreaBeginUserWindowMove(a):
    clibui.uiAreaBeginUserWindowMove(a)


# - void uiAreaBeginUserWindowResize(uiArea *a, uiWindowResizeEdge edge);
def uiAreaBeginUserWindowResize(a, edge):
    clibui.uiAreaBeginUserWindowResize(a, edge)


# - uiArea *uiNewArea(uiAreaHandler *ah);
def uiNewArea(area_handler):
    clibui.uiNewArea.restype = ctypes.POINTER(uiArea)
    clibui.uiNewArea.argtype = [ctypes.POINTER(uiAreaHandler)]
    return clibui.uiNewArea(area_handler)


# - uiArea *uiNewScrollingArea(uiAreaHandler *ah, int width, int height);
def uiNewScrollingArea(area_handler, width, height):
    clibui.uiNewScrollingArea.restype = ctypes.POINTER(uiArea)
    clibui.uiNewScrollingArea.argtype = [ctypes.POINTER(uiAreaHandler), ctypes.c_int, ctypes.c_int]
    return clibui.uiNewScrollingArea(area_handler, width, height)
