# Worked example: importing a small CSV file

**Illustrative example, written for this repository.** This is not a transcript,
an implemented feature, or evidence of a successful workflow run. It shows the
kind of information the task files and review loop are meant to hold. In actual
use the task files follow the English fields shown in the templates.

## Request

"Add a local CSV import for products. Each row has a code, name and price. Reject
invalid input and show which rows need fixing. Do not change the catalog unless
the entire file is valid."

This is a nontrivial local software task with a clear check. The example assumes
no production data, external writes or migrations, and uses the Fast path.

## Separate initial analyses

In `claude-pass.md`, before seeing the other pass:

> The request does not define duplicate product codes. I would ask whether a
> duplicate in the input should reject the file. A likely failure is applying
> earlier rows before a later row fails. Check that a bad last row leaves the
> original catalog unchanged.

In `gpt-pass.md`, before seeing the other pass:

> Price validation needs to reject values that can be parsed but are not usable
> prices. Check empty values, negative values and non-finite values. Also check
> that importing into a non-empty catalog does not silently overwrite a product.

Each pass ends with `SEALED_READY 03`. The lead reads both only after this point.

## Settling the task

The human clarifies: duplicate codes within the file or against the catalog
reject the import; prices must be finite and non-negative. Errors identify the
CSV row. No import writes occur before validation finishes.

The lead records those rules in `task.md`, with a plan: parse and validate the
whole input, gather errors, then update the catalog only if there are none.
The other agent checks the plan with `challenge 03` before implementation.

## Review finding

Suppose the first implementation uses `float(value)` and checks `price < 0`.
Its tests cover ordinary numbers, blank input and negative prices.

The reviewer proposes the input `NaN`. Parsing succeeds, and `NaN < 0` is false.
That lets an invalid value through. This is a correctness finding with a concrete
reproduction, not a style preference. The test suite had varied numeric signs
but held finiteness constant.

## Apply and confirm

The lead adds an explicit finiteness check and a regression case. Because this
changes validation behavior, the reviewer confirms that `NaN`, positive infinity
and negative infinity are rejected, an ordinary zero price is accepted, and a
file containing an invalid price leaves the existing catalog unchanged.

In a real run, closure would require actual code and recorded check results.
The outcome would record who first found the issue, which checks ran and any
remaining limitations. This example deliberately claims no such execution.
