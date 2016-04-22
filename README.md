# To run in emacs
```
C-c  To execute
```

NOTE: matplot lib is tricky to run in virtual env!

If you are using a virtualenv (i.e. ~/.virtualenvs/yourenv)
```
;; Set the python interpretter (for when python is executed):
(setq python-shell-interpreter "/path-to-your-virtual-env/bin/python")

;; Set the jedi environment
(setq jedi:environment-root "/path-to-your-virtual-env")
```

# To run an ipython notebook (i.e. one of the ipynb files)...

Make sure jupyter is installed (i.e. `pip3 install jupyter`).
Then to start the jupyter server:
```
jupyter notebook
```
