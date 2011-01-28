import os.path
import zope.interface

from plone.z3cform.templates import ZopeTwoFormTemplateFactory
from plone.z3cform.interfaces import IFormWrapper

from pmr2.app.browser.layout import FormWrapper


class IMathJaxLayoutWrapper(IFormWrapper):
    """
    The interface for the MathJax layout wrapper.
    """


path = lambda p: os.path.join(os.path.dirname(__file__), p)

mathjax_layout_factory = ZopeTwoFormTemplateFactory(
    path('mathjax_layout.pt'), form=IMathJaxLayoutWrapper)


class MathJaxLayoutWrapper(FormWrapper):

    zope.interface.implements(IMathJaxLayoutWrapper)
