# Modules

Hard to discuss

* Not any great support right now
* Polyfills only
* Still Fresh
* Least amount of tooling

## Bits of CommonJS & AMD

* Similar to CommonJS
    - Single Exports
    - Cyclic Dependencies
* Similar to AMD
    - Async Loading Support
    - Configurable Module Loading

## Major Design Goals

* **default** exports are favored
* static module structure
* support for sync/async loading
* support for cyclical dependencies

## Two Pieces

* Import/Export Syntax
* Programmatic Loading API

## Exporting Default

`MyClass.js`:

```javascript
class MyClass {
  constructor() {}
  // ...
}

export default MyClass
```

`Main.js`:

```javascript
import MyClass from 'MyClass';
```

## Exporting Multiple Exports

`lib.js`:

```javascript
export const sqrt = Math.sqrt;
export function square(x) {
  return x * x;
}
export function diag(x, y) {
  return sqrt(square(x) + square(y));
}
```

`main.js`:

```javascript
import { square, diag } from 'lib';
console.log(square(11));  // 121
console.log(diag(4, 3));  // 5
```

### Import all:

```javascript
import * as lib from 'lib';
console.log(lib.square(11));  // 121
console.log(lib.diag(4, 3));  // 5
```

## Export As

`lib.js`:

```javascript
class MyClass{}
export {MyClass as Dude};
```

`main.js`:

```javascript
import { Dude as Bro } from 'lib';
var bro = new Bro();  // instanceof MyClass
```

## Cyclical Dependencies

`lib.js`:

```javascript
import Main from 'main';

var lib = {message: "This Is A Lib"};

export { lib as Lib };
```

`main.js`:

```javascript
import { Lib } from 'lib';

export default class Main {
  // ...
}
```

## More Importing

```javascript
// Default exports and named exports
import theDefault, { named1, named2 } from 'src/mylib';
import theDefault from 'src/mylib';
import { named1, named2 } from 'src/mylib';

// Renaming: import named1 as myNamed1
import { named1 as myNamed1, named2 } from 'src/mylib';

// Importing the module as an object
// (with one property per named export)
import * as mylib from 'src/mylib';

// Only load the module, don't import anything
import 'src/mylib';
```

### `lib.js`

```javascript
export var myVar1 = ...;
export let myVar2 = ...;
export const MY_CONST = ...;

export function myFunc() {
  ...
}

export function* myGeneratorFunc() {
  ...
}
export class MyClass {
  ...
}
```

## Re-exporting

`lib.js`:

```javascript
export * from 'src/other_module';

export { foo, bar } from 'src/other_module';

// Export other_module's `foo` as `myFoo`
export { foo as myFoo, bar } from 'src/other_module';
```

---

# Progammatic Loading API

## `System.import` API

```javascript
System.import('some_module')
  .then(some_module => {
    ...
  })
  .catch(error => {
    ...
  })
```

* `System.import` returns `Promise`
* `Promise.then` provides `exports`

## Load All

```javascript
Promise.all(
  ['module1', 'module2', 'module3']
  .map(x => System.import(x))
  .then(function([module1, module2, module3]) {
    // ...
  });
)
```

## System "Module" Functions

```javascript
// Returns module via Promise
System.import(source);
System.module(source, options);

// Inline register a new module
System.set(name, module);

// Eval code, and register module
System.define(name, source, options?);
```
