# flask_server.py

*Path: `/Volumes/DATA/工作/Work/my_project/docapi/test/flask_project/flask_server.py`*

### GET - /users/{user_id}

##### Update time

2024-11-24 17:54

##### Description

This interface is used to retrieve information about a specific user. The user ID is provided as a path parameter, and the interface returns the user's information.

##### Parameters - Path

- `user_id` (integer): Required, the unique identifier of the user.

##### Return value - Text

- A string containing the user's information, formatted as "User {user_id}".

##### Code example

**curl:**

```bash
curl -X GET http://{API_BASE}/users/1
```

**python:**

```python
import requests

url = "http://{API_BASE}/users/1"

response = requests.get(url)

print("status code:", response.status_code)
print("response content:", response.text)
```

**javascript:**

```javascript
const axios = require('axios');

const url = 'http://{API_BASE}/users/1';

axios.get(url)
    .then(response => {
        console.log('状态码:', response.status);
        console.log('响应内容:', response.data);
    })
    .catch(error => {
        console.error('错误:', error.response ? error.response.data : error.message);
    });
```
---

### POST - /users/create

##### Update time

2024-11-24 17:54

##### Description

This interface is used to create a new student system user. The user needs to provide the name and age parameters, and the interface will return the created user information.

##### Parameters - Json

- `name` (string): Required, the name of the user.
- `age` (integer): Required, the age of the user.

##### Return value - Json

- `code` (integer): Return status code, 0 means success.
- `data` (object): Contains the created user information.
  - `name` (string): The name of the user.
  - `age` (integer): The age of the user.
- `error` (string): Error message, `null` if successful.

##### Code example

**curl:**

```bash
curl -X POST http://{API_BASE}/users/create -H "Content-Type: application/json" -d '{"name": "John Doe", "age": 20}'
```

**python:**

```python
import requests

url = "http://{API_BASE}/users/create"
data = {"name": "John Doe", "age": 20}

response = requests.post(url, json=data)

print("status code:", response.status_code)
print("response content:", response.json())
```

**javascript:**

```javascript
const axios = require('axios');

const url = 'http://{API_BASE}/users/create';
const data = { name: 'John Doe', age: 20 };

axios.post(url, data)
    .then(response => {
        console.log('状态码:', response.status);
        console.log('响应内容:', response.data);
    })
    .catch(error => {
        console.error('错误:', error.response ? error.response.data : error.message);
    });
```
---

### GET | POST - /users/list

##### Update time

2024-11-24 17:54

##### Description

This interface is used to obtain a list of students in a specified grade. The user needs to provide a grade parameter, and the interface will return a list of students in that grade.

##### Parameters - Json

- `grade` (string): Required, grade name.

##### Return value - Json

- `code` (integer): Return status code, 0 means success.
- `data` (array): Contains a list of students in that grade.
- `error` (string): Error message, `null` if successful.

##### Code example

**curl:**

```bash
curl -X GET http://{API_BASE}/users/list -H "Content-Type: application/json" -d '{"grade": "grade 1"}'
```

**python:**

```python
import requests

url = "http://{API_BASE}/users/list"
data = {"grade": "grade 1"}

response = requests.get(url, json=data)

print("status code:", response.status_code)
print("response content:", response.json())
```

**javascript:**

```javascript
const axios = require('axios');

const url = 'http://{API_BASE}/users/list';
const data = { grade: 'grade 1' };

axios.get(url, { params: data })
    .then(response => {
        console.log('Status code:', response.status);
        console.log('Response content:', response.data);
    })
    .catch(error => {
        console.error('Error:', error.response ? error.response.data : error.message);
    });
```

**Note:** The `error` field in the response will be `null` if the request is successful.
---

