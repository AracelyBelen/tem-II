from clinica import app, db

# IMPORTAR MODELOS
from models.medico import Medico
from models.paciente import Paciente
from models.consulta import Consulta
from models.usuario import Usuario

# IMPORTAR CONTROLADORES
from controllers.medico_controller import *
from controllers.paciente_controller import *
from controllers.consulta_controller import *
from controllers.auth_controller import *

if __name__ == '__main__':

    with app.app_context():
        db.create_all()

    print('Base de datos creada correctamente')

    app.run(debug=True)