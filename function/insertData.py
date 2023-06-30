from modelA import dbA,TemperatureA,HumidityA,SoilTemperatureA
from modelB import dbB,TemperatureB,HumidityB,SoilTemperatureB
import datetime
import random
from datetime import timezone
def createdata(days):
    list_dataA=[]
    list_dataB=[]
    today=datetime.datetime(2023, 6, 28,6,0,0)+datetime.timedelta(days)
    for i in range(48):
        today=today+datetime.timedelta(minutes=30)
        dataA={
            'date_time':today.strftime('%a %d %b %Y , %I:%M:%S%p'),
            'sm_sensor1':round(random.uniform(0,100),2),
            'sm_sensor2':round(random.uniform(0,100),2),
            'sm_sensor3':round(random.uniform(0,100),2),
            'sm_sensor4':round(random.uniform(0,100),2),
            'sm_sensor5':round(random.uniform(0,100),2),
            'sm_sensor6':round(random.uniform(0,100),2),
            'sm_sensor7':round(random.uniform(0,100),2),
            'sm_sensor8':round(random.uniform(0,100),2),
            'sm_sensor9':round(random.uniform(0,100),2),
            'hu_sensor1':round(random.uniform(0,100),2),
            'tm_sensor1':round(random.uniform(0,40),2)
            }
        dataB={
            'date_time':today.strftime('%a %d %b %Y , %I:%M:%S%p'),
            'sm_sensor1':round(random.uniform(0,100),2),
            'sm_sensor2':round(random.uniform(0,100),2),
            'sm_sensor3':round(random.uniform(0,100),2),
            'sm_sensor4':round(random.uniform(0,100),2),
            'sm_sensor5':round(random.uniform(0,100),2),
            'sm_sensor6':round(random.uniform(0,100),2),
            'sm_sensor7':round(random.uniform(0,100),2),
            'hu_sensor1':round(random.uniform(0,100),2),
            'tm_sensor1':round(random.uniform(0,40),2)
        }
        list_dataA.append(dataA)
        list_dataB.append(dataB)
    for i in range(len(list_dataA)):
        TA=TemperatureA(createdAt=list_dataA[i]["date_time"],sensor1=list_dataA[i]['tm_sensor1'])
        HA=HumidityA(createdAt=list_dataA[i]["date_time"],sensor1=list_dataA[i]['hu_sensor1'])
        SA=SoilTemperatureA(createdAt=list_dataA[i]["date_time"],
                            sensor1=list_dataA[i]['sm_sensor1'],
                            sensor2=list_dataA[i]['sm_sensor2'],
                            sensor3=list_dataA[i]['sm_sensor3'],
                            sensor4=list_dataA[i]['sm_sensor4'],
                            sensor5=list_dataA[i]['sm_sensor5'],
                            sensor6=list_dataA[i]['sm_sensor6'],
                            sensor7=list_dataA[i]['sm_sensor7'],
                            sensor8=list_dataA[i]['sm_sensor8'],
                            sensor9=list_dataA[i]['sm_sensor9']
                            )
        TB=TemperatureB(createdAt=list_dataB[i]["date_time"],sensor1=list_dataB[i]['tm_sensor1'])
        HB=HumidityB(createdAt=list_dataB[i]["date_time"],sensor1=list_dataB[i]['hu_sensor1'])
        SB=SoilTemperatureB(createdAt=list_dataA[i]["date_time"],
                            sensor1=list_dataA[i]['sm_sensor1'],
                            sensor2=list_dataA[i]['sm_sensor2'],
                            sensor3=list_dataA[i]['sm_sensor3'],
                            sensor4=list_dataA[i]['sm_sensor4'],
                            sensor5=list_dataA[i]['sm_sensor5'],
                            sensor6=list_dataA[i]['sm_sensor6'],
                            sensor7=list_dataA[i]['sm_sensor7'],
                            )
        # dbA.add(TA)
        # dbA.commit()
        # dbA.add(HA)
        # dbA.commit()
        # dbA.add(SA)
        # dbA.commit()
        # dbB.add(TB)
        # dbB.commit()
        # dbB.add(SB)
        # dbB.commit()
        dbB.add(HB)
        dbB.commit()
createdata(days=0)