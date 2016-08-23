#Tornado WebSocket Example

This example will going to combine `tornado` with various framework of python (ie: celery, requests,)

###Hello Tornado
-----------------
First at first, we need to run the tornado at a very simple level. output a string like `hello tornado` is good idea! but before do it, you need to get the `tornado` , it's very simple command can reach it! but I also like to install it on my `virtual env` , so you probably need to do the following command for now.

```
mkdir tornado-project
cd tornado-project
virtualenv tornadoEnv
source ./tornadoEnv/bin/activate
pip install tornado
```
If you just when to test my example code, you just need to `clone` my code from github and then do some prepare job.

```
git clone https://github.com/land-pack/tornado-websocket-example.git
cd tornado-websocket-example
virtualenv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

### WebScoket with Tornado
--------------------


