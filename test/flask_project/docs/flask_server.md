# flask_server.py

*Path: `/Volumes/DATA/工作/Work/my_project/docapi/test/flask_project/flask_server.py`*

### GET - /users/{user_id}

##### 更新时间
2024-11-18 19:18

##### 描述
该接口用于获取指定ID的用户信息。

##### 参数
- `user_id` (integer): 必填，用户的唯一标识ID。

##### 返回值
- `string`: 返回用户信息，格式为 "User {user_id}"。

##### 代码示例 

**curl:**
```bash
curl -X GET http://<api_url>/users/1
```

**python:**
```python
import requests

url = "http://<api_url>/users/1"

response = requests.get(url)

print("状态码:", response.status_code)
print("响应内容:", response.text)
```

**javascript:**
```javascript
const axios = require('axios');

const url = 'http://<api_url>/users/1';

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

##### 更新时间
2024-11-18 19:18

##### 描述
该接口用于创建一个新的学生系统用户。用户需要提供姓名和年龄，接口将返回创建的用户信息。

##### 参数
- `name` (string): 必填，学生的姓名。
- `age` (integer): 必填，学生的年龄。

##### 返回值
- `code` (integer): 返回状态码，0表示成功。
- `data` (object): 包含创建的用户信息，包含`name`和`age`字段。
- `error` (string|null): 错误信息，成功时为null。

##### 代码示例 

**curl:**
```bash
curl -X POST http://<api_url>/users/create -H "Content-Type: application/json" -d '{"name": "John Doe", "age": 20}'
```

**python:**
```python
import requests

url = "http://<api_url>/users/create"
data = {"name": "John Doe", "age": 20}

response = requests.post(url, json=data)

print("状态码:", response.status_code)
print("响应内容:", response.json())
```

**javascript:**
```javascript
const axios = require('axios');

const url = 'http://<api_url>/users/create';
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

### GET - /users/list

##### 更新时间
2024-11-18 19:18

##### 描述
该接口用于获取指定年级的学生列表。用户需要提供年级参数，接口将返回该年级的学生列表。

##### 参数
- `grade` (string): 必填，年级名称。

##### 返回值
- `code` (integer): 返回状态码，0表示成功。
- `data` (array): 包含该年级的学生列表。
- `error` (string|null): 错误信息，成功时为null。

##### 代码示例 

**curl:**
```bash
curl -X GET http://<api_url>/users/list -H "Content-Type: application/json" -d '{"grade": "高一"}'
```

**python:**
```python
import requests

url = "http://<api_url>/users/list"
data = {"grade": "高一"}

response = requests.get(url, json=data)

print("状态码:", response.status_code)
print("响应内容:", response.json())
```

**javascript:**
```javascript
const axios = require('axios');

const url = 'http://<api_url>/users/list';
const data = { grade: '高一' };

axios.get(url, { params: data })
  .then(response => {
    console.log('状态码:', response.status);
    console.log('响应内容:', response.data);
  })
  .catch(error => {
    console.error('错误:', error.response ? error.response.data : error.message);
  });
```
---

