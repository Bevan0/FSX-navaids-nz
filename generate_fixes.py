import xmltodict

airspace_f = open("Airspace.xml", "r")
airspace = xmltodict.parse(airspace_f.read())
airspace_f.close()

def fromDMS(coordinate):
    lat_dms = coordinate[0:10]
    lon_dms = coordinate[11:21]

    lat_sign = lat_dms[0]
    lat_deg = float(lat_dms[1:3])
    lat_min = float(lat_dms[3:5])
    lat_sec = float(lat_dms[5:])

    lon_sign = lon_dms[0]
    lon_deg = float(lon_dms[1:4])
    lon_min = float(lon_dms[4:6])
    lon_sec = float(lon_dms[6:])

    lat_deg = (lat_deg + (lat_min/60) + (lat_sec/(60 ** 2)))
    if lat_sign == "-": lat_deg = lat_deg * -1
    lon_deg = (lon_deg + (lon_min/60) + (lon_sec/(60 ** 2)))
    if lon_sign == "-": lon_deg = lon_deg * -1

    return lat_deg, lon_deg

class VOR:
    name: str
    latitude: float
    longitude: float
    frequency: str

    def __init__(self, name, coordinates, frequency):
        self.name = name
        self.latitude, self.longitude = fromDMS(coordinates)
        self.frequency = frequency

    def __str__(self): return f"""<Vor dme="TRUE" dmeOnly="FALSE" lat="{self.latitude}" lon="{self.longitude}" alt="1M" type="HIGH" frequency="{frequency}" range="240760.0M" magvar="22.5" region="NZ" ident="{self.name}" name="{self.name}"><Dme lat="{self.latitude}" lon="{self.longitude}" alt="1M" range="240760.0M" /></Vor>"""

class NDB:
    name: str
    latitude: float
    longitude: float
    frequency: str

    def __init__(self, name, coordinates, frequency):
        self.name = name
        self.latitude, self.longitude = fromDMS(coordinates)
        self.frequency = frequency
    
    def __str__(self): return f"""<Ndb lat="{self.latitude}" lon="{self.longitude}" alt="1M" type="HH" frequency="{frequency}" range="240760.0M" magvar="22.5" region="NZ" ident="{self.name}" name="{self.name}"></Ndb>"""

class Intersection:
    name: str
    latitude: float
    longitude: float
    magneticVariation: float = 22.5

    def __init__(self, name, coordinates):
        self.name = name
        self.latitude, self.longitude = fromDMS(coordinates)
    
    def __str__(self): return f'<Waypoint lat="{str(self.latitude)[0:10]}" lon="{str(self.longitude)[0:11]}" waypointType="NAMED" waypointRegion="NZ" waypointIdent="{self.name}"></Waypoint>'

export = []
seen_fixes = []

for fix in airspace["Airspace"]["Intersections"]["Point"]:
    name = fix["@Name"]
    if name in seen_fixes: # Remove duplicates
        continue
    else:
        seen_fixes.append(name)
    fix_type = fix["@Type"]
    coordinates = fix["#text"]
    if fix_type == "Navaid": # VORs and NDBs
        navaid_type = fix["@NavaidType"]
        frequency = fix["@Frequency"]
        if navaid_type == "VOR":
            export.append(VOR(name, coordinates, frequency))
        elif navaid_type == "NDB":
            export.append(NDB(name, coordinates, frequency))
    elif fix_type == "Fix" and len(name) == 5:
        export.append(Intersection(name, coordinates))

template = open("template.xml", "r").read()

exported = open("update.xml", "w")
content = ""
for exporting in export:
    content += str(exporting)
    content += "\n"

exported.write(template.replace("{content}", content))
exported.close()
