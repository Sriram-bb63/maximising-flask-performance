# Maximaising Flask performance in deployment

To maximise load handling capacity of a Flask API in deployment, we must first understand how it works.

## Flask and the internet

There are 2 components that helps Flask interact with the internet:

**1. Server**

A server is a piece of software responsible for handling incoming HTTP requests and sending back responses to clients, such as web browsers or API clients. The server is the component that listens on a specific port, waits for incoming requests, and then routes those requests to the appropriate Flask application for processing. Some commonly used servers for deploying Flask applications include Gunicorn, uWSGI, and the development server that comes with Flask.

**2. WSGI**

WSGI is a standard interface between web servers and web applications or frameworks written in Python. It defines how web servers and web applications should communicate. The primary purpose of WSGI is to provide a common and consistent way for web servers to interact with Python web applications, regardless of the specific web framework being used.

> TLDR: The server is a piece of code which listens for HTTP requests on a specific port. It directs the HTTP request to WSGI which creates a Request object and sends it to the right route in your app. 

## Flask and the OS

To know how Flask runs on a computer, we must first understand 2 key concepts: Concurrency and parallelism

Concurrency and parallelism are essential concepts in web development, and they often get mixed up. Concurrency is about managing multiple tasks simultaneously, but not necessarily executing them at the same time. In contrast, parallelism is about running multiple tasks at the same time.

When you run an app, you will notice the following message in the terminal:

```
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
```

The default development server that comes built-in with Flask is a single threaded process which can handle only one request at a time. The next request will be queued until a reponse has been generated for the first request.
<gif>

This could be optimized by processing multiple requests at the same time. If each requests gets to run on its own thread, then multiple requests can be processed at the same time.
<gif>

But there is something called GIL (Global Interpreter Lock) which prevents true parallelism. The GIL allows only one thread to execute Python code at a time. This limitation means that even though you can use multiple threads in a Python application, only one of them can execute Python code at any given moment. However we will be able to achieve concurrency using a multi threaded model.
<gif>

To bypass this issue, we have an option of running multiple instances of the app. Each instance will be an independent process with its own resource pool. This allows us to achieve true parallelism and enables the app to process multiple requests simultaneously.
<gif>

> TLDR: Flask can run on a computer using either a single-threaded development server, which handles one request at a time, or a multi-threaded model to process multiple requests concurrently. However, due to the Global Interpreter Lock (GIL) in Python, true parallelism is limited, but you can achieve it by running multiple independent app instances to process requests simultaneously.

## Using Gunicorn to deploy

Gunicorn (Green Unicorn) is a popular production-ready WSGI HTTP server for Python applications like Flask. It runs independent of the web app you deploy. It has 2 types of processes: Master process and worker processes.

The master process is a continous loop which is responsible to keep a pre defined number of worker processes up and running.

The worker processes are nothing but multiple instances of your web app running independent of eachother.
<gif>

### How Gunicorn works

**Server Initialization**: When you start Gunicorn, it initializes a master process that manages a set of worker processes. These worker processes are responsible for handling incoming requests.

**Accepting Requests**: The master process listens for incoming HTTP requests on a specified host and port. When a request arrives, it is passed to one of the worker processes for processing.

**Request Handling**: Each worker process is a separate Python interpreter running your web application. It handles the request by calling your application's WSGI callable (typically the app object in Flask). This isolation ensures that worker processes are independent and can handle multiple requests simultaneously.

**Response Delivery**: After processing the request, the worker process generates a response, and this response is sent back through the master process to the client, completing the request-response cycle.
<gif>

## Choosing the best deployment configuration

There are mainly 3 metrics to fine tune to squeeze maximum juice out of the server:

**Number of workers**

More number of workers can handle more number of requests parallely. But it also means that more number of processes are running which requires more resources like CPU and memory. The recommended number of workers is (2 $\times$ Cores) + 1. The reason provided in the documentation is *"While not overly scientific, the formula is based on the assumption that for a given core, one worker will be reading or writing from the socket while the other worker is processing a request."*

More workers are needed if the app contains a lot of CPU bound tasks. It can also improve the performance if the app is mainly IO bound but it will be an overkill for such tasks.

**Number of threads**

More number of threads can handle more number of requests concurrently. But not only does a higher thread count require more resources. Having more threads doesn't necessarily translate to significant improvements in CPU-bound task performance. In fact, it may lead to contention for the GIL, which can impact performance.

Multithreaded models are recommended for IO bound tasks. Threads are light weight when compared to workers thus they require lesser resources.

**Worker class**

There are multiple worker classes to choose from in Gunicorn.

1. Sync worker (Default) - t can handle only one request at a time. It is a mono-thread model and is a general-purpose worker type. It is more suited for CPU-bound tasks than for IO-bound tasks.

2. gthread - t is a multi-threaded version of the sync worker. It is more suited for IO-bound tasks than for CPU-bound tasks.

3. eventlet/gevent - It is similar to the gthread worker, but instead of using traditional threads, it makes use of gthreads/pseudo threads (based on greenlet), which are more lightweight compared to traditional threads. Due to this, it can perform as good as an async framework. Therefore, it is more suited for IO-bound tasks than for CPU-bound tasks.

## Conclusion

- Increasing the number of workers can handle multiple requests parallely. But it is more CPU and memory intensive. Do this if your app contains a lot of CPU-bound tasks.
- By making a worker multi threaded, each app can handle multiple requests concurrently. You can use this to reduce the number of workers thus reducing the CPU and memory load. Use this if your app contains a lot of IO-bound tasks.
- Choose a suitable worker based on the nature of the application.