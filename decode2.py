#!/bin/python3
import json, os

def parseData(n,metricName):
  # Parseo de los datos extraidos de Prometheus  
  data=(json.load(n))

  metricList = []
  for temp in (data['data']['result']):
    # recorro la lista de resultados y los parseo
    
    try:
      # Si esta presente el namespace lo agrego
      metricDict = "name=Custom Metrics|Prometheus Integration|{metricName}|{namespace}, value={value}".format(metricName=metricName,namespace=temp['metric']['namespace'],value=temp['value'][1])
    except:
      # Caso contrario indico que corresponde al total
      metricDict = "name=Custom Metrics|Prometheus Integration|{metricName}, value={value}".format(metricName=metricName,value=temp['value'][1])
    
    # Sumo el nuevo dict a la lista de metricas
    metricList.append(metricDict)
  # Devuelvo la lista de metricas lista para subir a APD
  return metricList

for file in os.listdir('E:/Users/JMP/Documents/Programacion/Python/Galicia/Prometheus/'):
  if ".json" in file:
    with(open(file, 'r')) as f:
      for item in (parseData(f,file.split(".")[0])):
        print(item)