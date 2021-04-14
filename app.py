#!/usr/bin/env Python3

from os import system

def loadOrder( fileName ):
    file = open( fileName, "r" )
    data = file.readlines()
    system( "clear" )
    
    i = 0
    totalCost = 0

    while i < len( data ):
     a = data[i]
     new_a = a.replace( "\n", "" )
     listNewA = new_a.split()
     name = listNewA[0]
     price = float( listNewA[1] )
     quantity = int( listNewA[2] )
     print( f"{name:6} : {price:6} : {quantity}" )
     input("hit enter")
     totalCost += price * quantity
     i += 1
    print( f"Total Cost = {totalCost}" )


loadOrder( "order.csv" )
