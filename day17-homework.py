#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx
import turtle

def main():
  #设置一个画面
  windows = turtle.Screen()
  #设置背景
  windows.bgcolor('blue')
  #生成一个黄色乌龟
  bran = turtle.Turtle()
  bran.shape('turtle')
  bran.color('yellow')
  #开始你的表演
  turtle.stamp()
  turtle.fd(50)

  turtle.circle(50,360,100)

  turtle.goto(300,200)

  turtle.stops(50)

if __name__ == '__main__':
  main()