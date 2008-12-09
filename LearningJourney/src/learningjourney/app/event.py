from learningjourney.app.interfaces import ILearningJourneyApplication, \
    IRegistrations, IRegistration, IConfirmationEmail, IPortalContent,\
    ILearningEntry
from learningjourney.app.registration import Registrations
from learningjourney.catalog.keywordindex import KeywordIndex
from learningjourney.log import log
from zope.app.authentication.authentication import PluggableAuthentication
from zope.app.authentication.principalfolder import PrincipalFolder
from zope.app.authentication.session import SessionCredentialsPlugin
from zope.app.catalog.catalog import Catalog
from zope.app.catalog.field import FieldIndex
from zope.app.catalog.interfaces import ICatalog
from zope.app.catalog.text import TextIndex
from zope.app.component.site import LocalSiteManager
from zope.app.container.interfaces import IObjectAddedEvent
from zope.app.intid import IntIds
from zope.app.intid.interfaces import IIntIds
from zope.app.security.interfaces import IAuthentication
from zope.component import adapter, getUtility
from zope.index.text.interfaces import ISearchableText
from zope.sendmail.interfaces import IMailDelivery
from zope.session.interfaces import ISessionDataContainer
from zope.session.session import RAMSessionDataContainer

    
@adapter(ILearningJourneyApplication, IObjectAddedEvent)
def configure_site(site, event):
    log.info(u"Making %s a site manager..." % site)
    sm = LocalSiteManager(site)
    site.setSiteManager(sm)
    
    log.info(u'Creating registrations utility...')
    sm['registrations'] = Registrations()
    sm.registerUtility(sm['registrations'], IRegistrations)
    
    log.info(u"Creating authentication systems...")
    
    sm['session_data'] = RAMSessionDataContainer()
    sm.registerUtility(sm['session_data'], ISessionDataContainer)
    
    sm['authentication'] = PluggableAuthentication()
    sm.registerUtility(sm['authentication'], IAuthentication)
    sm['authentication']['session_credentials'] = SessionCredentialsPlugin()
    sm['authentication']['members'] = PrincipalFolder() 
    sm['authentication'].authenticatorPlugins = ('members',)
    sm['authentication'].credentialsPlugins = ('session_credentials',)
    
    log.info(u"Creating indexing system...")
    
    sm['intids'] = IntIds()
    sm.registerUtility(sm['intids'], IIntIds)
    
    sm['catalog'] = Catalog()
    sm.registerUtility(sm['catalog'], ICatalog)
    sm['catalog']['searchableText'] = TextIndex(field_name="getSearchableText",
                                                interface=ISearchableText,
                                                field_callable=True)
    sm['catalog']['name'] = FieldIndex("name", IPortalContent, False)
    sm['catalog']['tags'] = KeywordIndex('tags', ILearningEntry, False)
    
    
@adapter(IRegistration, IObjectAddedEvent)
def send_registration_mail(registration, event):
    """Listen for a registration and send a mail to the user, asking for
    confirmation.
    """
    email = IConfirmationEmail(registration)
    mailer = getUtility(IMailDelivery, name="lj-mailer")
    mailer.send(email.addr_from, [registration.email], email.message)