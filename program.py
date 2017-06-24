import math
import json

def degree_to_radians(angle_degree):
    return (math.pi/180) * angle_degree

def distance_in_kms(distance_in_radians):
    radius_km = 6371
    return radius_km * distance_in_radians

def great_circle_distance_kms(lat2, lon2):
    lat1 = 0.22575966519569804
    lon1 = 1.354624680204907
    x = math.sin(lat1) * math.sin(lat2)
    y = math.cos(lat1) * math.cos(lat2)
    z = math.cos(lon1-lon2)
    d = math.acos(x+(y*z))
    return distance_in_kms(d)

def read_txt_json(max_dist = 100): 
    result = []
    result_dict = {}
    with open('customerJSON.txt') as f:
        content = f.readlines()
    for line in content:
        x = json.loads(line.strip())
        lt = degree_to_radians(x['lat'])
        ln = degree_to_radians(x['lon'])
        dist = great_circle_distance_kms(lt,ln)
        if int(dist) < max_dist:
            result_dict[x['id']] = {'name': x['name'], 'dist': dist}
            result.append(x['id'])
    sorted_result = sorted(result)
    print("===================================")
    print("ID\tName\tDistance")
    print("===================================")
    for i in sorted_result:
        print(i,'\t',result_dict[i]['name'],'\t',int(result_dict[i]['dist'])," kms")
    print("===================================")

def read_json(max_dist = 100):
    result = []
    result_dict = {}
    with open('customer.json') as f:
        content = json.load(f)
    for x in content:
        lt = degree_to_radians(x['lat'])
        ln = degree_to_radians(x['lon'])
        dist = great_circle_distance_kms(lt,ln)
        if int(dist) < max_dist:
            result_dict[x['id']] = {'name': x['name'], 'dist': dist}
            result.append(x['id'])
    sorted_result = sorted(result)
    print("===================================")
    print("ID\tName\tDistance")
    print("===================================")
    for i in sorted_result:
        print(i,'\t',result_dict[i]['name'],'\t',int(result_dict[i]['dist'])," kms")
    print("===================================")

print("\n\n\n\n")
print("Reading text file.............")
read_txt_json()
print("\n\n\n\n")
print("Reading json file.............")
read_json()
print("\n\n")
print("Processed successfully. Execution complete.")