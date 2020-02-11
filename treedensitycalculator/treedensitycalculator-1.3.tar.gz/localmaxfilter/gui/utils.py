# -*- coding: utf-8 -*-
import os
import sys
from qgis.PyQt.QtXml import QDomDocument
from qgis.PyQt import uic
from re import findall
from io import StringIO


# dictionary to store form classes and avoid multiple calls to read <my_ui>.ui
FORM_CLASSES = dict()


def load_ui_from_class(path_ui: str):
    """
    Loads Qt UI files (*.ui) while taking care on QgsCustomWidgets.
    Uses PyQt4.uic.loadUiType (see http://pyqt.sourceforge.net/Docs/PyQt4/designer.html#the-uic-module)

    :param path_ui: *.ui file path
    :return: the form class, e.g. to be used in a class definition like MyClassUI(QFrame, loadUi('my_ui.ui'))
    """

    assert os.path.exists(path_ui), '*.ui file does not exist: {}'.format(path_ui)

    if path_ui not in FORM_CLASSES.keys():
        # parse *.ui xml and replace *.h by qgis.gui
        doc = QDomDocument()

        # remove new-lines. this prevents uic.loadUiType(buffer, resource_suffix=RC_SUFFIX) to mess up the *.ui xml

        f = open(path_ui, 'r')
        txt = f.read()
        f.close()

        dir_ui = os.path.dirname(path_ui)

        locations = []
        for m in findall(r'(<include location="(.*\.qrc)"/>)', txt):
            locations.append(m)

        removed = []
        for t in locations:
            line, path = t
            if not os.path.isabs(path):
                p = os.path.join(dir_ui, path)
            else:
                p = path

            if not os.path.isfile(p):
                txt = txt.replace('<iconset resource="{}">'.format(path), '')
                txt = txt.replace('<include location="{}">'.format(path), '')
                removed.append(t)

        if len(removed) > 0:
            print('None-existing resource file(s) in: {}'.format(path_ui), file=sys.stderr)
            for t in removed:
                line, path = t
                print('\t{}'.format(line), file=sys.stderr)
            print(txt)

        doc.setContent(txt)

        # Replace *.h file references in <customwidget> with <class>Qgs...</class>, e.g.
        #       <header>qgscolorbutton.h</header>
        # by    <header>qgis.gui</header>
        # this is require to compile QgsWidgets on-the-fly
        element_custom_widget = doc.elementsByTagName('customwidget')
        for child in [element_custom_widget.item(i) for i in range(element_custom_widget.count())]:
            child = child.toElement()
            class_name = str(child.firstChildElement('class').firstChild().nodeValue())
            if class_name.startswith('Qgs'):
                class_header = child.firstChildElement('header').firstChild()
                class_header.setNodeValue('qgis.gui')

        # collect resource file locations
        element_include = doc.elementsByTagName('include')
        qrc_paths = []
        for i in range(element_include.count()):
            node = element_include.item(i).toElement()
            l_path = node.attribute('location')
            if len(l_path) > 0 and l_path.endswith('.qrc'):
                if not os.path.isabs(l_path):
                    p = os.path.join(dir_ui, l_path)
                else:
                    p = l_path
                qrc_paths.append(p)

        buffer = StringIO()  # buffer to store modified XML
        buffer.write(doc.toString())
        buffer.flush()
        buffer.seek(0)

        # make resource file directories available to the python path (sys.path)
        temp_dirs = []
        for qrc_path in qrc_paths:
            d = os.path.abspath(os.path.join(dir_ui, qrc_path))
            d = os.path.dirname(d)
            if d not in sys.path:
                temp_dirs.append(d)
        sys.path.extend(temp_dirs)

        # load form class
        try:
            form_class, _ = uic.loadUiType(buffer)
        except SyntaxError:
            form_class, _ = uic.loadUiType(path_ui)

        buffer.close()
        FORM_CLASSES[path_ui] = form_class

        # remove temporary added directories from python path
        for d in temp_dirs:
            sys.path.remove(d)

    return FORM_CLASSES[path_ui]
