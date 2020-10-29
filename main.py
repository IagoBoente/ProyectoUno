from ventana import *
import sys, var, events, clients

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_venPrincipal
        var.ui.setipUi(self)

        '''
        colección de datos
        '''
        var.rbtSexo = (var.ui.rbtFem, var.ui.rbtMasc)

    '''
    conexion de eventos con los objetos
    estamos conectando el codigo con la interfaz grafica
    '''
    var.ui.btnSalir.clicked.connect(events.Eventos.Salir)
    var.ui.actionSalir.triggered.connect(events.Eventos.Salir)
    var.ui.editDni.editingFinished.connect(clients.Clientes.validoDni)
    for i in var.rbtSexo:
        i.toggled.connect(clients.Clientes.selSexo)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())