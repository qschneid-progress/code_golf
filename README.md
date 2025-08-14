# How to kill a joke
### ...or Jason really is the smarter one here

Contains three submissions. Please grade according to your understanding of the rules.

If input files **never** contain trailing spaces, only digits separated by newlines:
```sh
$ python3 149.py <<filename>>
```
If input files **can** contain trailing spaces, and lines need to be stripped before parsing:
```sh
$ python3 152.py <<filename>>
```
If whitespace truly doesn't count, no matter what:
```sh
$ python3 cheating.py <<filename>>
```
If you don't want to run an `exec` blob for fear of having a rootkit installed, and would instead like to compile your own whitespace bomb:
```sh
$ python3 how_to_cheat.py 152.py > runme.py
$ python3 runme.py <<filename>>
```
You can also swap the `exec` for `print` to see what you'll be running before you run it.
