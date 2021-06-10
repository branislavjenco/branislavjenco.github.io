---
layout: post
title: Chromedriver fixes behaviour, breaks test
---
Our `selenium` CI tests started failing after a new version of Google's Chromedriver came out. As can be seen in the [release notes](https://chromedriver.storage.googleapis.com/index.html?path=91.0.4472.19/), v91 fixes an issue with the attribute endpoint. ChromeDriver (and other web drivers conforming to the [W3C web driver spec](https://w3c.github.io/webdriver/)) have a client-server architecture where commands are sent to specific endpoints. A command to get an element attribute is executed by a client (for example the Python Selenium module) making a request to a url like `http://<web-driver-hostname:port>/session/<session-id>/element/<element-id>/attribute/<attribute-name>'`.

The tests started failing because in our code, we mistakenly use the `get_attribute()` method in a couple places where we actually are querying for a DOM element `property`, not an `attribute` (namely `innerText`). The difference between a property and an attribute is well explained [here](https://stackoverflow.com/questions/6003819/what-is-the-difference-between-properties-and-attributes-in-html). Before v91, this method worked even though it was wrong. The solution is to obviously switch the calls from Selenium's `get_attribute()` to `get_property()`. It looks like [other people](https://groups.google.com/g/chromedriver-users/c/L82UzBKy58Q/m/m5moLZStAgAJ) were bitten by this as well.

