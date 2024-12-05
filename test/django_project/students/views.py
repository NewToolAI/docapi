from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Student


def student_list(request):
    '''学生列表'''
    students = Student.objects.all().values('id', 'name', 'age', 'grade', 'email')
    return JsonResponse(list(students), safe=False)


# 增加学生
def student_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        grade = request.POST.get('grade')
        email = request.POST.get('email')

        if not all([name, age, grade, email]):
            return JsonResponse({'error': 'Missing required fields.'}, status=400)

        student = Student.objects.create(name=name, age=age, grade=grade, email=email)
        return JsonResponse({'id': student.id, 'message': 'Student added successfully'}, status=201)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


def student_edit(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        student.name = request.POST.get('name', student.name)
        student.age = request.POST.get('age', student.age)
        student.grade = request.POST.get('grade', student.grade)
        student.email = request.POST.get('email', student.email)
        student.save()

        return JsonResponse({'id': student.id, 'message': 'Student updated successfully'})

    return JsonResponse({'error': 'Invalid request method'}, status=405)


def student_delete(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'DELETE':
        student.delete()
        return JsonResponse({'id': student_id, 'message': 'Student deleted successfully'})

    return JsonResponse({'error': 'Invalid request method'}, status=405)
