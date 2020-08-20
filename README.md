MCVE illustrating JPype method overloading woes.

## To reproduce

1. Install Java

2. Make an environment with jpype available:
    ```
    conda create -n jpype jpype1
    conda activate jpype1
    ```

3. Build and run:
    ```
    ./build.sh
    python run.py
    ```

## Expected output

```
Class path = .
Traceback (most recent call last):
  File "run.py", line 28, in <module>
    thing.doStuff()
TypeError: No matching overloads found for com.mystuff.DoStuffWithArgs.doStuff(), options are:
	public default void com.mystuff.DoStuffWithArgs.doStuff(java.lang.String)
```
