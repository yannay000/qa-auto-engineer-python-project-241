stylish_string ="""{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

plain_string ="""Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was added with value: true"""

json_string ="""{
  "host": "hexlet.io",
  "timeout": 20,
  "proxy": "123.234.53.22",
  "follow": false,
  "verbose": true
}"""