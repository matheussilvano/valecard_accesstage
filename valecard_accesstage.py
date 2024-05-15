import os

while True:
    print('====== PADRÃO VALECARD X ACCESSTAGE ======')
    cnpj = input('Digite o CNPJ do cliente: ')
    dsname = input('Informe o Dsname do cliente: ').upper()
    os.system('cls')

    print(f'''==== VALECARD.VALECARD (19798) ====

MÁSCARA ENTRADA BANCO:
ARQUIVO_CONCILIACAO_%y%m%d_{dsname}.txt

MÁSCARA SAÍDA BANCO:
REM.EXT.{cnpj}.230.%d%m%Y&C(5)

SCRIPT APÓS A RECEPÇÃO DO BANCO:
/home/skyline/scripts/inte_rvs/Judge /home/skyline/scripts/inte_rvs/judge.cfg ACCESSTAGE.OPERADORAS &F

ESTAÇÃO(BANCO):
14946''')

    continuar = input('Digite enter para continuar: ')
    os.system('cls')

    print(f'''
==== CAIXA ACCESSTAGE.OPERADORAS (34776) ====

MÁSCARA ENTRADA CLIENTE:
REM.EXT.{cnpj}.230

MÁSCARA SAÍDA CLIENTE:
{dsname}.V%d%m%y%H%M%S.TMP

SCRIPT P/ VALIDAÇÃO CLIENTE:
/home/skyline/scripts/todos/FromDos &F

SCRIPT ENVIO:
submit maxdelay=unlimited EXT-{dsname} process snode=$(ESTACAO)
step01 copy from (file=$(FORIGEM) pnode)
           to   (file=$(FDESTINO) disp=new snode)
step02 if (step01 eq 0) then
       run task snode sysopts="sub2acc $(FDESTINO) nexxera"
       eif
;


CAIXA POSTAL:
ACCESSTAGE.VALECARD-EXTRATO-67616128000155

NOME:
ACCESSTAGE - VALECARD - EXTRATO
      ''')
    terminar = input('Digite enter para sair: ')
    os.sysyem('cls')
