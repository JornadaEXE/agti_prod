from APT_Main.views import index, cad_credenciais, main_page, login, insere_cred, configuracao, cad_info, insere_for, insere_lic, manutencao, informacoes, responder_json
from django.urls import path, include
from . import views

urlpatterns = [
    path('', index),
    path('login/', views.login_view, name='login'),
    path('cad_credenciais/', cad_credenciais, name='cad_credenciais'),
    path('main_page/', main_page, name='main_page'),
    path('form_credencial/', views.insere_cred, name='cadastro_ant'),
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
    path('painel/', views.log_sec, name='painel'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('accounts/login/', views.red_login, name='red_login'),
    path('gtlan001/', views.lancamento_contrato, name='lancamento_contrato'),
    path('inend001/', views.cad_endip, name='end_eqp'),
    path('ceqp001/', views.cad_tipo, name='cad_tip'),
    path('ceqp002/', views.cad_equipamento, name='cad_equipamento'),
    path('cinfo001', views.cad_setores, name='cad_setores')
]
