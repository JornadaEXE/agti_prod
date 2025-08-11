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

class t002set(models.Model):

    scodset = models.CharField(max_length=5, verbose_name="SCodSet", help_text="Abrev. Setor")
    ssetnam = models.CharField(max_length=50, verbose_name="SSetNam", help_text="Nome do Setor")

    class Meta:
        db_table = 't002set'
        db_table_comment = 'Setores'

    def __str__(self):
        return self.ssetnam

class t003tip(models.Model):

    scodtip = models.CharField(max_length=5, verbose_name="SCodTip", help_text="Abrev. Tipo")
    stipnam = models.CharField(max_length=50, verbose_name="STipNam", help_text="Nome do Tipo")

    class Meta:
        db_table = 't003tip'
        db_table_comment = 'Tipos de Equipamentos'
    
    def __str__(self):
        return self.stipnam

class t004eqp(models.Model):

    scodeqp = models.IntegerField(verbose_name="SCodEqp", help_text="Código Equipamento")
    seqpnam = models.CharField(max_length=50, verbose_name="SEqpNam", help_text="Nome do Equipamento")

    class Meta:
        db_table = 't004eqp'
        db_table_comment = 'Equipamentos'

    def __str__(self):
        return self.seqpnam




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
    ssernum = models.CharField(max_length=200, verbose_name="SSerNum", help_text="Serial Number da Licença", blank=True)
    slinsit = models.CharField(max_length=500, verbose_name="SLinSit", help_text="Site da Licença", blank=True)
    susrcre = models.CharField(max_length=100, verbose_name="SUsrCre", help_text="Credencial de acesso", blank=True)
    ssencre = models.CharField(max_length=100, verbose_name="SSenCre", help_text="Senha de acesso", blank=True)
    ssetres = models.CharField(max_length=100, verbose_name="SSetRes", help_text="Setor responsavel pela renovação", blank=True)
    sobsadi = models.TextField(max_length=1000, verbose_name="SObsAdi", help_text="Observação Adicional", blank=True)
    ssitlic = models.CharField(max_length=20, verbose_name="SSitLic", help_text="Situação da Licença", blank=True)

    class Meta:
        db_table = 't100lic'
        db_table_comment = 'Cadastro de Licenças'

class JsonResponseMaxi(models.Model):
    nome = models.CharField(max_length=100)
    payload = models.JSONField()
    criado_em = models.DateTimeField(auto_now_add=True)

class t011lan(models.Model):
    nfilcod = models.IntegerField(verbose_name="NFilCod", help_text="Código da Filial", blank=False, null=False)
    ncnpfor = models.IntegerField(verbose_name="NCnpFor", help_text="CNPJ do fornecedor", blank=False, null=False)
    snomfor = models.CharField(max_length=100, verbose_name="SNomFor", help_text="Nomde do Fornecedor")
    ddatemi = models.DateField(max_length=100, verbose_name="DDatEmi", help_text="Data de Emissão")
    ddatven = models.DateField(max_length=100, verbose_name="DDatVen", help_text="Data de Vencimento")
    nvlrlan = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="NVlrLan", help_text="Valor do Lançamento")
    ncodsol = models.IntegerField(verbose_name="NCodSol", help_text="Código de Solicitação do ERP")
    ncodcon = models.IntegerField(verbose_name="NCodCon", help_text="Código do Contrato")
    ncodtra = models.IntegerField(verbose_name="NCodTra", help_text="Transação")
    scodccu = models.CharField(max_length=9, verbose_name="SCodCcu", help_text="Centro de Custo")
    sobslan = models.TextField(max_length=1000, verbose_name="SObsLan", help_text="Observação")

    class Meta:
        db_table = 't011lan'
        db_table_comment = 'Lançamentos de Contratos'


class t200ipc(models.Model):
    ssrvtag = models.CharField(max_length=50, verbose_name="SSrvTag", help_text="Identificador do equipamento")
    snomset = models.CharField(max_length=100, verbose_name="SNomSet", help_text="Setor do Equipamento")
    stipeqp = models.CharField(max_length=100, verbose_name="STipEqp", help_text="Tipo do Equipamento")
    sipeend = models.CharField(max_length=50, verbose_name="SIpeEnd", help_text="Endereço IP do Equipamento")
    smacend = models.CharField(max_length=100, verbose_name="SMacEnd", help_text="Endereço Mac do Equipamento")
    smodeqp = models.CharField(max_length=50, verbose_name="SModEqp", help_text="Modelo do Equipamento")
    sstteqp = models.CharField(max_length=5, verbose_name="SSttEqp", help_text="Status de Conexão")

    class Meta:
        db_table = 't200ipc'
        db_table_comment = 'Controle de Equipamentos por IP'

class t300med(models.Model):
    ncoduni = models.IntegerField(verbose_name="NCodUni", help_text="Código Único")
    sabrcon = models.CharField(max_length=20, verbose_name="SAbrCon", help_text="Abreviatura da Conversão")
    sdescon = models.CharField(max_length=200, verbose_name="SDesCon", help_text="Descrição da Conversão")

    class Meta:
        db_table = 't300med'
        db_table_comment = 'Métodos de Conversão de Medidas'
