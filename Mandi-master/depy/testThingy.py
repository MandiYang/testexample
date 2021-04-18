
import gi
if gi.require_version("Gtk", "3.0") == None:
    print('OK')
from gi.repository import Gtk

window = Gtk.Window(title="Hello World")
window.show()
window.connect("destroy", Gtk.main_quit)
Gtk.main()

