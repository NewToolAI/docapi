# students/views.py

*Path: `/Volumes/DATA/工作/Work/my_project/docapi/test/django_project/students/views.py`*

### GET - /student

##### Last Updated

2024-12-09 14:57

##### Description

This API endpoint retrieves a list of all students with their basic information including ID, name, age, grade, and email.

##### Request Headers

- None

##### Request Parameters

- None

##### Response - JSON

- `id` (integer): The unique identifier for the student.
- `name` (string): The name of the student.
- `age` (integer): The age of the student.
- `grade` (string): The grade of the student.
- `email` (string): The email address of the student.

##### Code Example 

**curl:**

```bash
curl -X GET 'http://API_BASE/student'
```

**python:**

```python
import requests

url = 'http://localhost:API_BASE/student'

response = requests.get(url)
print(response.json())
```

**javascript:**

```javascript
import axios from 'axios';

const url = 'http://API_BASE/student';

axios.get(url)
    .then(response => console.log(response.data))
    .catch(error => console.error(error));
```
---

### POST - /student/add

##### Last Updated

2024-12-09 14:57

##### Description

This API endpoint allows for the addition of a new student to the database. Users must provide the student's name, age, grade, and email. The endpoint will create a new student record and return the student's ID upon successful addition.

##### Request Headers

- `Content-Type` (string): Should be set to `application/x-www-form-urlencoded` or `multipart/form-data`.

##### Request Parameters - Form Data

- `name` (string): Required. The name of the student.
- `age` (integer): Required. The age of the student.
- `grade` (string): Required. The grade of the student.
- `email` (string): Required. The email address of the student.

##### Response - JSON

- `id` (integer): The ID of the newly created student record.
- `message` (string): A message indicating the success of the operation.
- `error` (string): Error message if the operation fails.

##### Code Example 

**curl:**

```bash
curl -X POST 'http://API_BASE/student/add' \
     -d 'name=John Doe' \
     -d 'age=15' \
     -d 'grade=10' \
     -d 'email=johndoe@example.com'
```

**python:**

```python
import requests

url = 'http://localhost:API_BASE/student/add'
data = {
    'name': 'John Doe',
    'age': '15',
    'grade': '10',
    'email': 'johndoe@example.com'
}

response = requests.post(url, data=data)
print(response.json())
```

**javascript:**

```javascript
import axios from 'axios';

const url = 'http://API_BASE/student/add';
const data = new FormData();
data.append('name', 'John Doe');
data.append('age', '15');
data.append('grade', '10');
data.append('email', 'johndoe@example.com');

axios.post(url, data)
    .then(response => console.log(response.data))
    .catch(error => console.error(error));
```
---

### DELETE - /student/delete/{student_id}

##### Last Updated

2024-12-09 15:00

##### Description

This API endpoint deletes a student record from the database based on the provided student ID. The endpoint only accepts DELETE requests.

##### Request Parameters

- `student_id` (integer): Required. The ID of the student to be deleted.

##### Response - JSON

- `id` (integer): The ID of the student that was deleted.

- `message` (string): A message indicating the success of the operation.

- `error` (string): An error message if the request method is invalid.

##### Code Example 

**curl:**

```bash
curl -X DELETE 'http://API_BASE/student/delete/123'
```

**python:**

```python
import requests

url = 'http://localhost:API_BASE/student/delete/123'
response = requests.delete(url)
print(response.json())
```

**javascript:**

```javascript
import axios from 'axios';

const url = 'http://API_BASE/student/delete/123';

axios.delete(url)
    .then(response => console.log(response.data))
    .catch(error => console.error(error));
```
---

### POST - /student/edit/<int:student_id>

##### Last Updated

2024-12-09 14:57

##### Description

This API endpoint allows for the editing of a student's details. Users must provide the student ID in the URL path and can update the student's name, age, grade, and email through POST parameters.

##### Request Parameters - URL Path

- `student_id` (integer): Required. The ID of the student to be edited.

##### Request Parameters - POST

- `name` (string): Optional. The new name of the student.
- `age` (integer): Optional. The new age of the student.
- `grade` (string): Optional. The new grade of the student.
- `email` (string): Optional. The new email of the student.

##### Response - JSON

- `id` (integer): The ID of the student that was updated.
- `message` (string): A success message indicating the student was updated successfully.

- **Error Response:**
  - `error` (string): Error message indicating an invalid request method.
  - `status` (integer): HTTP status code `405` for Method Not Allowed.

##### Code Example 

**curl:**

```bash
curl -X POST 'http://API_BASE/student/edit/123' \
     -d 'name=John Doe' \
     -d 'age=15' \
     -d 'grade=10' \
     -d 'email=johndoe@example.com'
```

**python:**

```python
import requests

url = 'http://localhost:API_BASE/student/edit/123'
data = {
    'name': 'John Doe',
    'age': '15',
    'grade': '10',
    'email': 'johndoe@example.com'
}

response = requests.post(url, data=data)
print(response.json())
```

**javascript:**

```javascript
import axios from 'axios';

const url = 'http://API_BASE/student/edit/123';
const data = {
    name: 'John Doe',
    age: '15',
    grade: '10',
    email: 'johndoe@example.com'
};

axios.post(url, data)
    .then(response => console.log(response.data))
    .catch(error => console.error(error));
```
---

