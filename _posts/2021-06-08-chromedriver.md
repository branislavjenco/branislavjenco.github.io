---
layout: post
title: ChromeDriver fixes behaviour, breaks our test
---
Our `selenium` ci tests started failing after a new version of Google's ChromeDriver came out. As can be seen in the [release notes](https://chromedriver.storage.googleapis.com/index.html?path=91.0.4472.19/), v91 fixes an issue with the attribute endpoint. ChromeDriver (and other web drivers conforming to the [W3C web driver spec](https://w3c.github.io/webdriver/) have a client-server where commands are sent to specific endpoints. A command to get an element attribute is executed by a client (for example the Selenium module) making a request to a url like `http://<web-driver-hostname:port>/session/<session-id>/element/<element-id>/attribute/<attribute-name>'`.

The tests started failing because in our code, we mistakenly use the `get_attribute()` a couple places where we actually are querying for a DOM element `property`, not an `attribute`, namely `innerText` (see difference between a property and an attribute [here](<https://stackoverflow.com/questions/6003819/what-is-the-difference-between-properties-and-attributes-in-html)). Before v91, this worked even though it was wrong. The solution was to switch the calls to Selenium's `get_attribute()` to `get_property()`. It looks like I wasn't [the only one](https://groups.google.com/g/chromedriver-users/c/L82UzBKy58Q/m/m5moLZStAgAJ) who had the issue.
