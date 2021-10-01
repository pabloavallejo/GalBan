import json, os, pprint

def parseData(n,metricName):
  # Parseo de los datos extraidos de Prometheus  
  data=(json.load(n))

  metricList = []
  for temp in (data['data']['result']):
    # recorro la lista de resultados y los parseo
    metricDict={}
    metricDict["metric"] = metricName
    try:
      # Si esta presente el namespace lo agrego
      metricDict["namespace"] = temp['metric']['namespace']
    except:
      # Caso contrario indico que corresponde al total
      metricDict["namespace"] = ""
    metricDict["eventTimestamp"] = int(temp['value'][0]*1000)
    metricDict["value"] = temp['value'][1]
    
    # Sumo el nuevo dict a la lista de metricas
    metricList.append(metricDict)
  # Devuelvo la lista de metricas lista para subir a APD
  return metricList

for file in os.listdir('E:/Users/JMP/Documents/Programacion/Python/Galicia/Prometheus/'):
  if ".json" in file:
    with(open(file, 'r')) as f:
      pprint.pprint((parseData(f,file.split(".")[0])))