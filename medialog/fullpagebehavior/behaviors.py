# -*- coding: utf-8 -*-
from plone.autoform.interfaces import IFormFieldProvider
from plone.directives import form
from zope import schema
from zope.interface import provider
 
from collective.z3cform.datagridfield import DataGridFieldFactory 
from collective.z3cform.datagridfield import DictRow
from plone.app.z3cform.wysiwyg import WysiwygFieldWidget	

from zope.i18nmessageid import MessageFactory
_ = MessageFactory('medialog.fullpagebehavior')
 
@provider(IFormFieldProvider)
class IPair(form.Schema):
    title = schema.TextLine(
        title=_(u"Title"),
        description=u"",
        required=False,
    )

    description = schema.Text(
        title=_(u"Title"),
        description=u"",
        required=False,
    )

    form.widget('body', WysiwygFieldWidget)
    body = schema.Text(
        title=_(u"Body text"),
        description=u"Body text",
        required=False,
    )

@provider(IFormFieldProvider)
class IFullpageBehavior(form.Schema):
    """Adds fields """

    form.widget(text_pairs=DataGridFieldFactory)
    text_pairs = schema.List(
        title = _(u"text_pairs", 
            default=u"Text pairs"),
        value_type= DictRow(schema=IPair),
        required=False
    )
    
  



 



       