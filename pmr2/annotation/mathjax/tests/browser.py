import zope.component
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile
from zope.publisher.browser import BrowserPage
from plone.z3cform import layout
from z3c.form.interfaces import IForm

from pmr2.app.exposure.interfaces import IExposureSourceAdapter
from pmr2.app.exposure.browser.browser import ExposureFileViewBase

from pmr2.annotation.mathjax.layout import MathJaxLayoutWrapper


class MathJaxTest(BrowserPage):
    """\
    The MathJax tester.
    """

    zope.interface.implements(IForm)

    template = ViewPageTemplateFile('mathjax_test.pt')

    def update(self):
        pass

    def render(self):
        return self.template()

MathJaxTestView = layout.wrap_form(MathJaxTest, 
    __wrapper_class=MathJaxLayoutWrapper)
