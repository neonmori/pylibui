/**
 *  Python wrapper for libui.
 *
 */

#include "pylibui.h"
#include "objects.h"


static uiWindow *mainwin;

static int onClosing(uiWindow *w, void *data)
{
    uiControlDestroy(uiControl(mainwin));
    uiQuit();
    return 0;
}

static int shouldQuit(void *data)
{
    uiControlDestroy(uiControl(mainwin));
    return 1;
}

PyObject *
pylibui_test(PyObject *m)
{
    uiMenu *menu;
    uiMenuItem *item;
    uiBox *box;
    uiLabel *label;

    menu = uiNewMenu("File");
    item = uiMenuAppendItem(menu, "Item");
    item = uiMenuAppendQuitItem(menu);
    uiOnShouldQuit(shouldQuit, NULL);

    mainwin = uiNewWindow("Window", 640, 480, 1);
    uiWindowSetMargined(mainwin, 1);
    uiWindowOnClosing(mainwin, onClosing, NULL);

    box = uiNewVerticalBox();
    uiBoxSetPadded(box, 1);
    uiWindowSetChild(mainwin, uiControl(box));

    label = uiNewLabel("Hello, World!");
    uiBoxAppend(box, uiControl(label), 0);

    uiControlShow(uiControl(mainwin));

    Py_RETURN_NONE;
}

PyObject *
pylibui_test_show_window(PyObject *m, PyObject *args)
{
    py_uiWindow *window;

    if (!PyArg_ParseTuple(args, "O", &window))
        return NULL;

    mainwin = window->uiWindow;
    uiWindowOnClosing(mainwin, onClosing, NULL);
    uiControlShow(uiControl(mainwin));

    Py_RETURN_NONE;
}