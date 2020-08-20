MCVE illustrating JPype method overloading woes.

## To reproduce

```
conda create -n jpype jpype1
conda activate jpype1
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
