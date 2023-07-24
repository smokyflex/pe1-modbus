from enum import Enum

class InputRegisters(Enum):
                                                    # adr   offset scale dec    unit    name                                            desc
    HEATER_TEMPERATURE =                            (30001, 30001, 2,    0,     "°C",   "HEATER_TEMPERATURE",                              "Kesseltemperatur")
    SENSOR_1 =                                      (30008, 30001, 2,    0,     "°C",   "SENSOR_1",                                     "Fühler 1")
    RETURN_FLOW_SENSOR =                            (30010, 30001, 2,    0,     "°C",   "RETURN_FLOW_SENSOR",                           "Fühler 1")
    OPERATING_HOURS =                               (30021, 30001, 1,    0,     "h",    "OPERATING_HOURS",                              "Betriebsstunden")
    FILL_LEVEL_PELLETS_CONTAINER =                  (30022, 30001, 201,  1,     "%",    "FILL_LEVEL_PELLETS_CONTAINER",                 "Füllstand im Pelletsbehälter")
    HEATER_STARTS_COUNT =                           (30023, 30001, 1,    0,     "#",    "HEATER_STARTS_COUNT",                          "Anzahl der Brennerstarts")
    CALCULATED_HEATER_TARGET_TEMPERATURE =          (30028, 30001, 2,    0,     "°C",   "CALCULATED_HEATER_TARGET_TEMPERATURE",         "Errechnete Kesselsolltemperatur")
    RETURN_FLOW_CONTROL =                           (30037, 30001, 1,    0,     "%",    "RETURN_FLOW_CONTROL",                          "Rücklaufpumpen Ansteuerung")
    HOURS_SINCE_LAST_MAINTENANCE =                  (30056, 30001, 1,    0,     "h",    "HOURS_SINCE_LAST_MAINTENANCE",                 "Stunden seit letzter Wartung")
    HOURS_OF_PELLETS_OPERATION =                    (30063, 30001, 1,    0,     "h",    "HOURS_OF_PELLETS_OPERATION",                   "Stunden im Pelletsbetrieb")
    HOURS_OF_HEATING =                              (30064, 30001, 1,    0,     "h",    "HOURS_OF_HEATING",                             "Stunden im Heizen")
    CALCULATED_TARGET_RETURN_FLOW =                 (30067, 30001, 2,    0,     "°C",   "CALCULATED_TARGET_RETURN_FLOW",                "Rücklauf Soll errechnet")
    KG_COUNT =                                      (30082, 30001, 1,    0,     "kg",   "KG_COUNT",                                     "Resetierbarer kg-Zähler")
    TONS_COUNT =                                    (30083, 30001, 1,    0,     "t",    "TONS_COUNT",                                   "Resetierbarer t-Zähler")
    TOTAL_PELLETS_CONSUMPTION =                     (30084, 30001, 10,   1,     "t",    "TOTAL_PELLETS_CONSUMPTION",                    "Pelletverbrauch Gesamt")
    REMAINING_HOURS_UNTIL_ASH_REMOVAL =             (30087, 30001, 1,    0,     "h",    "REMAINING_HOURS_UNTIL_ASH_REMOVAL",            "Verbleibende Heizstunden bis zur Asche entleeren Warnung")
    COUNT_CLEANING_CYCLES =                         (30102, 30001, 1,    0,     "#",    "COUNT_CLEANING_CYCLES",                        "Anzahl der Reinigungen")
    MINUTES_UNTIL_NEXT_CLENAING_CYLCLE =            (30103, 30001, 1,    0,     "min",  "MINUTES_UNTIL_NEXT_CLENAING_CYLCLE",           "Zeit bis zur nächsten Reinigung")
    RETURN_FLOW_TEMPERATURE_AT_CIRCULATION_LINE =   (30712, 30001, 2,    0,     "°C",   "RETURN_FLOW_TEMPERATURE_AT_CIRCULATION_LINE",  "Rücklauftemperatur an der Zirkulations Leitung")
    OUTSIDE_TEMPERATURE =                           (31001, 30001, 2,    0,     "°C",   "OUTSIDE_TEMPERATURE",                          "Außentemperatur")
    HEATING_FLOW_TEMPERATURE_ACTUAL =               (31031, 30001, 2,    0,     "°C",   "HEATING_FLOW_TEMPERATURE_ACTUAL",              "HK1 - Vorlauf-Isttemperatur")
    HEATING_FLOW_TEMPERATURE_TARGET =               (31032, 30001, 2,    0,     "°C",   "HEATING_FLOW_TEMPERATURE_TARGET",              "HK1 - Vorlauf-Solltemperatur")
    ROOM_TEMPERATURE =                              (31033, 30001, 2,    0,     "°C",   "ROOM_TEMPERATURE",                             "HK1 - Raumtemperatur")
    BOILER_TEMPERATURE_TOP =                        (31631, 30001, 2,    0,     "°C",   "BOILER_TEMPERATURE_TOP",                       "Boiler 1 - Boilertemperatur oben")
    BUFFER_TEMPERATURE_TOP =                        (32001, 30001, 2,    0,     "°C",   "BUFFER_TEMPERATURE_TOP",                       "Puffertemperatur oben")
    #BUFFER_TEMPERATURE_CENTER =                     (32002, 30001, 2,    0,     "°C",   "BUFFER_TEMPERATURE_CENTER",                    "Puffertemperatur Mitte")
    BUFFER_TEMPERATURE_BOTTOM =                     (32003, 30001, 2,    0,     "°C",   "BUFFER_TEMPERATURE_BOTTOM",                    "Puffertemperatur unten")
    BUFFER_CHARGING_STATE =                         (32007, 30001, 1,    0,     "%",    "BUFFER_CHARGING_STATE",                        "Pufferladezustand")


"""
    PE1_TEMPERATURE = 30001# Kesseltemperatur °C 2 0
    #30002,# Abgastemperatur °C 1 0
    #30003,# Boardtemperatur °C 2 0
    #30004,# Restsauerstoffgehalt % 10 1
    #30005,# Position der Primärluftklappe % 1 0
    #30006,# T4 Bgr2 - Position der Sekundärluftklappe % 1 0
    #30007,# Saugzugdrehzahl Upm 1 0
    SENSOR_1 = 30008# Fühler 1 °C 2 0
    #30009,# Abgastemperatur nach dem Brennwertwärmetauscher °C 2 0
    RETURN_FLOW_SENSOR = 30010# Rücklauffühler °C 2 0
    #30011,# Luftgeschwindigkeit in der Ansaugöffnung m/s 100 2
    #30012,# Primärluft % 1 0
    #30013,# Saugzug - Ansteuerung % 1 0
    #30014,# Sekundärluft % 1 0
    #30015,# Kesselstellgröße % 1 0
    #30016,# Abgas-Solltemperatur °C 1 0
    #30017,# Sauerstoffregler % 1 0
    #30018,# Boardtemperatur Pelletsmodul °C 2 0
    #30019,# Ansauglufttemperatur °C 2 0
    #30020,# Stromaufnahme der Austragschnecke A 1000 2
    OPERATING_HOURS = 30021# Betriebsstunden h 1 0
    FILL_LEVEL_PELLETS_CONTAINER = 30022# Füllstand im Pelletsbehälter % 207 1
    BOILER_STARTS_COUNT = 30023# Anzahl der Brennerstarts   1 0
    #30024,# S4 - Zündungsstarts   1 0
    #30025,# Betriebsstunden in der Feuererhaltung h 1 0
    #30026,# Einschub % 1 0
    #30027,# Einschubregler % 1 0
    CALCULATED_BOILER_TARGET_TEMPERATURE = 30028# Errechnete Kesselsolltemperatur °C 2 0
    #30029,# Solarfühler Pufferunten °C 2 0

    #30030,# Stromaufnahme der Förderschnecke A 1000 2
    #30031,# Stromaufnahme der Zellradschleuse A 1000 2
    #30032,# Stromaufnahme der Stokerschnecke A 1000 2
    #30033,# Feuerraum-Unterdruck Pa 1 0
    #30034,# Position Absperrschieber % 10 0
    #30035,# Position Rostmotor % 10 0
    #30036,# Einschubkorrektur-Regler % 1 0
    RETURN_FLOW_CONTROL = 30037# Rücklaufpumpen Ansteuerung % 1 0
    #30038,# Verbrennungs Zuluftgebläse % 1 0
    #30039,# Verbrennungs Zuluftgebläse % 1 0
    #30040,# Betriebsstunden Stokerschnecke h 1 0
    #30041,# Betriebsstunden Förderschnecke h 1 0
    #30042,# Betriebsstunden ZRS h 1 0
    #30043,# Betriebsstunden Rüttler min 1 0
    #30044,# Lastspiele Kippantrieb   1 0
    #30045,# Betriebsstunden WOS h 1 0
    #30046,# Betriebsstunden Ascheschnecke h 1 0
    #30047,# Betriebsstunden Zündung h 1 0
    #30048,# Betriebsstunden Lambdasonde h 1 0
    #30049,# Betriebsstunden Saugturbine(n) h 1 0
    #30050,# Betriebsstunden Austragsschnecke h 1 0
    #30051,# Lastspiele Sicherheitsbelüftung   1 0
    #30052,# Betriebsstunden Saugzug h 1 0
    #30053,# Lastspiele RBK   1 0
    #30054,# Gemessener Fahrweg des Absperrschiebers % 10 0
    #30055,# Lambdasondenspannung gemessen mV 100 2
    HOURS_SINCE_LAST_MAINTENANCE = 30056# Stunden seit letzter Wartung h 1 0
    #30057,# Kesselanforderung über Heizkreis oder Boiler steht an   1 0
    #30058,# FR-Kühlung durch Sekundärluft % 1 0
    #30059,# Einschub wird begrenzt auf maximal % 1 0
    #30060,# Leistungsanhebung durch FR-Regelung % 1 0
    #30061,# Abschöpf Ausgang % 1 0
    #30062,# Lambdasondenspannung korrigiert mV 100 2
    HOURS_OF_PELLETS_OPERATION = 30063# Stunden im Pelletsbetrieb h 1 0
    HOURS_OF_HEATING = 30064# Stunden im Heizen h 1 0
    #30065,# Fühler Weiche Oben °C 2 0
    #30066,# Fühler Weiche Unten °C 2 0
    CALCULATED_TARGET_RETURN_FLOW = 30067# Rücklauf Soll errechnet °C 2 0
    #30068,# Drehzahl Kesselladepumpe % 1 0
    #30069,# Breitbandsonde Heizstrom A 1000 2
    #30070,# Breitbandsonde Heizungs Spannung V 1000 2
    #30071,# Breitbandsonde Nernst Spannung V 1000 3
    #30072,# Breitbandsonde Pump Strom mA 1000 3

    #30073,# Breitbandsonde Innenwiderstand Ohm 1 0
    #30074,# Unterdruck-Soll Pa 1 0
    #30075,# Stunden in Teillastbetrieb (Kesselstellgröße < 40 %) h 1 0
    #30076,# Saugzug - Ansteuerung % 1 0
    #30077,# Stunden im Scheitholzbetrieb h 1 0
    #30078,# Eingang WOS Funktionsrückmeldung (Fühler 2)   1 0
    #30079,# Unterdruck-Ist Pa 1 0
    #30080,# Stromaufnahme der Schnecke 0.1 A 1000 2
    #30081,# Stromaufnahme der Schnecke 0.2 A 1000 2
    KG_COUNT = 30082# Resetierbarer kg-Zähler: kg 1 0
    TONS_COUNT = 30083# Resetierbarer t-Zähler: t 1 0
    TOTAL_PELLETS_CONSUMPTION = 30084# Pelletverbrauch Gesamt t 10 1
    #30085,# Tagesertrag [kWh] kWh 1 0
    #30086,# Gesamtertrag [kWh] kWh 1 0
    REMAINING_HOURS_UNTIL_ASH_REMOVAL = 30087# Verbleibende Heizstunden bis zur Asche entleeren Warnung h 1 0
    #30089,# Feuerraumtemperatur °C 1 0
    #30090,# Boardtemperatur Hackgutmodul °C 2 0
    #30091,# Aktuelles FRT-Signal % 1 0
    #30093,# Position der AGR Primärluftklappe % 1 0
    #30094,# Stromaufnahme vom Rührwerk A 1000 2
    #30095,# Stromaufnahme der Schnecke 1 A 1000 2
    #30096,# Stromaufnahme der Schnecke 2 A 1000 2
    #30097,# Betriebsstunden vom Rührwerk h 1 0
    #30098,# Betriebsstunden Saugturbine h 1 0
    #30099,# Betriebsstunden der Schnecke auf LS h 1 0
    #30100,# Betriebsstunden der Schnecke auf LS h 1 0
    #30101,# Leistungsbedarf   1 0
    COUNT_CLEANING_CYCLES = 30102# Anzahl der Reinigungen   1 0
    MINUTES_UNTIL_NEXT_CLENAING_CYLCLE = 30103# Zeit bis zur nächsten Reinigung min 1 0
    #30104,# Betriebsstunden E-Filter h 1 0
    #30105,# Saugzug - Ansteuerung % 1 0
    #30106,# E-Filter - Leistungsstufe HV-Modul 1   1 0
    #30107,# E-Filter - Leistungsstufe HV-Modul 2   1 0
    #30108,# E-Filter - Leistungsstufe HV-Modul 3   1 0
    #30109,# E-Filter - Leistungsstufe HV-Modul 4   1 0
    #30110,# E-Filter - Filterrückmeldung   1 0
    #30111,# E-Filter - Wasser detektiert   1 0
    #30112,# E-Filter - Zustand Filter   1 0
    #30113,# Auf / Zu Bewegung des Rostes   1 0
    #30114,# Eingang externe Leistungsanforderung % 1 0
    #30115,# Aktuelle externe Leistungsanforderung % 1 0
    #30116,# ASKK Pumpenansteuerung % 1 0
    #30117,# Gefilterter Rostdifferenzdruck Pa 1 0

    #30118,# Druckdifferenz Rost Pa 1 0
    #30119,# Solldifferenzdruck Rost Pa 1 0
    #30120,# Unterdruck über dem Rost Pa 1 0
    #30121,# Unterdruck unter dem Rost Pa 1 0
    #30122,# Lastspiele Kippantrieb 1   1 0
    #30123,# Position der AGR Sekundärluftklappe % 1 0
    #30124,# Einschub absolut % 10 1
    #30125,# Ist-Druck im AGR-Kanal Pa 1 0
    #30126,# Solldruck im AGR-Kanal Pa 1 0
    #30127,# Position der AGR-Klappe % 1 0
    #30128,# Automatischer Maximaleinschub % 10 1
    #30129,# Temperatur unter dem Rost °C 1 0
    #30130,# Stromaufnahme der Schnecke 1 A 1000 2
    #30131,# WOS-Zustand   1 0
    #30132,# Temperatur Aufschubkanal °C 2 0
    #30133,# T4 - Lastspiele Kippantrieb 2   1 0
    #30134,# Anzahl der Überschläge   1 0
    #30135,# Leistung HV-Modul 1 W 100 2
    #30136,# Leistung HV-Modul 2 W 100 2
    #30139,# Aufgenommene Energie kWh 100 2
    #30140,# Lambdasondenzustand   1 0
    #30141,# Spannungsrückmeldung HV-Modul 1 kV 100 2
    #30142,# Stromrückmeldung HV-Modul 1 mA 1000 3
    #30143,# System "Loop" - Looppumpe % 1 0
    #30144,# Spannungsrückmeldung HV-Modul 2 kV 100 2
    #30145,# Stromrückmeldung HV-Modul 2 mA 1000 3
    #30146,# Absperrschieber - Aktuelle Position   1 0
    #30147,# Brennwert-WT - Anzahl der Spülvorgänge   1 0
    #30148,# Vergangene Zeit seit letzter Wärmetauscherreinigung min 1 0
    #30149,# Status Absperrschieber   1 0
    #30150,# 1-2-3 Saugmodul Motor 1   1 0
    #30151,# 1-2-3 Saugmodul Motor 2   1 0
    #30152,# 1-2-3 Saugmodul Motor 3   1 0
    #30153,# T4/T4e - Einschub % 10 1
    #30154,# Zyklon m. 2 ZRS - MAX-Sensor   1 0
    #30155,# Zyklon m. 2 ZRS - MIN-Sensor   1 0
    #30156,# 1-2-3 Saugmodul - Aktive Sonde   1 0
    #30157,# 1-2-3 Saugmodul - Aktives Saugsystem   1 0
    #30501,# Temperatur des Zweitkessel °C 2 0
    #30502,# Zustand des Brennerrelais   1 0
    #30503,# Betriebsstunden von Kessel 2 (Brennerkontakt) h 1 0
    #30504,# Umschaltventil Zweitkessel % 1 0
    #30601,# Zirku. Pumpe - Strömungsschalter an der Brauchwasser Leitung   2 0

    #30701,# Drehzahl Netzpumpe % 1 0
    #30702,# Netzrücklauf Temperatur °C 2 0
    #30703,# Drehzahl Verteiler 1 Pumpe % 1 0
    #30704,# Rücklauf Temperatur Verteiler 1 °C 2 0
    #30705,# Drehzahl Verteiler 2 Pumpe % 1 0
    #30706,# Rücklauf Temperatur Verteiler 2 °C 2 0
    #30707,# Drehzahl Verteiler 3 Pumpe % 1 0
    #30708,# Rücklauf Temperatur Verteiler 3 °C 2 0
    #30709,# Drehzahl Verteiler 4 Pumpe % 1 0
    #30710,# Rücklauf Temperatur Verteiler 4 °C 2 0
    #30711,# Drehzahl der Zirkulations Pumpe % 1 0
    RETURN_FLOW_TEMPERATURE_AT_CIRCULATION_LINE = 30712# Rücklauftemperatur an der Zirkulations Leitung °C 2 0
    #30801,# Diff- Regler - Temperatur der Wärmequelle °C 2 0
    #30802,# Diff- Regler - Temperatur der Wärmesenke °C 2 0
    #30803,# Diff- Regler - Drehzahl der Pumpe % 1 0
    #30901,# Kaskade Folgekessel 1 - Folgekessel Kesseltemperatur °C 2 0
    #30902,# Kaskade Folgekessel 2 - Folgekessel Kesseltemperatur °C 2 0
    #30903,# Kaskade Folgekessel 3 - Folgekessel Kesseltemperatur °C 2 0
    #30904,# Kaskade Folgekessel 1 - Folgekessel OK   1 0
    #30905,# Kaskade Folgekessel 2 - Folgekessel OK   1 0
    #30906,# Kaskade Folgekessel 3 - Folgekessel OK   1 0
    #30907,# Kaskade Folgekessel 1 - Folgekessel ist im Heizen   1 0
    #30908,# Kaskade Folgekessel 2 - Folgekessel ist im Heizen   1 0
    #30909,# Kaskade Folgekessel 3 - Folgekessel ist im Heizen   1 0
    #30910,# Kaskade Folgekessel 1 - Folgekessel Stellgröße % 1 0
    #30911,# Kaskade Folgekessel 2 - Folgekessel Stellgröße % 1 0
    #30912,# Kaskade Folgekessel 3 - Folgekessel Stellgröße % 1 0
    #30913,# Kaskade Folgekessel 1 - Drehzahl Kesselladepumpe % 1 0
    #30914,# Kaskade Folgekessel 2 - Drehzahl Kesselladepumpe % 1 0
    #30915,# Kaskade Folgekessel 3 - Drehzahl Kesselladepumpe % 1 0
    #30916,# Kaskade Folgekessel 1 - Folgekessel Abgastemperatur °C 1 0
    #30917,# Kaskade Folgekessel 2 - Folgekessel Abgastemperatur °C 1 0
    #30918,# Kaskade Folgekessel 3 - Folgekessel Abgastemperatur °C 1 0
    #30919,# Kaskade Folgekessel 1 - Folgekessel Paketalter s 1 0
    #30920,# Kaskade Folgekessel 2 - Folgekessel Paketalter s 1 0
    #30921,# Kaskade Folgekessel 3 - Folgekessel Paketalter s 1 0
    #30922,# Kaskade Folgekessel 1 - Folgekessel Rücklauffühler °C 2 0
    #30923,# Kaskade Folgekessel 2 - Folgekessel Rücklauffühler °C 2 0
    #30924,# Kaskade Folgekessel 3 - Folgekessel Rücklauffühler °C 2 0
    #30925,# Kaskade o. Puffer - Kaskaden-ist Temperatur °C 2 0
    #30926,# Slave - Kesselladepumpe % 1 0
    OUTSIDE_TEMPERATURE = 31001# Außentemperatur °C 2 0
    HEATING_FLOW_TEMPERATURE_ACTUAL = 31031# HK1 - Vorlauf-Isttemperatur °C 2 0

    HEATING_FLOW_TEMPERATURE_TARGET = 31032# HK1 - Vorlauf-Solltemperatur °C 2 0
    ROOM_TEMPERATURE = 31033# HK1 - Raumtemperatur °C 2 0
    #31061,# HK2 - Vorlauf-Isttemperatur °C 2 0
    #31062,# HK2 - Vorlauf-Solltemperatur °C 2 0
    #31063,# HK2 - Raumtemperatur °C 2 0
    #31091,# HK3 - Vorlauf-Isttemperatur °C 2 0
    #31092,# HK3 - Vorlauf-Solltemperatur °C 2 0
    #31093,# HK3 - Raumtemperatur °C 2 0
    #31121,# HK4 - Vorlauf-Isttemperatur °C 2 0
    #31122,# HK4 - Vorlauf-Solltemperatur °C 2 0
    #31123,# HK4 - Raumtemperatur °C 2 0
    #31151,# HK5 - Vorlauf-Isttemperatur °C 2 0
    #31152,# HK5 - Vorlauf-Solltemperatur °C 2 0
    #31153,# HK5 - Raumtemperatur °C 2 0
    #31181,# HK6 - Vorlauf-Isttemperatur °C 2 0
    #31182,# HK6 - Vorlauf-Solltemperatur °C 2 0
    #31183,# HK6 - Raumtemperatur °C 2 0
    #31211,# HK7 - Vorlauf-Isttemperatur °C 2 0
    #31212,# HK7 - Vorlauf-Solltemperatur °C 2 0
    #31213,# HK7 - Raumtemperatur °C 2 0
    #31241,# HK8 - Vorlauf-Isttemperatur °C 2 0
    #31242,# HK8 - Vorlauf-Solltemperatur °C 2 0
    #31243,# HK8 - Raumtemperatur °C 2 0
    #31271,# HK9 - Vorlauf-Isttemperatur °C 2 0
    #31272,# HK9 - Vorlauf-Solltemperatur °C 2 0
    #31273,# HK9 - Raumtemperatur °C 2 0
    #31301,# HK10 - Vorlauf-Isttemperatur °C 2 0
    #31302,# HK10 - Vorlauf-Solltemperatur °C 2 0
    #31303,# HK10 - Raumtemperatur °C 2 0
    #31331,# HK11 - Vorlauf-Isttemperatur °C 2 0
    #31332,# HK11 - Vorlauf-Solltemperatur °C 2 0
    #31333,# HK11 - Raumtemperatur °C 2 0
    #31361,# HK12 - Vorlauf-Isttemperatur °C 2 0
    #31362,# HK12 - Vorlauf-Solltemperatur °C 2 0
    #31363,# HK12 - Raumtemperatur °C 2 0
    #31391,# HK13 - Vorlauf-Isttemperatur °C 2 0
    #31392,# HK13 - Vorlauf-Solltemperatur °C 2 0
    #31393,# HK13 - Raumtemperatur °C 2 0
    #31421,# HK14 - Vorlauf-Isttemperatur °C 2 0
    #31422,# HK14 - Vorlauf-Solltemperatur °C 2 0
    #31423,# HK14 - Raumtemperatur °C 2 0
    #31451,# HK15 - Vorlauf-Isttemperatur °C 2 0
    #31452,# HK15 - Vorlauf-Solltemperatur °C 2 0

    #31453,# HK15 - Raumtemperatur °C 2 0
    #31481,# HK16 - Vorlauf-Isttemperatur °C 2 0
    #31482,# HK16 - Vorlauf-Solltemperatur °C 2 0
    #31483,# HK16 - Raumtemperatur °C 2 0
    #31511,# HK17 - Vorlauf-Isttemperatur °C 2 0
    #31512,# HK17 - Vorlauf-Solltemperatur °C 2 0
    #31513,# HK17 - Raumtemperatur °C 2 0
    #31541,# HK18 - Vorlauf-Isttemperatur °C 2 0
    #31542,# HK18 - Vorlauf-Solltemperatur °C 2 0
    #31543,# HK18 - Raumtemperatur °C 2 0
    BOILER_TEMPERATURE_TOP = 31631# Boiler 1 - Boilertemperatur oben °C 2 0
    #31632# Boiler 1 - Boilertemperatur Solarreferenz °C 2 0
    #31633# Boiler 1 - Boilerpumpe Ansteuerung % 1 0
    #31661,# Boiler 2 - Boilertemperatur oben °C 2 0
    #31662,# Boiler 2 - Boilertemperatur Solarreferenz °C 2 0
    #31663,# Boiler 2 - Boilerpumpe Ansteuerung % 1 0
    #31691,# Boiler 3 - Boilertemperatur oben °C 2 0
    #31692,# Boiler 3 - Boilertemperatur Solarreferenz °C 2 0
    #31693,# Boiler 3 - Boilerpumpe Ansteuerung % 1 0
    #31721,# Boiler 4 - Boilertemperatur oben °C 2 0
    #31722,# Boiler 4 - Boilertemperatur Solarreferenz °C 2 0
    #31723,# Boiler 4 - Boilerpumpe Ansteuerung % 1 0
    #31751,# Boiler 5 - Boilertemperatur oben °C 2 0
    #31752,# Boiler 5 - Boilertemperatur Solarreferenz °C 2 0
    #31753,# Boiler 5 - Boilerpumpe Ansteuerung % 1 0
    #31781,# Boiler 6 - Boilertemperatur oben °C 2 0
    #31782,# Boiler 6 - Boilertemperatur Solarreferenz °C 2 0
    #31783,# Boiler 6 - Boilerpumpe Ansteuerung % 1 0
    #31811,# Boiler 7 - Boilertemperatur oben °C 2 0
    #31812,# Boiler 7 - Boilertemperatur Solarreferenz °C 2 0
    #31813,# Boiler 7 - Boilerpumpe Ansteuerung % 1 0
    #31841,# Boiler 8 - Boilertemperatur oben °C 2 0
    #31842,# Boiler 8 - Boilertemperatur Solarreferenz °C 2 0
    #31843,# Boiler 8 - Boilerpumpe Ansteuerung % 1 0
    BUFFER_TEMPERATURE_TOP = 32001# Puffer 1 - Puffertemperatur oben °C 2 0
    BUFFER_TEMPERATURE_CENTER = 32002# Puffer 1 - Puffertemperatur Mitte °C 2 0
    BUFFER_TEMPERATURE_BOTTOM = 32003# Puffer 1 - Puffertemperatur unten °C 2 0
    #32004,# Puffer 1 - Pufferpumpen Ansteuerung % 1 0
    #32005,# Puffer 1 - Puffertemperatur Fühler 2 °C 2 0
    #32006,# Puffer 1 - Puffertemperatur Fühler 3 °C 2 0
    BUFFER_CHARGING_STATE = 32007# Puffer 1 - Pufferladezustand % 1 0
    #32008,# Solarfühler Puffer oben °C 2 0
    #32041,# Puffer 2 - Puffertemperatur oben °C 2 0

    #32042,# Puffer 2 - Puffertemperatur Mitte °C 2 0
    #32043,# Puffer 2 - Puffertemperatur unten °C 2 0
    #32044,# Puffer 2 - Pufferpumpen Ansteuerung % 1 0
    #32081,# Puffer 3 - Puffertemperatur oben °C 2 0
    #32082,# Puffer 3 - Puffertemperatur Mitte °C 2 0
    #32083,# Puffer 3 - Puffertemperatur unten °C 2 0
    #32084,# Puffer 3 - Pufferpumpen Ansteuerung % 1 0
    #32121,# Puffer 4 - Puffertemperatur oben °C 2 0
    #32122,# Puffer 4 - Puffertemperatur Mitte °C 2 0
    #32123,# Puffer 4 - Puffertemperatur unten °C 2 0
    #32124,# Puffer 4 - Pufferpumpen Ansteuerung % 1 0
    #32301,# Zustandslaufzeit aktuell   1 0
    #32302,# Zustandslaufzeit maximal   1 0
    #32601,# Ansteuerung Kollektorpumpe % 1 0
    #32602,# Kollektortemperatur °C 2 0
    #32603,# Laufzeit Kollektorpumpe h 1 0
    #32604,# Kollektor Rücklauftemperatur °C 2 0
    #32605,# Solar - Wärmetauscher Sek. Vorlauftemperatur (Leitung zum Puffer) °C 2 0
    #32606,# Solar - Pumpe zwischen Wärmetauscher und Puffer % 1 0
    #32607,# Solar - Pumpe zwischen Wärmetauscher und Boiler % 1 0
    #32608,# Solar - Ventil für Umschaltung zw. Puffer oben und unten % 1 0
    #32609,# Boilertemperatur Solarreferenz °C 2 0
    #32610,# Solar - DFL Sensor [l/h] l/h 1 0
    #32611,# Aktuelle Leistung des Solar WMZ [kW] kW 100 2
    #32612,# Solar - Kollektor Rücklauftemperatur °C 2 0
    #32613,# Solar - Kollektor Vorlauftemperatur °C 2 0
    #32614,# Solar - Tagesertrag vor 1 Tag kWh 1 0
    #32615,# Solar - Tagesertrag vor 2 Tagen kWh 1 0
    #32616,# Solar - Tagesertrag vor 3 Tagen kWh 1 0
    #32617,# Solar - Tagesertrag vor 4 Tagen kWh 1 0
    #32618,# Solar - Tagesertrag vor 5 Tagen kWh 1 0
    #32619,# Solar - Tagesertrag vor 6 Tagen kWh 1 0
    #32620,# Tagesertrag [kWh] kWh 1 0
    #32621,# Gesamtertrag [MWh] MWh 1 0
    #32622,# Gesamtertrag [kWh] kWh 1 0
    #32623,# Aktuelle Ansteuerung der Kollektor - Boiler Pumpe % 1 0
    #32624,# Laufzeit der Kollektor - Boiler Pumpe h 1 0
    #32625,# Solarsystem 3 - Anzahl der Schaltzyklen des Umschaltventils   1 0
    
    #40001,# Kessel-Solltemperatur °C 2 0 70 90 R/W
"""