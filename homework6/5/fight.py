#!/usr/bin/python3
# -*- coding: utf-8 -*-

from dog import Dog
from people import People
import random

class Fight:
    d=3
    p=2
    def fight(self):
        people1=People("人1")
        people2=People("人2")
        pl=[people1,people2]
        dog1=Dog("狗1")
        dog2=Dog("狗2")
        dog3=Dog("狗3")
        dl=[dog1,dog2,dog3]
        u=random.randint(0,1)
        if(u==0):
            while(self.d!=0 and self.p!=0):
                x=random.randint(0,self.p-1)
                y=random.randint(0,self.d-1)
                pl[x].attack_pattern(dl[y])
                print("{}攻击了{}一次".format(pl[x].name,dl[y].name))
                if(dl[y].blood<=0):
                    print("{}死亡".format(dl[y].name))
                    del dl[y]
                    self.d=self.d-1
                    if(self.d==0):
                        break
                x=random.randint(0,self.p-1)
                y=random.randint(0,self.d-1)
                dl[y].attack_pattern(pl[x])
                print("{}攻击了{}一次".format(dl[y].name,pl[x].name))
                if(pl[x].blood<=0):
                    print("{}死亡".format(pl[x].name))
                    del pl[x]
                    self.p=self.p-1
                    if(self.p==0):
                        break
            if(self.d==0):
                print("人类胜利！")
            else:
                print("汪星人胜利！")
        else:
            while(self.d!=0 and self.p!=0):
                x=random.randint(0,self.p-1)
                y=random.randint(0,self.d-1)
                dl[y].attack_pattern(pl[x])
                print("{}攻击了{}一次".format(dl[y].name,pl[x].name))
                if(pl[x].blood<=0):
                    print("{}死亡".format(pl[x].name))
                    del pl[x]
                    self.p=self.p-1
                    if(self.p==0):
                        break
                x=random.randint(0,self.p-1)
                y=random.randint(0,self.d-1)
                pl[x].attack_pattern(dl[y])
                print("{}攻击了{}一次".format(pl[x].name,dl[y].name))
                if(dl[y].blood<=0):
                    print("{}死亡".format(dl[y].name))
                    del dl[y]
                    self.d=self.d-1
                    if(self.d==0):
                        break
            if(self.d==0):
                print("人类胜利！")
            else:
                print("汪星人胜利！")

x=Fight()
x.fight()
            
            




