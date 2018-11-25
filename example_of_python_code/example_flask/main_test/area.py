#!/usr/bin/env python
#coding=utf-8
from const import PI
def calc_round_area(radius):
    return PI * (radius ** 2)
def main():
    print "round area: ", calc_round_area(2)
main()
