#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Dog:
    blood=80
    attack=15
    def __init__(self,n):
        self.name=n
    def attack_pattern(self,people):
        if(self.attack>0):
            people.blood=people.blood-self.attack
            people.attack=people.attack-2


