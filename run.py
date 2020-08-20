# Python-side imports.
import jpype
import jpype.imports
from jpype import JClass

# Start Java.
jpype.startJVM(classpath=['.'])

# Java-side imports.
from java.lang import Class

def importWorkaround(javaClassName):
    javaSideClass = Class.forName(javaClassName)
    return JClass(javaSideClass)

# Print out the class path.
from java.lang import System
classpath = System.getProperty('java.class.path')
print(f'Class path = {classpath}')

# Load the class.
#from com.mystuff import MyClass
# HACK: Avoid problem with direct jpype-style import.
MyClass = importWorkaround('com.mystuff.MyClass')

# Create an instance of the class.
thing = MyClass()

# Execute the method!
thing.doStuff()

# NB: Can use Java reflection to work around the issue:
#thing.getClass().getMethod('doStuff', None).invoke(thing)
