def text_as_json(text, delimiter):
  elements = text.split(delimiter)
  json = "["
  for element in elements:
    json += "\"" + element + "\","
  if len(json) > 1:
    json = json[0:len(json) - 1]
  json += "]"
  return json

def json_as_text(json):
  return json[2:len(json) - 2].replace("\",\"", "\n")
