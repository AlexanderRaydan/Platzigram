from django.http import HttpResponse

from datetime import datetime
import json

def hello_world(request):

    now = datetime.now().strftime('%b %dth, %Y - %H: %M hr')

    return HttpResponse('wenaaaaaaaas {now} '.format(now=str(now)))


def sorted_numbers(request):

    #import pdb ; pdb.set_trace()
    numbers = request.GET['numbers']

    numbers = numbers.split(',')

    print(numbers)

    numbers = sorted([int(i) for i in numbers])
    
    print(numbers)

    data = {

        'status': 'OK',
        'numbers': numbers,
        'massage': 'Integers sorted succesfuly'
    }

    return HttpResponse(json.dumps(data, indent=4), content_type = 'application/json')


def sayHi(request, name , age):

    return HttpResponse('no pareces de 15 {name} , {age}'.format(name = name, age = age))




