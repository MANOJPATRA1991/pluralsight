# Proper Tail Call

> Proper tail recursion is a property of the asymptotic space complexity of a language's runtime behavior. That is, in improperly tail recursive languages, control can consume unbounded amounts of space for programs that, when run in properly tail recursive languages, only require a constant amount of space.

> ---Dave Herman, Principal Researcher w/ Mozilla

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
