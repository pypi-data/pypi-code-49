# -*- coding: utf-8 -*-
from kitconcept.richpage import _
from zope import schema
from zope.interface import Interface
from plone.dexterity.content import Item
from zope.interface import implementer
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

align = SimpleVocabulary(
    [SimpleTerm(value=u'left', title=_(u'Left')),
     SimpleTerm(value=u'right', title=_(u'Right'))]
    )


class IImage(Interface):

    title = schema.TextLine(
        title=_(u"Title"),
        required=False,
    )

    align = schema.Choice(
            title=_(u"Align"),
            vocabulary=align,
            required=False,
        )


@implementer(IImage)
class Image(Item):
    """ The Image content type """
