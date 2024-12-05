# flask_project/server.py

*Path: `/Volumes/DATA/工作/Work/my_project/docapi/test/flask_project/server.py`*

### GET - /users/<user_id>

##### 更新时间

2023-04-01 12:00

##### 描述

该接口用于获取指定用户ID的用户信息。通过访问该接口，可以获取到用户的基本信息。

##### 参数

- `user_id` (integer): 必填，用户的唯一标识符。

##### 返回值

- 返回用户信息字符串，格式为 "User <user_id>"。

##### 代码示例

**curl:**

```bash
curl -X GET http://{API_BASE}/users/123
```

**python:**

```python
import requests

url = "http://{API_BASE}/users/123"

response = requests.get(url)

print("状态码:", response.status_code)
print("响应内容:", response.text)
```

**javascript:**

```javascript
const axios = require('axios');

const url = 'http://{API_BASE}/users/123';

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

2024-12-05 12:22

##### 描述

该接口用于创建学生系统用户。用户需要通过POST请求提交用户名和年龄信息，接口将返回创建的用户信息。

##### 参数 - Json

- `name` (string): 必填，用户名。
- `age` (integer): 必填，用户年龄。

##### 返回值 - Json

- `code` (integer): 返回状态码，0表示成功，1表示失败。
- `data` (object): 包含创建的用户信息。
- `error` (string): 错误信息，成功时为空字符串。

##### 代码示例 

**curl:**

```bash
curl -X POST http://{API_BASE}/users/create -H "Content-Type: application/json" -d '{"name": "张三", "age": 20}'
```

**python:**

```python
import requests

url = "http://{API_BASE}/users/create"
data = {"name": "张三", "age": 20}

response = requests.post(url, json=data)

print("状态码:", response.status_code)
print("响应内容:", response.json())
```

**javascript:**

```javascript
const axios = require('axios');

const url = 'http://{API_BASE}/users/create';
const data = { name: '张三', age: 20 };

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

##### 更新时间

2024-12-05 12:22

##### 描述

该接口用于获取指定年级的学生列表。用户需要提供年级参数，接口将返回该年级的学生列表。

##### 参数 - Json

- `grade` (string): 必填，年级名称。

##### 返回值 - Json

- `code` (integer): 返回状态码，0表示成功，1表示失败。

- `data` (array): 包含该年级的学生列表。

- `error` (string): 错误信息，成功时为空字符串。

##### 代码示例 

**curl:**

```bash
curl -X GET http://{API_BASE}/users/list -H "Content-Type: application/json" -d '{"grade": "高一"}'
```

**python:**

```python
import requests

url = "http://{API_BASE}/users/list"
data = {"grade": "高一"}

response = requests.get(url, json=data)

print("状态码:", response.status_code)
print("响应内容:", response.json())
```

**javascript:**

```javascript
const axios = require('axios');

const url = 'http://{API_BASE}/users/list';
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

