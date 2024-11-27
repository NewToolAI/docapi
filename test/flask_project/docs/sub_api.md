# sub_api.py

*Path: `/Volumes/DATA/工作/Work/my_project/docapi/test/flask_project/sub_api.py`*

### GET - /users/scores

##### 更新时间

2024-11-27 14:03

##### 描述

该接口用于获取指定学生的成绩列表。用户需要提供学生ID参数，接口将返回该学生的成绩信息。

##### 参数 - Query

- `ID` (string): 必填，学生ID。

##### 返回值 - Text

- 成绩信息：包含指定学生的成绩列表。

##### 代码示例 

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

print("状态码:", response.status_code)
print("响应内容:", response.text)
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

