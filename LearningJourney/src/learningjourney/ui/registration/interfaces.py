from learningjourney.i18n import _
from zope.interface import Interface, invariant
from zope.schema import Password, TextLine, ValidationError


class IRegistrationSchema(Interface):
    username = TextLine(
                     title=_(u"Username"),
                     description=_(u"Please enter the desired username"),
                     required=True,
                     )
    password = Password(
                     title=_(u"Password"),
                     description=_(u"Provide a password. Minimum 5 characters"),
                     required=True,
                 )
    password_check = Password(
                     title=_(u"Check password"),
                     description=_(u"Repeat the entered password"),
                     required=True,
                 ) 
    email = TextLine(
                     title=_(u"Email address"),
                     description=_(u"Please provide your email address to which a"
                                   u"confirmation email will be sent to."),
                     required=True,
                     )
    
    @invariant
    def check_password(self):
        if self.password and self.password_check:
            if self.password != self.password_check:
                raise ValidationError("The password needs to be repeated on the two password fields")