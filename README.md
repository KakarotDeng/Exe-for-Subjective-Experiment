# Exe-for-Subjective-Experiment
An executable file for subjective experiment

Structure:

-inputpage.py
--tablepage.py
---startmenu.py
----exppage.py

If you want to ensemble them into an exe file
Run : pyinstaller -F -w inputpage.py -p exppage.py -p inputa.py -p output.py -p start.py -p startmenu.py -p tablepage.py --hidden-import exppage --hidden-import inputa --hidden-import output --hidden-import start --hidden-import startmenu --hidden-import tablepage
