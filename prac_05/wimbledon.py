"""
Game, Set, Match
Estimate: 60 min
Actual:   66 min
"""

FILENAME = "wimbledon.csv"


def main():
    """Read and process data file, then display data"""
    pairs = get_data(FILENAME)
    countries, champion_to_win_count = process_data(pairs)
    display_data(champion_to_win_count, countries)


def display_data(champions_to_score, countries):
    """Display champions and countries that have won Wimbledon"""
    print("Wimbledon Champions:")
    for champion in champions_to_score.items():
        print(f"{champion[0]} {champion[1]}")
    print()  # Blank line for formatting
    print(f"These {len(countries)} have won Wimbledon:")
    print(", ".join(country for country in sorted(countries)))


def process_data(data):
    """Process data into a set of countries and dictionary of champions and win counts"""
    countries = set()
    champion_to_win_count = {}
    for pair in data:
        countries.add(pair[0])
        if pair[1] in champion_to_win_count:
            champion_to_win_count[pair[1]] += 1
        else:
            champion_to_win_count[pair[1]] = 1
    return countries, champion_to_win_count


def get_data(filename):
    """Extract data from file and add to a list of lists"""
    pairs = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            line = line.strip().split(",")
            pairs.append(line[1:3])
    return pairs


main()
