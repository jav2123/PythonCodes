'''
Problema 
You have three jugs, measuring 12 gallons, 8 gallons, and 3 gallons,
and a water faucet. You can fill the jugs up or empty them out from one to
another or onto the ground. You need to measure out exactly one gallon.
Estado Inicial: (0,0,0)
Estados: Tripleta de gallones(0,0,0),...,(12,8,3)
Objetivo: Alguna jarra con 1 galon (1,*,*),(*,1,*),(*,*,1)
Modelo de transicion: Definir cada estado en un grafo y la accion 
te lleva al siguiente nodo
Prueba de Objetivo:Alguna de las 3 variables ya contiene el 1?
Costo del camino: Cada accion equivale a 1 unidad de costo el mejor 
camino es el de menor costo
'''


