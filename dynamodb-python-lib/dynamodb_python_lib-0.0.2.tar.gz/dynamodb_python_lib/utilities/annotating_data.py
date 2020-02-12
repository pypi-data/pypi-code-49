import uuid
import requests
import json


URL = "http://amerigo.ai-labs.us-west-2.test.expedia.com/ccaip-facade-service/execute"
LOCALE = "en_us"


def execute(text: str, url: str = URL, locale: str = LOCALE) -> dict:
    result = {
        "intent": "",
        "intent_confidence": 0,
        "sentiment": "",
        "sentiment_confidence": 0,
        "product": "",
        "amenity_class": "",
        "amenity_value": ""
    }
    data = {"botVersion": "latest",
            "locale": locale,
            "sessionId": str(uuid.uuid4()),
            "message": text}

    r = requests.post(url,
                      headers={"Content-Type": "application/json"},
                      data=json.dumps(data))

    if not r or r.status_code != 200:
        return None
    response_json = json.loads(r.text)

    if len(response_json) > 0:
        result["intent"] = response_json["intentName"]
        result["intent_confidence"] = float(response_json["confidenceScore"])
        result["sentiment"] = response_json["sentiment"]["name"]
        result["sentiment_confidence"] = float(response_json["sentiment"]["score"])

        slots = response_json["slots"]
        for slot in slots:
            if "name" in slot:
                if slot["name"] == "product":
                    result["product"] = slot["value"] if "value" in slot else ""

                elif slot["name"] == "hotelAmenity":
                    result["amenity_class"] = slot["value"] if "value" in slot else ""
                    result["amenity_value"] = slot["extra"] if "extra" in slot else ""

    return result
