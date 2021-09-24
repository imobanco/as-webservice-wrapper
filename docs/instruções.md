# Tipo de pagamento
```
01 = Crédito em Conta Corrente/Salário (transferência entre contas)
03 = DOC/TED (1) (2)
05 = Crédito em Conta Poupança
11 = Pagamento de tributos com código de barras
41 = TED – Outra Titularidade
43 = TED – Mesma Titularidade
30 = Liquidação de Títulos do Próprio Banco
31 = pagamento de Títulos de Outros Bancos
```

## Email
Basicamente os arquivos do banco tem a seguinte estrutura:

 

HEADER DO ARQUIVO –  É o cabeçalho do arquivo, nesse parte do arquivo o banco espera os dados da empresa, no caso da Imobanco.

HEADER DE LOTE  - É o complemento do Header, dentre algumas informações, é nessa parte que será informado que forma de pagamento se refere, sendo assim, se no mesmo arquivo CSV vocês enviarem pagamentos de boleto e TED por exemplo será gerado 2 header de lote.

 

SEGMENTO A – Será utilizado se a forma de pagamento for DOC/TED e transferência entre contas (coluna type transfer_payment), é onde será inserido os dados de conta do favorecido. Favorecido é a pessoa física ou jurídica que a Imobanco esta fazendo o pagamento.

SEGMENTO B – É o complemento das informações do favorecido.

 

SEGMENTO J - Será utilizado se a forma de pagamento for pagamentos de boletos (coluna type invoice_payment), nessa forma de pagamento  a pessoa física ou jurídica que recebe o pagamento é chama de Beneficiário ou Cedente, uma das informações que é inserida nesse segmento é o código de barra.

SEGMENTO J52 - É o complemento das informações do beneficiário.

 

 

TRAILER DE LOTE  - é o fechamento do lote do arquivo.

TRAILER DO ARQUIVO é o fechamento do arquivo.

 

3 – Estrutura DE/PARA

 

Abaixo vou informar o que precisa ser validado, alterado e inserido para atender o layout do banco, vou separar por segmento do layout do banco.

 

HEADER DO ARQUIVO

 

    Coluna payer_document - A descrição que você me encaminhou diz que é o CNPJ do pagador, ou seja, da Imobanco, esse campo tem de ser preenchido com 14 caracteres e apenas com números, caso a empresa tenha apenas um CNPJ eu posso fixar esse informação no mapa.

Favor me informar se devo fixar o CNPJ ou se essa informação será enviada no arquivo com as especificações.

 

    Código do Convênio no Banco - Esse número é informado pelo banco, ele é vinculado ao número da conta corrente da empresa, precisa criar um coluna para informar o código. 

 

    Coluna payer_bank_account_routing - Na descrição diz que é a agencia do pagador, esse campo deve ser preenchidos com 5 números. Em todos os campos que o banco solicitar o número de agencia e de conta corrente é necessário informar também o digito da conta e/ou agencia. No layout do banco existe um campo especifico para o numero conta e/ou agencia e outro campo para o digito, ou seja, eles tem que estar separados. Nesse caso apresento duas opções:

Você pode criar uma coluna apenas para informar o digito ou posso criar um regra utilizando os números que a empresa enviar na coluna payer_bank_account_routing,  ao invés de preencher essa coluna apenas com número 5 números da agencia , você preencheria com 6 dígitos (agencia+digito), a regra que vou solicitar é que se a coluna tiver mais de 5 dígitos,  o  arquivo do banco será preenchido apenas o campo de agencia, caso tenha 6 dígitos a regra pegaria o sexto digito e colocaria no campo correspondente ao digito da agencia no arquivo do banco. Nesse caso é importante se atentar se o preenchimento está com a quantidade de números correta, pois sempre a sexta posição da agencia será digito, se tiver 5 números a posição 6 no arquivo será preenchida com branco.  

Uma informação de preenchimento desse campo é que a agencia tiver menos de 5 dígitos, é necessário completar as posições com zeros à esquerda.

 

    Coluna payer_bank_account_number -  A descrição do CSV diz que é a conta do pagador, no layout do banco é um campo numérico que deve ter 12 dígitos, sendo necessário completar as posições com zeros à esquerda.  Assim como o caso que expliquei da coluna payer_bank_account_routing, será necessário criar uma coluna dessa vez para informar o digito da conta ou posso criar uma regra seguindo o mesmo molde, ao invés de 12 números vocês preencheriam com 13 onde no arquivo do banco a decima terceira seria o digito da conta.

 

HEADER DE LOTE  

 

    Forma de lançamento -  No arquivo CSV será necessário criar um coluna onde será informada a forma de pagamento para cada um dos títulos que estão sendo enviados no arquivo, cada forma de pagamento tem um código de dois dígitos, seguindo essa regra:

01 = Crédito em Conta Corrente/Salário (transferência entra contas)

03 = DOC/TED (1) (2)

41 = TED – Outra Titularidade  

43 = TED – Mesma Titularidade

30 = Liquidação de Títulos do Próprio Banco

31 = pagamento de Títulos de Outros Bancos

 

SEGMENTO A

 

    receiver_bank_account_bank_code - A descrição diz que é informado o número do banco do favorecido , esse campo é numérico com 3 dígitos.
    receiver_bank_account_routing  - A descrição diz que é a agencia do favorecido - a regra é a mesma da coluna payer_bank_account_routing
    receiver_bank_account_number -  A descrição diz que é a conta do favorecido - a regra é a mesma da coluna da  coluna payer_bank_account_number

 

 

    Dígito Verificador Agência/Conta - alguns bancos possuem 2 dígitos verificadores, o primeiro é o digito que expliquei nos casos das colunas  payer_bank_account_number e receiver_bank_account_number e para o segundo digito será necessário criar um coluna para informar o número ou posso também solicitar uma criação de regra. Na regra você preenche a coluna receiver_bank_account_number com 12 números ferente a conta do favorecido + 1 número do digito da conta e + 1 referente ao digito da conta, então quando o arquivo passar pelo mapa e  tiver 12 dígitos ele preenche somente o campo da conta, 13 dígitos ele preencher os campos de conta e digito e 14 dígitos ele preencher os campos conta, digito da conta e Dígito Verificador Agência/Conta.

Para contas do banco do brasil esse campo não é preenchido.

 

 

    Número do título (seu número) - é um campo alfanumérico , nele é informado o número de identificação do título gerado para a empresa, é como se fosse o “RG” do título. Cada título tem seu número e ele não pode ser repetido, caso a Imobanco gere um pagamento e por algum motivo esse pagamento ser rejeitado pelo banco, a empresa deverá fazer a correção encaminhar novamente título, nesse caso o título corrigido deve ter um número diferente daquele que foi rejeitado. 

Pelo que entendi na descrição do CSV vocês enviam o número do título na coluna ID, favor me confirmar se seria essa coluna mesmo e caso positivo será necessário fazer algum ajuste na geração desse ID, pois o campo referente ao número do título tem o máximo de 20 posições.

 

SEGMENTO B

 

    Tipo de Inscrição do Favorecido – Precisa criar um coluna para identificar se o favorecido é pessoa física ou jurídica. Os códigos preenchimento:

1 CFP

2 CNPJ

    receiver_document – A descrição do CSV diz que é o número de inscrição do favorecido. Deve ser um campo de 14 posições e contar apenas números para convertemos ao layout do banco, caso a inscrição do favorecido for CPF então deve-se preencher zero à esquerda para completar as posições.

 

SEGMENTO J

 

    Nome do Cedente/Beneficiário – Precisa ser incluído uma coluna para informar o nome do beneficiário a qual o boleto está sendo pago, pelo li na descrição que você enviou a coluna receiver_name é utilizada para informar o nome do favorecido, você pode utilizar a mesma coluna para o beneficiário ou criar um coluna especifica.
    Data do Vencimento (Nominal) – Criar uma coluna para informar a data de vencimento do boleto.

 

 

    Número do título (seu número) – mesmo caso que expliquei no segmento A.

 

 

SEGMENTO J52

 

    Tipo de Inscrição do beneficiário – Precisa criar um coluna para identificar se o beneficiário é pessoa física ou jurídica. Os códigos preenchimento:

1 CFP

2 CNPJ

    receiver_document – A descrição do CSV diz que é o número de inscrição do favorito, mas você também pode utilizar para beneficiário. Deve ser um campo de 14 posições e contar apenas números para convertemos ao layout do banco, caso a inscrição do beneficiário for CPF então deve-se preencher zero à esquerda para completar as posições.
