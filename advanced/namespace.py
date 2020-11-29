# 3 個主要層級
# built-in Namespace (print...
# Module: Global Namespace (file
# Function: Local Namespace (

# LEGB
# L: local
# E: enclosed
# G: global
# B: built-in


x = 'global'  # global


def f1():
    # enclosed
    x = 'enclosed'

    def ff1():
        # local
        x = 'local'


def f2():
    y = 'local'
