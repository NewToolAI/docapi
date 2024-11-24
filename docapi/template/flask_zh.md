## 输入

```python
# 获取年级学生列表
@app.route('/users/list', methods=['GET', 'POST'])
def get_users():
    try:
        parmams = request.get_json()
        grade = parmams['grade']
        data = f'List of {{grade}} students'.split(' ')

        return jsonify(code=0, data=data, error='')
    except Exception as e:
        return jsonify(code=1, data=None, error=str(e))
```

## 输出

### GET | POST - /users/list

##### 更新时间

{datetime}

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
curl -X GET http://{{API_BASE}}/users/list -H "Content-Type: application/json" -d '{{"grade": "高一"}}'
```

**python:**

```python
import requests

url = "http://{{API_BASE}}/users/list"
data = {{"grade": "高一"}}

response = requests.get(url, json=data)

print("状态码:", response.status_code)
print("响应内容:", response.json())
```

**javascript:**

```javascript
const axios = require('axios');

const url = 'http://{{API_BASE}}/users/list';
const data = {{ grade: '高一' }};

axios.get(url, {{ params: data }})
    .then(response => {{
       console.log('状态码:', response.status);
        console.log('响应内容:', response.data);
      }})
    .catch(error => {{
        console.error('错误:', error.response ? error.response.data : error.message);
    }});
```
