from main import db 

class Emitente(db.Model):
    __tablename__ = "emitente"

    cnpj = db.Column(db.String(), primary_key = True)
    inscricao_municipal = db.Column(db.String())

    def __init__(self, cnpj, inscricao_municipal):
        self.cnpj = cnpj
        self.incricao_municipal = inscricao_municipal

    def __repr__(self):
        return f"<Entidade {self.cnpj}>"
    
class Cliente(db.Model):
    __tablename__ = "cliente"

    razao_social= db.Column(db.String(), primary_key = True)
    tipo_documento= db.Column(db.String())
    numero_documento= db.Column(db.String())
    inscricao_municipal= db.Column(db.String())
    endereco_logradouro= db.Column(db.String())
    endereco_numero= db.Column(db.String())
    endereco_complemento= db.Column(db.String())
    endereco_bairro= db.Column(db.String())
    endereco_cod_municipio= db.Column(db.String())
    endereco_uf= db.Column(db.String())
    endereco_cep= db.Column(db.String())
    endereco_pais= db.Column(db.String())
    endereco_telefone= db.Column(db.String())
    email= db.Column(db.String())

class Servico(db.Model):
    valor_servico=db.Column(db.String())
    iss_retido=db.Column(db.String())
    item_lista=db.Column(db.String())
    discriminacao=db.Column(db.String())
    codigo_municipio=db.Column(db.String())
    # Dados opcionais
    codigo_cnae =db.Column(db.String())
    codigo_tributacao_municipio =db.Column(db.String())
    valor_deducoes =db.Column(db.String())
    valor_pis =db.Column(db.String())
    valor_confins =db.Column(db.String())
    valor_inss =db.Column(db.String())
    valor_ir =db.Column(db.String())
    valor_csll =db.Column(db.String())
    valor_iss =db.Column(db.String())
    valor_iss_retido =db.Column(db.String())
    valor_liquido =db.Column(db.String())
    outras_retencoes =db.Column(db.String())
    base_calculo =db.Column(db.String())
    aliquota =db.Column(db.String())
    desconto_incondicionado =db.Column(db.String())
    desconto_condicionado =db.Column(db.String())
    
class NotaFiscalServico(db.Model):
    identificador=db.Column(db.String())
    data_emissao=db.Column(db.String())
    servico=db.Column(db.String())
    emitente=db.Column(db.String())
    cliente=db.Column(db.String())
    # Optante Simples Nacional
    simples=db.Column(db.String())
    natureza_operacao=db.Column(db.String())
    # 5 –Exigibilidade suspensa por decisão judicial 6 – Exigibilidade suspensa por procedimento administrativo
    # regime_especial=db.Column(db.String())
    # 3 – Sociedade de profissionais 4 – Cooperativa 5 - Microempresário Individual (MEI) 
    # 6 - Microempresário e Empresa de Pequeno Porte (ME EPP)
    incentivo=db.Column(db.String())
    serie=db.Column(db.String())
    tipo=db.Column(db.String())