#!/usr/local/bin/python3
from yaml import load
import os

def build(pn, pwd):
    for ck, cc in pn.items():
        if isinstance(cc, dict):
            # make the directory named 'ck' and move into it
            if os.system('mkdir '+pwd+'/'+ck) == 0:
                build(cc, pwd+'/'+ck)
        if isinstance(cc, str):
            # download the file from the url 'cc' and save
            # it with name 'ck'
            os.system('wget '+cc+' -O '+pwd+'/'+ck)

f = open("conf.yaml", "r")
dirt = load(f)
build(dirt, './')
