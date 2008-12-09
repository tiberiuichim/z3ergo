##############################################################################
#
# Copyright (c) 2008 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################

from learningjourney.app.config import EMAIL_TEMPLATE
from learningjourney.app.interfaces import IConfirmationEmail, IRegistration, \
    IRegistrations
from learningjourney.app.util import get_site_url
from persistent import Persistent
from zope.app.authentication.principalfolder import InternalPrincipal
from zope.app.container.btree import BTreeContainer
from zope.app.container.contained import Contained
from zope.app.container.interfaces import INameChooser
from zope.app.security.interfaces import IAuthentication
from zope.component import adapts, getUtility
from zope.interface import implements
from zope.app.component.hooks import getSite
from learningjourney.app.userhome import UserHome
from zope.securitypolicy.interfaces import IPrincipalRoleManager
import datetime
import sha


class Registration(Contained, Persistent):

    implements(IRegistration)

    def __init__(self, hash, email, data):
        self.hash = hash
        self.email = email
        self.data = data
        
        
class Registrations(BTreeContainer):

    implements(IRegistrations)

    def _createHash(self, email, data=None):
        return sha.new(email + datetime.datetime.now().isoformat()).hexdigest()

    def register(self, email, data=None, factory=Registration):
        """Create a new registration for the given email address and data."""
        hash = self._createHash(email, data)
        self[hash] = registration = factory(hash, email, data)
        return registration

    def confirm(self, hash):
        """Confirm the registration identified by the hash."""
        registration = self[hash]
        data = registration.data
        util = getUtility(IAuthentication)
        members = util['members']
        username = data['username']
        if username in members:
            raise ValueError("Username already registered")
        ip = InternalPrincipal(login=username,
                               password=data['password'],
                               title=username)
        #XXX: there's a possibility for subtle bugs here
        name = INameChooser(members).chooseName(username, ip)   
        members[name] = ip
        
        site = getSite()
        site[name] = uh = UserHome()
        IPrincipalRoleManager(uh).assignRoleToPrincipal('lj.Owner', username)
        del self[hash]


class ConfirmationEmail(object):
    """A basic confirmation email."""

    adapts(IRegistration)
    implements(IConfirmationEmail)
    
    addr_from = "Ad Ministrator <admin@example.com>"
    confirmation_url = "%s/@@confirm.html?hash=%s"

    def __init__(self, registration):
        self.message = EMAIL_TEMPLATE % {
            'to': registration.email,
            'from': self.addr_from,
            'link': self.confirmation_url % (get_site_url(), registration.hash)}