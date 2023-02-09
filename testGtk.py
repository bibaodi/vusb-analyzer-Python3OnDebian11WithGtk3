import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk as gtk

all=dir(gtk.Layout)
for i in all:
    if i.find("FILL") >=0:
        print(i)

