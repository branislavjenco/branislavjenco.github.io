#  Notes for more writing on desired state

I read Elements of Clojure, which talks about a lot of the same things I do in my Desired State Systems blog post/talk. It uses some different definitions for things like interfaces, abstractions but they generally map to what I'm talking about.

Need to think more about the inductive vs deductive reasoning part

"Deduction maps the environment into the model and then uses the model to infer new facts about the environment."

It's a bit interesting this part about the General Problem Solver, which would "observe current state, compare it to the desired outcome and search for a path between the two by simulating intermediate actions". That sounds exactly like what I'm talking about in desired state systems. But it's presented as a deductive, failed approach.

I'm not sure why the General Problem Solver is presented as an example of "deductive reasoning" though.

Conclusions we draw from induction are contingent, they're allowed to be wrong, okay?

"Where the solver tries to predict, the tick only compares" but isn't comparison central to the GPS as mentioned above? I'm confused.

This I can very much agree with:
"The models of mathematics don’t acknowledge their environment. We can use them to
judge whether our software is self-consistent, but not whether it is useful. The models of
physics are built atop deductive mechanisms, and aspire towards perfection. The models
of software are built atop inductive analogies and aspire only to satisfice"