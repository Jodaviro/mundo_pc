from computadora import Computadora
from teclado import Teclado
from raton import Raton
from monitor import Monitor
from orden import Orden

#computadoras                
intel3=Computadora ('Corei3')
intel5=Computadora ('Corei5')
intel7=Computadora ('Corei7')
amd3=Computadora ('Ryzen3')
amd5=Computadora ('Ryzen5')
amd7=Computadora('Ryzen7')

#monitores
monitor_samsumg = Monitor ('Samsumg',32)
monitor_asus= Monitor ('Asus',27)
monitor_lg = Monitor ('Lg', 27)
monitor_msi = Monitor ('Msi', 22)
monitor_aoc = Monitor ('Aoc', 24)
#teclados
teclado1= Teclado ('logitec', 'Bluetooth')
teclado2= Teclado ('microsoft', 'Usb')
teclado3= Teclado ('havit', 'Usb')
teclado4= Teclado ('microsoft', 'Bluetooth')
teclado5= Teclado ('Razord', 'Usb')
#ratones
raton1= Raton ('Hp', 'usb')
raton2= Raton ('Logitec', 'bluetooth')
raton3= Raton ('microsoft', 'usb')
raton4= Raton ('apple', 'bluetooth')
#################################

intel3.set_monitor(monitor_samsumg)
intel3.set_raton(raton4)
intel3.set_teclado(teclado4)

intel5.set_monitor(monitor_asus)
intel5.set_teclado (teclado1)
intel5.set_raton (raton1)

intel7.set_monitor (monitor_lg)
intel7.set_raton(raton3)
intel7.set_teclado(teclado3)

amd3.set_monitor (monitor_lg)
amd3.set_raton (raton2)
amd3.set_teclado (teclado5)

amd5.set_raton (raton2)


pago= [intel7]
pago2= [amd7,amd5]

pedido = Orden (pago)
pedido.agregarComputadora(amd3)
pedido.agregarComputadora (intel5)
print (pedido)

pedido2= Orden (pago2)
pedido2.agregarComputadora(amd7)
print (pedido2)