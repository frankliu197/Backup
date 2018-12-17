#!/usr/bin/python3
# adds required code to files 
# really lazy implementation and are contributions welcome

import re

lookfor = """  <layoutList>
    <layout>
      <configItem>
        <name>us</name>
        <shortDescription>en</shortDescription>
        <description>English (US)</description>
        <languageList>
          <iso639Id>eng</iso639Id>
        </languageList>
      </configItem>
      <variantList>"""

add = """
        <variant>
          <configItem>
            <name>custom_us</name>
            <shortDescription>Custom US Keyboard</shortDescription>
            <description>Custom US Keyboard</description>
          </configItem>
        </variant>"""

xkbrules = '/usr/share/X11/xkb/rules/'
filename = xkbrules + 'evdev.xml'
text = open(filename).read()
with open(filename, 'w') as w:
    w.write(text.replace(lookfor, lookfor + add)) #inswert the required text

lookfor = '! variant'
add = '
  custom_us       us: English (Custom)'

filename = xkbrules + 'evdev.lst'
text = open(filename).read()
with open(filename, 'w') as w:
    w.write(text.replace(lookfor, lookfor + add)) #inswert the required text


