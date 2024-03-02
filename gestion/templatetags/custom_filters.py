from django import template

register = template.Library()

#Codigo realiza que el numero de la visualizacion solo muertre los ultimos 4 digitos 

@register.filter(name='obligacion_format')
def obligacion_format(value):
    # Verifica que el valor sea una cadena antes de aplicar el formato
    if isinstance(value, str) and len(value) >= 4:
        # Muestra solo los últimos 4 dígitos y oculta el resto con '*'
        return '*' * (len(value) - 4) + value[-4:]
    else:
        return value