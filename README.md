## Introduction

This keyboard is designed for people who:
  - Want to type accents with latin characters for French, Spanish, Portegueuse, or even Chinese Pinyin
  - Want to type Math, Physics and Currency symbols
  - And would like to use the keyboard without changing their typing habits

If any of them math what you are looking for, keep reading:

This keyboard uses the default US keyboard as its base layout; Any key that you press on the US keyboard remain the same key on this keyboard. All the additional fancy characters
are created with an third level shift and a compose key (Right alt and Right control by default).

Here are the following additions:
  - Type any combination of the following accents: acute, breve, caron, cedilla, circumflex, diaeresis, grave, macron, tilde
    e.g. ẍ, ṕ, ṻ and even ǖ
  - Type all greek letters
    e.g. υ, α, β
  - Type special symbols
    e.g. ¥, ¶, µ, ¿, °
  - Type all the math symbols you probably need (create a pull request if I am missing any)
    e.g. ≡, ∀, ≋, ≩, ⊊, ∰, ¾
  - Type superscripts and subscripts
    e.g. ⁴, ⁺, ₀ 
  - Type letters surrounded by a circle
    e.g. ⓔ

How to use: 

You certainly do not need to remember this to use it, but it is a nice reference. Here are the images of the keyboard in the third-level shift and fourth level shift:


You will notice these keyboard will contain almost no keys that I have specified above. I have mapped most of those keys through dead_keys (mapped in gray above) and through the compose key, so it would be easy to remember how to type them in.
:
The following dead_keys which are remapped from its original purpose: 
dead_hook → dead_inverted: Inverts the keys (inverts up and down but not left and right)
dead_horn → dead_other: For miscellaneous symbols
dead_abovedot → dead_superscript: superscripts
dead_belowdot → dead_subscript: subscripts

INSTRUCTIONS:
- The functionality of the Compose Key is now very specific. The compose key will only combine keys together if they can form a key graphically.
e.g. <compose> <equal> <underscore> →  ≡      and  <compose> <less> <underscore> → ≤ 
It will no longer compose keys that logically work together:
e.g. <compose> <equals> <less> ↛  ≤ 
- The key order you press is very important. The order of keys you must press for your character must start from left to right, and top to bottom.
e.g. <compose> <minus> <plus> →   ∓             and  <compose> <plus> <minus> → ±
<compose> <less> <minus> →   ←
<compose> <macron> <diaeresis> <u> → ṻ     and  <compose> <diaeresis> <macron> <u> → ǖ
- The key order of some characters however, is slightly ambigious. In those cases, all the key orders will work as long is it doesn't stray too far from the rules outlined above.
e.g. <compose> <bar> <slash> = <compose> <slash> <bar> → ∤
- When typing in punctuation or math operators, you will need to press the enter key when using the compose key, which is space. This is to prevent longer compose key sequences from overriding the shorter ones
such as ≤ and ≰ (the second being just a slash more). Thus for all the examples above except ǖ and ṻ, you will need a to add a space key.
- The division_slash (∕ alt-Gr + .) is used for all division, otherwise the slash is used.
e.g. <compose> <1> <division_slash> <3>   → ⅓    
- The dead_key will only modify the next key.
Thus: 
<dead_inverted> <?> <!> 
will only invert the question mark, and not the exclamation mark
However, you could use 
<dead_inverted> <?> <dead_inverted> <!> 
to invert both keys
- Similar to the dead_key, the slash will only be used on the next key. If you want to slash out the combinations of all the keys before it, you must press slash last.
e.g. <compose> <tilde> <slash> <equals> → ≆      and <compose> <tilde> <equals> <slash> → ≆
- For convienence purposes, the compose key will print out a long phrase when used with letter first. These combinations created to type phrases you often type faster.
e.g. <compose> <g> <p> → git push origin master      (g for git and p for push)

All the key combinations are highly editable. Visit: to learn how.




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
