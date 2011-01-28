import zope.interface
import zope.component

from pmr2.app.factory import named_factory
from pmr2.app.annotation.interfaces import *
from pmr2.app.annotation.annotator import ExposureFileAnnotatorBase

from pmr2.annotation.mathjax.interfaces import IMathJaxNote


class MathJaxAnnotator(ExposureFileAnnotatorBase):
    zope.interface.implements(IExposureFileAnnotator)

    title = u'MathML Viewer'
    label = u'MathML View'
    for_interface = IMathJaxNote

    def generate(self):
        return ()

MathJaxAnnotatorFactory = named_factory(MathJaxAnnotator)
