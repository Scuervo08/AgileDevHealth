from django.contrib import admin

from django.contrib import admin
from .models.user import User
from .models.account import Account
from .models.auxiliar import Auxiliar
from .models.medicos import Medicos
from .models.paciente import Pacientes
from .models.enfermero import Enfermero
from .models.signos_vitales import Signosvitales
from .models.familiar import Familiar
from .models.historia_clinica import Historia_clinica
from .models.registro_signosvitales import Registro_signosvitales


admin.site.register(User)
admin.site.register(Account)
admin.site.register(Auxiliar)
admin.site.register(Medicos)
admin.site.register(Enfermero)
admin.site.register(Signosvitales)
admin.site.register(Pacientes)
admin.site.register(Familiar)
admin.site.register(Historia_clinica)
admin.site.register(Registro_signosvitales)


