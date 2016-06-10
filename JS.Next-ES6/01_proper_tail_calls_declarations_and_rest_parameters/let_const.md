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
