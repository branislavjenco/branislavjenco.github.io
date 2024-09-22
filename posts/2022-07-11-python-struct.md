---
Tiny project - Python `struct` format explainer
2022-07-11
---

Over the last weekend and a half I made this tiny website [pythonstruct.com](https://pythonstruct.com). It gives users a quick explanation of the format strings used in [Python's `struct` module](https://docs.python.org/3/library/struct.html). You can paste in a string like `<hhl` and get an instant explanation that the structure being packed/unpacked used is two `short`s and one `long` with little-endian byte order.

This was motivated by me stumbling upon the use of this module in a codebase at work and having to look through the docs to decipher the format strings. A side benefit of writing this tool is that now I understand the `struct` module better.  The source code is at [https://github.com/branislavjenco/struct-explainer/](https://github.com/branislavjenco/struct-explainer/).

It's a simple static webpage with some JavaScript. No server-side components are used. Writing plain JavaScript for simple websites like this is such a nice experience, not having to deal with build steps, transpiling, and so on. Only wish TypeScript was natively supported in browsers. The parsing and rendering code is in [`lib.js`](https://github.com/branislavjenco/struct-explainer/blob/gh-pages/lib.js) and the code for the various event handlers is in [`main.js`](https://github.com/branislavjenco/struct-explainer/blob/gh-pages/main.js). There are also some [unit tests](https://github.com/branislavjenco/struct-explainer/blob/gh-pages/test.js) that can be run using `node test`, thanks to the fact that `main.js` exports its functions [both for the browser and `node`](https://github.com/branislavjenco/struct-explainer/blob/3f5c1f5ee518e8afcc443694d24246a94c581d31/lib.js#L355).
