## Introduction



## Installation

If you want to learn how to set up your own keyboard, click here.
Otherwise follow the instructions to set up the keyboard with default configurations.
WARNING: If you have made your own compose file or changed files in the xkb folder, you may have to tweak the steps below so it would be compatable with your current keyboard.

1. Download the keyboard source code into your computer.
```
git clone https://github.com/frankliu197/Compose 
cd Compose
```
2. Move the keyboard settings files onto your computer:
```
sudo cp us /usr/share/X11/xkb/symbols/us
ln -sf .XCompose ~/.XCompose
``` 
3. Change directory into /usr/share/X11/xkb/rules/ and change several configuration files
```
cd /usr/share/X11/xkb/rules
```
In /usr/share/X11/xkb/rules/evdev.xml, inside the \<layout\> with the configItem us, e.g. 
```xml
<layout>
  <configItem>
    <name>us</name>
    <shortDescription>en</shortDescription>
    <description>English (US)</description>
    <languageList>
      <iso639Id>eng</iso639Id>
    </languageList>
  </configItem>
  <variantList>
```
add the following the the variant list:
```xml
    <variant>
      <configItem>
        <name>custom_us</name>
        <shortDescription>Custom US Keyboard</shortDescription>
        <description>Custom US Keyboard</description>
      </configItem>
    </variant>
```
Then in evdev.lst, under 
```
! variant
```
   add: 
```
  custom_us       us: English (Custom)
```
You may have to do the same thing for base.xml and base.lst. A simple shortcut would be to execute the following two commands:
```
sudo cp /usr/share/X11/xkb/rules/evdev.lst /usr/share/X11/xkb/rules/base.lst
sudo cp /usr/share/X11/xkb/rules/evdev.xml /usr/share/X11/xkb/rules/base.xml
```

4. Install uim (Universal Input Manager) on your Linux system. On Ubuntu, run:
```
sudo apt install uim
```
5. Add the following lines to your ~/.profile
```
# Use uim instead of ibus or fcitx
# Allows you to use the custom keyboard combinations
export GTK_IM_MODULE=uim
export QT_IM_MODULE=uim
```

4. 5. Restart several services (Note: you will log out)
```
setxkbmap
sudo systemctl restart lightdm
```
6. The custom-us keyboard should pop up as one of the keyboards in Settings→ Keyboards. Add the keyboard layout to your layout list and enjoy!

## Usage
