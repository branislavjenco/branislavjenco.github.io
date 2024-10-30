---
layout: post
title: Escape key clears the mind
---

I've been a user of `vim` for many years. `vim` is a modal text editor. It uses "modes" that change what the keys on my keyboard do, in order to make writing and editing text more pleasant. There's a default one for moving around and typing commands (Normal mode), one for selecting text (Visual mode), one for actually typing (Insert mode), etc. I would define a modal user interface as one where, at any point in time, we find ourselves in some specific "mode" of operation that changes what the available set of inputs do. This lets us do more things with a limited number of inputs. [^1]

While `vim` is a known example to developers, most people are familiar with the `Caps Lock` key. That is also an example of a modal interface, where tapping it lets me type capital letters. Video games often have similar systems as they try to map more actions on a limited number of buttons on a controller. Even something like using `Shift` to type capital letters is a mode, but because it's toggled by holding a key, I might not consider this as modal UI in the same sense. The physical sensation of holding the button is a strong anchor for my brain to know we are in "capitals" mode. [^2]

Without an anchor, using modes adds cognitive overhead, because I have to track which mode I am in. That's why `Caps Lock` often has an indicator light on keyboards and why `vim` shows the current mode in the bottom bar. I'd argue those are band-aids. While touch typing, I want to look at what I'm doing and looking at some indicator of the current mode is a distraction. But it's not that hard to lose track and of your current mode and suddenly the numbers type symbols, entire lines get deleted, hell breaks loose. 

As users of `vim` probably know there is a savior, which is the `Esc` key (unless you remapped it to something else, ironically `Caps Lock` is a nice alternative). If `vim` starts doing something unexpected, I can just mash the `Esc` key a couple times and I know I'm back to Normal mode, and can work with a clean slate, blissfully forgetting how I found myself in this mess. It's a reset.

To reduce the cognitive overhead, it's very useful when a modal UI has a quick way to getting back to some "initial state".[^3] In `vim`  Normal mode is the default. The important bit here is that I can mash  `Esc` to "really make sure" that I'm back to Normal mode. If in Normal mode, hitting `Esc` again does nothing. Pressing `Esc` is _idempotent_. This removes the need for a feedback loop (check the mode -> do a thing), which lets us get _really_ fast with the UI. It also frees the mind to think about the important parts, i.e. the text itself.

This is one of the reasons why I always hated `Caps Lock` &mdash; it's a toggle, so pressing it multiple times keeps switching modes and you can never rely on it unless you check what mode you're in.

---
&nbsp;  

[^1]: There's other philosophies as well, such as use chording (holding a modifier key and then another key, think `Ctrl+c`) or combos (tapping multiple keys at the same time).

[^2]: I've always wanted to experiment with different physiological or audiovisual anchors. Imagine playing different types of background music based on your vim mode, or an chair-mounted actuator pushing into your back when Caps Lock is turned on.

[^3]:Something similar could be said about any stateful system, like your computer, for example. The reason rebooting tends to help fix problems is that we are going back to some initial state (hopefully), throwing the accumulated cruft and problems away. And rebooting is idempotent as repeating it isn't going to change what initial state you get into (at least in principle).
