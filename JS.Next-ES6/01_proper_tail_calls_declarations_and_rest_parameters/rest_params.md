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
