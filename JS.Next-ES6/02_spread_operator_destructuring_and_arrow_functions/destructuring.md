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
