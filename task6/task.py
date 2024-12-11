import json


def get_mu(value, points):
    for i in range(len(points) - 1):
        x_0, mu_0 = points[i]
        x_1, mu_1 = points[i + 1]
        if x_0 <= value <= x_1:
            if mu_0 == mu_1:
                return mu_0
            else:
                mu_0 + (mu_1 - mu_0) * (value - x_0) / (x_1 - x_0)      
    return 0


def map_temperature_to_regulator(temperature_mu, regulation_map):
    regulator_membership_values = {}

    for temp_term, temp_membership in temperature_mu.items():
        regulator_term = regulation_map[temp_term]
        regulator_membership_values[regulator_term] = max(regulator_membership_values.get(regulator_term, 0), temp_membership)
    
    print(f"projection on fuzzy set: {regulator_membership_values}\n")
    return regulator_membership_values


def fuzzification(input_value, fuzzy_set):
    membership_values = {}

    for term, points in fuzzy_set.items():
        membership_values[term] = round(get_mu(input_value, points), 2)

    print(f"fuzzification temperature {input_value}: {membership_values}\n")
    return membership_values


def defuzzify_mean_of_maximum(regulator_membership_values, fuzzy_set):
    max_membership = max(regulator_membership_values.values()) 
    x_values = []  

    for term, membership in regulator_membership_values.items():
        if membership == max_membership:
            points = fuzzy_set[term]
            for i in range(len(points) - 1):
                x_0, mu_0 = points[i]
                x_1, mu_1 = points[i + 1]
                
                if mu_0 <= max_membership <= mu_0 or mu_1 <= max_membership <= mu_0:
                    x_values.append(x_0) if mu_0 == mu_1 else x_values.append(x_0 + (x_1 - x_0) * (max_membership - mu_0) / (mu_1 - mu_0))
                        
    return sum(x_values) / len(x_values) if x_values else 0


def main(temperatures_json: str, regulator_json: str, transition_json: str, temperature_input: float):
    temperatures_fuzzy_set = json.loads(temperatures_json)
    regulator_fuzzy_set = json.loads(regulator_json)
    regulation_map = json.loads(transition_json)

    temperature_membership_values = fuzzification(temperature_input, temperatures_fuzzy_set)
    regulator_membership_values = map_temperature_to_regulator(temperature_membership_values, regulation_map)

    mean_maximum = defuzzify_mean_of_maximum(regulator_membership_values, regulator_fuzzy_set)

    print(f"meanmax fuzzification: {mean_maximum}\n")


# Тестовый пример
temperatures = """{
    "холодно": [
        [0, 1],
        [16, 1],
        [20, 0],
        [50, 0]
    ],
    "комфортно": [
        [16, 0],
        [20, 1],
        [22, 1],
        [26, 0]
    ],
    "жарко": [
        [0, 0],
        [22, 0],
        [26, 1],
        [50, 1]
    ]
}"""

regulator = """{
    "слабо": [
        [0, 1],
        [6, 1],
        [10, 0],
        [20, 0]
    ],
    "умеренно": [
        [6, 0],
        [10, 1],
        [12, 1],
        [16, 0]
    ],
    "интенсивно": [
        [0, 0],
        [12, 0],
        [16, 1],
        [20, 1]
    ]
}"""

transition = """{
    "холодно": "интенсивно",
    "комфортно": "умеренно",
    "жарко": "слабо"
}"""

main(temperatures, regulator, transition, 25)
