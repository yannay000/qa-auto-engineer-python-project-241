stylish_string ="""{
  - proxy: 123.234.53.22
  - follow: False
  - timeout: 50
  + timeout: 20
  + verbose: True
    host: hexlet.io
}"""

plain_string ="""Property 'proxy' was removed
Property 'follow' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was added with value: true
"""