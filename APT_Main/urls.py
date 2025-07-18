from APT_Main.views import index, cad_credenciais, main_page, login, insere_cred, configuracao, cad_info, insere_for, insere_lic, manutencao, informacoes, responder_json
from django.urls import path
from . import views

urlpatterns = [
    path('', index),
    path('login/', views.login, name='login'),
    path('cad_credenciais/', cad_credenciais, name='cad_credenciais'),
    path('main_page/', main_page, name='main_page'),
    path('form_credencial/', views.insere_cred, name='cadastro'),
    path('configuracao/', configuracao, name='configuracao'),
    path('cad_info/', cad_info, name='cad_info'),
    path('gtfor001/', views.insere_for, name='gtfor001'),
    path('inlic001/', views.insere_lic, name='inlic001'),
    path('manutencao/', views.manutencao, name='manutencao'),
    path('informacoes/', views.informacoes, name='informacoes'),
    path('fornecedor/<int:id>/editar/', views.editar_fornecedor, name='editar_fornecedor'),
    path('fornecedor/<int:id>/excluir/', views.excluir_fornecedor, name='excluir_fornecedor'),
    path('resposta/', views.responder_json),
    path('licenca/<int:id>/excluir/', views.excluir_licenca, name='excluir_licenca'),
]
