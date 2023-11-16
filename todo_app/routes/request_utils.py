def get_data_from_json(request):
    json = request.get_json()
    if type(json) == list:
        return json[0]
    else:
        return json