from django.contrib import admin
from .models import Guardian, FAQ, Solucao, Pergunta, Resposta

admin.site.register(Guardian)
admin.site.register(FAQ)
admin.site.register(Solucao)
admin.site.register(Pergunta)
admin.site.register(Resposta)

