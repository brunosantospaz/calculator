from django.shortcuts import render

def calculate(request):
    if request.method == 'POST':
        first_number = int(request.POST['first_number'])
        second_number = int(request.POST['second_number'])
        operation = request.POST['operation']
        result = None
        if operation == 'add':
            result = first_number + second_number
        elif operation == 'subtract':
            result = first_number - second_number
        elif operation == 'multiply':
            result = first_number * second_number
        elif operation == 'divide':
            result = first_number / second_number
        return render(request, 'calculatorapp/result.html', {'result': result})
    return render(request, 'calculatorapp/calculate.html')
