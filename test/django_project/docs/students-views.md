# students/views.py

*Path: `/Volumes/DATA/工作/Work/my_project/docapi/test/django_project/students/views.py`*

### GET - /student/list

##### 更新时间

2024-12-05 12:21

##### 描述

该接口用于获取所有学生的信息列表。接口将返回包含学生ID、姓名、年龄、年级和电子邮件的JSON数组。

##### 参数

无

##### 返回值 - Json

- `id` (integer): 学生的唯一标识符。

- `name` (string): 学生的姓名。

- `age` (integer): 学生的年龄。

- `grade` (string): 学生的年级。

- `email` (string): 学生的电子邮件地址。

##### 代码示例 

**curl:**

```bash
curl -X GET http://{API_BASE}/student/list
```

**python:**

```python
import requests

url = "http://{API_BASE}/student/list"

response = requests.get(url)

print("状态码:", response.status_code)
print("响应内容:", response.json())
```

**javascript:**

```javascript
const axios = require('axios');

const url = 'http://{API_BASE}/student/list';

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

2024-12-05 12:21

##### 描述

该接口用于添加一个新的学生记录。用户需要通过POST请求提交学生的姓名、年龄、年级和电子邮件。

##### 参数 - Form Data

- `name` (string): 必填，学生的姓名。
- `age` (integer): 必填，学生的年龄。
- `grade` (string): 必填，学生的年级。
- `email` (string): 必填，学生的电子邮件地址。

##### 返回值 - Json

- `id` (integer): 新添加的学生记录的ID。
- `message` (string): 操作结果信息。

- `error` (string): 错误信息，成功时为空字符串。

##### 状态码

- 201: 创建成功。
- 400: 请求中缺少必要的字段。
- 405: 请求方法无效。

##### 代码示例 

**curl:**

```bash
curl -X POST http://{API_BASE}/student/add -H "Content-Type: application/x-www-form-urlencoded" -d "name=张三&age=18&grade=高一&email=zhangsan@example.com"
```

**python:**

```python
import requests

url = "http://{API_BASE}/student/add"
data = {
    "name": "张三",
    "age": "18",
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
    age: '18',
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

### DELETE - /student/<student_id>

##### 更新时间

2023-04-01 12:00

##### 描述

该接口用于删除指定ID的学生信息。用户需要提供学生的ID，接口将删除该学生的信息。

##### 参数

- `student_id` (integer): 必填，学生的唯一标识符。

##### 返回值

- `id` (integer): 删除成功的学生的ID。
- `message` (string): 操作结果信息。

##### 状态码

- 200: 删除成功。
- 405: 请求方法错误。

##### 代码示例

**curl:**

```bash
curl -X DELETE http://{API_BASE}/student/123
```

**python:**

```python
import requests

url = "http://{API_BASE}/student/123"

response = requests.delete(url)

print("状态码:", response.status_code)
print("响应内容:", response.json())
```

**javascript:**

```javascript
const axios = require('axios');

const url = 'http://{API_BASE}/student/123';

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

### GET | POST - /student/edit/<student_id>

##### 更新时间

2024-12-05 12:21

##### 描述

该接口用于编辑指定学生的信息。用户需要提供学生的ID，接口将允许用户更新学生的姓名、年龄、年级和电子邮件信息。

##### 参数

- `student_id` (integer): 必填，学生的唯一标识符。

##### 请求方法

- `POST`: 用于提交学生信息的更新。

##### 返回值 - Json

- `id` (integer): 更新后的学生ID。
- `message` (string): 操作结果信息，成功时显示“Student updated successfully”。

##### 错误返回 - Json

- `error` (string): 错误信息，当请求方法不正确时显示“Invalid request method”。

##### 代码示例

**curl:**

```bash
curl -X POST http://{API_BASE}/student/edit/123 -H "Content-Type: application/json" -d '{"name": "张三", "age": 20, "grade": "大一", "email": "zhangsan@example.com"}'
```

**python:**

```python
import requests

url = "http://{API_BASE}/student/edit/123"
data = {"name": "张三", "age": 20, "grade": "大一", "email": "zhangsan@example.com"}

response = requests.post(url, json=data)

print("状态码:", response.status_code)
print("响应内容:", response.json())
```

**javascript:**

```javascript
const axios = require('axios');

const url = 'http://{API_BASE}/student/edit/123';
const data = { name: '张三', age: 20, grade: '大一', email: 'zhangsan@example.com' };

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

