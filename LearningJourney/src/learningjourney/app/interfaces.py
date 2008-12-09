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


from learningjourney.i18n import _
from learningjourney.schema.html import Html
from learningjourney.schema.multioptchoice import MultiOptionalChoice
from zope.app.container.constraints import contains, containers
from zope.interface import Interface, Attribute
from zope.schema import BytesLine, TextLine


class ILearningJourneyApplication(Interface):
    """A site that holds learning journeys for users"""

    
class IUserHome(Interface):
    """A home for the items of one user"""
    
    contains('ILearningEntry')


class ILearningEntry(Interface):
    """An item holds information about learning"""
    
    text = Html(title=_(u"Text"), required=True)
    tags = MultiOptionalChoice(
                title=_(u"Tags"),
                value_type=TextLine(title=_(u"Tag")),
                required=True,
                vocabulary="lj.tags"
            )
    
    containers(IUserHome)


class IPortalContent(Interface):
    """Holds information about the metadata of a portal content item (object)"""
    
    name = Attribute(u"Object name")


class IRegistrations(Interface):
    """Provide self-registration functionality.

    Registrations are done for users giving their email address and
    possibly more data.

    A registration requires confirmation by the user. For this we
    send an email containing a confirmation link to his address.

    Upon opening the link a RegistrationConfirmedEvent is sent out
    and the application can perform whatever is necessary to active
    the user's account.

    After the successful confirmation the intermediate registration
    object is deleted.

    """

    def register(email, data=None):
        """Create a new registration for the given email address and
        data.

        Sends out an ObjectAddedEvent for the newly created
        IRegistration object.
        """

    def confirm(hash):
        """Confirm the registration identified by the hash.

        If successful sends out an IRegistrationConfirmed event.
        """


class IRegistration(Interface):
    """A registration."""

    hash = BytesLine(title=u"A hash identifying this registration",)
    email = TextLine(title=u"The email for sending the confirmation mail to.")
    data = Attribute(u"Application-specific registration data.")
    
    
class IConfirmationEmail(Interface):
    """An email to confirm a registration."""

    message = Attribute("A string containing an RFC 2822 message.")