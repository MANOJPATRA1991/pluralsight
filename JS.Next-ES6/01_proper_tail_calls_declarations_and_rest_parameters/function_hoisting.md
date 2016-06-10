# Function Hoisting

```javascript
// ...

// Function declaration
function foo() {
  // code here
}

// Function expressin
var bar = function() {
  // code here
}
```

is compiled to ...

```javascript
var bar = undefined;
function foo() {  // function declaration hoisted
  // code here
}

// ...

bar = function() {
  // function name hoisted, but variable assignment doesn't happen until the code gets here
};
```

Per Douglas Crockford's [JS Styleguide](#):

> Define all variables at the top of the function.

*In other words, hoist your own variables.*
