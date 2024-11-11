# flask_server.py

*path: `/Volumes/DATA/工作/Work/my_project/docapi/docapi/../test/flask_server.py`*

## 接口: /users

*md5: `3d2de1f5180f3a2558e73c252bc4aa56`*

### 参数: 
无

### 返回值: 
- `string`: 返回用户列表的字符串。

### 描述: 
该接口用于获取用户列表。调用此接口将返回一个包含用户信息的字符串。

### 代码示例: 
```bash
curl -X GET http://<api_url>/users
```
## 接口: /users/<int:user_id>

*md5: `e9906ee690e020ab8b2672c7f683042f`*

### 参数: 
- `user_id` (integer): 用户的唯一标识符，必填。

### 返回值: 
- `string`: 返回用户的描述信息，格式为"User {user_id}"。

### 描述: 
该接口用于获取指定用户的信息。用户需要提供用户的唯一标识符，接口将返回该用户的描述信息。

### 代码示例: 
```bash
curl -X GET http://<api_url>/users/1
```
## 接口: /users/create

*md5: `2620df460ceadf3fb0fdaba1ecc7bb37`*

### 参数: 
- `name` (string): 学生的姓名，必填。
- `age` (integer): 学生的年龄，必填。

### 返回值: 
- `code` (integer): 返回状态码，0表示成功。
- `data` (object): 包含创建的用户信息，包含`name`和`age`字段。
- `error` (string|null): 错误信息，成功时为null。

### 描述: 
该接口用于创建一个新的学生系统用户。用户需要提供姓名和年龄，接口将返回创建的用户信息。

### 代码示例: 
```bash
curl -X POST http://<api_url>/users/create -H "Content-Type: application/json" -d '{"name": "John Doe", "age": 20}'
```
