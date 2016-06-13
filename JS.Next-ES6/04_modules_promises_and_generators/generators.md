# Generators

Consider:

```javascript
setTimeout(function() {
  console.log("Wait 1 MS");
}, 1);

function foo() {
  for (var i = 0; i <= 1E10; i++) {
    // How long will this take?
    // What if we could pause this, and restart it?
    console.log(i);
  }
}

foo();
// 0..1E10
// "Wait 1 MS"
```

## Basic Syntax

```javascript
function *myGen() {
  //...
}

// You can put it right after 'function'
```

## Usage

* Besides `yield`, generator bodies are just a method

```javascript
function *three() {
  yield 1;
  yield 2;
  return 3;
}

var geni = three();  // Calling 'three()' didn't execute the method
                     // It returned a generator iterator

geni.next();  // Return { value: 1, done: false }
//   ^^^^
// calling '.next()'

geni.next();  // Return { value: 2, done: false }
geni.next();  // Return { value: 3, done: true }
```

## Example

```javascript
function *foo() {
  yield 1;
  yield 2;
  yield 3;
  yield 4;
  yield 5;
  return 6;
}

for (var v of foo()) {
  console.log(v);
}
```

* Logs only `1, 2, 3, 4, 5`
* `6` doesn't get logged because `done: true`
* `for-of` loops only continue while `done: false`

## Another Example

```javascript
function *foo(x) {              // means that x = 5
  var y = 2 * (yield (x + 1));  // yields 6 (UNdone)
                                // (yield (x + 1)) = 12
                                // y = 2*12 == 24
  var z = yield (y / 3);        // yields 24/3 == 8
                                // (yield (y / 3)) = 13
  return (x + y + z);           // x = 5, y = 24, z = 13
                                // total = 42
}

var genit = foo(5);

console.log(genit.next());    // { value: 6  , done: false }
console.log(genit.next(12));  // { value: 8  , done: false }
console.log(genit.next(13));  // { value: 42 , done: true  }
```
