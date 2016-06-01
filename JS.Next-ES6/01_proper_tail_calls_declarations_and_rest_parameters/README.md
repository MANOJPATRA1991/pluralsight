> Proper tail recursion is a property of the asymptotic space complexity of a language's runtime behavior. That is, in improperly tail recursive languages, control can consume unbounded amounts of space for programs that, when run in properly tail recursive languages, only require a constant amount of space.

> ---Dave Herman, Principal Researcher w/ Mozilla

---

# Proper Tail Call

* ES6 introduces Propert Tail Calls into JavaScript
* If used correctly, PTC will add recursion
* Previous stacks are garbage-collected (GC'ed)

## Vocabulary

### Tail Position

* The last instruction to fire before the return statement

```javascript
function greet(num) {
  return "Hello";
}
```

* Instruction `"Hello"` is in Tail Position

### Tail Call

* An instruction in Tail Position is a method call

```javascript
function greet() {
  return getSalutation();  // Tail Position && Tail Call
}

function getSalutation() {
  return "Hello";  // Tail Position, but not Tail Call
}

function resultsHandler(err, results, callback) {
  if (err) {
    return callback(true);
  }
  return callback(false, results);
}
// TWO TAIL POSITIONS, TWO TAIL CALLS
```

### Close Call

* Close call looks like a tail call, but it isn't

```javascript
function foo() {
  return 1 + bar();
}
// It has to return the result of bar(), then add 1
```

* Because it does something after the call, it isn't a tail call

### Proper Tail Call Pre-ES6

```javascript
function fibonacci(x, y, limit, index) {
  if (arguments.length == 1) {
    if (x)
      return fibonacci(0, 1, x, 1);
    return 0;
  } else {
    if (index < limit)
      return fibonacci(y, x+y, limit, ++index);
    return y;
  }
}

console.log(fibonacci(3));      // 2
console.log(fibonacci(10));     // 55
console.log(fibonacci(12495));  // RangeError
```

## Final Thoughts

* Proper Tail Calls only work in Strict Mode `"use strict";`
* Optimize code so that Tail Position is a Tail Call

---

> Don't grep-replace `var` with `let` or you will break the internet.

> ---Doug Crockford, Senior Architect of JS

> With `var`, the arrangement of code has less to do with the way it executes than you think it does.

# Variable Hoisting

* Compiler automatically hoists your variables
* Compiler reformats your code

    ```javascript
    var foo = 2;
    if (true) {
      var bar = 1;
    }
    console.log(foo + bar);  // Throw error, logs 2, 3, or undefined?
    ```

    is compiled to ...

    ```javascript
    var foo = 2;
    var bar = undefined;

    if (true) {
      bar = 1;  // `bar` wasn't declared in here
    }
    console.log(foo + bar);  // 3
    ```

* Trap variables inside functions only

    ```javascript
    var a = 1;
    function run() {
      var a = 2;
      console.log(a);  // logs 2
    }
    run();
    console.log(a);  // logs 1
    ```

* Pre-ES6, variables are "Function Scoped"

---

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

---

# `let`

## `let` in its most basic forms

```javascript
// var foo = 1;
let foo = 2;
foo = 3;  // you can reassign it

if (true) {
  let bar = 1;  // can't access outside of IF block scope
}

console.log(foo + bar);  // Throws Error: "bar" not defined
```

```javascript
let a = 0;
if (true) {
  let a = 2;
  console.log("here a = ", a);  // logs 2
}
console.log("at the end, a = ", a);  // logs 0
```

**IMPORTANT: 2 `let`s, same name == BAD**

```javascript
var a = 0;
var a = 1;  // NO, but no errors

let b = 0;
let b = 1;  // SyntaxError: Variable 'b' has already been declared

var c = 0;
let c = 1;  // SyntaxError: Variable 'c' has already been declared

let c = 0;
var c = 1;  // SyntaxError: Variable 'c' has already been declared
```

## `let` with looping

```javascript
for (var i = 0; i < 10; i++) {
  console.log(i);  // logs 0 - 9
}
for (let j = 0; j < 10; j++) {
  console.log(j);  // logs 0 - 9
}
console.log("--");
console.log(i);  // logs 10
console.log(j);  // ReferenceError
```

## Vocabulary

### Temporal Dead Zone

```javascript
function doSomething() {
  console.log(a);  // What here?
  let a = 1;
  console.log(a);
}
```

* Space in memory is reserved
* Variable is not accessible until defined
* Throws `ReferenceError`

---

# `const`

```javascript
const a = 0;
a = 1;  // SyntaxError: Assignment to constant variable
```

Block Functions

```javascript
function doSomething() {
  if (true) {  // want to scope 'a', so if-true
    // ...
    let a = 0;
    // ...
  }
  // ...
}
```

* No `if-true` necessary
* Same lexical scope as an `if-true`

---

# Rest Parameters

* Similar to `*args` in python
* Exist in function signature

    ```javascript
    function foo(...bar) {
      console.log(bar.join(" "));  // Logs "I can haz teh arguments"
    }
    foo("I", "can", "haz", "teh", "arguments");
    ```

* We've had the "arguments" object

    ```javascript
    function foo() {  // leave the signature empty
      var output = "";
      for (var i = 0; i < arguments.length; i++) {
        output += arguments[i];
      }
      console.log(output);  // Logs 'I can haz teh arguments'
    }
    foo('I', 'can', 'haz', 'teh', 'arguments');
    ```

* Array-ish: has length, get by index (not an array, but a pseudo-array)
* No prototype methods: `forEach`, `join`, `pop`, `push`, etc...
* Use "arguments" like `Array`:

    ```javascript
    function foo() {  // leave the signature empty
      var output = Array.prototype.join.call(arguments, " ");
      console.log(output);  // logs 'I can haz teh arguments'
    }
    foo('I', 'can', 'haz', 'teh', 'arguments');
    ```

## Difference between Rest and `arguments`:

* Rest Arg only includes non-specified arguments
* `arguments` include all arguments, regardless

    ```javascript
    function argumenty(name) {
      console.log(name, arguments);
    }
    function resty(name, ...other) {
      console.log(name, other);
    }
    argumenty("Aaron", "Frost", "Salt Lake City", "Utah");  // Aaron ["Aaron", "Frost", "Salt Lake City", "Utah"]
    resty("Aaron", "Frost", "Salt Lake City", "Utah");  // Aaron ["Frost", "Salt Lake City", "Utah"]
    ```

## Rules of Rest Paramaters

* One per function

    ```javascript
    function lotsOfArgs(...first, ...second) {
      console.log("FIRST: " + first.join(" "));
      console.log("SECOND: " + second.join(" " ));
    }
    lotsOfArgs("where", "does", "first", "stop", "and", "second", "begin");
    // SyntaxError: Multiple RestParams Defined
    ```

* Must be the last parameter

    ```javascript
    function doSomething(...bar, biz) {
      // ...
    }
    doSomething(1, 2, 3, 4);  // Where does it cutoff for 'biz'?
    doSomething(1);  // Does 1 go in 'bar' or 'biz'?
    ```

* Can't use `arguments`

    ```javascript
    function doSomething() {
      console.log(arguments.length);  // SyntaxError
    }
    doSomething(1, 2, 3);
    ```

* No default values

    ```javascript
    function doSomething(...params=[1,2,3]) {  // SyntaxError
      console.log(params.join(" "));
    }
    doSomething();
    ```

## TRY THIS

- **Rest Params** in Firefox
- **Rest Params** in [Traceur Repl](https://google.github.io/traceur-compiler/demo/repl.html#)
- **Rest Params** w/ `arguments` object
- Two **Rest Params**
- **Rest Params** as first argument
- **Rest Params** w/ **Default Values**
- **Rest Params**: get an error for using it w/ `arguments`
- **Rest Params**: get an error for using two of them
- **Rest Params**: get an error for not being last param

---


