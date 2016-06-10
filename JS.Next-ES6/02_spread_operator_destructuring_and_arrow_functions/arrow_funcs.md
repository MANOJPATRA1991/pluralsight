# Arrow Functions

Precedence

* Lambda
* Far Arrow Functions

Defacto Standards

* CoffeeScript
* Fat Arrow Functions
* Skinny Arrow Functions
* ES6 uses Fat Arrow syntax, calls it Arrow Function

Compared to regular functions:

```javascript
var fn1 = function() { return 2; };
var fn2 = () => 2;
```

* Parenthesis for the parameters
* No braces for single-line arrow function bodies
* Single-line arrow, implicit return statement

## Parenthesis-Parameter Rules

```javascript
var x;
x = () => {};      // No parameters, MUST HAVE PARENS
x = (val) => {};   // One parameter w/ parens, OPTIONAL
x = val => {};     // One parameter w/o parens, OPTIONAL
x = (y, z) => {};  // Two or more parameters, MUST HAVE PARENS
x = y, z => {};    // SyntaxError: must wrap with parens when using multiple params
```

## Method Body Declarations

```javascript
var square;
square = x => x * x;             // Body w/o braces
square = x => { return x * x };  // Body w/ braces
```

## Usages

### Replacing anonymous functions

```javascript
let nums = [1, 2, 3];
let res = nums.map( n => n * n );
console.log(res);  // logs [1, 4, 9]
```

### Return an object literal, wrap in parens

```javascript
let key_maker = val => ({key: val});
console.log(key_maker(100));  // logs {key: 100}
```

### The REAL benefit: lexical binding of `this`

```javascript
var Widget = {
  init: function() {
    document.addEventListener("click", function(event) {
      this.doSomething(event.type);  // Why does this error?
    }, false);
  },

  doSomething: function() {
    console.log("Handling " + type + " event");
  }
};
Widget.init();
```

Solutions:

```javascript
// ...

/* #1 - use 'bind' */
init: function() {
  document.addEventListener("click", function(event) {
    this.doSomething(event.type);
  }).bind(this), false);
}

/* #2 - alias 'this' */
init: function() {
  var self = this;
  document.addEventListener("click", function(event) {
    self.doSomething(event.type);
  }, false);
}

/* #3 - use arrow functions */
init: function() {
  document.addEventListener("click", (event) => {
    this.doSomething(event.type);
  }, false);
}
```

## Additional Info about `() => {}`

```javascript
typeof ()=>{};  // 'function'
```

* Although it doesn't have a prototype, this still happens

    ```javascript
    Object.getPrototypeOf(()=>{});  // Function.prototype

    var Foo = function(){};
    var Bar = () => {};
    new Foo();
    new Bar();  // Bar is not a constructor
    ```

* You can't alter `this` on arrow functions

    ```javascript
    function Widget) {
      this.id = 123;
      this.log = () => {
        console.log("Widget Log", this.id);
      }
    }

    var psuedoWidget = {
      id: 456
    };

    new Widget().log.call(pseudoWidget);  // What logs?
    ```

## TRY THIS

- **Arrow Functions** in Firefox
- **Arrow Functions** in [Traceur Repl](https://google.github.io/traceur-compiler/demo/repl.html#)
- **Arrow Functions** inside an `Object`
- **Arrow Functions** with EventHandlers
- **Arrow Functions** with `Array.prototype` methods
