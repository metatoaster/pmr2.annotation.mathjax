import zope.interface

from pmr2.app.annotation.note import ExposureFileNoteBase
from pmr2.annotation.mathjax.interfaces import IMathJaxNote


class MathJaxNote(ExposureFileNoteBase):

    zope.interface.implements(IMathJaxNote)
