# pe1-modbus

REMARQUE : Ce projet n'est pas une intégration officielle de HA ou HACS !

Ce projet propose une ligne directrice sur la manière dont une chaudière à pellets Fröling PE1 / Lambdatronic peut être intégrée dans Home Assistant (HA - https://www.home-assistant.io) en utilisant l'interface Modbus intégrée.

Ce dépôt comprend également des scripts python qui utilisent un module modbus pour lire les registres de PE1 puis les publier via MQTT pour être utilisés dans Home Assistant, mais cela n'est pas nécessaire puisque HA dispose de sa propre interface Modbus où nous pouvons mapper directement les registres PE1 aux entités HA.

Au moment de la rédaction, le seul inconvénient est qu'il semble impossible de combiner ces entités Modbus dans HA en un appareil Homeassistant. L'interface MQTT prend en charge cela, donc si vous le souhaitez, vérifiez le code dans /src/pe1modbus.

## Exigences matérielles
La carte Lambdatronic offre 2 interfaces série, qui peuvent être configurées en Modbus TCP dans les paramètres.
Pour intégrer facilement l'appareil dans le réseau LAN local, la connexion série nécessite un adaptateur vers RJ45 (Convertisseur RS232 vers Ethernet). Celui de Waveshare (Convertisseur Industriel RS232/RS485 vers Ethernet) a été utilisé et son fonctionnement est confirmé :
- https://www.waveshare.com/rs232-485-to-eth-for-eu.htm

Le côté RS232 peut être connecté au port COM2 sur la Lambdatronic. Assurez-vous d'utiliser le câble approprié qui croise les broches RX TX.

Plus d'informations sur la configuration matérielle peuvent être trouvées dans ce guide :
https://loxwiki.atlassian.net/wiki/spaces/LOX/pages/1704984631/Fr+ling+Pelletskessel+RS232+an+Loxone+Modbus+TCP?focusedCommentId=1705050279


## Modbus TCP
Après la configuration matérielle, il existe de nombreuses façons de tester la communication modbus. QModMaster est un excellent outil pour explorer les registres via une interface graphique - https://github.com/zhanglongqi/qModMaster. Vous pouvez également écrire un court script en Python en utilisant le module pyModbusTCP (https://pypi.org/project/pyModbusTCP/), voir la section /src/ de ce dépôt pour un exemple.

Les informations sur les adresses des registres, etc., peuvent être étudiées dans le document de définition ModBus Lambdatronic 3200 Modbus (une recherche Google devrait fournir un lien pour télécharger).

## Home Assitant Modbus

Home Assitant offre une interface pour inclure des entités en utilisant le protocole Modbus - https://www.home-assistant.io/integrations/modbus/

La manière la plus propre de faire cela serait de créer un fichier modbus.yaml dans votre répertoire domestique HA (à côté du configuration.yaml) et de l'inclure dans la configuration ainsi :

```yaml
modbus: !include modbus.yaml
```

Ce dépôt comprend un fichier `modbus.yaml` exemple incluant quelques entités qui peuvent être facilement étendues selon vos besoins.

Dans le fichier `modbus.yaml`, nous devons d'abord spécifier le `hub`, qui pour cette configuration est l'adresse du convertisseur Waveshare.

La chaudière PE1 utilise une connexion Ethernet séparée qui est destinée au service Fröling Connect. Assurez-vous de spécifier l'adresse du convertisseur Waveshare dans le yaml.

```yaml
- name: pe1_hub
  type: tcp
  host: xxx.xxx.xxx.xxx # address of the Waveshare converter
  port: 502
  sensors:
    ...
```

Dans la section des capteurs, vous pouvez spécifier les adresses des registres que vous souhaitez mapper aux entités HA. Pour plus d'informations sur la manière d'adresser les registres d'entrée, les registres de conservation, etc., étudiez la documentation HA Modbus liée ci-dessus.

Le système PE1 propose deux registres d'entrée qui spécifient l'état du système et l'état de la chaudière qui sont implémentés via un enum. Voir le PDF de définition Modbus Lambdatronic pour plus d'informations à ce sujet. Si vous souhaitez associer ces valeurs entières d'état aux chaînes de caractères correspondantes, vous pouvez le faire dans HA via le templating.

Exemple : Disons que nous avons déclaré une entité pour le statut du système dans notre fichier `modbus.yaml` comme ceci :

```yaml
- name: Modbus PE1 System Status Enum
  unique_id: modbus_pe1_system_status_enum
  slave: 2
  input_type: input
  address: 4000
  scan_interval: 30
  device_class: enum
```

Nous pouvons ensuite créer une entité de template dans un autre fichier yaml utilisé pour les entités de template dans le répertoire de configuration de HA `template.yaml`, qui est à nouveau inclus dans le `configuration.yaml` ainsi :

```yaml
template: !include template.yaml
```

À l'intérieur de ce fichier, nous pouvons mapper les valeurs énumérées de notre entité `modbus_pe1_system_status_enum` à des valeurs de chaînes de caractères que nous pouvons utiliser pour afficher dans le frontend dans un format lisible par l'homme :

```yaml
- name: "Modbus PE1 System Status"
  unique_id: "modbus_pe1_system_status"
  state: >
    {% set mapper =  {      
      '0' : 'Continuous load',
      '1' : 'Domestic hot water',
      '2' : 'Automatic',
      '3' : 'Firewood operation',
      '4' : 'Cleaning',
      '5' : 'Boiler off',
      '6' : 'Extra heating',
      '7' : 'Chimney sweep',
      '8' : 'Cleaning' } %}
    {% set state =  states.sensor.modbus_pe1_system_status_enum.state %}
    {{ mapper[state] if state in mapper else 'Unknown' }}
  icon: >
    {% if this.state == 'Automatic' %}
      mdi:refresh-auto
    {% elif this.state == 'Domestic hot water' %}
      mdi:water-pump
    {% elif this.state == 'Continous load' %}
      mdi:hours-24
    {% else %}
      mdi:alert-circle
    {% endif %}
```
Ici, vous pourriez également changer l'icône de l'entité en fonction de son état, comme montré ci-dessus.

La même chose peut être faite pour le statut de la chaudière/du four. Voir le `modbus.yaml` complet et le `template.yaml` inclus dans ce dépôt pour plus d'informations.

## TODO

Le document de définition Modbus Lambdatronic décrit comment utiliser modbus pour contrôler à distance le mode de chauffage de la chaudière. Je n'ai pas encore réussi à faire fonctionner cela. Selon le document, les adresses des registres du mode de chauffage devraient se trouver entre 48047 et 48064 dans les registres de maintien.
Théoriquement, nous devrions être capables d'écrire sur ces registres pour changer le mode de chauffage.
Il y a 18 registres pour cela parce que nous pourrions avoir un maximum de 18 circuits de chauffage possibles. Ces registres devraient contenir des valeurs de 0 à 5 pour les six différents modes :

 * 0 ... Éteint
 * 1 ... Automatique
 * 2 ... Chauffage d'appoint
 * 3 ... Réduction
 * 4 ... Réduction permanente
 * 5 ... Mode fête

Cependant, lors de l'expérimentation avec ces registres, je ne suis ni capable de lire la valeur correcte du mode de chauffage ni d'écrire dessus. Toute aide ici serait très appréciée.
