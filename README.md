
可以获得国内银行卡的一些信息。

## Install

```bash
pip install bankinfo
```

## 实例
```python
from bankinfo.validator import BankInfoValidator
bank.validate('6217000130008255555')
```
```json
{
 'bank': 'CCB', # 银行名称
 'cardType': 'DC', # 信用卡 储蓄卡
 'key': '6217000130008255555',
 'messages': [],
 'stat': 'ok',
 'validated': True
 }
```

或者
```
bankinfo 6217000130008255555
```