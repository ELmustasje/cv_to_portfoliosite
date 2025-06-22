import json
import re
import AIExtractor


def run(path_to_cv):
    text = AIExtractor.run(path_to_cv)
    match = re.search(r'```json(.*)```', text, re.MULTILINE | re.DOTALL)
    if match:
        json_content = match.group(1).strip()
        parsed = json.loads(json_content)
        print("Extracted parsed JSON:")

        with open("siteCreator/site/public/data.json", "w") as file:
            json.dump(parsed, file, indent=4)
    else:
        print("No parsed JSON found.")
