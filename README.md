<link rel="stylesheet" href="Markdown.css">
## Introduction

This keyboard is designed for people who:
  - Want to type accents with latin characters for French, Spanish, Portegueuse, or even Chinese Pinyin
  - Want to type Math, Physics and Currency symbols
  - And would like to use the keyboard without changing their typing habits

If any of them match what you are looking for, keep reading:

This keyboard uses the default US keyboard as its base layout; Any key that you press on the US keyboard remain the same key on this keyboard. All the additional fancy characters
are created with an third level shift and a compose key. 

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


Usage and Installation instructions are below:

## Usage: 

You certainly do not need to remember this to use it, but it is a nice reference. Here are the images of the keyboard in the third-level shift and fourth level shift:

**Third Level Shift (default: Right-Alt):**

**Fourth Level Shift (default: Right-Alt + Shift):**

You will notice these keyboard will contain almost no keys that I have specified in the introduction. I have mapped most of those keys through dead keys (mapped in gray above) and through the compose key, so it would be easy to remember how to type them in.

**DEAD KEYS:**  
Dead keys are similar to another modifier key (like shift), but are only for a certain purpose:
- dead\_inverted (Right-Alt <span>+</span> -): Inverts the keys upside down, but not left and right  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e.g.  dead\_inverted + A → ∀  
- dead\_miscellaneous (Right-Alt <span>+</span>  \_): Maps several keys that can't really be composed. Currently only containing music keys.  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e.g. dead\_miscellaneous <span>+</span> e → ♪ (eighth note)
- dead\_superscript (Right-Alt <span>+</span> =): For superscript letters  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e.g. dead\_superscript <span>+</span> 1 → ¹  
- dead\_subscript (Right-Alt <span>+</span> +): For subscript letters  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e.g. dead\_subscript <span>+</span> 1 → ₁  
- dead\_currency: Maps currency symbols    
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e.g. dead\_currency <span>+</span> y → ¥ (yen symbol)  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dead\_currency <span>+</span> c → ¢ (cent symbol)  
- dead\_greek: For greek letters. Because there are letters in greek than one letter in greek that starts with the same letter (e.g. tau and theta),
some greek keys are not mapped in a position that is favourable.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e.g. dead\_greek <span>+</span> a → α (alpha)   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dead\_greek <span>+</span> G → Γ (capital gamma, γ)    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dead\_greek <span>+</span> t → τ (tau)   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dead\_greek <span>+</span> j → θ (theta)   

COMPOSE KEY:  
Compose keys will combine a combination of keys graphically to form another character.   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e.g. compose <span>+</span> equal <span>+</span> underscore <span>+</span> space →  ≡     
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;compose <span>+</span> less <span>+</span> underscore <span>+</span> space → ≤    
On the default Ubuntu, compose keys also compose keys that logically work together, but this is no longer true   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e.g. compose <span>+</span> equal <span>+</span> less <span>+</span> space ↛  ≤    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;compose <span>+</span> ^ <span>+</span> 1 <span>+</span> space ↛ ¹    
The key order you press is very important. The order of keys you must press for your character must start from left to right, and top to bottom.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e.g. compose <span>+</span> minus <span>+</span> plus <span>+</span> space → ∓   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;compose <span>+</span> plus <span>+</span> minus <span>+</span> space → ±  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;compose <span>+</span> macron <span>+</span> diaeresis <span>+</span> u → ṻ   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;compose <span>+</span> diaeresis <span>+</span> macron <span>+</span> u → ǖ  
Because the key order of some characters is slightly ambigious, there are multiple key combinations to make the same symbol. In these cases, as long as you don't stray too far from the rules outlined here, you should have no problem writing your symbol of desire.    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e.g. compose <span>+</span> bar <span>+</span> slash <span>+</span> space = compose <span>+</span> slash <span>+</span> bar <span>+</span> space → ∤  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;compose <span>+</span> equal <span>+</span> underscore <span>+</span> space = compose <span>+</span> underscore <span>+</span> equal <span>+</span> space ↛ ≡  
The key order of slash is slight special. Similar to the dead\_key, the slash will only slash out the next key. If you want to slash out the whole combination, you must press slash last.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e.g. compose <span>+</span> tilde <span>+</span> slash <span>+</span> equals <span>+</span> space → ≆  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;compose <span>+</span> tilde <span>+</span> equals <span>+</span> slash <span>+</span> space → ≇  
When typing in any non-latin characters with the compose key (like punctuation or math operators), you will need to finish your combination with the space key. This is to prevent longer compose key sequences from overriding the shorter ones
such as ≤ and ≰ (the second being just a slash more).  
Finally, you may notice that there are two slashes, the normal slash (/) and the division\_slash (∕, Right Alt <span>+</span> .). Use compose with division slash for all division related keys, and use the slash otherwise.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e.g. compose <span>+</span> 1 <span>+</span> division\_slash <span>+</span> 3 <span>+</span> space → ⅓     


WHEN USING DEAD KEYS IN COMBINATION WITH COMPOSE KEYS:  
Note that the dead_key only modifies the next key. Thus the dead_inverted in the combination below:   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;compose <span>+</span> dead_inverted <span>+</span> ? <span>+</span> !   
will only invert the question mark, and not the exclamation mark. However, you could use   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;compose <span>+</span> dead_inverted <span>+</span> ? <span>+</span> dead_inverted <span>+</span> !   to invert both keys.  
Always start with the compose key if you are planning to do a composition of keys. It does not matter whether your key combination contains dead keys or not.  

OTHER FUNCTIONS:
For convienence purposes, the compose key will print out a long phrase when used with only letter first. These combinations created to type phrases you type often faster.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e.g. compose <span>+</span> g <span>+</span> p → git push origin master      (g for git and p for push)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;compose <span>+</span> j <span>+</span> p → System.out.println(         (j for java and p for print)  
These key combinations are easily editable in the Compose file.  

Visit my tutorial here to learn how to edit your custom keyboard in more detail.  


## Installation

If you want to learn how to set up your own keyboard, click here.  
Otherwise follow the instructions below to set up the keyboard with default configurations.  
WARNING: If you created/edited the files: /usr/share/X11/xkb/symbols/us or ~/.XCompose, blindly following the steps below will delete all your custom configurations. You will need to tweak the steps below so it would be compatable with your current keyboard.  

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

6. Reset/restart two services:
Reset your xkb service
```
setxkbmap
```
and use one of the two commands below to restart your X sessions:
```
sudo systemctl restart lightdm
sudo service lightdm restart
sudo pkill X
```
If none of these commands work, you may not be able to install this keyboard. However, try restarting your computer and continue to the next step of your installation process.

7. And you are done installing! The custom-us keyboard should now pop up as one of the keyboards in Settings→ Keyboards. Add the keyboard layout to your layout list to use it!
