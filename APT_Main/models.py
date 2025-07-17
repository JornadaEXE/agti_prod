from django.db import models

# Create your models here.



class t001log(models.Model):
    susrlog = models.EmailField(max_length=100, verbose_name='SUsrLog', help_text='Logins de Email')
    susrnam = models.CharField(max_length=100, verbose_name='SUsrNam', help_text='Nome do Usuário', blank='True', null='True')
    susrset = models.CharField(max_length=100, verbose_name='SUsrSet', help_text='Setor do Usuário', blank='True', null='True')
    susrsen = models.CharField(max_length=100, verbose_name='SUsrSen', help_text='Senha do Usuário', blank='True', null='True')

    class Meta:
        db_table = 't001log'
        db_table_comment = 'Login HomePage'

class t010for(models.Model):
    nforcod = models.IntegerField(verbose_name='NForCod', help_text='Codigo do Fornecedor')
    sfornam = models.CharField(max_length=100, verbose_name='SForNam', help_text='Nome do Fornecedor')
    sforcnp = models.CharField(max_length=20, verbose_name='SForCnp', help_text='CNPJ do Fornecedor', blank=True, null=True)

    class Meta:
        db_table = 't010for'
        db_table_comment = 'Cadastro de Fornecedores'

class t100lic(models.Model):
    ncodlic = models.IntegerField(verbose_name="NCodLic", help_text="Código da Licença", blank=False, null=False)
    snomlic = models.CharField(max_length=100, verbose_name="SNomLic", help_text="Nome da Licença", blank=False, null=False)
    ssigite = models.CharField(max_length=20, verbose_name="SSigIte", help_text="Sigla da Licença")
    ssetlic = models.CharField(max_length=100, verbose_name="SSetLic", help_text="Setor da Licença")
    ddatini = models.DateField(verbose_name="DDatIni", help_text="Data de Inicio da Licença")
    ddatfin = models.DateField(verbose_name="DDatFin", help_text="Data de Fim da Licença")
    fdurlic = models.FloatField(verbose_name="FDurLic", help_text="Duração da Licença")
    ssernum = models.CharField(max_length=200, verbose_name="SSerNum", help_text="Serial Number da Licença")
    slinsit = models.CharField(max_length=500, verbose_name="SLinSit", help_text="Site da Licença")
    susrcre = models.CharField(max_length=100, verbose_name="SUsrCre", help_text="Credencial de acesso")
    ssencre = models.CharField(max_length=100, verbose_name="SSenCre", help_text="Senha de acesso")
    ssetres = models.CharField(max_length=100, verbose_name="SSetRes", help_text="Setor responsavel pela renovação")
    sobsadi = models.TextField(max_length=1000, verbose_name="SObsAdi", help_text="Observação Adicional")
    ssitlic = models.CharField(max_length=20, verbose_name="SSitLic", help_text="Situação da Licença")

    class Meta:
        db_table = 't100lic'
        db_table_comment = 'Cadastro de Licenças'

class JsonResponseMaxi(models.Model):
    nome = models.CharField(max_length=100)
    payload = models.JSONField()
    criado_em = models.DateTimeField(auto_now_add=True)
