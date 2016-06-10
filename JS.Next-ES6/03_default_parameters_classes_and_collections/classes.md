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
