Creating a basic zope3 skin.
------------------------------

* browser skins and layers are just interfaces
* browser layers inherit from IBrowserRequest
* browser skins are a collection of (inherit) layers, IDefaultBrowserLayer and other skin
* to provide a name for a skin, a named utility is created (with <interface /> in configure.zcml
* a new resource was added (browser:resource declaration)
* resources, pages and views are registered to layers (which are identified by their class name )
* the skin inherits from Rotterdam, which means it gets just one small change
  (the blue background color - force refresh browser to view)
* to see the skin look at http://localhost:8080/++skin++DemoSkin/@@contents.html




Technical documentation: (What's new in Zope 3)
==================================================

Skins are technically interfaces defined using zope.interface. To create a custom skin it is always better to inherit from a standard skin interface. It is by convention that skins will be created in sub-package named skin in your browser package of your main package. For example if your package name is foo, then foo.browser.skin will be the skin package, but this is not mandatory. Your skin interfaces can be defined in foo.browser.skin.interfaces. Here is an example interfaces.py:

from zope.app.rotterdam import Rotterdam

class IShanghaiSkin(Rotterdam):
  """Wo zhu zai Shanghai"""

To register this we will use interface and utility directives in zope namespace. The type of the IShanghaiSkin? skin is zope.publisher.interfaces.browser.IBrowserSkinType?. Here is a sample configure.zcml:

<interface
    interface=".interfaces.IShanghaiSkin"
    type="zope.publisher.interfaces.browser.IBrowserSkinType"
    />

<utility
    component=".interfaces.IShanghaiSkin"
    provides="zope.publisher.interfaces.browser.IBrowserSkinType"
    name="ShanghaiSkin"
    />

As a shortcut, we can also just use the interface directive and pass the new name parameter. The following one directive has the same effect as the two above regarding the skin registration:

<interface
    interface=".interfaces.IShanghaiSkin"
    type="zope.publisher.interfaces.browser.IBrowserSkinType"
    name="ShanghaiSkin"
    />

Registering views and resources is not any different now, but you can simply register them on the skin directly:

<browser:resource
    name="zope3logo.gif"
    file="shanghailogo.gif"
    layer=".interfaces.IShanghaiSkin"
    />

As you can see, we don't have to create an extra layer just to create a custom skin. We were also able to use standard Component Architecture ZCML directives instead of custom ones whose special syntax the developer needs to remember additionally.

A typical browser:page with with layer specified is like this:

<browser:page
    for="*"
    name="dialog_macros"
    permission="zope.View"
    layer=".interfaces.IShanghaiSkin"
    template="dialog_macros.pt"
    />




Simplify skinning proposal
==============================

Simplify skinning
Author

Philipp von Weitershausen, philikon@philikon.de
Status

IsProposal
Version

4
Original

http://codespeak.net/svn/user/philikon/SimplifySkinning.txt
Current situation

Being inspired by the CMF, Zope 3 has a system for customizing browser views by overriding existing ones. This system is based on two concepts:

    * Layers are interfaces extending IBrowserRequest. Views can be registered for a certain layer by being registered for the layer interface as request type instead of a mere IBrowserRequest request type. If no layer is specified, the IDefaultLayer layer is assumed.

      Layers are distinguished from regular interfaces by providing the ILayer interface which extends IInterface.
    * Skins are interfaces that aggregate one or more layers by simply extending the layer interfaces. The order of the interface inheritance defines the layer ordering inside the skin. Skin interfaces obviously also extend IBrowserRequest, if not directly then indirectly. Request objects can be marked with a skin by directly providing it. This can happen through various methods, e.g. setting a default skin or the ++skin++ namespace traverser.

      Skins are distinguished from regular interfaces by providing the ISkin interface which extends IInterface.

Both layers and skins can have simple aliases with which they can be referred to in ZCML, e.g. default for the IDefaultLayer layer or Rotterdam for the zope.app.rotterdam.Rotterdam skin. These aliases are also used by the ++skin++ namespace traverser. The layer/skin machinery uses the utility registration to look up layers and skins by their simple aliases.

Layers and skins don't necessarily have to be created in Python code. The browser:layer and browser:skin ZCML directives can create the interfaces on the fly, though in which case they won't be available for import in Python, though. In such case they will be registered with the utility registration as a named utility with their simple alias as the name.
Example

In order to customize an existing skin, say Rotterdam, you currently have to register a new layer. A typical usage would be to use the simple alias as an identifier and not construct it in Python code:

      <browser:layer name="shanghai_layer" />

Then you have to make a skin based on Rotterdam's layer and the new layer. Again, typical use-cases don't create the skin in Python code:

      <browser:skin
          name="ShanghaiSkin"
          layers="shanghai_layer rotterdam default"
          />

Now you can register views and resources that are available in the new skin. You have to put them on the layer, though:

      <browser:resource
          name="zope3logo.gif"
          file="shanghailogo.gif"
          layer="shanghai_layer"
          />

You will see your new skin with its custom logo by putting /++skin++ShanghaiSkin/ in your URL.
Problem

From a technical point of view, the distinction that layers are interfaces for which views are registered whereas skins are interfaces with which views are looked up seems arbitrary. It is also unnecessarily complicated. (From an end-user point of view, this distinction might still be wanted, but this doesn't mean the implementation behind it has to reflect that.)

Imagine you want to customize a few views on an existing skin (this is a common deployment problem). You would do, as above in the example,

    * create a new layer,
    * register your views for this layer,
    * then create a new skin based on your new layer and the layers of the skin you want to customize.

Why couldn't you simply create a skin that extends the old skin? And why coudln't you simply register your views on that custom skin of yours directly? Why do you have to do it on a layer?

Having to go through the extra hoops of making a layer that only serves the creation of a new skin is an unnecessary indirection. Seeing that the shanghai_layer from the example above is related to the ShanghaiSkin might not seem obvious to all Zope 3 programmers (especially when the names are not as well chosen). Also, realizing that the browser:layer and browser:skin directives use interface semantics is also not easy to understand just from the usage of their directives.

That leads us to another aspect of indirection on a totally different level: In the end, layers and skins are nothing but interfaces. They are code constructs, they could possibly have docstrings, would want to show up in generated API documentation, etc. There is thus a strong reason to define these in Python directly. ZCML's task on the other hand is not to construct components but to take care of the wiring. ZCML hides the simplicity of layer and skins (they're simply marker interfaces on the request) through extra ZCML directives that are not necessary when standard Python code and simpler ZCML directives can take over.
Goals

    * Make the customization of existing skins easy and straight-forward without creating too many constructs just to satisfy the framework.
    * Retain the flexibility of grouping several layers into a skin, reusing layers from another skin, etc.
    * Still be able to distinguish between layers and skins for the end-user: Layers are an implementation detail that the end-user doesn't care about, skins represent the look-and-feel of an application and could be chosen explicitly by the end-user.
    * Make the creation and registration of layers and skins straight-forward for the Component Architecture programmer.

Proposal

I propose to get rid of skins as a separate type of component and simply use layers everywhere. Like views are special kinds of adapters, skins would still be around as a conceptual term. In the implementation they will only be special kinds of layers.

Layers, on the other hand, do not need to be specially identifiable. They are simple interfaces extending IBrowserRequest. They do not need an extra marker and needn't be known under a human-readable alias (as opposed to skins).
Architecture

    * Skins and layers will have to be defined through Python as regular interfaces, not through the browser:layer and browser:skin directives anymore. These will disappear.
    * Layers are simple interfaces extending IBrowserRequest, ILayer as a marker is removed and rendered useless. Layer interfaces will be identified (e.g. in ZCML) using their dotted import name.
    * The layer argument of browser ZCML directives will be deprecated in favour of a new type argument which will allow you to define the layer interface. This is in analogy to the type argument of the view directive adds some more consistency to the ZCML directives in Zope 3. It defaults to IDefaultLayer (like layer does currently) and only accepts interfaces that are or extend IBrowserRequest.
    * Layer interfaces that should also be available as skins can be marked with IBrowserSkinType (previously ISkin) and registered as named utility (very much like what browser:skin does currently).

      On the renaming of ISkin to 'IBrowserSkinType?': This is to indicate that a) the skins concept is browser-specific and b) this interface is an interface for interfaces (extending IInterface). Naming these interfaces ISomethingType (e.g. IContentType or IMenuItemType as well as queryType()) is an informal convention in Zope.
    * As a bonus, we will also provide a vocabulary called Browser Skin Names which returns the names of all available skins (=interfaces that provide IBrowserSkinType). This would simply be based on zope.app.component.vocabulary.UtilityVocabulary.
    * The ++skin++ namespace traverser will not change its behaviour.

Implementation and backward compatability plan
Changes in Zope 3.3:

    * zope.publisher.interfaces.browser.ISkin is renamed to IBrowserSkinType.
    * The type argument is introduced to ZCML browser directives.
    * The (optional) name argument is introduced to the interface directive.
    * The vocabulary Browser Skin Names is provided.

Deprecated in Zope 3.3/2.10 and slated for removal after 12 months (Zope 3.5/2.12):

    * the ILayer interface
    * the browser:layer, browser:skin ZCML directives
    * the layer argument to ZCML browser directives

Example

The skin customization from above will be much simpler to accomplish. You only have to create a new skin interface inheriting from Rotterdam's skin interface:

      from zope.app.rotterdam import Rotterdam

      class ShanghaiSkin(Rotterdam):
          """Wo zhu zai Shanghai"""

Of course, we still need to make this a proper skin (right now it's just an interface which puts it on the same level as layers) so that it's available under a human-readable name. We can do that in ZCML using two standard Component Architecture directives now:

      <interface
          interface=".interfaces.ShanghaiSkin"
          type="zope.publisher.interfaces.browser.IBrowserSkinType"
          />

      <utility
          component=".interfaces.ShanghaiSkin"
          provides="zope.publisher.interfaces.browser.IBrowserSkinType"
          name="ShanghaiSkin"
          />

As a shortcut, we can also just use the interface directive and pass the new name parameter. The following one directive has the same effect as the two above regarding the skin registration:

      <interface
          interface=".interfaces.ShanghaiSkin"
          type="zope.publisher.interfaces.browser.IBrowserSkinType"
          name="ShanghaiSkin"
          />

Registering views and resources is not any different now, but you can simply register them on the skin directly (notice the type parameter instead of layer):

      <browser:resource
          name="zope3logo.gif"
          file="shanghailogo.gif"
          type=".interfaces.ShanghaiSkin"
          />

As you can see, we didn't have to create an extra layer just to create a custom skin. We were also able to use standard Component Architecture ZCML directives instead of custom ones whose special syntax the developer needs to remember additionally.
Risks

    * Other applications could already have a vocabulary called Browser Skin Names defined. The result would be a conflict in the ZCML configuration.

Implementation status

This proposal has been implemented on the Zope 3 trunk, except:

    * the layer argument of browser directives wasn't renamed to type
    * a vocabulary of browser skins called Browser Skins was implemented instead of Browser Skin Names.

The Zope 2 (Five) implementation has yet to follow on the Five trunk.
Things that this proposal does not cover

    * Some people have expressed that the way the CMF skin machinery lets one drop resources and templates into a folder that represents a skin layer is vastly simpler than the tedious process of registering many resources at once in Zope 3. While this is probably true, improving the way resources are registered is out of scope of this proposal.
