## Introduction
- impure computations which do not leak and are not externaly observable **are pure** 

### Idioms for handling pre-conditions

1. **Run-time failures on bad input:** Shift burden of responsibility to caller - possible exceptions also require documentation to be clear + extensive in order to be useful. 
2. **Returning a dummy value:** ^ + still requires knowledge on caller's part to be aware of said value and handle them responsibly. 
3. **Returning a value with an option type:** better than returning dummy value as type-system will help us ensure that caller handles the errors but it is still onerous and still shifts responsibility onto the caller, even when the error case might not be possible
4. **Modifying input types to exclude bad inputs:** approach chosen by authors of gdp paper. we encode some knowledge in our types and restrict our function to accept only valid types. because the construction of the type is proof of existence, we know that the operation is safe

### Ghosts of departed proofs

**Properties and proofs are represented in code**: By having types represent propositions and a value of a type represents a proof of that proposition

**Proofs carried by phantom type parameters:** Proofs are encoded using phantom type parameters, which don't exist at runtime -> no runtime cost associated 
		- in haskell, this is done through `newtype` wrappers, which create *nominally different* types with the same underlying representation

**Library-controlled APIs to create proofs:** Authors have control over how the proofs are created; users cannot sidestep the behaviour to create their own (invalid) types 

**Combinators for manipulating ghost proofs:** Give more power to the end-user so that they do not side-step our mechanisms  and interact productively with the library

> [!INFO] Combinators
> Combinators are functions that **do not read/write** to variables beyond the function scope

## Example implementation

1. define a `newtype` wrapper that is not exported - this has the same runtime value as the underlying type but represents a proof of some proposition.
	-  by not exporting the type, users are forced to use lib functions and cannot sidestep validation
2. the function that returns the `newtype` has to attach a name to the `newtype` that encodes the proof into the type
3. end users should only be allowed to consume the phantoms **not** to name them.

