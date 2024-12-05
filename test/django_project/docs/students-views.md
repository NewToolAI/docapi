# students/views.py

*Path: `/Volumes/DATA/工作/Work/my_project/docapi/test/django_project/students/views.py`*

### GET - /student

##### 更新时间

2024-12-05 14:55

##### 描述

该接口用于获取所有学生的列表，返回学生的基本信息，包括ID、姓名、年龄、年级和邮箱。

##### 参数

无需参数。

##### 返回值 - Json

- `id` (integer): 学生的唯一标识符。
- `name` (string): 学生的姓名。
- `age` (integer): 学生的年龄。
- `grade` (string): 学生所在的年级。
- `email` (string): 学生的邮箱地址。

##### 代码示例 

**curl:**

```bash
curl -X GET http://{API_BASE}/student
```

**python:**

```python
import requests

url = "http://{API_BASE}/student"

response = requests.get(url)

print("状态码:", response.status_code)
print("响应内容:", response.json())
```

**javascript:**

```javascript
const axios = require('axios');

const url = 'http://{API_BASE}/student';

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

### POST - /student/add

##### 更新时间

2024-12-05 14:55

##### 描述

该接口用于增加一个新的学生记录。用户需要提供学生的姓名、年龄、年级和邮箱信息，接口将创建学生记录并返回学生的ID。

##### 参数 - POST

- `name` (string): 必填，学生姓名。
- `age` (integer): 必填，学生年龄。
- `grade` (string): 必填，学生年级。
- `email` (string): 必填，学生邮箱。

##### 返回值 - Json

- `id` (integer): 新增学生的ID。
- `message` (string): 操作成功或失败的消息。
- `error` (string): 错误信息，如果请求成功则为空字符串。

##### 代码示例 

**curl:**

```bash
curl -X POST http://{API_BASE}/student/add -d "name=张三&age=18&grade=高一&email=zhangsan@example.com"
```

**python:**

```python
import requests

url = "http://{API_BASE}/student/add"
data = {
    "name": "张三",
    "age": 18,
    "grade": "高一",
    "email": "zhangsan@example.com"
}

response = requests.post(url, data=data)

print("状态码:", response.status_code)
print("响应内容:", response.json())
```

**javascript:**

```javascript
const axios = require('axios');

const url = 'http://{API_BASE}/student/add';
const data = {
    name: '张三',
    age: 18,
    grade: '高一',
    email: 'zhangsan@example.com'
};

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

### DELETE - /student/delete/{student_id}

##### 更新时间

2024-12-05 14:55

##### 描述

该接口用于删除指定ID的学生记录。用户需要提供学生ID，接口将删除该学生记录并返回删除成功的消息。

##### 参数 - URL

- `student_id` (integer): 必填，学生的唯一标识符。

##### 返回值 - Json

- `id` (integer): 被删除学生的ID。
- `message` (string): 删除成功的消息。
- `error` (string): 错误信息，成功时为空字符串。

##### 代码示例 

**curl:**

```bash
curl -X DELETE http://{API_BASE}/student/delete/123
```

**python:**

```python
import requests

url = "http://{API_BASE}/student/delete/123"

response = requests.delete(url)

print("状态码:", response.status_code)
print("响应内容:", response.json())
```

**javascript:**

```javascript
const axios = require('axios');

const url = 'http://{API_BASE}/student/delete/123';

axios.delete(url)
    .then(response => {
        console.log('状态码:', response.status);
        console.log('响应内容:', response.data);
    })
    .catch(error => {
        console.error('错误:', error.response ? error.response.data : error.message);
    });
```
---

### POST - /student/edit/<int:student_id>

##### 更新时间

2024-12-05 14:55

##### 描述

该接口用于编辑指定学生的信息。用户需要提供学生ID，并通过POST请求发送更新后的学生信息。

##### 参数 - URL

- `student_id` (integer): 必填，学生的唯一标识符。

##### 参数 - POST

- `name` (string): 可选，学生的姓名。
- `age` (integer): 可选，学生的年龄。
- `grade` (string): 可选，学生的年级。
- `email` (string): 可选，学生的电子邮件地址。

##### 返回值 - Json

- `id` (integer): 成功更新后返回的学生ID。
- `message` (string): 操作成功或失败的消息。
- `error` (string): 错误信息，仅在请求方法无效时返回。

##### 代码示例 

**curl:**

```bash
curl -X POST http://{API_BASE}/student/edit/123 -H "Content-Type: application/x-www-form-urlencoded" -d "name=张三&age=18&grade=高二&email=zhangsan@example.com"
```

**python:**

```python
import requests

url = "http://{API_BASE}/student/edit/123"
data = {
    "name": "张三",
    "age": 18,
    "grade": "高二",
    "email": "zhangsan@example.com"
}

response = requests.post(url, data=data)

print("状态码:", response.status_code)
print("响应内容:", response.json())
```

**javascript:**

```javascript
const axios = require('axios');

const url = 'http://{API_BASE}/student/edit/123';
const data = new URLSearchParams({
    name: '张三',
    age: 18,
    grade: '高二',
    email: 'zhangsan@example.com'
});

axios.post(url, data.toString(), {
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
})
    .then(response => {
        console.log('状态码:', response.status);
        console.log('响应内容:', response.data);
    })
    .catch(error => {
        console.error('错误:', error.response ? error.response.data : error.message);
    });
```
---

