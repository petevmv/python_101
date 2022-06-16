def gas_stations(distance, tank_size, stations):
    result = []
    travaled_distance = tank_size
    
    for idx, station in enumerate(stations):

        if travaled_distance > station:
            continue

        travaled_distance = tank_size + stations[idx - 1]
        result.append(stations[idx - 1])

    if travaled_distance > stations[-1] and travaled_distance < distance:
        result.append(stations[-1])


    print(result)    
    return result
print(gas_stations(320, 90, [50, 80, 140, 180, 220, 290]) == [80, 140, 220, 290])
print(gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350]) == [70, 140, 210, 280, 350])
print(gas_stations(100, 50, [10, 20, 30, 40, 50, 60, 70, 80, 90, 150]) == [40, 80])
print(gas_stations(100, 50, [10, 90]) == [])


# def gas_stations(distance, tank_size, stations):
#     res = []
#     destination = 0
#     for idx, val in enumerate(stations):
#         try:
#             if tank_size + val <= stations[idx + 1]:
#                 print ([])
#                 return []
#         except :
#             pass
#         if stations[-1] >= distance:
#             stations.remove(stations[-1])
#         if val >= (tank_size + destination):
#             destination = stations[idx - 1]
#             res.append(destination)
#             if val == stations[-1] and tank_size + destination <= distance:
#                 res.append(stations[-1])
#     print(res)

# gas_stations(320, 90, [50, 80, 140, 180, 220, 290])
#gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350])
#gas_stations(100, 50, [10, 20, 30, 40, 50, 60, 70, 80, 90, 150])
#gas_stations(100, 50, [10, 90])


