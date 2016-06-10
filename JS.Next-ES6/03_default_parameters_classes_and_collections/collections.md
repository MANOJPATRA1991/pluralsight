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
