from zope.component import adapts
from zope.interface import Interface
from zope.publisher.interfaces.browser import IBrowserView
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from plone.app.portlets.manager import ColumnPortletManagerRenderer
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from msd.footerportlet.browser.interfaces import IFooterPortletManager

class FooterPortletRenderer(ColumnPortletManagerRenderer):
    """
    A renderer for the content-well portlets
    """
    adapts(Interface, IDefaultBrowserLayer, IBrowserView, IFooterPortletManager)
    template = ViewPageTemplateFile('templates/renderer.pt')
