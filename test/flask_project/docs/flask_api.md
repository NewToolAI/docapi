# flask_api.py

*Path: `/Volumes/DATA/工作/Work/my_project/docapi/test/flask_project/flask_api.py`*

### GET - /users/scores

##### 更新时间
2024-11-18 19:20

##### 描述
该接口用于获取指定学生的成绩列表。用户需要提供学生的ID，接口将返回该学生的成绩信息。

##### 参数
- `ID` (string): 必填，学生的ID。

##### 返回值
- `string`: 返回学生的成绩信息，格式为 `"scores of <ID>"`。

##### 代码示例 

**curl:**
```bash
curl -X GET http://<api_url>/users/scores?ID=12345
```

**python:**
```python
import requests

url = "http://<api_url>/users/scores"
params = {"ID": "12345"}

response = requests.get(url, params=params)

print("状态码:", response.status_code)
print("响应内容:", response.text)
```

**javascript:**
```javascript
const axios = require('axios');

const url = 'http://<api_url>/users/scores';
const params = { ID: '12345' };

axios.get(url, { params })
  .then(response => {
    console.log('状态码:', response.status);
    console.log('响应内容:', response.data);
  })
  .catch(error => {
    console.error('错误:', error.response ? error.response.data : error.message);
  });
```
---

