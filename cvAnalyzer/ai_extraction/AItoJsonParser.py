import json
import regex as re
import ai_extraction.AIExtractor as AIExtractor


def run(path_to_cv):
    text = AIExtractor.run(path_to_cv)
    print(text)
    match = re.search(r'({(?:[^{}]|(?R))*})', text, re.DOTALL)
    if match:
        json_content = match.group(1).strip()
        print(json_content)
        parsed = json.loads(json_content)
        print("Extracted parsed JSON:")

        with open("siteCreator/site/src/data/info.json", "w") as file:
            json.dump(parsed, file, indent=4)
    else:
        print("No parsed JSON found.")
