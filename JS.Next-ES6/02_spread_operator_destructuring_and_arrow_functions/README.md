# Spread Operator

* `...` before an array:

    ```javascript
    var nums = [1, 2, 3];

    log(nums);     // logs [1, 2, 3]
    log(...nums);  // logs 1, 2, 3
    ```

    ```javascript
    function returnTwo(a,b) {
      return [b, a];  // Flips 'a' and 'b'
    }

    var a = [1, 2, 3];
    var b = returnTwo(a[0], a[1]);  // [2, 1]
    var c = returnTwo(...a);        // [2, 1]
    ```

* Combine Arrays

    ```javascript
    let nums = [1, 2, 3];
    let abcs = ['a', 'b', 'c'];

    let alphanum = [...nums, ...abcs];  // [1, 2, 3, 'a', 'b', 'c']
    ```

* Spread return values

    ```javascript
    function getNums() {
      return [1, 2, 3];
    }

    var b = [0, ...getNums()];
    console.log(b);  // [0, 1, 2, 3]
    ```

---

# Destructuring

> **Destructuring** allows you to bind a set of variables to a corresponding set of values anywhere that you can normally bind a vlaue to a single value.

## Thoughts

* Normally we construct
* Destructuring has always been manual
* New syntax
* Pattern matching

## TRY THIS

- **Destructuring** in [Traceur Repl](https://google.github.io/traceur-compiler/demo/repl.html#)
- **Destructuring** in [Firefox
- **NO WHERE RESPECT PATTERNS**
- Destructure in a method signature
- Destructure return value of method
- Destructure canvas bitarray
- Read: <http://wiki.ecmascript.org/doku.php?id=harmony:destructuring>
- Read: <http://wiki.ecmascript.org/doku.php?id=harmony:refutable_matching>

---

# Destructuring Objects

## Basic Example

```javascript
function getAddress() {
  return {
    city: "Salt Lake City",
    state: "UT",
    zip: 84115
  }
}

let {city, state, zip} = getAddress();

console.log(city);   // "Salt Lake City"
console.log(state);  // "UT"
console.log(zip);    // 84115

console.log(city, state, zip);  // 'Salt Lake City', 'UT', 84115
```

**NOTICE**: braces on the left side of assignment expression

## Alias names

```javascript
let {city: c, state: s, zip: z} = getAddress();

console.log(c, s, z);           // 'Salt Lake City', 'UT', 84115
console.log(city, state, zip);  // Throws Error: city, state, zip not defined
```

## Extended Example

```javascript
var person = {name: "Aaron", age: 35}
displayPerson(person);

/* The Old Way */
function displayPerson(p) {
  var name = p.name;
  var age = p.age;
  // ...
}

/* The New Way */
function displayPerson(p) {
  let {name, age} = p;
  // ...
}

/* The New Way - Improved */
function displayPerson({name, age}) {
  // ...
}

/* The New Way - More Improved (Default Values) */
function displayPerson({name = "No Name Provided", age = 0}) {
  // ...
}
```

## Another Example:

```javascript
try {
  throw "WorstError"
} catch({type, message, filename, lineNumber}) {
  // ...
}
```

## Patterns Crash Course

```javascript
let {a: x} = {};   // throw
let ?{a: x} = {};  // x = undefined
let ?{a: x} = 0;   // x = undefined
let {?a: x} = {};  // x = undefined
let {?a: x} = 0;   // throw
```

### Irrefutable Pattern

* `}` on the left means destructuring the right
* object on the right must have properties with the names

    ```javascript
    var person = {name: "Aaron", age: 35}
    displayPerson(person);

    function displayPerson(p) {
      let {name, age, address} = p;  // Throws Error: 'address' not a property
      // ...
    }
    ```

### Refutable Pattern

```javascript
var person = {name: "Aaron", age: 35};

// Forgives each of them individually
let {name, age, ?address} = person;

// Forgives the whole pattern
let ?{name, age, address} = person;
```

## Patterns with Default Values

```javascript
let ?{a: x = 1} = undefined;  // x = 1
let {?a: x = 1} = undefined;  // throw
let {?a: x = 1} = {};         // x = 1
```

## Patterns with Nested Objects

```javascript
let {a: x, b: {c: y}, d: z} = {a: 1, b: {}, d: 2};  // throw
let {a: x, ?b: {c: y}, d: z} = {a: 1, b: 0, d: 2};  // x = 1, y = undefined, z = 2
let ?{a: x, b: {c: y}, d: z} = {b: {}, d: 2};       // x, y = undefined, z = 2
```

```javascript
let person = {
  name: "Aaron",
  age: "35",
  address: {
    city: "Salt Lake City",
    state: "UT",
    zip: 84115
  }
};

let {name, age, address: {city, state, zip}} = person;
```

---

# Destructuring Arrays

## Basic Example

```javascript
var nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

var [first, second,,,,,,,, tenth] = nums;
console.log(first, second, tenth);  // 1, 2, 10
```

## Swap Variables

```javascript
var a = 1, b = 2;

/* The Old Way */
var temp = a, a = b, b = temp;

/* The New Way */
[b, a] = [a, b];
```

## Method Signature

```javascript
var nums = [1, 2, 3, 4];
doSomething(nums);

function doSometing([first, second, ...others]) {
  console.log(first);   // logs 1
  console.log(second);  // logs 2
  console.log(others);  // logs [3, 4]
};
```

## Nested Destructuring of Array

```javascript
var nums = [1, 2, [3, 4, [5, 6]]];

var [one,,[three,,[,six]]] = nums;
```

## Pattern Errors

```javascript
let [x] = [2, 3]        // x = 2
let [x] = {'0': 4}      // x = 4
let [x, y, z] = [1, 2]  // throw

// Entire pattern is refutable
let ?[x, y, z] = [1, 2]  // x = 1, y = 2, z = undefined

// Only 'z' is refutable
let [x, y, ?z] = [1, 2]  // x = 1, y = 2, z = undefined
```

---

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

---
