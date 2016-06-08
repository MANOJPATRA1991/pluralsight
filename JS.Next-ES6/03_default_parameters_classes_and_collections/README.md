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
var x = "INIT;

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

---

# Classes

## History of ES6 Classes

* Goes back to ES4 days
* Lots of churn
* Lots of precedence
* Russell Leggett, Match 19 2012

## Russell Leggett's Proposal

* Called "maximal minimal classes"
* Points out the need for classes in JS, a la CoffeeScript
* Make sure it is enhanceable in Future Harmony Releases
* Points to Brendan's **Goldilocks Proposal**
* Proposes new analogy - **Safety School Proposal**
* Since we must have something in ES6, what is it?

## Example

```javascript
/* Functionally the same */

function Foo() {
  // ...
}

class Foo {
  // ...
}
```

* Class is sugar

## Constructor

```javascript
class Animal {

  constructor(name) {
    this.name = name;
  }

}
```

## Private Properties

```javascript
const monsterHealth = Symbol();

class Monster {
  constructor(name, health) {
    this.name = name;
    this[monsterHealth] = health;
  }

  set name(name) {  // endless loop!
    this.name = name;  // RangeError: Maximum call stack size exceeded
  }

  set health(val) {
    if (val < 0) { throw new Error("Health must be non-negative!"); }
    this[monsterHealth] = val;
  }

  attack(target) {
    console.log(this.name + ' attacks ' + target.name);
  }

  get isAlive() {
    console.log("Someone wants to know if I am alive");
    return this[monsterHealth] > 0;
  }

  set isAlive() {
    if (!alive) { this[monsterHealth] = 0; }
  }

  foo() {
    console.log("FOO", this.isAlive)
  }
}
```

## Extending Classes

```javascript
const monsterHealth = Symbol();

class Monster {
  constructor(name, health) {
    this.name = name;
    this[monsterHealth] = health;
  }
  // ...
}

class Godzilla extends Monster {
  constructor() {
    super('Godzilla', 10000);
  }
}
```

* Could we do this with prototypes?

### Extend via Expression

```javascript
class MySocket extends getClass() {
  // ...
}

function getClass() {
  if(isIE()) { return IEWebSocketImpl; }
  return WebSocket;

  function isIE() {
    return false;
  }
}
```

## Classes Do Not Hoist

```javascript
new Bar();  // runtime error
class Bar {}
```

## If no constructor, default behavior

```javascript
constructor(...args) {
  super(...args);
}
```

## Benefits of Classes

* Syntactic sugar
* Easier to learn #noobs
* Subclassing easier to learn #noobs
* Subclass builtin object: Array, Error, etc
* Code more portable between JS Frameworks
* Possible performance gains

---

# Collections

## What's new

* `Set` (*like* `Array`)
* `Map` (*like* Key-Value Object)
* `WeakMap`

## `Set`

Unique collection of elements.

### Basic

```javascript
var set = new Set();
set.add(1);
set.add(2);
set.add(3);
console.log(set.size);  // logs 3
```

### Unique Values

```javascript
var set = new Set();
set.add(1);
set.add(1);
set.add(1);
console.log(set.size);  // logs 1
```

### Prototype Methods

```javascript
var set = new Set();
set.has(1);  // false
set.add(1);
set.has(1);  // true
set.add(1);
set.add(2);
set.size;    // 2
set.delete(2);
set.size;    // 1
```

### No Typecasting

```javascript
var set = new Set();

set.add(1);
set.has(1);    // true
set.has("1");  // false

set.add("1");
set.has("1");  // true
```

### No Iteration

```javascript
var items = new Set([1,2,3,4,5]);

for (let num of items) {
  console.log(num);  // logs 1, 2, 3, 4, 5
}
```

## `Map`

### Basic

```javascript
var json = { name: "Aaron" };

var map = new Map();
map.set('name', 'Aaron');

map.get('name');  // Aaron
```

* `map.set`
* `map.get`

### No Typecasting

```javascript
var map = new Map();

map.set(1, true);
map.has("1");        // false

map.set("1", true);
map.has("1");        // true
```

### Objects as Keys

```javascript
var user = { name: "Aaron", id: 1234 };

var userHobbyMap = new Map();

userHobbyMap.set(user, ['Ice Fishing', 'Family Outting']);
```

* Keys: primitives/objects/functions

### Must Use the Same Key

```javascript
var user1 = { name: "Aaron", id: 1234 };
var user2 = { name: "Aaron", id: 1234 };

var userHobbyMap = new Map();
userHobbyMap.set(user1, ['Ice Fishing', 'Family Outting']);

userHobbyMap.get(user2);  // undefined
userHobbyMap.get(user1);  // ['Ice Fishing', 'Family Outting']
```

* You must use the **SAME KEY**
* JSON maps, different string with same contents

### Usage

```javascript
var elem = document.querySelector('#my-element');

var elemMap = new Map();
elemMap.set(elem, {loaded: true, opacity: 0});

elemMap.get(elem);  // logs the element
```

* Thoughts about why this is bad?

## `WeakMap`

> A weakmap holds only a weak reference to a key, which means the reference inside of the weakmap doesn't prevent garbage collection of that object.
>
> Nicolas Zakas (@slicknet)

### A Lot Like `Map`

```javascript
var weak = new WeakMap()

weak.set('name', 'Aaron');
weak.get('name');  // 'Aaron'
```

### MOAR likeness

```javascript
var user = { name: 'Aaron', id: 1234 };
var weak = new WeakMap();

weak.has(user);  // false
weak.set(user, {lastAction: new date()});
weak.has(user);  // true
weak.delete(user);
weak.has(user);  // false
weak.set(uer, {lastAction: new Date()});
weak.clear();
weak.has(user);  // false
```

### Isn't Really Like a `Map`

```javascript
let map = new Map();
let weak = new WeakMap();

map.set('aaron', {name: 'Aaron', age: 35});
weak.set('aaron', {name: 'Aaron', age: 35});  // Throws: Invalid key type

map.size;   // 1
weak.size;  // undefined
```

* No primitive keys
* No size


### Releases References

```javascript
var elem = document.querySelector('#my-element');
var weak = new WeakMap();

weak.set(elem, { hidden: false });
//        ^
//   if THIS is the only pointer to the element, the map releases it
