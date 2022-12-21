import geocoder

def converter(endereco):
    #g = geocoder.google(request.POST['endereco'], key='', method='places')
    g = geocoder.osm(endereco)
    resultado = [g.latlng[0], g.latlng[1]]
    return resultado