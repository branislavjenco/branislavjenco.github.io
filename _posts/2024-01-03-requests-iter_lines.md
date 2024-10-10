---
layout: post
title: Python's requests package doesn't always yield lines in iter_lines()
---

The widely used `requests` package allows you to make HTTP requests from within Python. To better handle large responses, we can stream data using the parameter `stream=True` (e.g. `requests.get("http://some.com/bigfile", stream=True`). This means the library only gets the HTTP headers and gives back control to you to deal with getting the content of the response using a couple of different methods and properties. One of them is `response.iter_lines()` which is a Python generator that yields lines in the response. In combination with `stream=True` this allows us to not have to load the entire response into memory at once, rather process it line by line.

But it has a small quirk in its implementation that tripped me up when testing the behaviour with `netcat`. `iter_lines` actually uses another similar method, `iter_content()` under the hood, where you have to specify the `chunk_size` &mdash; specifying how big are the chunks in which we iterate over the content. `iter_lines()` by default uses [512](https://github.com/psf/requests/blob/72eccc8dd8b7c272e520f22b0256386c80864e94/src/requests/models.py#L81) (it used to be [10*1024!](https://github.com/psf/requests/commit/297aa04beaee5e80845841f257723fc472fd6fd7)) which means any line shorter than that sent in the HTTP response won't be immediately yielded. Only once the chunk is "filled" will all the lines that fit into the chunk yielded &ndash; at once.

Relevant links

- [Implementation](https://github.com/psf/requests/blob/main/src/requests/models.py#L853)
- GitHub Issues [1](https://github.com/psf/requests/issues/989) [2](https://github.com/psf/requests/issues/2433)
