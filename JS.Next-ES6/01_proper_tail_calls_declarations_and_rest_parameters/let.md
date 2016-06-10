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


