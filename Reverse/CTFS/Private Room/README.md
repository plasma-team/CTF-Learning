## Private Room (Reverse)

### Proof of Concept
- Open file ```privateroom.py``` look at line 8 [View code](privateroom.py#L8) the code in array will be changed to string.

- Step by Step
	- Make simple script to solve this challenges
	```php
	// create directory from A-Z, a-z, 0,9, etc..
	$alpha = array_merge(range('A', 'Z'), range('a', 'z'), range(0, 9), str_split("!@#$%^&*()-_=+"));
	foreach ($alpha as $str) {
	    $dict[] = ((((ord($str) << 5) | (ord($str) >> 3)) ^ 111) & 255);
	}

	// solver
	foreach ([233, 129, 9, 5, 130, 194, 195, 39, 75, 229] as $u) {
		echo $alpha[array_search($u, $dict)];
	}
	```

- Capture the flag :triangular_flag_on_post:
```
>> php {file}.php
```