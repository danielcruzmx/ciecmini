#from Procesos.queries import q_saldo_inicial, q_acumulados_mes
#from SadiCarnot10.models import AcumuladoMes
from explorer.models import Query
from django.db import transaction
from django.db import connection
from SadiCarnot10.models import AcumuladoMes
from Procesos.models import PeriodoProceso

def dictfetchall(cursor):
	desc = cursor.description
	return [
       dict(zip([col[0] for col in desc],row))
       for row in cursor.fetchall()
	]

def execsql(consulta):
	cursor = connection.cursor()
	#print(consulta)
	cursor.execute(consulta)
	result_list = dictfetchall(cursor)
	cursor.close()
	return result_list

def run_acumuladosMensuales(condominio):
	print(" generando acumulados %s " % condominio)
	with transaction.atomic():
		
		if str(condominio) == 'SADICARNOT10':			
			n = execsql('delete from sadi_acumulado_mes')
			saldo_condominio = 0 
			rows = execsql(Query.objects.get(id=4).sql)
			for r in rows:
				saldo_inicial = float(r['saldo_inicial'])
				print(r['cuenta'], saldo_inicial)
			
				saldo = saldo_inicial
				rows2 = execsql(Query.objects.get(id=2).sql)
				for r2 in rows2:
					if r2['cuenta'] == r['cuenta']:
						saldo = round(saldo + float(r2['depositos']) - float(r2['retiros']),2) 
						#print(saldo)
						print(r2['nombre'], r2['cuenta'], r2['mes'], r2['depositos'], r2['retiros'], saldo)

						reg = AcumuladoMes(condominio=str(condominio),cuenta_banco=r2['cuenta'], \
										   mes=r2['mes'],fecha_inicial=r2['fec_ini'], \
										   fecha_final=r2['fec_fin'],depositos=r2['depositos'], \
										   retiros=r2['retiros'],saldo=saldo)
						reg.save()

				saldo_condominio = saldo_condominio + saldo		
				print(saldo_condominio)
			oPer = PeriodoProceso.objects.get(id=1)
			oPer.saldo_inicial=saldo_condominio
			oPer.save()

