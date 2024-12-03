# sub_api.py

*Path: `/Volumes/DATA/工作/Work/my_project/docapi/test/flask_project/sub_api.py`*

### GET - /users/scores

##### 更新时间

2023-04-01 12:00

##### 描述

该接口用于获取指定学生的成绩列表。用户需要提供学生ID，接口将返回该学生的成绩信息。

##### 参数 - Query String

- `ID` (string): 必填，学生的唯一标识符。

##### 返回值 - Text

- 返回指定学生的成绩信息，格式为 "scores of {ID}"。

##### 代码示例 

**curl:**

```bash
curl -X GET http://{API_BASE}/users/scores?ID=123456
```

**python:**

```python
import requests

url = "http://{API_BASE}/users/scores"
params = {"ID": "123456"}

response = requests.get(url, params=params)

print("响应内容:", response.text)
```

**javascript:**

```javascript
const axios = require('axios');

const url = 'http://{API_BASE}/users/scores';
const params = { ID: '123456' };

axios.get(url, { params: params })
    .then(response => {
        console.log('响应内容:', response.data);
    })
    .catch(error => {
        console.error('错误:', error.message);
    });
```
---

