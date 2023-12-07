def load_conversion_map(lines):
    conversion_map = []
    for line in lines:
        values = line.split()
        if len(values) >= 3:
            dest_start, source_start, length = map(int, values[:3])
            conversion_map.append((dest_start, source_start, length))
    return conversion_map

def apply_conversion_map(value, conversion_map):
    for dest_start, source_start, length in conversion_map:
        if source_start <= value < source_start + length:
            return dest_start + (value - source_start)
    return value

def convert_seed_to_location(seed, conversion_maps):
    for conversion_map in conversion_maps:
        seed = apply_conversion_map(seed, conversion_map)
    return seed

def find_min_location(seeds, conversion_maps):
    min_location = min(convert_seed_to_location(seed, conversion_maps) for seed in seeds)
    return min_location

def main():
    with open('input.txt') as file:
        lines = file.read().splitlines()

    seeds = list(map(int, lines[0].split()[1:]))
    seed_to_soil_map = load_conversion_map(lines[10:18])
    soil_to_fertilizer_map = load_conversion_map(lines[19:28])
    fertilizer_to_water_map = load_conversion_map(lines[29:38])
    water_to_light_map = load_conversion_map(lines[39:48])
    light_to_temperature_map = load_conversion_map(lines[49:58])
    temperature_to_humidity_map = load_conversion_map(lines[59:68])
    humidity_to_location_map = load_conversion_map(lines[69:78])

    conversion_maps = [
        seed_to_soil_map,
        soil_to_fertilizer_map,
        fertilizer_to_water_map,
        water_to_light_map,
        light_to_temperature_map,
        temperature_to_humidity_map,
        humidity_to_location_map
    ]

    result = find_min_location(seeds, conversion_maps)
    print(result)

if __name__ == "__main__":
    main()
