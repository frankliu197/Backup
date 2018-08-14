
How to install this keyboard:

If you want to learn how to set up your own keyboard, click here.
Otherwise follow the instructions to set up the keyboard with default configurations.
  
1. install uim (Universal Input Manager) on your Linux system. On Ubuntu, run:
      sudo apt install uim

2. Add the following lines to your ~/.profile
      # Use uim instead of ibus or fcitx
      # Allows you to use the custom keyboard combinations
      export GTK_IM_MODULE=uim
      export QT_IM_MODULE=uim

3. Move the keyboard settings files to thier proper place:
      sudo cp us /usr/share/X11/xkb/symbols/us
      sudo cp .XCompose ~/.XCompose

4. In evdev.xml, inside the <layout> with the configItem us, e.g. 
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

    add the following the the variant list:
        <variant>
          <configItem>
            <name>custom_us</name>
            <shortDescription>Custom US Keyboard</shortDescription>
            <description>Custom US Keyboard</description>
          </configItem>
        </variant>

   Then in evdev.lst, under 
! variant
   add: 
  custom_us       us: English (Custom)
  
    You may have to do the same thing for base.xml and base.lst

5. Restart several services (Note: you will log out)
      setxkbmap
      sudo systemctl restart lightdm

6. The custom-us keybaord should pop up as one of the keyboards in Settings→ Keyboards. Add the keyboard layout to your layout list and enjoy!
