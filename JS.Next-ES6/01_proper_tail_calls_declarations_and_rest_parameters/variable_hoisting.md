# Variable Hoisting

> Don't grep-replace `var` with `let` or you will break the internet.

> ---Doug Crockford, Senior Architect of JS

> With `var`, the arrangement of code has less to do with the way it executes than you think it does.

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
