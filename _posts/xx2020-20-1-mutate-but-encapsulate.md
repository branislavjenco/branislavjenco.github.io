# Mutate, but encapsulate

This post is about the inherent tension between the theoretical underpinnings of computer science and the actual day to day engineering practice of software development. This tension has many names, you could call it imperative vs functional programming, procedural vs object oriented programming, reference semantics vs value semantics, immediate mode vs retained mode and so on, maybe even lambda calculus vs turing machine.

The underlying conflict arises from the fact that our world is not mathematical, it is not immutable. The architecture on which all our programs are running is mutable. After all the compilation steps, even the most elegant Haskell program is a sequence of instructions that change bits in registers. However, immutable semantics can make reasoning about programs much simpler. Object-oriented programming is one way of solving this tension, functional programming or declarative programming is another. 



