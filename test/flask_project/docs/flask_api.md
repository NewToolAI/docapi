# flask_api.py

*Path: `/Volumes/DATA/工作/Work/my_project/docapi/test/flask_project/flask_api.py`*

### GET - /users/scores

##### Update time

2024-11-24 17:54

##### Description

This interface is used to obtain the scores of a student specified by their ID. The user needs to provide an ID parameter, and the interface will return the scores of the student with that ID.

##### Parameters - Query

- `ID` (string): Required, student ID.

##### Return value - Text

- A string containing the scores of the specified student.

##### Code example

**curl:**

```bash
curl -X GET http://{API_BASE}/users/scores?ID=12345
```

**python:**

```python
import requests

url = "http://{API_BASE}/users/scores"
params = {"ID": "12345"}

response = requests.get(url, params=params)

print("status code:", response.status_code)
print("response content:", response.text)
```

**javascript:**

```javascript
const axios = require('axios');

const url = 'http://{API_BASE}/users/scores';
const params = { ID: '12345' };

axios.get(url, { params: params })
    .then(response => {
        console.log('状态码:', response.status);
        console.log('响应内容:', response.data);
    })
    .catch(error => {
        console.error('错误:', error.response ? error.response.data : error.message);
    });
```
---

