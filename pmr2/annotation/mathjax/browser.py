import zope.component
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile
from zope.publisher.browser import BrowserPage
from plone.z3cform import layout
from z3c.form.interfaces import IForm

from pmr2.app.exposure.interfaces import IExposureSourceAdapter
from pmr2.app.exposure.browser.browser import ExposureFileViewBase

from pmr2.annotation.mathjax.layout import MathJaxLayoutWrapper


class MathJaxNote(ExposureFileViewBase):
    """\
    The MathJax viewer class.
    """

    index = ViewPageTemplateFile('mathjax_index.pt')
    template = ViewPageTemplateFile('mathjax_text.pt')
    title = ViewPageTemplateFile('mathjax_title.pt')

    def source_uri(self):
        values = zope.component.getAdapter(
            self.context, IExposureSourceAdapter).source()
        exposure, workspace, path = values
        return '%s/@@rawfile/%s/%s' % (
            workspace.absolute_url(), exposure.commit_id, path)

    def content(self):
        a = zope.component.queryAdapter(self.context, IExposureSourceAdapter)
        if a:
            return a.file()


class DeferredMathJaxNote(MathJaxNote):

    index = ViewPageTemplateFile('deferred_mathjax_index.pt')
