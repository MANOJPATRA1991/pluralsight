# Promises

Why do we need promises?

* Async code can look scary
* Callback Pyramid of Death
* Code organization

## Example of Ugly Code Without Promises

```javascript
var img1 = document.querySelect('.img-1');

function load() {
  // woo yey image loaded
}

if (img1.complete) {
  loaded();
} else {
  img1.addEventListener('load', loaded);
}

img1.addEventListener('error', function() {
  // argh everything's broken
});
```

## Promise - Top Down

### Promise Constructor

```javascript
var promise = new Promise(function(resolve, reject) {
  // do a thing, possibly async, then

  if (/* everything turned out fine */) {
    resolve("Stuff worked!");
  }
  else {
    reject(Error("It broke"));
  }
});

return promise;
```

* AJAX
* Load image
* Read/Write localStorage
* Write lots of DOM
* Show a spinner when loading
* Etc.

### Promise Instance

We have a `promise` object. Now what?

A `promise` can be in **1** of **4** states:

* **fulfilled**: successfully resolved - 1
* **rejected**: rejected - 2
* **pending**: hasn't resolved or rejected yet - undefined
* **settled**: fulfilled or rejected - 1 or 2 (is really fulfilled or rejected; more for terminology)

```javascript
var promise = new Promise(function(resolve, reject) {
  // Do something
  if (somethingWorked) {
    resolve("Stuff worked!");
  } else {
    reject(Error("It broke"));
  }
});

promise
  .then(function(result) {
    console.log(result);  // "Stuff worked!"
  }, function(err) {
    console.log(err);  // Error: "It broke"
  });
```

#### Make the Promise

```javascript
// My Own GET Method

function get(url) {
  return new Promise(function(resolve, reject) {
    $.get(url, function(data) {
      resolve(data);
    })
    .fail(function() {
      reject();
    });
  });
}
```

#### Use the Promise

```javascript
var usersPromise = get('users.all');
var postsPromise = get('posts.everyone');

// Wait until BOTH are settled
Promise.all([usersPromise, postsPromise])
  .then(function(results) {
    myController.users = results[0];
    myController.posts = results[1];
  }, function() {
    delete myController.users;
    delete myController.posts;
  });
```

* What if the response is a string?

    ```javascript
    get('users.all')
      .then(function(usersString) {
        return JSON.parse(usersString);
      })
      .then(function(users) {
        myController.users = users;
      });
    ```

* Even more compacy

    ```javascript
    get('users.all')
      .then(JSON.parse)
      .then(function(users) {
        myController.users = users;
      });
    ```

### Static Promise Methods

* `Promise.all(iterable)`: wait until all settles
* `Promise.race(iterable)`: wait until 1 settles
* `Promise.reject(reason)`: create a promise that is already rejected
* `Promise.resolve(value)`: create a promise that is already resolved
