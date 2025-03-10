from add import *
import pytest

status = app.test_client().get('/').status_code
data=app.test_client().get('/').data

assert status==200 , 'invalid'
assert data== b'<h1 style = "color:red;"> Hello World <h1>'


