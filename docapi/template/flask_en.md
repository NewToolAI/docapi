## Input

```python
# Get a list of students in a certain grade
@app.route('/users/list', methods=['GET', 'POST'])
def get_users():
    api_key = request.headers.get('API-KEY')
    if api_key != EXPECTED_API_KEY:
        return jsonify(code=1, data=[], error='Invalid API key'), 401

    if request.method == 'POST':
        params = request.get_json(silent=True) or {{}}
    else: 
        params = request.args.to_dict()

    grade = params.get('grade')
    if not grade:
        return jsonify(code=1, data=[], error='grade is required'), 400

    try:
        data = stuents.get_students(grade)
        return jsonify(code=0, data=data, error=''), 200
    except Exception as e:
        return jsonify(code=1, data=[], error=str(e)), 500
```

## Output

### GET | POST - /users/list

##### Last Updated

{datetime}

##### Description

This API endpoint retrieves the list of students for a specified grade. Users must provide the grade parameter, and the API will return the list of students in that grade.

##### Request Headers

- `API-KEY` (string): The API key used for authentication.

##### Request Parameters - JSON

- `grade` (string): Required. The name of the grade.

##### Response - JSON

- `code` (integer): Status code. `0` indicates success, `1` indicates failure.

- `data` (array): Contains the list of students for the specified grade.

- `error` (string): Error message. An empty string if the operation is successful.

##### Code Example 

**curl:**

```bash
curl -X GET 'http://API_BASE/users/list?grade=3' \
     -H 'API-KEY: your_api_key'
```

**python:**

```python
import requests

url = 'http://API_BASE/users/list'
headers = {{'API-KEY': 'your_api_key'}}
params = {{'grade': '3'}}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

**javascript:**

```javascript
import axios from 'axios';

const url = 'http://API_BASE/users/list';
const headers = {{ 'API-KEY': 'your_api_key' }};
const params = {{ grade: '3' }}

axios.get(url, {{ headers, params }})
    .then(response => console.log(response.data))
    .catch(error => console.error(error));
```
