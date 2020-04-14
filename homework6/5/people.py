#!/usr/bin/python3
# -*- coding: utf-8 -*-


class People:
    blood=100
    attack=10
    def __init__(self,n):
        self.name=n
    def attack_pattern(self,dog):
        if(self.attack>0):
            dog.blood=dog.blood-self.attack
            dog.attack=dog.attack-3