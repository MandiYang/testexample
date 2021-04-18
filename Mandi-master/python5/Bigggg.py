#!/usr/bin/env python
# aptinstall.py
'''import random, tkinter as tk, MYexample, tkmacosx

counter = 0 
def counter_label(label):
  counter = 0
  def count():
    global counter
    counter += 1
    label.config(text=str(counter))
    label.after(1000, count)
  count()
 
 
root = tk.Tk()
root.title("Counting Seconds")
label = tk.Label(root, fg="dark green")
label.pack()
counter_label(label)
button = tkmacosx.Button(root, text='Stop', width=200, command=root.destroy,
							bg='#ADEFD1', 
            						fg='#00203F', borderless=1)
button.pack()
root.mainloop()'''

import apt
import sys

pkg_name = "hello"

cache = apt.cache.Cache()
cache.update()
cache.open()

pkg = cache[pkg_name]
if pkg.is_installed:
    print "{pkg_name} already installed".format(pkg_name=pkg_name)
else:
    pkg.mark_install()

    try:
        cache.commit()
    except Exception, arg:
        print >> sys.stderr, "Sorry, package installation failed [{err}]".format(err=str(arg))



