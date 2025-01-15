import sys

filename = sys.argv[1]

def open_file(filename):
    try:
        f = open(filename, mode="r")
        data = f.readlines()
        f.close()
        return data
    except:
        print("FILE NOT FOUND. TRY AGAIN")

def get_driver_name_and_team_from_code(driver_code):
        f = open("f1_drivers.txt", mode="r")
        data = f.readlines()
        code_to_name = {}
        values = []
        for i in data:
            individual = i.split('.')
            stripped = individual[0].split(',')
            for i in stripped:
                code_to_name[stripped[1]] = [stripped[2], stripped[3]]

        return code_to_name[driver_code]

def map_driver_to_time(file_data):
    data = file_data[1:]
    driver_code_array = []
    for i in data:
        driver_code_array.append(i[0:3])
    drivers_set = set(driver_code_array)
    driver_racetime_dict = {}
    for driver in drivers_set:
        driver_racetime_dict[driver] = []
    for k, v in driver_racetime_dict.items():
        for driver_time in data:
            if k in driver_time:
                v.append(float(driver_time[3:-1]))
    return driver_racetime_dict

def display_average_and_fast(driver_time_dict):
    for k, v in driver_time_dict.items():
        driver_data = get_driver_name_and_team_from_code(k)
        print(f"FOR {driver_data[0]} -> {driver_data[1]}")
        avg_time = sum(v) / len(v)
        fastest = v[0]
        for i in v:
            if i < fastest:
                fastest = i
        # print("="*10)
        print(f"AVERAGE TIME: %.3f" % avg_time)
        print(f"FASTEST TIME FOR: {fastest}")
        print("="*40)

def display_race_name(data_from_file):
    return data_from_file[0]

def set_race_time_array(file_data):
   racer_and_time = file_data[1:]

   only_numbers = []
   for data in racer_and_time:
       only_numbers.append(float(data[3:-1]))

   return only_numbers, racer_and_time

def overall_average(time_arr):

    avg_overall = sum(time_arr) / len(time_arr)
    return avg_overall

def display_fastest_time_overall(race_time_arr, racer_arr):
    fastest = race_time_arr[0]

    for i in race_time_arr:
        if i < fastest:
            fastest = i

    for i in racer_arr:
        if str(fastest) in i:
            return i
        
def display_results():
    file_data = open_file(filename)
    on, rat = set_race_time_array(file_data)
    code_with_time = display_fastest_time_overall(on, rat)
    code = code_with_time[0:3]
    driver_data = get_driver_name_and_team_from_code(code)
    overall_average_racers = overall_average(on)
    dict_driver_racetime = map_driver_to_time(file_data)
    # map_driver_to_time(file_data)

    # map_driver_to_time(file_data)


    print(f"\t\tIN THE FILE {filename}\t\t\n")
    print(f"RACING VENUE: {display_race_name(file_data)}")
    print(f"THE FASTEST DRIVER WAS {driver_data[0]} - {driver_data[1]}\n")
    print(f"HIS TIME WAS {code_with_time[3:]}")
    print(f"\t\tOVERALL AVERAGE TIME OF ALL PLAYERS: %.3f\t\t\n" % overall_average_racers)
    display_average_and_fast(dict_driver_racetime)
    print('\n')


display_results()
