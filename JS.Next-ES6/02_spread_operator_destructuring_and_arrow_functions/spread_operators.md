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
