def gas_stations(distance, tank_size, stations):
    result = []
    travaled_distance = tank_size
    
    for idx, station in enumerate(stations):
        
        if distance < stations[-1]:
            stations.remove(stations[-1])

        if travaled_distance > station:
            continue

        travaled_distance = tank_size + stations[idx - 1]
        result.append(stations[idx - 1])

        if travaled_distance <= station:
            return []

    if travaled_distance > stations[-1] and travaled_distance < distance:
        result.append(stations[-1])


    print(result, travaled_distance)    
    return result
# print(gas_stations(320, 90, [50, 80, 140, 180, 220, 290]) == [80, 140, 220, 290])
# print(gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350]) == [70, 140, 210, 280, 350])
# print(gas_stations(100, 50, [10, 20, 30, 40, 50, 60, 70, 80, 90, 150]) == [40, 80])
# print(gas_stations(100, 50, [10, 90]) == [])
# print(gas_stations(150, 40, [30, 40, 80, 90, 130]) == [])


