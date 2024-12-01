import json

def main(ranking_json1, ranking_json2):
    ranking1 = json.loads(ranking_json1)
    ranking2 = json.loads(ranking_json2)

    def extract_elements(ranking):
        elements = []
        for item in ranking:
            if isinstance(item, list):
                elements.extend(item)
            else:
                elements.append(item)
        return set(elements)

    elements1 = extract_elements(ranking1)
    elements2 = extract_elements(ranking2)

    conflict_core = []
    for elem in elements1:
        if elem not in elements2:
            conflict_core.append(str(elem))

    return json.dumps([conflict_core])

if __name__ == "__main__":
    main()