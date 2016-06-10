# Default Parameters

Some other ways to refer to default parameters:

* Default Arguments
* Default Values
* Default Function Arguments
* Default Optional Parameters
* Some similar combination of words from these xamples

New verison of an old seam

* C++
* Python
* CoffeeScript
* Now EcmaScript!

## Historically

* Short-Circuit Expression:

    ```javascript
    function test(a) {
      a = a || getSomeDefaultValue();  // data proofing
      /* ... */
    }
    ```

* Ternary Expression:

    ```javascript
    function test(a) {
      a = a ? a : getSomeDefaultValue(); // data proofing
      /* ... */
    }
    ```

## Examples

```javascript
function sayHello(name = "World") {
  console.log("Hello " + name + "!");
}

sayHello("Dt Dew");   // Hello Dt Dew!
sayHello("");         // Hello !
sayHello();           // Hello World!
sayHello(undefined);  // Hello World!
```

* Undefined: TRIGGERS
* Empty Strng: DOESN'T TRIGGER
* Explicit Undefined: TRIGGERS

## What Does It Get Me?

* Write less code
* Easier to read
* Improved predictability

## Assign with Method Call

```javascript
function getRand() {
  return Math.ceil(Math.random() * 10000000) + new Date().getTime();
}

function myFunction(id=getRand()) {
  console.log("My ID: " + id);
}

myFunction();   // logs random number
myFunction(1);  // logs
```

```javascript
function die() {
  throw "x";
}

function test(a = die()) {
  console.log("Didn't die");
}

test();  // throws an error
```

## Assignment Happens Lexically (AVOID THIS)

```javascript
var x = "INIT";

function test(a = x) {
  var x;
  return a;
}

console.log(test());  // undefined
```

## Default Parm Gotchas

* No default parameters with rest parameters

    ```javascript
    function f( ...rest=100 ) {  // SyntaxError
      // ...
    }
    ```

* Default values don't appear in `arguments`:

    ```javascript
    function test(a = 1, b = 2, c = 3) {
      console.log(arguments.length);
    }

    test();           // 0
    test(1);          // 1
    test(1,2,3,4,5);  // 5
    ```
