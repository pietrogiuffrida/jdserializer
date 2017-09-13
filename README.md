# jdserializer

This function enable json.dumps method to serialize datetime objects, by parsing them as strings.

## Usage

```python
d = {'test': datetime.now()}

json.dump(d, default=jdserializer)
# returns: '{"d": "20170913 230550"}'
```
