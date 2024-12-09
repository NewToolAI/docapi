## 输入

```python
# 获取年级学生列表
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

## 输出

### GET | POST - /users/list

##### 更新时间

{datetime}

##### 描述

该接口用于获取指定年级的学生列表。用户需要提供年级参数，接口将返回该年级的学生列表。

##### 请求头

- `API-KEY` (string): 用于身份验证的API密钥。

##### 请求参数 - Json

- `grade` (string): 必填，年级名称。

##### 返回值 - Json

- `code` (integer): 返回状态码，0表示成功，1表示失败。

- `data` (array): 包含该年级的学生列表。

- `error` (string): 错误信息，成功时为空字符串。

##### 代码示例 

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
const params = {{ 'grade': '3' }};

axios.get(url, {{ headers, params }})
    .then(response => console.log(response.data))
    .catch(error => console.error(error));
```
