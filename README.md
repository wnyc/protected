### Overview

Wouldn't it completely suck to accidentally leak sensitive configuration data like your AWS keys into the wild while running Django in DEBUG mode? 

Yes, Django protects your configuration variables from disclosure if
your variable name happens to match one of their "magic" pattersn like
"API" or "SECRET".  But good engineers don't depend on magic and that
particular bit of magic does little to protect your secrets once they
make it from your configuiration variables into the local varaibles in
your code, which Django also happily shares in debug mode.

Well, WNYC's new protected module puts an end to that problem.  

### Getting started

First, lets install protected.  Its already been uploaded to pypi, so you can just type this:

``` 
easy_install protected
```

Now lets look at how protected works. 

Normally when you create a seccret, its easily readable like this:

```
$ python
Python 2.6.5
Type "help", "copyright", "credits" or "license" for more information"
>>> secret = 'secret'
>>> secret
secret
```

That sort of sucks; ProtectedString tries to remedy this situation by
providing an alternative `__repr__` method for your secret so it isn't
disclosed.  Lets try it out

```
>>> from protected import ProtectedString
>>> secret = ProtectedString("uber secret")
>>> secret
>>> <Protected String #139757326589296 ***********>
```

Now you can get at the contents of this as a normal string if you really want like this:

```
>>> str(secret)
uber secret
```

So, what's happening?  A ProtectedString object is simply a superclass of a string with __repr__ overridden to prevent its display.   You can still convert it to a normal string to print its value by calling str() on it, which demotes it to a normal string.

But there's a little more happening under the hood than that.

```
>>> secret + "!"
<Protected String #139757326589392 ***********>
>>> str(secret + "!")
'uber secret!'
```

ProtectedString can survive basic operations against it.   Even this works

```
>>> very = "Very %s!" % secret
>>> very
<Protected String #139757326548616 ***********>
>>> str(very)
'Very uber secret!'
>>> 
```

There are some limits to ProtectedString's ability to obfuscate itself.   This operation does not protect the string:

```
>>> "%s" % (secret,)
uber secret
```

The difference likes in whom __rmod__ is called against. 


`"%s" % ProtectedString("secret")` calls ProtectedString's `__rmod__` method.   `"%s%" % (ProtectedString("secret"),)` doesn't.  

While imperfect, if we use this, it may decrease the surface area from
which secrets might leak.

Anyhow, I encourage you to play with this, apply it to our config
files and try to break it.  Please try to break it.  I look forward to
your feedback - Adam DePrince (@adamdeprince)



