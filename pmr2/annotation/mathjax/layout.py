import os.path
import zope.interface
from Products.CMFCore.utils import getToolByName
from Products.PythonScripts.standard import url_quote
from Acquisition import aq_inner

from plone.z3cform.templates import ZopeTwoFormTemplateFactory
from plone.z3cform.interfaces import IFormWrapper

from pmr2.app.browser.layout import FormWrapper


class IMathJaxLayoutWrapper(IFormWrapper):
    """
    The interface for the MathJax layout wrapper.
    """


class IDeferredMathJaxLayoutWrapper(IFormWrapper):
    """
    The interface for the MathJax layout deferred wrapper.

    The rendering is deferred and controlled by the wrapped elements.
    """


path = lambda p: os.path.join(os.path.dirname(__file__), p)

mathjax_layout_factory = ZopeTwoFormTemplateFactory(
    path('mathjax_layout.pt'), form=IMathJaxLayoutWrapper)

deferred_mathjax_layout_factory = ZopeTwoFormTemplateFactory(
    path('deferred_mathjax_layout.pt'), form=IDeferredMathJaxLayoutWrapper)


class XMLCSSFormWrapper(FormWrapper):

    def xml_stylesheet(self):
        """Returns a stylesheet with all content styles"""

        registry = getToolByName(aq_inner(self.context), 'portal_css')
        registry_url = registry.absolute_url()
        context = aq_inner(self.context)

        styles = registry.getEvaluatedResources(context)
        skinname = url_quote(aq_inner(self.context).getCurrentSkinName())
        result = []

        for style in styles:
            if style.getMedia() not in ('print', 'projection') \
                    and style.getRel()=='stylesheet':
                src = '<?xml-stylesheet href="%s/%s/%s" type="text/css"?>' % \
                    (registry_url, skinname, style.getId())
                result.append(src)
        return "\n".join(result)


class MathJaxLayoutWrapper(XMLCSSFormWrapper):

    zope.interface.implements(IMathJaxLayoutWrapper)


class DeferredMathJaxLayoutWrapper(XMLCSSFormWrapper):

    zope.interface.implements(IDeferredMathJaxLayoutWrapper)
